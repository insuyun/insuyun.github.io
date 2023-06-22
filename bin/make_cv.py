#!/usr/bin/env python3
import os
import copy
import bibtexparser
import pandas as pd
import re
from bibtexparser.bparser import BibTexParser

ROOT = os.path.join(os.path.dirname(__file__), "..")
CONTENT_DIR = os.path.join(ROOT, "content")

NEWS_NUM = 8
MY_NAME = 'Insu Yun'

LB = ' \\\\'

# Exceptions
# - alphabetic order
ALPHABETIC = ['cui:rept']

DOMESTIC_CONFS = [
    'CISC'
]

def authors_to_string(authors):
    if len(authors) == 1:
        return authors[0] # e.g., thesis
    else:
        return ', '.join(authors[:-1]) + ', and ' + authors[-1]

def purify_bib_entry(entry):
    # Remove curly braces
    for k, v in entry.items():
        entry[k] = v.strip().lstrip('{').rstrip('}')

    if 'author' in entry:
        # Change author1 and author2 and author3
        # -> author, author2, and author3
        # and highlight my name
        authors = entry['author']
        authors = authors.split(' and ')
        index = authors.index(MY_NAME)
        assert index != -1
        authors[index] = tex_highlight(authors[index])
        entry['author'] = authors_to_string(authors)

        # alphabetic order
        if entry['ID'] in ALPHABETIC:
            entry['author'] += ' (alphabetical)'
    return entry

def replace_text(text, key, content):
    tag = '{{ %s }}' % key
    assert(tag in text)
    return text.replace(tag, content)

def tex_highlight(s):
    return "\\textbf{%s}" % s

def read_cve():
    # Example
    #   date: 2016/01/24
    #   proj: PHP
    #   cve : IBB-PHP #11326, Pull request #1738
    #   url : https://github.com/php/php-src/pull/1738
    #   desc: Integer overflow in wordwrap
    #

    with open(os.path.join(ROOT, "./cv/cve.md"), encoding="utf-8") as f:
        entries = []
        entry = {}
        for l in f:
            l = l.strip()
            if not l:
                # Empty line represents the end of an entry
                entries.append(entry)
                entry = {}
            else:
                k, v = l.strip().split(': ', 1)
                k = k.strip()
                v = v.strip()
                if k == 'cve':
                    v = v.split(', ')
                entry[k] = v
    return entries

def make_cve():
    entries = read_cve()
    cves = ', '.join(sorted(map(lambda entry: f"\\cc{{{entry['cve'][0]}}}", entries)))
    cves = cves.replace("#", "\\#")
    return cves

def get_conf(confs, entry):
    if 'crossref' in entry:
        return confs[entry['crossref']]

    conf = copy.copy(entry)
    if 'booktitle' in entry:
        conf['title'] = entry['booktitle']
    if 'journal' in entry:
        conf['title'] = entry['journal']

    return conf

def bib_to_tex(confs, pub_entries):
    text = ''
    for entry in pub_entries:
        conf = get_conf(confs, entry)

        entry['author'] = entry['author'].replace('\\*', '*')
        content = ['\\item %s %s' % (tex_highlight(entry['title']), LB),
            '{\\footnotesize',
            '  ' + entry['author'] + LB,
            '  ' + conf['title'] + LB]

        location = ''
        if 'address' in conf:
            location += '%s, ' % conf['address']

        if 'month' in conf:
            location += '%s ' % conf['month']
        location += '%s' % (conf['year'])
        content.append(location)

        if 'acceptance_rate' in conf:
            content[-1] += LB
            content.append('  (Acceptance rates: ' + conf['acceptance_rate'] + ')')

        if 'award' in entry:
            content[-1] += LB
            content.append('  ' + tex_highlight('\\textcolor{red}{%s}' % entry['award']))

        content += ['}', '']
        text += '\n'.join(content)
    return text

def add_acceptance_rate(entry):
    def normalize(ID):
        ID = ID[:-2]
        if ID == 'SP':
            return 'Oakland'
        if ID == 'SEC':
            return 'UsenixSec'
        if ID == 'ATC':
            return 'USENIX-ATC'
        return ID
    csv_file = os.path.join(os.path.dirname(__file__), 'csconferences.csv')
    df = pd.read_csv(csv_file)
    df2 = df.loc[
            (df['Year'] == int(entry['year'])) &
            (df['Conference'] == normalize(entry['ID']))]

    if not df2.empty:
        accepted = df2['Accepted'].sum()
        submitted = df2['Submitted'].sum()
        rate = round((accepted / submitted) * 100)
        entry['acceptance_rate'] = f"{rate}\%, {accepted}/{submitted}"


def is_top_tier(ID):
    ID = ID[:-2]
    return ID in ['CCS', 'SEC', 'NDSS', 'SP', 'OSDI', 'ATC']

class MultiBibTexParser():
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.conf = self.read_conf()
        self.pub = self.read_pub()

    def read_conf(self):
        conf_bib = os.path.join(self.root_dir, 'conf.bib')
        parser = BibTexParser(common_strings=True)
        with open(conf_bib, encoding="utf-8") as f:
            conf_entries = bibtexparser.load(f, parser).entries

        conf = {}
        for entry in conf_entries:
            # Add year to its nick
            # e.g., (SECURITY) -> (SECURITY 2019)
            title = entry['title']
            if title.endswith(')'):
                assert(title.endswith(')'))
                entry['title'] = title[:-1] + ' ' + entry['year'] + title[-1:]
                if is_top_tier(entry['ID']):
                    entry['title'] = re.sub(r'\((.*)\)', r'(\\toptier{\1})', entry['title'])
            add_acceptance_rate(entry)
            conf[entry['ID']] = entry

        return conf

    def read_pub(self):
        pub_bib = os.path.join(self.root_dir, 'pub.bib')
        parser = BibTexParser(common_strings=True)
        with open(pub_bib, encoding="utf-8") as f:
            pub_entries = bibtexparser.load(f, parser).entries

        return list(map(purify_bib_entry, pub_entries))

    def to_tex(self):
        return bib_to_tex(self.conf, self.pub)

    def filter(self, filter_fn):
        new = copy.copy(self)
        new.pub = list(filter(filter_fn, self.pub))
        return new


def make_cv():
    def filter_domestic(entry):
        return 'crossref' in entry and \
            any(entry['crossref'].startswith(conf) for conf in DOMESTIC_CONFS)

    def filter_intl_conf(entry):
        return entry['ENTRYTYPE'] == 'inproceedings' and not filter_domestic(entry)

    def filter_intl_journal(entry):
        return entry['ENTRYTYPE'] == 'article'

    with open(os.path.join(ROOT, 'cv/cv.tex'), encoding='utf-8') as f:
        txt = f.read()
        txt = replace_text(txt, 'CVE', make_cve())

        parser = MultiBibTexParser(os.path.join(ROOT, 'assets/pubs'))
        filtered = parser.filter(filter_intl_conf)
        txt = replace_text(txt, 'INTL_CONF', filtered.to_tex())

        filtered = parser.filter(filter_intl_journal)
        txt = replace_text(txt, 'INTL_JOURNAL', filtered.to_tex())

        filtered = parser.filter(filter_domestic)
        txt = replace_text(txt, 'DOM_CONF', filtered.to_tex())

        # Should we support domestic journal?

    out = os.path.join(ROOT, 'cv/cv-gen.tex')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(txt)

if __name__ == '__main__':
    make_cv()

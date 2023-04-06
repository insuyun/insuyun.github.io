#!/usr/bin/env python3
import sys
import os
import bibtexparser
from bibtexparser.bparser import BibTexParser

ROOT = os.path.join(os.path.dirname(__file__), "..")
CONTENT_DIR = os.path.join(ROOT, "content")

NEWS_NUM = 8
MY_NAME = 'Insu Yun'

LB = ' \\\\'

def get_bib_files(domestic):
    bib_dir = "assets/pubs/"

    if domestic:
        bib_dir += "dom"
    else:
        bib_dir += "intl"

    conf_bib = os.path.join(bib_dir, "conf.bib")
    pub_bib = os.path.join(bib_dir, "pub.bib")

    return conf_bib, pub_bib

def md_highlight(s):
    return '**%s**' % s

def authors_to_string(authors):
    if len(authors) == 1:
        return authors[0] # e.g., thesis
    else:
        return ', '.join(authors[:-1]) + ', and ' + authors[-1]

def purify_bib_entry(entry, highlight):
    for k, v in entry.items():
        entry[k] = v.strip().lstrip('{').rstrip('}')

    if 'author' in entry:
        # Change author1 and author2 and author3
        # -> author, author2, and author3
        # and highlight my name
        authors = entry['author']

        has_cofirst = '*' in authors
        if has_cofirst:
            # handle asterisk for markdown
            authors = authors.replace('*', '\\*')
        authors = authors.split(' and ')
        index = authors.index(MY_NAME)
        assert(index != -1)
        authors[index] = highlight(authors[index])
        entry['author'] = authors_to_string(authors)

        # alphabetic order
        if entry['ID'] == 'cui:rept':
            entry['author'] += ' (alphabetical)'
        if has_cofirst:
            entry['author'] += ' (\\* co-first)'
    return entry

def replace_text(text, key, content):
    tag = '{{ %s }}' % key
    assert(tag in text)
    return text.replace(tag, content)

def read_bib(highlight, domestic=False):
    conf_dict = {}
    conf_bib, pub_bib = get_bib_files(domestic)
    parser = BibTexParser(common_strings=True)
    conf_entries = bibtexparser.load(open(conf_bib), parser).entries

    for entry in conf_entries:
        # Add year to its nick
        title = entry['title']
        if title.endswith(')'):
            assert(title.endswith(')'))
            entry['title'] = title[:-1] + ' ' + entry['year'] + title[-1:]
        conf_dict[entry['ID']] = entry

    parser = BibTexParser(common_strings=True)

    pub_entries = []
    raw_pub_entries = bibtexparser.load(open(pub_bib), parser).entries

    for i, entry in enumerate(raw_pub_entries):
        if 'crossref' in entry:
            metadata = conf_dict[entry['crossref']]
            pub_entries.append(purify_bib_entry(entry, highlight))
        else:
            pub_entries.append(purify_bib_entry(entry, highlight))

    return conf_dict, pub_entries

def get_location(entry):
    if 'address' in entry:
        return entry['address']
    elif 'school' in entry:
        return entry['school'] # for thesis
    raise ValueError('Unexpected format')

def make_pub():
    conf_dict, pub_entries = read_bib(md_highlight)
    texts = ['<pre>']

    count = 1
    for entry in pub_entries:
        if 'crossref' in entry:
            metadata = conf_dict[entry['crossref']]
        else:
            metadata = entry

        opts = [ ]
        file_id = os.path.join(metadata['year'], entry['ID'])
        paper_file = os.path.join('pubs', file_id + '.pdf')
        if os.path.exists(os.path.join(CONTENT_DIR, paper_file)):
            opts.append('[[paper]](%s)' % paper_file)

        slides_file = os.path.join('pubs', file_id + '-slides.pdf')
        if os.path.exists(os.path.join(CONTENT_DIR, slides_file)):
            opts.append('[[slides]](%s)' % slides_file)

        if 'www-git' in entry:
            opts.append('[[code]](%s)' % entry['www-git'])

        if 'www-url' in entry:
            opts.append('[[web]](%s)' % entry['www-url'])

        texts.append('%d. **%s** %s' % (count, entry['title'], ' '.join(opts)))

        contents = [entry['author']]
        if 'booktitle' in metadata:
            contents.append(metadata['booktitle'])
        elif entry['ENTRYTYPE'] == 'phdthesis':
            contents.append('Ph.D. thesis, %s' % entry['school'])

        place = ''
        if 'address' in metadata:
            place += '%s, ' % metadata['address']
        contents.append('%s %s' % ( metadata['month'], metadata['year']))

        if 'award' in entry:
            contents.append('** * %s **' % entry['award'])

        for content in contents:
            texts.append('    ' + content)

        count += 1

    texts += ['</pre>']
    return '\n'.join(texts)

def make_news():
    # TODO: Support folding
    lines = open(NEWS_MD).read().splitlines()[:NEWS_NUM]
    lines[0] = '**%s**' % lines[0]
    lines = list(map(lambda l: '- %s' % l, lines))
    return '\n'.join(lines)

def make_award():
    # TODO: Support folding
    lines = open(AWARD_MD).read().splitlines()

    for i, l in enumerate(lines):
        # Highlight title
        items = l.split(', ')
        items[0] = '%d. **%s**' % (i + 1, items[0])
        lines[i] = ', '.join(items)
    return '\n'.join(lines)



def tex_highlight(s):
    return "\\textbf{%s}" % s

def read_cve():
    with open(os.path.join(ROOT, "./cv/cve.md")) as f:
        entries = []
        entry = {}
        for l in f:
            l = l.strip()
            if not l:
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
    cves = ', '.join(sorted(map(lambda entry: "\\cc{%s}" % entry['cve'][0], entries)))
    cves = cves.replace("#", "\\#")
    return cves

def bib_to_tex(conf_dict, pub_entries):
    text = ''
    for entry in pub_entries:
        if 'crossref' in entry:
            conf = conf_dict[entry['crossref']]
        else:
            conf = entry

        if entry['ENTRYTYPE'] == 'phdthesis':
            conf['title'] = 'Ph.D. thesis, %s' % entry['school']
            continue

        # XXX: Fix this... so bad design
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

        if 'award' in entry:
            content[-1] += LB
            content.append('  ' + tex_highlight('$\\bullet$ %s' % entry['award']))

        content += ['}', '']
        text += '\n'.join(content)
    return text

def make_bib2tex(domestic=False):
    conf_dict, pub_entries = read_bib(tex_highlight, domestic)
    return bib_to_tex(conf_dict, pub_entries)

def make_cv():
    with open(os.path.join(ROOT, 'cv/cv.tex')) as f:
        txt = f.read()
        txt = replace_text(txt, 'CVE', make_cve())
        txt = replace_text(txt, 'INTL_PUB', make_bib2tex(False))
        txt = replace_text(txt, 'DOM_PUB', make_bib2tex(True))

    out = os.path.join(ROOT, 'cv/cv-gen.tex')
    with open(out, 'w') as f:
        f.write(txt)

if __name__ == '__main__':
    make_cv()

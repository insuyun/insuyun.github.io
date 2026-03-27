# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal academic website and CV for Prof. Insu Yun (KAIST). The site is built with Hugo (Wowchemy/Academic theme) and the CV is generated as a LaTeX PDF.

## Build Commands

### Full site build (from repo root)
```bash
make          # runs make_pub.py, make_cv.py, builds CV PDF, then runs hugo
```

### CV only (from cv/ directory)
```bash
make          # generates cv-gen.tex from cv.tex via make_cv.py, then compiles to cv.pdf
```

### Publishing to GitHub Pages
```bash
./publish.sh  # builds everything and pushes public/ to the publish branch
```

### Python environment
```bash
virtualenv venv && source venv/bin/activate && pip install -r requirements.txt
```

## Architecture

### CV Generation Pipeline
1. `bin/make_cv.py` reads `assets/pubs/pub.bib` and `assets/pubs/conf.bib` (BibTeX), parses them with `bibtexparser`
2. It reads `cv/cv.tex` as a template containing `{{ INTL_CONF }}`, `{{ INTL_JOURNAL }}`, `{{ DOM_CONF }}`, `{{ NOPUB }}`, and `{{ CVE }}` placeholders
3. Publications are filtered by type (conference/journal, international/domestic, nopub) and rendered to LaTeX
4. Output is written to `cv/cv-gen.tex`, which is then compiled to `cv.pdf` via `latexrun`
5. The PDF is copied to `static/` for the website

### Website Content Pipeline
- `bin/make_pub.py` generates Hugo content pages under `content/publication/` from the same BibTeX sources
- Conference metadata (acceptance rates, top-tier status) comes from `bin/csconferences.csv`
- Hugo config lives in `config/_default/`

### Key conventions
- **Adding a publication**: Update `assets/pubs/pub.bib` (and `conf.bib` if new venue), then run `bin/make_pub.py`
- **cv.tex is a template**, not the final LaTeX — never edit `cv-gen.tex` directly (it's auto-generated)
- The `\forkaist{}{}` macro switches content between KAIST-specific and general CV variants
- Top-tier conferences are highlighted via `\toptier{}` macro, determined by `bin/csconferences.csv`
- `MY_NAME = 'Insu Yun'` in `make_cv.py` controls author name bolding in publications

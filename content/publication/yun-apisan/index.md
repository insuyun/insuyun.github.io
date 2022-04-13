---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'APISan: Sanitizing API Usages through Semantic Cross-checking'
subtitle: ''
summary: ''
authors:
- Insu Yun
- Changwoo Min
- Xujie Si
- Yeongjin Jang
- Taesoo Kim
- Mayur Naik
tags: []
categories: []
date: '2016-08-01'
lastmod: 2022-02-10T11:34:02+09:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-02-10T02:34:02.598221Z'
publication_types:
- '0'
abstract: "API misuse is a well-known source of bugs. Some of them (e.g., incorrect\
  \ use of\nSSL API, and integer overflow of memory allocation size) can cause serious\n\
  security vulnerabilities (e.g., man-in-the-middle (MITM) attack, and privilege\n\
  escalation). Moreover, modern APIs, which are large, complex, and fast\nevolving,\
  \ are error-prone. However, existing techniques to help finding bugs\nrequire manual\
  \ effort by developers (e.g., providing specification or model) or\nare not scalable\
  \ to large real-world software comprising millions of lines of\ncode.\n\nIn this\
  \ paper, we present APISAN, a tool that automatically infers correct API\nusages\
  \ from source code without manual effort. The key idea in APISAN is to\nextract\
  \ likely correct usage patterns in four different aspects (e.g., causal\nrelation,\
  \ and semantic relation on arguments) by considering semantic\nconstraints. APISAN\
  \ is tailored to check various properties with security\nimplications. We applied\
  \ APISAN to 92 million lines of code, including Linux\nKernel, and OpenSSL, found\
  \ 76 previously unknown bugs, and provided patches for\nall the bugs.\n"
publication: '*Proceedings of the 25th USENIX Security Symposium (Security)*'
url_slides: pubs/2016/yun:apisan-slides.pdf
url_paper: pubs/2016/yun:apisan.pdf
url_code: https://github.com/sslab-gatech/apisan
award: '**Nominated as a finalist in CSAW Best Applied Research Paper Award 2016**'
---

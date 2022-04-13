---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Preventing Use-After-Free Attacks with Fast Forward Allocation
subtitle: ''
summary: ''
authors:
- Brian Wickman
- Hong Hu
- Insu Yun
- Daehee Jang
- JungWon Lim
- Sanidhya Kashyap
- Taesoo Kim
tags: []
categories: []
date: '2021-08-01'
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
publishDate: '2022-02-10T02:34:01.947950Z'
publication_types:
- '0'
abstract: "Memory-unsafe languages are widely used to implement critical systems like\
  \ kernels and browsers, leading to thousands of memory safety issues every year.\
  \ A use-after-free bug is a temporal memory error where the program accidentally\
  \ visits a freed memory location. Recent studies show that useafter-free is one\
  \ of the most exploited memory vulnerabilities. Unfortunately, previous efforts\
  \ to mitigate use-after-free bugs are not widely deployed in real-world programs\
  \ due to either inadequate accuracy or high performance overhead.\n\nIn this paper,\
  \ we propose to resurrect the idea of one-time allocation (OTA) and provide a practical\
  \ implementation with efficient execution and moderate memory overhead. With onetime\
  \ allocation, the memory manager always returns a distinct memory address for each\
  \ request. Since memory locations are not reused, attackers cannot reclaim freed\
  \ objects, and thus cannot exploit use-after-free bugs. We utilize two techniques\
  \ to render OTA practical: batch page management and the fusion of bump-pointer\
  \ and fixed-size bins memory allocation styles. Batch page management helps reduce\
  \ the number of system calls which negatively impact performance, while blending\
  \ the two allocation methods mitigates the memory overhead and fragmentation issues.\
  \ We implemented a prototype, called FFmalloc, to demonstrate our techniques. We\
  \ evaluated FFmalloc on widely used benchmarks and real-world large programs. FFmalloc\
  \ successfully blocked all tested useafter-free attacks while introducing moderate\
  \ overhead. The results show that OTA can be a strong and practical solution to\
  \ thwart use-after-free threats.\n"
publication: '*Proceedings of the 30th USENIX Security Symposium (Security)*'
url_slides: pubs/2021/wickman:ffmalloc-slides.pdf
url_paper: pubs/2021/wickman:ffmalloc.pdf
url_code: https://github.com/bwickman97/ffmalloc
---

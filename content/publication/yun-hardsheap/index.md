---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'HardsHeap: A Universal and Extensible Framework for Evaluating Secure Allocators'
subtitle: ''
summary: ''
authors:
- Insu Yun
- Woosun Song
- Seunggi Min
- Taesoo Kim
tags: []
categories: []
date: '2021-11-01'
lastmod: 2022-02-10T11:34:01+09:00
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
publishDate: '2022-02-10T02:34:01.886297Z'
publication_types:
- '0'
abstract: "Secure allocators have been extensively studied to mitigate heap\nvulnerabilities.\
  \ They employ safe designs and randomized mechanisms to stop or\nmitigate heap exploitation.\
  \ Despite extensive research efforts, secure\nallocators can only be evaluated by\
  \ with theoretical analysis or pre-defined\ndata sets, which are insufficient to\
  \ effectively reflect powerful adversaries in\nthe real world.\n\nIn this paper,\
  \ we present HardsHeap, an automatic tool for evaluating secure\nallocators. The\
  \ key idea of HardsHeap is to use random testing (i.e., fuzzing)\nto evaluate secure\
  \ allocators. To handle the diverse properties of secure\nallocators, HardsHeap\
  \ supports an extensible framework, making it easy to write\na validation logic\
  \ for each property. Moreover, HardsHeap employs sampling-based\ntesting, which\
  \ enables us to evaluate a probabilistic mechanism prevalent in\nsecure allocators.\
  \ To eliminate redundancy in findings from HardsHeap, we devise\na new technique\
  \ called Statistical Significance Delta Debugging (SSDD), which\nextends the existing\
  \ delta debugging for stochastically reproducible test cases.\n\nWe evaluated HardsHeap\
  \ to 10 secure allocators. Consequently, we found 56\ninteresting test cases, including\
  \ several unsecure yet underestimated behaviors\nfor handling large objects in secure\
  \ allocators. Moreover, we discovered 10\nimplementation bugs. One of the bugs is\
  \ integer overflow in secure allocators,\nmaking them even more invulnerable than\
  \ ordinary allocators. Our evaluation also\nshows that SSDD successfully reduces\
  \ test cases by 37.2% on average without a\nloss of reproducibility.\n"
publication: '*Proceedings of the 28th ACM Conference on Computer and Communications
  Security (CCS)*'
url_slides: pubs/2021/yun:hardsheap-slides.pdf
url_paper: pubs/2021/yun:hardsheap.pdf
url_code: https://github.com/kaist-hacking/HardsHeap
---

---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Kargus: A Highly-scalable Software-based Intrusion Detection System'
subtitle: ''
summary: ''
authors:
- Muhammad Jamshed
- Jihyung Lee
- Sangwoo Moon
- Insu Yun
- Deokjin Kim
- Sungryoul Lee
- Yung Yi
- KyoungSoo Park
tags: []
categories: []
date: '2012-10-01'
lastmod: 2022-02-10T18:42:47+09:00
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
publishDate: '2022-02-10T09:42:47.401092Z'
publication_types:
- '0'
abstract: "As high-speed networks are becoming commonplace, it is increasingly challenging\n\
  to prevent the attack attempts at the edge of the Internet. While many\nhigh-performance\
  \ intrusion detection systems (IDSes) employ dedicated network\nprocessors or special\
  \ memory to meet the demanding performance requirements, it\noften increases the\
  \ cost and limits functional flexibility. In contrast,\nexisting softwarebased IDS\
  \ stacks fail to achieve a high throughput despite\nmodern hardware innovations\
  \ such as multicore CPUs, manycore GPUs, and 10 Gbps\nnetwork cards that support\
  \ multiple hardware queues.\n\nWe present Kargus, a highly-scalable software-based\
  \ IDS that exploits the full\npotential of commodity computing hardware. First,\
  \ Kargus batch processes\nincoming packets at network cards and achieves up to 40\
  \ Gbps input rate even\nfor minimum-sized packets.  Second, it exploits high processing\
  \ parallelism by\nbalancing the pattern matching workloads with multicore CPUs and\
  \ heterogeneous\nGPUs, and benefits from extensive batch processing of multiple\
  \ packets per each\nIDS function call. Third, Kargus adapts its resource usage depending\
  \ on the\ninput rate, significantly saving the power in a normal situation. Our\n\
  evaluation shows that Kargus on a 12-core machine with two GPUs handles up to\n\
  33 Gbps of normal traffic and achieves 9 to 10 Gbps even when all packets\ncontain\
  \ attack signatures, a factor of 1.9 to 4.3 performance improvements over\nthe existing\
  \ state-of-the-art software IDS. We design Kargus to be compatible\nwith the most\
  \ popular software IDS, Snort.\n"
publication: '*Proceedings of the 19th ACM Conference on Computer and Communications
  Security (CCS)*'
url_slides: pubs/2012/jamshed:kargus-slides.pdf
url_paper: pubs/2012/jamshed:kargus.pdf
url_web: https://shader.kaist.edu/kargus/
---

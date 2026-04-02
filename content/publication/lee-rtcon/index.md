---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'RTCon: Context-Adaptive Function-Level Fuzzing for RTOS Kernels'
subtitle: ''
summary: ''
authors:
- Eunkyu Lee
- Junyoung Park
- Insu Yun
tags: []
categories: []
date: '2026-02-01'
lastmod: 2026-04-02T20:43:11+09:00
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
publishDate: '2026-04-02T11:43:11.280559Z'
publication_types:
- '0'
abstract: "Real-Time Operating System (RTOS) is widely used in embedded systems with\
  \ its various subsystems such as Bluetooth and Wi-Fi. As its functionalities grow,\
  \ its attack surface also expands, exposing it to more security threats. To address\
  \ this, dynamic testing techniques like fuzzing have been widely applied to embedded\
  \ systems. However, for RTOS, these techniques struggle to effectively test deeply\
  \ located functions within the kernel due to their complexity.\n\nIn this paper,\
  \ we present RTCon, a context-adaptive function-level fuzzer for RTOS kernels. RTCon\
  \ performs function-level fuzzing on any target functions within the RTOS kernel\
  \ by adaptively generating function contexts during fuzzing. Additionally, RTCon\
  \ employs Multi-layer Classification to classify crashes by confidence levels, helping\
  \ analysts focus on high-confidence crashes. We implemented the prototype of RTCon\
  \ and evaluated it on four popular RTOS kernels: Zephyr, RIOT, FreeRTOS, and ThreadX.\
  \ As a result, RTCon discovered 27 bugs, including 25 new bugs. We reported all\
  \ of them to maintainers and received 14 CVEs. RTCon also demonstrated its effectiveness\
  \ in crash classification, achieving a 92.7% precision for high-confidence crashes,\
  \ compared to a 5.8% precision for low-confidence crashes.\n"
publication: '*Proceedings of the 2026 Annual Network and Distributed System Security
  Symposium (NDSS)*'
url_slides: pubs/2026/lee:rtcon-slides.pdf
url_paper: pubs/2026/lee:rtcon.pdf
---

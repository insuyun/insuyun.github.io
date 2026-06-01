---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Function-Level Fuzzing for RTOS Kernels with RTCon
subtitle: ''
summary: ''
authors:
- Insu Yun
- Eunkyu Lee
tags: []
categories: []
date: '2026-05-01'
lastmod: 2026-06-01T21:08:58+09:00
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
publishDate: '2026-06-01T12:08:58.737736Z'
publication_types:
- '0'
abstract: "Real-Time Operating Systems (RTOS) are widely used in embedded systems\
  \ to support functionalities such as Bluetooth and Wi-Fi. As RTOS kernels grow in\
  \ functionality, their attack surface also expands, increasing the need for effective\
  \ security testing. However, existing dynamic testing techniques such as fuzzing\
  \ have difficulty effectively testing deeply located kernel functions because these\
  \ functions require complex execution contexts.\n\nThis tutorial presents RTCon,\
  \ a context-adaptive function-level fuzzer for RTOS kernels. The tutorial uses Zephyr,\
  \ an open-source RTOS for embedded and IoT devices that has been adopted as the\
  \ embedded controller platform for ChromeOS devices, as the target system. Participants\
  \ will learn the principles of function-level fuzzing, execution context construction\
  \ for kernel functions, and practical techniques for testing RTOS kernels.\n"
publication: '*Proceedings of the 2026 IEEE International Conference on Software Testing,
  Verification and Validation (ICST) Tutorial*'
url_slides: pubs/2026/lee:rtcontutorial-slides.pdf
---

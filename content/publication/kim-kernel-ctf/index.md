---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'One shot, Triple kill: Pwning all three Google kernelCTF instances with a
  single 1-day Linux vulnerability'
subtitle: ''
summary: ''
authors:
- Dongok Kim
- Seunghyun Lee
- Insu Yun
tags: []
categories: []
date: '2023-11-01'
lastmod: 2024-07-31T22:41:44+09:00
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
publishDate: '2024-07-31T13:41:44.896788Z'
publication_types:
- '0'
abstract: "Desktops, servers, cloud computing services, mobile devices, and IoT devices.\
  \ Linux is the most popular open-source kernel and is used in various IT platforms.\
  \ Because of the ubiquitous presence of Linux and the characteristic of the kernel\
  \ which governs the entire system, security threat against Linux kernel is a significant\
  \ concern. Numerous vulnerabilities in Linux are reported frequently, either discovered\
  \ by fuzzer or through manual analysis. However, assessing the exploitability of\
  \ these vulnerabilities is not a straightforward task these days, where various\
  \ mitigations are applied.\n\nTo address these issues, Google recently announced\
  \ kernelCTF — a bug bounty program that is specifically designed for studying Linux\
  \ kernel exploits. kernelCTF originated from kCTF, which initially was a bug bounty\
  \ program for GKE (Google Kubernetes Engine). Then, it has evolved into kernelCTF,\
  \ to provide an environment for kernel security researchers to actively engage in\
  \ vulnerability identification and exploit mitigations. For the intention of the\
  \ program, kernelCTF provides various targets such as the latest LTS Linux kernel,\
  \ Container-optimized OS (COS) used for GKE, and LTS Linux kernel with Google’s\
  \ custom kernel exploit mitigations. Unlike other bug bounty programs, Google considers\
  \ submissions as valid regardless of whether the vulnerability is 0-day or 1-day\
  \ if they can successfully achieve full LPE kernel exploits with container escape.\n\
  \nIn this talk, we will present our exploits submitted to kernelCTF. Notably, this\
  \ is the first submission in kernelCTF's history that exploits every target with\
  \ a single (1-day) vulnerability. We will briefly introduce what kernelCTF is and\
  \ each target kernel instance of kernelCTF. Then, we will explain how we built the\
  \ 1-day vulnerability exploit for every target instance in detail. This will include\
  \ how we discovered this vulnerability, and how we made exploits working for the\
  \ different target kernel versions, build configs, and applied mitigations. Finally,\
  \ we will share our novel research and insights into kernel exploit mitigations\
  \ of Linux and Google, focusing on their limitations and side effects. We will also\
  \ discuss the difficulties to apply mitigations to the Linux kernel."
publication: '*POC 2023*'
url_slides: pubs/2023/kim:kernel-ctf-slides.pdf
---

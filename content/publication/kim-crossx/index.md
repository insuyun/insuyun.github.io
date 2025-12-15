---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'CROSS-X: Generalized and Stable Cross-Cache Attack on the Linux Kernel'
subtitle: ''
summary: ''
authors:
- Dongok Kim
- Juhyun Song
- Insu Yun
tags: []
categories: []
date: '2025-10-01'
lastmod: 2025-12-15T20:31:07+09:00
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
publishDate: '2025-12-15T11:31:07.660704Z'
publication_types:
- '0'
abstract: 'The cross-cache attack is a fundamental component of modern Linux kernel
  exploits, spanning real-world attacks and recent research. Despite its importance,
  it is often regarded as unreliable due to its complex setup, and existing studies
  lack in-depth analysis of its mechanics. In this paper, we address this gap by:
  (1) reviewing public strategies and their limitations, (2) proposing two optimized
  strategies effective in varied conditions, and (3) introducing CROSS-X, an automated
  system that identifies suitable target objects for cross-cache attacks. We evaluated
  our strategies on a synthetic vulnerability and nine real-world CVEs, achieving
  over 99% and 85% success rates under idle and busy workloads, respectively. They
  also outperformed existing methods in 6 of 8 CVEs under idle workloads and 5 of
  8 under busy workloads. For object identification, we define three key properties:
  (1) spray capability, (2) minimal interference, and (3) useful primitives. Based
  on these, CROSS-X identified seven versatile target objects and their relationship
  with interfering allocations. We believe our work will enhance public understanding
  of cross-cache attacks and contribute to improving Linux kernel security.'
publication: '*Proceedings of the 32nd ACM Conference on Computer and Communications
  Security (CCS)*'
url_slides: pubs/2025/kim:crossx-slides.pdf
url_paper: pubs/2025/kim:crossx.pdf
author_notes:
- Equal contribution
- Equal contribution
---

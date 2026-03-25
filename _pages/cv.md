---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* **Ph.D. Candidate** in Information and Communication Engineering, Southwest Jiaotong University, Chengdu, China, 2017 - 2025
  * Advisors: Prof. Turgay Celik, Prof. Hengchao Li
* **B.S.** in Electronic Information Engineering, Wuhan University of Science and Technology, Wuhan, China, 2012 - 2016

Research Experience
======
* **Feb 2023 - Aug 2024: Research Intern**
  * Infocomm Research (I2R), A*STAR, Singapore
  * Advisor: Dr. Xun Xu
  * Projects:
    * Open-set semi-supervised object detection
    * Source-free domain adaptation for object detection
    * Weakly-supervised Segment Anything Model

* **Aug 2024 - Dec 2024: Research Intern**
  * Centre for Frontier AI Research (CFAR), A*STAR, Singapore
  * Advisor: Dr. Foo Chuan Sheng
  * Projects:
    * Improving robustness of object detection against common perturbations and adversarial attacks

Skills
======
* Deep Learning & Computer Vision
  * PyTorch, TensorFlow
  * Object Detection (Faster R-CNN, YOLO, DETR)
  * Image Segmentation (SAM, U-Net)
* Remote Sensing Image Analysis
* Programming: Python, MATLAB, C++

Honors & Awards
======
* 2024: IEEE GRSS Travel Grant, IGARSS 2024, Athens, Greece
* 2020: Huawei Second-Class Scholarship, Chengdu, China

Academic Service
======
* **Guest Editor**: Future Internet
* **Journal Reviewer**: TIP, TCSVT, GRSM, TGRS, ISPRS, TIM, JSTARS, GRSL
* **Conference Reviewer**: NeurIPS 2026, ECCV 2026, CVPR 2026, IGARSS 2025/2026, ACM MM 2024/2025/2026, ICONIP 2023
* **Membership**: IEEE Member

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

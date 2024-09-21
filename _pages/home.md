---
layout: splash
permalink: /
hidden: true
header:
  overlay_image: /assets/images/welcome.jpg
  text_color: black
  actions:
    - label: "Check out the latest publication!"
      url: /publications/
excerpt: "Pablo Capilla-Lasheras' research"
author_profile: false
feature_row:
  - image_path: /assets/images/home/research_block.jpg
    alt: " "
    title: " "
    excerpt: " "
    url: "/research/"
    btn_label: "Research"
    btn_class: "btn--inverse"
  - image_path: /assets/images/home/publications_block.jpg
    alt: " "
    title: " "
    excerpt: " "
    url: "/publications/"
    btn_label: "Publications"
    btn_class: "btn--inverse"
  - image_path: /assets/images/home/bio_block.jpg
    title: " "
    excerpt: " "
    url: "/bio/"
    btn_label: "Bio"
    btn_class: "btn--inverse"
news_section:
    title: "News"
---

{% include feature_row %}

<div class="news-section">
  <h2>{{ page.news_section.title }}</h2>
  <ul class="news-list">
    <li class="news-item">
      <h3>Exciting New Research Published</h3>
      <p>Our latest paper on migratory birds has been published. Check out the publication <a href="/publications/">here</a>.</p>
      <span class="news-date">September 1, 2023</span>
    </li>
    <li class="news-item">
      <h3>Project MIGRALIGHT Begins</h3>
      <p>We have officially launched the MIGRALIGHT project, studying the effects of artificial light on migratory birds.</p>
      <span class="news-date">June 15, 2023</span>
    </li>
  </ul>
</div>

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
      <h3>New paper on sex differences in cooperation</h3>
      <p>In this paper, recently published in PLoS Biology, we investigate the main hypotheses for the evolution of sex differences in cooperation. You can find the paper Open Access <a href="https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002859">here</a>.</p>
      <span class="news-date">October 24, 2024</span>
    </li>
    <li class="news-item">
      <h3>New Urban Ecology and Evolution paper published in the Journal of Animal Ecology</h3>
      <p>Differences in clutch size between birds living in anthropogenic and more pristine environments are commonly reported. However, we don't know why. Is this pattern an adaptive strategy to survive in anthropogenic habitats? Do these differences represent environmental constraints? In this paper, under the brilliant lead of <a href="https://www.gla.ac.uk/pgrs/markpitt/">Mark Pitt</a>, we investigate these questions. Find the paper <a href="https://besjournals.onlinelibrary.wiley.com/doi/pdfdirect/10.1111/1365-2656.14171">here</a>.</p>
      <span class="news-date">September 1, 2024</span>
    </li>
    <li class="news-item hidden">
      <h3>Project MIGRALIGHT Begins</h3>
      <p>We have officially launched the <a href="https://pablocl.com/MIGRALIGHT/">MIGRALIGHT project</a>, studying the effects of urbanisation and artificial light on migratory birds.</p>
      <p>The project is funded by a Marie Skłodowska-Curie Actions Global Fellowship and represents a collaboration between the <a href="https://www.vogelwarte.ch/en/">Swiss Ornithological Institute</a> and <a href="https://www.ebd.csic.es/en/node">Doñana Biological Station - CSIC</a>.</p>
      <span class="news-date">August 1, 2024</span>
    </li>
  </ul>
  <button id="toggle-news-btn" class="btn">Show more news</button>
</div>

<script>
  document.getElementById('toggle-news-btn').addEventListener('click', function () {
    const hiddenItems = document.querySelectorAll('.news-item.hidden');
    const allItems = document.querySelectorAll('.news-item');

    if (this.textContent === 'Show more news') {
      hiddenItems.forEach(item => item.classList.remove('hidden'));
      this.textContent = 'Show less news';
    } else {
      allItems.forEach((item, index) => {
        if (index >= 2) item.classList.add('hidden');
      });
      this.textContent = 'Show more news';
    }
  });
</script>

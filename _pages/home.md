---
layout: landing
permalink: /
title: "Pablo Capilla-Lasheras"
excerpt: "Behavioural ecology, migration and evolution in human-altered environments."
classes: home-landing
author_profile: false
---

<section class="landing-hero" aria-labelledby="landing-title">
  {% assign featured_image_path = "/assets/images/home/carousel/tagging_scops_owls_Daniel_Leopoldsberger (24).JPG" %}
  {% assign carousel_images = site.static_files | where_exp: "image", "image.path contains '/assets/images/home/carousel/'" | sort: "path" %}
  <div class="landing-hero__media" data-landing-carousel data-interval="8000">
    <img class="landing-hero__image landing-hero__image--featured is-active" src="{{ featured_image_path | relative_url | uri_escape }}" alt="Researchers tagging Eurasian scops owls beneath an oak tree" width="5568" height="3712" fetchpriority="high" data-credit="Photo: Daniel Leopoldsberger">
    <img class="landing-hero__image" src="/assets/images/home/landing-hero.jpg" alt="" width="1500" height="958" loading="lazy" aria-hidden="true">
    {% for image in carousel_images %}
      {% assign extension = image.extname | downcase %}
      {% unless image.path == featured_image_path %}
        {% if extension == ".jpg" or extension == ".jpeg" or extension == ".png" or extension == ".webp" or extension == ".avif" %}
          {% assign focal_class = "" %}
          {% case image.name %}
            {% when "falcon.jpg" %}{% assign focal_class = "landing-hero__image--focus-25" %}
            {% when "IMG_4362.jpg" %}{% assign focal_class = "landing-hero__image--focus-68" %}
            {% when "Predation Risk.jpg" %}{% assign focal_class = "landing-hero__image--focus-65" %}
            {% when "publications_block.jpg" %}{% assign focal_class = "landing-hero__image--focus-70" %}
            {% when "sparrowhawk-1.jpg" %}{% assign focal_class = "landing-hero__image--focus-35" %}
            {% when "wbsw.jpg" %}{% assign focal_class = "landing-hero__image--focus-35" %}
            {% when "wbsw2.jpg" %}{% assign focal_class = "landing-hero__image--focus-35" %}
            {% when "WhatsApp Image 2023-06-10 at 23.42.00.jpeg" %}{% assign focal_class = "landing-hero__image--focus-70" %}
          {% endcase %}
          <img class="landing-hero__image {{ focal_class }}" src="{{ image.path | relative_url | uri_escape }}" alt="" loading="lazy" aria-hidden="true"{% if image.name contains "Daniel_Leopoldsberger" %} data-credit="Photo: Daniel Leopoldsberger"{% endif %}>
        {% endif %}
      {% endunless %}
    {% endfor %}
  </div>
  <div class="landing-hero__shade"></div>
  <div class="landing-hero__content">
    <p class="eyebrow"></p>
    <h1 id="landing-title">Behaviour, Ecology & Evolution in a human-altered world</h1>
    <p class="landing-hero__statement">We study animals in human-altered environments, integrating across disciplines, from behaviour and physiology to ecology and evolution.</p>
    <p class="landing-hero__role">Global Change Research Institute - Rey Juan Carlos University (Madrid, Spain)</p>
    <a class="text-arrow text-arrow--light" href="/BeEcoEvo/">Explore the research <span aria-hidden="true">→</span></a>
  </div>
  <p class="landing-hero__credit" data-carousel-credit>Photo: Daniel Leopoldsberger</p>
</section>

<script src="{{ '/assets/js/landing-carousel.js' | relative_url }}" defer></script>

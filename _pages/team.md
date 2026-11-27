---
permalink: /team/
title: "The team"
layout: single
author_profile: false
classes: editorial-page people-page
excerpt: "Students and collaborators working across behavioural ecology, migration and environmental change."
---

<p class="page-intro">We have recently moved to Rey Juan Carlos University (Madrid, Spain) and are actively looking for students and fellows interested in working with us. Scroll to the bottom of the page and get in touch if our work and research systems are of your interest.</p>

<div class="people-intro">
  <p>Our work draws on movement ecology, field experiments, ecological genomics, acoustic monitoring, physiology, stable-isotope ecology and many other methods. We value collaborative, open, fair and supportive science, and welcome people with different personal and academic backgrounds. Everyone in the group is committed to following our <a href="/manifesto/">Diversity and Inclusion Manifesto</a>.</p>
  <p>Prospective fellows, PhD, MSc and BSc students, and interns are welcome to get in touch when their interests align with our research or methodological expertise.</p>
</div>

<header class="people-section-heading">
  <h2 id="current-researchers-and-students">Current researchers and students</h2>
  <p class="people-heading-note">Team members are listed alphabetically by first name.</p>
</header>

<div class="people-grid">
  {% for person in site.data.team.current %}
    <article class="person-card">
      {% if person.image %}
        <img src="{{ person.image | relative_url }}" alt="{{ person.alt }}" loading="lazy">
      {% else %}
        <div class="person-card__placeholder" aria-hidden="true"><span>{{ person.name | slice: 0 }}</span></div>
      {% endif %}
      <div class="person-card__body">
        <p class="eyebrow">{{ person.role }}</p>
        <h3>{{ person.name }}{% if person.pronouns %} <span class="person-card__pronouns">({{ person.pronouns }})</span>{% endif %}</h3>
        <p class="person-card__institution">{{ person.institution }}</p>
        <p>{{ person.description }}</p>
        {% if person.supervision %}<p class="person-card__supervision">{{ person.supervision }}</p>{% endif %}
        {% if person.profile_url %}<a class="text-arrow person-card__profile" href="{{ person.profile_url | relative_url }}">Full profile <span aria-hidden="true">→</span></a>{% endif %}
      </div>
    </article>
  {% endfor %}
</div>

## Past members

<ul class="compact-list">
  {% for person in site.data.team.past %}
    <li>
      {{ person.name }} · {{ person.degree }} {{ person.year }} · {{ person.institution }}
      {% if person.supervision %}<span class="past-member__supervision">{{ person.supervision }}</span>{% endif %}
    </li>
  {% endfor %}
</ul>

## Collaborators

<div class="collaborator-grid">
  {% for person in site.data.team.collaborators %}
    <div><strong>{{ person.name }}</strong><span>{{ person.institution }}</span></div>
  {% endfor %}
</div>

<aside class="callout callout--dark">
  <p class="eyebrow">Join us!</p>
  <h2>Interested in working with us?</h2>
  <p>We are always keen to hear from prospective collaborators, fellows, students and interns. Send us a short introduction describing your interests, experience and the kind of project or collaboration you have in mind.</p>
  <a class="text-arrow text-arrow--light" href="mailto:pablo.capilla@urjc.es">Get in touch <span aria-hidden="true">→</span></a>
</aside>

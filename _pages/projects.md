---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

<ul class="project-list">
  {% for project in site.projects reversed %}
    <li style="margin-bottom: 2em;">
      <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
      {% if project.image.feature %}
        <img src="{{ project.image.feature | relative_url }}" alt="{{ project.title }}" style="max-width: 300px;">
      {% endif %}
      <p>{{ project.excerpt }}</p>
      {% if project.links %}
        <p>
          {% for link in project.links %}
            <a href="{{ link.url }}" target="_blank" style="margin-right: 1em;">🔗 {{ link.label }}</a>
          {% endfor %}
        </p>
      {% endif %}
    </li>
  {% endfor %}
</ul>

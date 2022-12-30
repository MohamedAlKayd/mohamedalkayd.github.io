---
layout: page
title: Projects
permalink: /projects/
description: Completed Projects.
nav: true
nav_order: 2
display_categories: [Academic, Industry]
horizontal: false
---

<style>
.pictures{
width: 95%;
height: 5%:
}
</style>

<!-- pages/projects.md -->
<!-- <div class="projects"> -->
<!-- {%- if site.enable_project_categories and page.display_categories %}

  <!-- Display categorized projects -->
  <!-- {%- for category in page.display_categories %} -->
  <!-- <h2 class="category">{{ category }}</h2> -->
  <!-- {%- assign categorized_projects = site.projects | where: "category", category -%} -->
  <!-- {%- assign sorted_projects = categorized_projects | sort: "importance" %} --> -->

  <img src = "../assets/img/project_1.jpg" class="pictures"/>
  <br>  <br>
    <img src = "../assets/img/project_2.jpg" class="pictures"/>
  <br>  <br>
    <img src = "../assets/img/project_3.jpg" class="pictures"/>
  <br>  <br>
    <img src = "../assets/img/project_4.jpg" class="pictures"/>
  <br>  <br>
    <img src = "../assets/img/project_5.jpg" class="pictures"/>
  <br>  <br>
    <img src = "../assets/img/project_6.jpg" class="pictures"/>
  <br>  <br>
    <img src = "../assets/img/project_7.jpg" class="pictures"/>
  <br>  <br>
    <img src = "../assets/img/project_8.jpg" class="pictures"/>
  <br>  <br>
    <img src = "../assets/img/project_9.jpg" class="pictures"/>
  <br>  <br>
    <img src = "../assets/img/project_10.jpg" class="pictures"/>
  <br>  <br>

  <!-- Generate cards for each project -->
  <!-- {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %} -->

<!-- 
{%- else -%}
<!-- Display projects without categories -->
  <!-- {%- assign sorted_projects = site.projects | sort: "importance" -%}
  <!-- Generate cards for each project -->
  <!-- {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%} -->
<!-- {%- endif -%} -->
<!-- </div> -->
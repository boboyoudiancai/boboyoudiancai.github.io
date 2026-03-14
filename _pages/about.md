---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<div class="lang-toggle-wrap">
  <div class="lang-toggle" aria-label="Language switcher">
    <button type="button" class="lang-toggle__button" data-lang-switch="en" onclick="window.switchSiteLanguage && window.switchSiteLanguage('en'); return false;">EN</button>
    <button type="button" class="lang-toggle__button" data-lang-switch="zh" onclick="window.switchSiteLanguage && window.switchSiteLanguage('zh'); return false;">中文</button>
  </div>
</div>

<div class="lang-panel" data-lang-panel="en">
  {% capture home_content_en %}{% include home-content-en.html %}{% endcapture %}
  {{ home_content_en | markdownify }}
</div>

<div class="lang-panel" data-lang-panel="zh">
  {% capture home_content_zh %}{% include home-content-zh.html %}{% endcapture %}
  {{ home_content_zh | markdownify }}
</div>

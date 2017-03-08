{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Новости{% endblock %}

{% block head_imports %}
    <link rel="stylesheet" href="{{url_for('.static', filename='css/news/news.css')}}">
{% endblock %}


{% block maincontent %}


<h2>НОВОСТИ</h2>

<div class="news-list">
{% for s in news_list %}
<div onClick="document.location.href='{{ url_for('news:details', pk=s.id) }}'">
  <span class="width150 news-datebegin">
{{ s.datebegin|strftime('%Y/%m/%d %H:%M', 3) }}
  </span>
  <span class="">
<span class="news-name">{{ s.name }}</span>
<span class="news-description">{{ s.description }}</span>
  </span>
</div>
{% endfor %}
</div>

{% endblock %}



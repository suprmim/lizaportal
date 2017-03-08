{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары{% endblock %}
{% block head_imports %}
    <link rel="stylesheet" href="{{url_for('.static', filename='css/news/news-crud.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/news/news.css')}}">
{% endblock %}

{% block maincontent %}

<h2>НОВОСТИ, РЕДАКТИРОВАНИЕ</h2>

<a href="{{ url_for('news:crud_create') }}" class="common_button">СОЗДАТЬ</a>

<div class="news-crud-list">
{% for s in news_list %}
<div onClick="document.location.href='{{ url_for('news:crud_update', pk=s.id) }}'">
  <span class="width150 news-datebegin">
{{ s.datebegin|strftime('%Y/%m/%d %H:%M', 3) }}
  </span>
  <span class="">
<span class="news-name">{{ s.name }}</span>
<span class="news-description">{{ s.description }}</span>
  </span>
  <span class="width30">
    <a class="common_button" href="{{ url_for('news:crud_delete', pk=s.id) }}">
DEL
    </a>
  </span>
</div>
{% endfor %}
</div>

{% endblock %}



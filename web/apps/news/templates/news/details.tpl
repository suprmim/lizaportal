{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Новости{% endblock %}

{% block maincontent %}


<h2>НОВОСТЬ:
{{ news.name }}
</h2>


<a href="{{ url_for('news:list') }}" class="common_button">Назад</a>
<br>
<br>

Начало: {{ news.datebegin|strftime('%Y/%m/%d %H:%M', 3) }}<br>
<br>

{{ news.description }}<br>
<br>
{{ news.body }}


{% endblock %}


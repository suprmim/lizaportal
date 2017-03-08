{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары{% endblock %}

{% block maincontent %}


<h2>СЕМИНАРЫ</h2>


<a href="{{ url_for('seminars:list') }}" class="common_button">Назад</a>
<br>
<br>

{{ seminar.datebegin|strftime('%Y/%m/%d %H:%M', 3) }}<br>

{{ seminar.name }}<br>
{{ seminar.description }}<br>
{{ seminar.body }}

<br>
<br>
<a href="{{ url_for('seminars:list') }}" class="common_button">Записаться</a>

{% endblock %}


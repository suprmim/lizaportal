{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары{% endblock %}

{% block maincontent %}


<h2>СЕМИНАР:
{{ seminar.name }}
</h2>


<a href="{{ url_for('seminars:list') }}" class="common_button">Назад</a>
<br>
<br>

Начало: {{ seminar.datebegin|strftime('%Y/%m/%d %H:%M', 3) }}<br>
<br>

{{ seminar.description }}<br>
<br>
{{ seminar.body }}

<br>
<br>
{{ seminar.is_expired }}
<a href="{{ url_for('seminars:list') }}" class="common_button">Записаться</a>

{% endblock %}


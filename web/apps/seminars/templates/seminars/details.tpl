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
{% if user and not seminar.is_expired %}
    {% if seminar.user_assigned(user.id) %}
<a href="{{ url_for('seminars:unassign', pk=seminar.id) }}" class="common_button">Не приду</a>
    {% elif seminar.user_assigne_avalible %}
<a href="{{ url_for('seminars:assign', pk=seminar.id) }}" class="common_button">Записаться</a>
    {% endif %}
{% endif %}

{% endblock %}


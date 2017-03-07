{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Кабинет{% endblock %}

{% block maincontent %}

<br>
КАБИНЕТ
<br>
КАБИНЕТ
<br>
КАБИНЕТ
<br>
КАБИНЕТ
<br>
КАБИНЕТ

{% if "admin" in user_groups %}
    <a href="{{ url_for('seminars:crud_list') }}">СЕМИНАРЫ</a><br>
{% endif %}


{% endblock %}



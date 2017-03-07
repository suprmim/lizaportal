{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары{% endblock %}

{% block maincontent %}

<h2>СЕМИНАРЫ</h2>

<a href="{{ url_for('seminars:crud_create') }}" class="common_button">СОЗДАТЬ</a>

{% endblock %}



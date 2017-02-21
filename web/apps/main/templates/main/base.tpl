{% extends "bootstrap/base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Uni-Taxi Portal{% endblock %}
{%- block styles %}
    <!-- Bootstrap -->
    <link rel="stylesheet" type="text/css" href="{{ bootstrap_find_resource('css/bootstrap.css', cdn='bootstrap')}}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
{%- endblock styles %}

{% block navbar %}
    {% include 'main/navbar.tpl' %}
{% endblock navbar %}

{% block content %}
    <div class="container">
        {% block page_content %}{% endblock %}
    </div>

    {% include 'main/underground.tpl' %}
{% endblock %}

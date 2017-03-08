{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары{% endblock %}
{% block head_imports %}
    <link rel="stylesheet" href="{{url_for('.static', filename='css/seminars/seminars-crud.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/seminars/seminars.css')}}">
{% endblock %}

{% block maincontent %}

<h2>МОИ СЕМИНАРЫ</h2>

<a href="{{ url_for('seminars:crud_create') }}" class="common_button">СОЗДАТЬ</a>

<div class="seminars-crud-list">
{% for s in seminars %}
<div onClick="document.location.href='{{ url_for('seminars:crud_update', pk=s.id) }}'">
  <span class="width150 seminars-datebegin">
{{ s.datebegin|strftime('%Y/%m/%d %H:%M', 3) }}
  </span>
  <span class="">
<span class="seminars-name">{{ s.name }}</span>
<span class="seminars-setts">Записалось: 0/{{ s.capacity }}</span>
<span class="seminars-setts">Стоимость: {{ s.price }} руб</span>
<span class="seminars-description">{{ s.description }}</span>
  </span>
  <span class="width30">
    <a class="common_button" href="{{ url_for('seminars:crud_delete', pk=s.id) }}">
DEL
    </a>
  </span>
</div>
{% endfor %}
</div>

{% endblock %}



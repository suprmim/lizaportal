{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары{% endblock %}

{% block head_imports %}
    <link rel="stylesheet" href="{{url_for('.static', filename='css/seminars/seminars.css')}}">
{% endblock %}


{% block maincontent %}


<h2>{% if is_mylist %}МОИ {% endif %}СЕМИНАРЫ</h2>

<div class="seminars-list">
{% for s in seminars %}
<div onClick="document.location.href='{{ url_for('seminars:details', pk=s.Seminars.id) }}'">
  <span class="width150 seminars-datebegin">
{{ s.Seminars.datebegin|strftime('%Y/%m/%d %H:%M', 3) }}
  </span>
  <span class="">
<span class="seminars-name">{{ s.Seminars.name }}</span>
<span class="seminars-setts">Записалось: {{ s.assigned|int }}/{{ s.Seminars.capacity }}</span>
<span class="seminars-setts">Стоимость: {{ s.Seminars.price }} руб</span>
<span class="seminars-description">{{ s.Seminars.description }}</span>
  </span>
</div>
{% endfor %}
</div>

{% endblock %}



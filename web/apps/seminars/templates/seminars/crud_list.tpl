{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары{% endblock %}

{% block maincontent %}

<h2>СЕМИНАРЫ</h2>

<a href="{{ url_for('seminars:crud_create') }}" class="common_button">СОЗДАТЬ</a>

<table width="60%">
{% for s in seminars %}
<tr>
  <td>
{{ s.datebegin }}
  </td>
  <td>
<a href="{{ url_for('seminars:crud_update', pk=s.id) }}">
{{ s.name }}<br>
{{ s.description }}
</a>
  </td>
  <td>
<a class="common_button" href="{{ url_for('seminars:crud_delete', pk=s.id) }}">
DEL
</a>
  </td>
</tr>
{% endfor %}
</table>

{% endblock %}



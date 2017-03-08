{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары{% endblock %}

{% block maincontent %}


<h2>СЕМИНАРЫ</h2>


<table width="60%">
{% for s in seminars %}
<tr>
  <td>
{{ s.datebegin }}
  </td>
  <td>
<a href="{{ url_for('seminars:details', pk=s.id) }}">
{{ s.name }}<br>
{{ s.description }}
</a>
  </td>
</tr>
{% endfor %}
</table>


{% endblock %}



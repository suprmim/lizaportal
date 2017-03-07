{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары{% endblock %}

{% block maincontent %}

<br>
Семинары
<br>
Семинары
<br>
Семинары
<br>
Семинары
<br>
Семинары

<button onClick="top.document.location.href='{{ url_for('seminars:crud_create') }}'">СОЗДАТЬ</button>

{% endblock %}



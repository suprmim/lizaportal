{% if user %}
<div style="float: right; padding-left: 10px;" onClick="top.document.location.href='{{ url_for('auth:logout') }}'">Выход</div>
<div style="float: right; padding-left: 10px;" onClick="top.document.location.href='{{ url_for('auth:login') }}'">ЛК</div>
{% else %}
<div onClick="top.document.location.href='{{ url_for('auth:login') }}'">Войти</div>
{% endif %}

{% if user %}
<div class="site-auth-controls">
<span><a class="site-auth-login-bt" href="{{ url_for('my:cabinet') }}">ЛК</a></span>
<span><a class="site-auth-login-bt" href="{{ url_for('auth:logout') }}">Выход</a></span>
</div>
<div class="site-auth-fio">
{{ user.fio }}
</div>
{% else %}
<a class="site-auth-login-bt" href="{{ url_for('auth:login') }}">Войти</a>
{% endif %}

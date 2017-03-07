{% if user %}
<a class="site-auth-login-bt" href="{{ url_for('my:cabinet') }}">ЛК</a>
<a class="site-auth-login-bt" href="{{ url_for('auth:logout') }}">Выход</a>
{% else %}
<a class="site-auth-login-bt" href="{{ url_for('auth:login') }}">Войти</a>
{% endif %}

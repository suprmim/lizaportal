{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Авторизация{% endblock %}

{% block maincontent %}

<form name="auth" method="POST" action="{{ url_for('auth:login') }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
        <h2 style="margin-bottom: 1em;"> Авторизация </h2>
        <div class="common_input_field"><input type="text" class="common_input width250" placeholder="Логин" name="username" value="{{ form.data.username }}"></div>
        <div class="common_input_field"><input type="password" class="common_input width250" placeholder="Пароль" name="passwd"></div>
        <div class="common_input_field auth_btn_wrapper width300">
          <a class="common_button" href="{{ url_for('auth:register') }}">Регистрация</a>
          <button type="reset" class="common_button">Отмена</button>
          <button type="submit" class="common_button common_button_warn">Войти</button>
        </div>
</form>

Errors: {{ form.errors }}

{% endblock %}

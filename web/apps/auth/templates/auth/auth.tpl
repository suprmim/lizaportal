{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Авторизация{% endblock %}

{% block maincontent %}

<form name="auth" method="POST" action="{{ url_for('auth:login') }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
        <h2 style="margin-bottom: 1em;"> Авторизация </h2>
        <div><input type="text" class="auth_input" placeholder="Логин" name="username" value="{{ form.data.username }}"></div>
        <div><input type="password" class="auth_input" placeholder="Пароль" name="passwd"></div>
        <div class="auth_btn_wrapper">
          <button type="button" style="float: left;" class="btn btn-default auth_btn" onClick="top.document.location='{{ url_for('auth:register') }}';">Регистрация</button>
          <button type="reset" class="btn btn-default auth_btn">Отмена</button>
          <button type="submit" class="btn btn-default auth_btn_enter">Войти</button>
        </div>
</form>

Errors: {{ form.errors }}

{% endblock %}

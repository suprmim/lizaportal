
{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Регистрация{% endblock %}

{% block maincontent %}

<form name="auth" method="POST" action="{{ url_for('auth:register') }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">

        <h2 style="margin-bottom: 1em;"> Регистрация </h2>
        <h3>Необходимые регистрационные данные:</h3>
        <div><input type="text" class="auth_input" placeholder="Логин" name="username" value="{{ form.data.username }}"></div>
        <div><input type="text" class="auth_input" placeholder="Телефон" name="phone" value="{{ form.data.phone }}"></div>
        <div><input type="password" class="auth_input" placeholder="Пароль" name="passwd" value="{{ form.data.passwd }}"></div>
        <div><input type="password" class="auth_input" placeholder="Повторите пароль" name="passwd2" value="{{ form.data.passwd2 }}"></div>

        <h3>Личные данные пациента:</h3>
        <div><input type="text" class="auth_input" placeholder="Фамилия" name="surname" value="{{ form.data.surname }}"></div>
        <div><input type="text" class="auth_input" placeholder="Имя" name="name" value="{{ form.data.name }}"></div>
        <div><input type="text" class="auth_input" placeholder="Отчество" name="lastname" value="{{ form.data.lastname }}"></div>
        <div><input type="text" class="auth_input" placeholder="Электронный адрес" name="email" value="{{ form.data.email }}"></div>
        <div class="auth_btn_wrapper">

          <button type="reset" style="float: left;" class="btn btn-default auth_btn">Отмена</button>
          <button type="submit" class="btn btn-default auth_btn_enter">Зарегистрировать</button>
        </div>

</form>

Errors: {{ form.errors }}

{% endblock %}



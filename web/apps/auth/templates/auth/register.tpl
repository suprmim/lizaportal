
{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Регистрация{% endblock %}

{% block maincontent %}

<form name="auth" method="POST" action="{{ url_for('auth:register') }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">

        <h2 style="margin-bottom: 1em;"> Регистрация </h2>
        <h3>Необходимые регистрационные данные:</h3>
        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Логин" name="username" value="{{ form.data.username }}"></div>
        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Телефон" name="phone" value="{{ form.data.phone }}"></div>
        <div class="common_input_field"><input type="password" class="common_input width300" placeholder="Пароль" name="passwd" value="{{ form.data.passwd }}"></div>
        <div class="common_input_field"><input type="password" class="common_input width300" placeholder="Повторите пароль" name="passwd2" value="{{ form.data.passwd2 }}"></div>

        <h3>Личные данные пациента:</h3>
        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Фамилия" name="surname" value="{{ form.data.surname }}"></div>
        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Имя" name="name" value="{{ form.data.name }}"></div>
        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Отчество" name="lastname" value="{{ form.data.lastname }}"></div>
        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Электронный адрес" name="email" value="{{ form.data.email }}"></div>
        <div class="auth_btn_wrapper common_input_field width300">

          <button type="reset" style="float: left;" class="common_button">Отмена</button>
          <button type="submit" class="common_button common_button_warn">Зарегистрировать</button>
        </div>

</form>

Errors: {{ form.errors }}

{% endblock %}



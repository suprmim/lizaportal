{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Кабинет{% endblock %}

{% block maincontent %}

<h2>ЛИЧНЫЙ КАБИНЕТ</h2>


<div class="common-small-header" style="margin-top: 20px; margin-bottom: 0px;">Общие:</div>
<ul class="cabinet_control_buttons">
  <li>
    <a href="#" class="common_button_disabled">Записаться</a><br>
  </li>
  <li>
    <a href="#" class="common_button_disabled">Мои записи</a><br>
  </li>
  <li>
    <a href="#" class="common_button_disabled">Мои семинары</a><br>
  </li>
</ul>


<div class="common-small-header" style="margin-top: 20px; margin-bottom: 0px;">Настройки:</div>
<ul class="cabinet_control_buttons">
  <li>
    <a href="#" class="common_button_disabled">Анкета</a><br>
  </li>
  <li>
    <a href="#" class="common_button_disabled">Сменить пароль</a><br>
  </li>
  <li>
    <a href="#" class="common_button_disabled">Сменить E-Mail</a><br>
  </li>
</ul>


{% if "admin" in user_groups %}
<div class="common-small-header" style="margin-top: 20px; margin-bottom: 0px;">Контент:</div>
<ul class="cabinet_control_buttons">
  <li>
    <a href="#" class="common_button_disabled">Новости</a><br>
  </li>
  <li>
    <a href="{{ url_for('seminars:crud_list') }}" class="common_button">Семинары</a><br>
  </li>
  <li>
    <a href="#" class="common_button_disabled">Статьи</a><br>
  </li>
</ul>
{% endif %}


{% if "admin" in user_groups %}
<div class="common-small-header" style="margin-top: 20px; margin-bottom: 0px;">Управление:</div>
<ul class="cabinet_control_buttons">
  <li>
    <a href="#" class="common_button_disabled">Пользователи</a><br>
  </li>
</ul>
{% endif %}

{% endblock %}



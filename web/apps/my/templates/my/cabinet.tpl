{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Кабинет{% endblock %}

{% block maincontent %}

<h2>ЛИЧНЫЙ КАБИНЕТ</h2>

<ul class="cabinet_control_buttons">
  <li>
    <a href="#" class="common_button">АНКЕТА</a><br>
  </li>
  <li>
    <a href="#" class="common_button">СМЕНИТЬ ПАРОЛЬ</a><br>
  </li>
  <li>
    <a href="#" class="common_button">СМЕНИТЬ E-MAIL</a><br>
  </li>
</ul>

{% if "admin" in user_groups %}
<div class="common-small-header" style="margin-top: 20px; margin-bottom: 0px;">Контент:</div>
<ul class="cabinet_control_buttons">
  <li>
    <a href="#" class="common_button">СТАТЬИ</a><br>
  </li>
  <li>
    <a href="#" class="common_button">НОВОСТИ</a><br>
  </li>
  <li>
    <a href="{{ url_for('seminars:crud_list') }}" class="common_button">СЕМИНАРЫ</a><br>
  </li>
</ul>
{% endif %}


{% if "admin" in user_groups %}
<div class="common-small-header" style="margin-top: 20px; margin-bottom: 0px;">Управление:</div>
<ul class="cabinet_control_buttons">
  <li>
    <a href="#" class="common_button">ПОЛЬЗОВАТЕЛИ</a><br>
  </li>
</ul>
{% endif %}

{% endblock %}



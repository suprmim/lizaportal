{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Кабинет{% endblock %}

{% block maincontent %}

<h2>ЛИЧНЫЙ КАБИНЕТ</h2>

<ul class="cabinet_control_buttons">
  <li>
    <a href="#" class="common_button">АНКЕТА</a><br>
  </li>
  <li>
    <a href="#" class="common_button">СМНИТЬ ПАРОЛЬ</a><br>
  </li>

{% if "admin" in user_groups %}
  <li>
    <a href="{{ url_for('seminars:crud_list') }}" class="common_button">СЕМИНАРЫ</a><br>
  </li>
{% endif %}

</ul>


{% endblock %}



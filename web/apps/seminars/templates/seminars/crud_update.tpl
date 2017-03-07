{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары: редактирование{% endblock %}

{% block maincontent %}


{% if object %}
<h2>СЕМИНАРЫ: РЕДАКТИРОВАНИЕ</h2>
<form name="auth" method="POST" action="{{ url_for('seminars:crud_update', pk=object.pk) }}">
{% else %}
<h2>СЕМИНАРЫ: НОВЫЙ</h2>
<form name="auth" method="POST" action="{{ url_for('seminars:crud_create') }}">
{% endif %}
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">

        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Название" name="name" value="{{ form.data.name }}"></div>
        <div class="common_input_field"><textarea type="text" class="common_input width300" placeholder="Краткое описание" name="description">{{ form.data.description }}</textarea></div>
        <div class="common_input_field"><textarea type="text" class="common_input width300" placeholder="Описание" name="body">{{ form.data.body }}</textarea></div>

        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Цена" name="price" value="{{ form.data.price }}"></div>
        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Количество мест" name="capacity" value="{{ form.data.capacity }}"></div>
        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Начало" name="date_begin" value="{{ form.data.date_begin }}"></div>
        <div class="common_input_field common_btn_wrapper width300">
          <button type="reset" class="common_button">Отмена</button>
          <button type="submit" class="common_button common_button_warn">Сохранить</button>
        </div>

</form>

Errors: {{ form.errors }}



{% endblock %}


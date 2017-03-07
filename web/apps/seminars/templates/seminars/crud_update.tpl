{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары: редактирование{% endblock %}

{% block maincontent %}


{% if object %}
<form name="auth" method="POST" action="{{ url_for('seminars:crud_update', pk=object.pk) }}">
{% else %}
<form name="auth" method="POST" action="{{ url_for('seminars:crud_create') }}">
{% endif %}
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">

        <h2 style="margin-bottom: 1em;"> Редактирование семинара</h2>
        <div><input type="text" class="common_input" placeholder="Название" name="name" value="{{ form.data.name }}"></div>
        <div><textarea type="text" class="common_input" placeholder="Краткое описание" name="description">{{ form.data.description }}</textarea></div>
        <div><textarea type="text" class="common_input" placeholder="Описание" name="body">{{ form.data.body }}</textarea></div>

        <div><input type="text" class="common_input" placeholder="Цена" name="price" value="{{ form.data.price }}"></div>
        <div><input type="text" class="common_input" placeholder="Количество мест" name="capacity" value="{{ form.data.capacity }}"></div>
        <div><input type="text" class="common_input" placeholder="Начало" name="date_begin" value="{{ form.data.date_begin }}"></div>
        <div class="common_btn_wrapper">
          <button type="reset" style="float: left;" class="btn btn-default auth_btn">Отмена</button>
          <button type="submit" class="btn btn-default auth_btn_enter">Сохранить</button>
        </div>

</form>

Errors: {{ form.errors }}



{% endblock %}


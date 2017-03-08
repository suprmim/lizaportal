{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Семинары: редактирование{% endblock %}

{% block maincontent %}


{% if object %}
<h2>НОВОСТЬ: РЕДАКТИРОВАНИЕ</h2>
<form name="auth" method="POST" action="{{ url_for('news:crud_update', pk=object.id) }}">
{% else %}
<h2>НОВОСТЬ: НОВАЯ</h2>
<form name="auth" method="POST" action="{{ url_for('news:crud_create') }}">
{% endif %}
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">

        <div class="common_input_field"><input type="text" class="common_input width300" placeholder="Название" name="name" value="{{ form.data.name }}"></div>
        <div class="common_input_field"><textarea type="text" class="common_input width300" placeholder="Краткое описание" name="description">{{ form.data.description }}</textarea></div>
        <div class="common_input_field"><textarea type="text" class="common_input width300" placeholder="Описание" name="body">{{ form.data.body }}</textarea></div>

        <div class="common_input_field"><input type="text" class="js-date_begin common_input width300" placeholder="Начало" name="datebegin" value="{{ form.data.datebegin|strftime('%Y/%m/%d %H:%M', 3) }}"></div>
        <div class="common_input_field common_btn_wrapper width300">
          <a href="{{ url_for('news:crud_list') }}" class="common_button">Назад</a>
          <button type="reset" class="common_button">Отмена</button>
          <button type="submit" class="common_button common_button_warn">Сохранить</button>
        </div>

</form>

Errors: {{ form.errors }}

<script>

$( document ).ready(function() {

        $('.js-date_begin').periodpicker({
            inline: false,

            norange: true, // use only one value
            cells: [1, 1], // show only one month

            todayButton: true,
            formatDateTime: 'YYYY/MM/DD HH:mm',
            yearsLine: false,

            clearButton: false,
            okButton: false,
            closeAfterClear: true,
            draggable: false,
            mousewheel: true,

            resizeButton: false, // deny resize picker
            lang: 'ru',
            animation: true,
            showTimepickerInputs: false,
            showDatepickerInputs: false,
            hideAfterSelect: true,
            hideOnBlur: true,
            likeXDSoftDateTimePicker: true,

            fullsizeButton: false,
            fullsizeOnDblClick: false,


            timepicker: true, // use timepicker
            timepickerOptions: {
                steps: [1, 5, 2, 1],
                hours: true,
                minutes: true,
                seconds: false,
                ampm: false,
                clickAndSelect: true,
                saveOnChange: true,
                listenKeyPress: true,
                //onChange: function(e) {
                //    return false;
                //},
                twelveHoursFormat: false
            }

        }).on('keydown', function(e) {
            $(this).periodpicker('change');
        });

});


</script>


{% endblock %}


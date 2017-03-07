{% extends "index.tpl" %}

{% block title %}OSTEOLA.RU Подтверждение регистрации{% endblock %}

{% block maincontent %}

{% if error == 'validated' %}
    Учетная запись уже подтверждена!
[
<a href="{{ url_for('index:index') }}" class="common_button">На главную</a>
]

{% elif error and error != 'notexpired' %}
    {% if error == 'expired' %}
<p>Код подтверждения просрочен!</p>
<p>Он действует только в течении часа!</p>
    {% elif error == 'wrong' %}
Не верный код подтверждения!
    {% elif error == 'notvalidated' %}
Ваша учетная запись не подтверждена!
    {% endif %}
[
<a href="{{ url_for('auth:revalidate') }}" class="common_button">Отправить новый код подтверждения</a>
]

{% else %}
    {% if error == 'notexpired' %}
<p>Предыдущий код подтверждения еще действует! </p>
<p>Он действует в течении часа!</p>
<br>
    {% endif %}
<p>
Введите код подтверждения: <input type="text" id="validation_code">
<input type="button" class="common_button" value="Подтвердить" onClick="location.href='{{ url_for('auth:validate') }}/'+top.document.getElementById('validation_code').value;">
</p>

<br>
<p>
[
<a href="{{ url_for('auth:revalidate') }}" class="common_button">Отправить новый код подтверждения</a>
]
</p>

{% endif %}
{% endblock %}

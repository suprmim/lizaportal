<html>
<body>

{% if error == 'validated' %}
    Your account allready validated!
[
<a href="{{ url_for('index:index') }}">Go to main page</a>
]

{% elif error and error != 'notexpired' %}
    {% if error == 'expired' %}
Your validation code is expired!
    {% elif error == 'wrong' %}
Your validation code is wrong!
    {% elif error == 'notvalidated' %}
Your account not validated!
    {% endif %}
[
<a href="{{ url_for('auth:revalidate') }}">Get new validation code</a>
]

{% else %}
    {% if error == 'notexpired' %}
        Your token is not expired yet!
    {% endif %}
Enter validation code: <input type="text" id="validation_code">
<input type="button" value="Validate!" onClick="location.href='{{ url_for('auth:validate') }}/'+top.document.getElementById('validation_code').value;">

[
<a href="{{ url_for('auth:revalidate') }}">Get new validation code</a>
]

{% endif %}
</body>
</html>

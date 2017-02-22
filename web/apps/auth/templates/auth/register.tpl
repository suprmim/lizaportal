
<html>
<body>
<form name="auth" method="POST" action="{{ url_for('auth:register') }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
Username: <input type="text" name="username" value="{{ form.data.username }}">
<br>
Password: <input type="password" name="passwd" value="{{ form.data.passwd }}">
<br>
Retype password: <input type="password" name="passwd2" value="{{ form.data.passwd2 }}">
<br>
Email: <input type="text" name="email" value="{{ form.data.email }}" >
<br>
Name, Surname: <input type="text" name="fio" value="{{ form.data.fio }}">
<br>
<input type="submit" name="REGISTER!">
</form>

Errors: {{ form.errors }}
</body>
</html>


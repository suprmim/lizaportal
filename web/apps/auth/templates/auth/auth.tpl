
<html>
<body>
<form name="auth" method="POST" action="{{ url_for('auth:login') }}">
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
Username: <input type="text" name="username">
<br>
Password: <input type="password" name="passwd">
<br>
<input type="submit" name="Ok">
</form>

Errors: {{ form.errors }}
</body>
</html>

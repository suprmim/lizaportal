<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="description" content="Pushy is an off-canvas navigation menu for your website.">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">

    <link rel="stylesheet" href="{{url_for('.static', filename='css/normalize.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/index.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/common.css')}}">
    <!--link rel="stylesheet" href="{{url_for('.static', filename='css/menu.css')}}"-->
    <!--link rel="stylesheet" href="{{url_for('.static', filename='css/button.css')}}"-->
    <link rel="stylesheet" href="{{url_for('.static', filename='css/jquery.periodpicker.min.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/jquery.timepicker.min.css')}}">

    <script src="{{ url_for('.static', filename='js/jquery.min.js') }}"></script>
    <script src="{{ url_for('.static', filename='js/jquery.periodpicker.full.min.js') }}"></script>
    <script src="{{ url_for('.static', filename='js/jquery.timepicker.min.js') }}"></script>
    <title>
{% block title %}OSTEOLA.RU Портал{% endblock %}
    </title>

  </head>
  <body>
    <div class="wrapper">
      <div class="header">
        <div class="header-top-line">
          <div class="site-logo">
              <a href="{{ url_for('index:index') }}"><img src="{{url_for('.static', filename='img/logo.png')}}"></a>
          </div>
          <div class="site-contacts">
            <span>УЛ. МАРШАЛА РОКОССОВСКОГО, 35</span>
            <span>C 10:00 ДО 22:00-7 </span>
            <span class="site-contacts-phone"><a href="#">+7 (495) 785 90 89</a></span>
          </div>
          <div class="site-auth-wrapper">
          {% include "authed.tpl" %}
          </div>
        </div>

        <ul class="header-menu">
          <li class="header-menu-button">
            <a href="#">
              <span>
Новости
              </span>
            </a>
          </li>

          <li class="header-menu-button">
            <a href="#">
              <span>
Контакты
              </span>
            </a>
          </li>

          <li class="header-menu-button">
            <a href="{{ url_for('seminars:list') }}">
              <span>
Семинары
              </span>
            </a>
          </li>

          <li class="header-menu-button">
            <a href="#">
              <span>
Статьи
              </span>
            </a>
          </li>




        </ul>
      </div>
      <br> 

      <div class="site-content">
        {% block maincontent %}{% endblock %}
      </div>                                            <!-- Close for <div class="site-content"> -->
      <div class="pusher"></div>
    </div>                                              <!-- Close for <div class="wrapper"> -->
    <div class="footer">
      <div style="float: right; padding: 20px; color: #ffffff; font-weight: bolder;">
        ProGroup, 2017.
      </div>
    </div>

  </body>
</html>

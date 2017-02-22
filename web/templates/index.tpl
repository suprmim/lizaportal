<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="{{ url_for('.static', filename='css/menu.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('.static', filename='css/search.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('.static', filename='css/button.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('.static', filename='css/modal.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('.static', filename='css/main.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('.static', filename='css/auth.css') }}">

    <script src="{{ url_for('.static', filename='js/jquery.min.js') }}"></script>
    <script src="{{ url_for('.static', filename='js/modal.js') }}"></script>
    <title>
{% block title %}OSTEOLA.RU Портал{% endblock %}
    </title>

  </head>

  <body>

    <div id="modal-window" class="modal-window" keyboard="true">
      <div class="window-container animation">
        <div class="close">&times;</div>
          <form>
            <div><input type="text" class="modal_input" placeholder="Логин"></div>
            <div><input type="text" class="modal_input" placeholder="Пароль"></div>
            <div class="modal_btn_wrapper">
              <button type="submit" class="btn btn-default modal_btn_enter">Войти</button>
              <button type="submit" class="btn btn-default modal_btn">Отмена</button>
              <button type="submit" style="padding: 0.1em; margin-top: 1em;" class="btn modal_btn">Вспомнить пароль</button>
            </div>
          </form>
        </div>
      </div>

      <div class="wrapper">
        <div id="wrap">
          <nav id="menu-wrap">
            <ul id="menu">
              <li><a href="">Семинары</a></li>
              <li><a href="">Записаться на прием</a>
                <ul>
                  <li><a href="">Мои записи</a><li>
                  <li><a href="">ЛФК</a><li>
                  <li><a href="">Остеопат</a><li>
                </ul>
              </li>
              <li><a href="">Цены</a></li>
              <li><a href="">Контакты</a></li>
              <li><a href="">О клинике</a>
                <ul>
                  <li><a href="">Новости</a><li>
                  <li><a href="">FAQ</a><li>
                  <li><a href="">Форум</a><li>
                  <li><a href="">Отзывы</a><li>
                  <li><a href="">Помощь</a><li>
                </ul>
              </li>
              <li style="border-right: 0em; -moz-box-shadow: 0em 0 0; -webkit-box-shadow: 0em 0 0; box-shadow: 0em 0 0; margin: 0.2em 0em 0em 0em;"><a style="padding: 0.5em 0em 0em 1em;">
                <form class="search">
                  <div class="form-group">
                    <input type="text" class="form-control" placeholder="Поиск">
                    <button type="submit" class="btn btn-default">Найти</button>
                  </div>
                </form>
              </a></li>
              <li style="font-style: italic; border-right: 0em; padding: 0.2em 0em 0em 1em; -moz-box-shadow: 0em 0 0; -webkit-box-shadow: 0em 0 0; box-shadow: 0em 0 0;"><a style="padding: 0.3em 0em 0em 1em; font-style: italic;">
                <div style="font-size: 1.2em;">
                  ул. Маршала Рокоссовского, 35
                </div>
                <div>
                  <span style="padding-right: 3em;">c 10:00 до 22:00</span><span style="font-size: 1.3em;">+7 (495) 785 90 89</span>
                </div>
              </a></li>
              <li style="margin: 0.8em 1em 1em 1.8em; font-style: italic; border-right: 0em; -moz-box-shadow: 0em 0 0; -webkit-box-shadow: 0em 0 0; box-shadow: 0em 0 0;"><a style="padding: 0.3em 0em 0em 0.7em; font-size: 0.85em;" href="#modal-window" class="open-window">
{% include "authed.tpl" %}
              </a></li>
            </ul>
          </nav>
        </p>
      </div>

      <div class="site-content">
{% block maincontent %}{% endblock %}
      </div>

      <div class="pusher"></div>
    </div>                                            <!-- Close for <div class="wrapper"> -->
    <div class="footer">footer</div>
  </body>
</html>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>Osteola</title>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="description" content="Pushy is an off-canvas navigation menu for your website.">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">

    <link rel="stylesheet" href="{{url_for('.static', filename='css/normalize.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/index.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/menu.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/button.css')}}">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>

  </head>
  <body>
    <div class="wrapper">
      <div class="site-content">

        <!-- Pushy Menu -->
        <nav class="pushy pushy-left" data-focus="#first-link">
          <div class="pushy-content">
            <ul>
              <li class="pushy-submenu">
                <button id="first-link">Семинары</button>
                <ul>
                  <li class="pushy-link"><a href="#">Мои семинары</a></li>
                  <li class="pushy-link"><a href="#">Предстоящие</a></li>
                  <li class="pushy-link"><a href="#">История</a></li>
                </ul>
              </li>
              <li class="pushy-submenu">
                <button>Записаться на прием</button>
                <ul>
                  <li class="pushy-link"><a href="#">Врачи</a></li>
                  <li class="pushy-link"><a href="#">Мои записи</a></li>
                  <li class="pushy-link"><a href="#">Отменить</a></li>
                </ul>
              </li>
              <li class="pushy-submenu">
                <button>О клинике</button>
                <ul>
                  <li class="pushy-link"><a href="#">Новости</a></li>
                  <li class="pushy-link"><a href="#">FAQ</a></li>
                  <li class="pushy-link"><a href="#">Форум</a></li>
                  <li class="pushy-link"><a href="#">Отзывы</a></li>
                  <li class="pushy-link"><a href="#">Помощь</a></li>
                </ul>
              </li>
              <li class="pushy-link"><a href="#">Цены</a></li>
              <li class="pushy-link"><a href="#">Контакты</a></li>
              <li class="pushy-link"><a href="#">Соискателям</a></li>
            </ul>
          </div>
        </nav>
        <!-- Pushy Menu -->

        <div id="container">
          <button class="menu-btn">&#9776; Menu</button>
        </div>
        <div class="header" style="background-color: blue; overflow: hidden; padding: 1.55%;">
          <div style="float: right; margin: 0.5% 0.5% 0% 2%; color: #003366; font-weight: bolder; cursor: pointer;">
            Войти
          </div>
          <div style="float: right; margin: 0% 0% 0% 0.5%; color: #003366; font-style: italic;">
            <div>
              УЛ. МАРШАЛА РОКОССОВСКОГО, 35
            </div>
            <div>
              <span style="float: left; font-size: 0.8em;">C 10:00 ДО 22:00-7</span> <span style="float: right;">+7 (495) 785 90 89</span>
            </div>
          </div>
          <div style="float: right; width: 35%; text-align: center;">
            <input type="text" placeholder="Найти" style="padding: 5px; border-radius: 10px; width: 75%;">
            <button type="submit" class="btn btn-default">Найти</button>
          </div>
          <div style="float: right; margin: 0.5% 1% 0% 1%; color: #003366; font-weight: bolder; cursor: pointer;">
            О клинике
          </div>
          <div style="float: right; margin: 0.5% 1% 0% 1%; color: #003366; font-weight: bolder; cursor: pointer;">
            Цены
          </div>
          <div style="float: right; margin: 0.5% 1% 0% 1%; color: #003366; font-weight: bolder; cursor: pointer;">
            Записаться
          </div>
          <div style="float: right; margin: 0.5% 1% 0% 1%; color: #003366; font-weight: bolder; cursor: pointer;">
            Семинары
          </div>
          <div style="background-color: lime; float: right; margin: 2px;">
          </div>
        </div>
        <br> 
        AAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<br>
        AAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<br>
        AAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<br>
        AAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<br>

        <!-- Pushy JS -->
        <script type="text/javascript" src="{{url_for('.static', filename='js/pushy.min.js') }}"></script>

      </div>                                            <!-- Close for <div class="site-content"> -->
      <div class="pusher"></div>
    </div>                                              <!-- Close for <div class="wrapper"> -->
    <div class="footer">
      <div style="float: right; padding: 20px; color: #330099; font-weight: bolder;">
        ProGroup, 2017.
      </div>
    </div>

  </body>
</html>

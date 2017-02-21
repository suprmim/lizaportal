<!DOCTYPE html>
<html>

  <head>

    <title>MyPortal</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">

    <link rel="stylesheet" href="{{url_for('.static', filename='css/bootstrap-theme.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/bootstrap-theme.min.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/bootstrap.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/bootstrap.min.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/ie10-viewport-bug-workaround.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/navbar.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/variables.css')}}">
    <link rel="stylesheet" href="{{url_for('.static', filename='css/styles.css')}}">

    <script src="{{url_for('.static', filename='js/bootstrap.min.js') }}"></script>

    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link href='http://fonts.googleapis.com/css?family=Varela+Round' rel='stylesheet' type='text/css'>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.13.1/jquery.validate.min.js"></script>

    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />

    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->

  </head>

  <body>

    <div class="wrapper container">

      <div class="row">
        <section class="col-md-20">

          <div class="row">

      <!-- Static navbar -->
      <nav class="navbar navbar-default">
        <div class="container-fluid">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Project name</a>
          </div>
          <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#">About</a></li>
              <li><a href="#">Contact</a></li>
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                <ul class="dropdown-menu">
                  <li><a href="#">Action</a></li>
                  <li><a href="#">Another action</a></li>
                  <li><a href="#">Something else here</a></li>
                  <li role="separator" class="divider"></li>
                  <li class="dropdown-header">Nav header</li>
                  <li><a href="#">Separated link</a></li>
                  <li><a href="#">One more separated link</a></li>
                </ul>
              </li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
              <li class="active"><a href="./">Default <span class="sr-only">(current)</span></a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div><!--/.container-fluid -->
      </nav>

          </div>

          <div class="row">
            <form name="search" action="#" method="get" class="form-inline form-search pull-right">
              <div class="input-group">
                <label class="sr-only" for="searchInput">Search</label>
                <input class="form-control" id="searchInput" type="text" name="search" placeholder="Search">
                <div class="input-group-btn">
                  <button type="submit" class="btn btn-search ">.</button>
                </div>
              </div>
            </form>
          </div>

        </section>

        <section class="col-md-4">

          <div class="wrapper" style="padding-bottom: 0px;">
            <form class="form-signin">

              <div class="form-group" style="margin: 0px 0px 5px 0px;">
                <select class="selectpicker form-control" style="color: #666666; height: 20px; margin: 0px; padding: 0px;">
                  <option>Москва</option>
                  <option>Ногинск</option>
                  <option>Сочи</option>
                </select>
              </div>




              <input type="text" class="form-control" name="username" placeholder="Email Address" required="" autofocus="" />
              <input type="password" class="form-control" name="password" placeholder="Password" required="" />
              <label class="checkbox">
                <input type="checkbox" value="remember-me" id="rememberMe" name="rememberMe"> Remember me
              </label>
              <button class="btn btn-lg btn-primary" type="submit">Ok</button>
            </form>
          </div>

        </section>

      </div>


      <div class="row" style="padding: 5% 0% 0% 0%;">
        <section class="col-md-14" style='text-align: left; cursor: pointer;'>
            <img src="../../../../static/img/transport.png" style="width: 60%;"></img>
        </section>

        <section class="col-md-9" style='text-align: right; cursor: pointer;'>
            <img src="../../../../static/img/hotel.png" style="width: 60%;"></img>
        </section>

      </div>

      <div class="row">
        <section class="col-md-22" style='text-align: center; cursor: pointer; padding: 3% 0% 0% 0%;'>
            <img src="../../../../static/img/zap.png" style="width: 30%;"></img>
        </section>
      </div>


    </div>

    <div id="footer">
      <div class="container">
        <div class="row">
        <p class="text-muted">Some contacts.</p>
        </div>
      </div>
    </div>
    <script>window.jQuery || document.write('<script src="../../../../assets/js/jquery.min.js"><\/script>')</script>

  </body>

</html>

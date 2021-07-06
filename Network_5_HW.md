
# Продемонстрировать работу протоколов прикладного уровня HTTP и SMTP при помощи программы telnet:

### 1.Отправить GET запрос удаленному серверу.

```
nuacho@nuacho-VirtualBox:~$ telnet 84.201.154.44 9292
Trying 84.201.154.44...
Connected to 84.201.154.44.
Escape character is '^]'.
GET / HTTP/1.1
Host: 84.201.154.44

HTTP/1.1 200 OK
Content-Type: text/html;charset=utf-8
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Set-Cookie: rack.session=BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiRWMzMGFhM2FlNGY2OGRlNzJiMTgy%0AMzAxZjczNDBmNjQzYzAxZjIxYWY0N2Y0NDllOTZiMDJmZDdlM2MwYTcwYTQG%0AOwBGSSIJY3NyZgY7AEZJIjF6bVZEbEhYTVJDWCtiektrR3ZpNWIxNUNnK1hZ%0Aa1ZHYlpKbUN2aDkzZDlFPQY7AEZJIg10cmFja2luZwY7AEZ7B0kiFEhUVFBf%0AVVNFUl9BR0VOVAY7AFRJIi1kYTM5YTNlZTVlNmI0YjBkMzI1NWJmZWY5NTYw%0AMTg5MGFmZDgwNzA5BjsARkkiGUhUVFBfQUNDRVBUX0xBTkdVQUdFBjsAVEki%0ALWRhMzlhM2VlNWU2YjRiMGQzMjU1YmZlZjk1NjAxODkwYWZkODA3MDkGOwBG%0A--409c45da123dbd79657a549453ec03b96f4a1c49; path=/; HttpOnly
Content-Length: 2908

<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<meta content='IE=Edge,chrome=1' http-equiv='X-UA-Compatible'>
<meta content='width=device-width, initial-scale=1.0' name='viewport'>
<title>Monolith Reddit :: All posts</title>
<link crossorigin='anonymous' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css' integrity='sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7' rel='stylesheet' type='text/css'>
<link crossorigin='anonymous' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css' integrity='sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r' rel='stylesheet' type='text/css'>
<script crossorigin='anonymous' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js' integrity='sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS'></script>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script>
</head>
<body>
<div class='navbar navbar-default navbar-static-top'>
<div class='container'>
<div class='navbar-header'>
<button class='navbar-toggle' data-target='.navbar-responsive-collapse' data-toggle='collapse' type='button'>
<span class='icon-bar'></span>
<span class='icon-bar'></span>
<span class='icon-bar'></span>
</button>
<a class='navbar-brand' href='/'>Monolith Reddit</a>
</div>
<div class='navbar-collapse collapse'>
<ul class='nav navbar-nav navbar-right'>
<li>
<a href='/signup'>Sign up</a>
</li>
<li>
<a href='/login'>Login</a>
</li>
</ul>
</div>
</div>
</div>
<div class='container'>
<div class='row'>
<div class='col-lg-9'>
<div id='postlist'>
<div class='panel'>
<div class='panel-heading'>
<div class='text-center'>
<div class='row'>
<div class='col-sm-1'>
<form action='/post/60e1e7ea7342450d66bfe6da/vote/1' id='form-upvote' method='post'>
<input name='_method' type='hidden' value='put'>
<button class='btn btn-default btn-sm' type='submit'>
<span class='glyphicon glyphicon-menu-up'></span>
</button>
</form>
<h4 class='pull-center'>0</h4>
<form action='/post/60e1e7ea7342450d66bfe6da/vote/-1' id='form-downvote' method='post'>
<input name='_method' type='hidden' value='put'>
<button class='btn btn-default btn-sm' type='submit'>
<span class='glyphicon glyphicon-menu-down'></span>
</button>
</form>
</div>
<div class='col-sm-8'>
<h3 class='pull-left'>
<a href='/post/60e1e7ea7342450d66bfe6da'>Test</a>
</h3>
</div>
<div class='col-sm-3'>
<h4 class='pull-right'>
<small>
<em>04-07-2021</em>
<br>16:55</br>
</small>
</h4>
</div>
</div>
</div>
</div>
<div class='panel-footer'>
<a class='btn btn-link' href='http://yandex.ru'>Go to the link</a>
</div>
</div>
</div>

</div>
<div class='col-lg-3'>
<div class='well sidebar-nav'>
<h3>Menu</h3>
<ul class='nav nav-list'>
<li>
<a href='/'>All posts</a>
</li>
<li>
<a href='/new'>New post</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</body>
</html>
Connection closed by foreign host.

```

### 2. Отправить POST запрос удаленному серверу.
```
nuacho@nuacho-VirtualBox:~$ telnet getpost.itgid.info 80
Trying 185.104.45.14...
Connected to getpost.itgid.info.
Escape character is '^]'.
POST /index2.php?auth=DdC33D7d2C2a7&action=1 HTTP/1.1
Host: getpost.itgid.info

HTTP/1.1 200 OK
Server: nginx
Date: Sun, 04 Jul 2021 20:14:46 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
Access-Control-Allow-Origin: *
x-ray: p17866:19.000/wn26928:0.000/wa26928:D=7642

5
hello
0

```

### 3. Отправить письмо самому себе.
```
serg@quantori:~$ telnet mx.yandex.ru 25
Trying 77.88.21.249...
Connected to mx.yandex.ru.
Escape character is '^]'.
220 sas1-fa9d05dd56ad.qloud-c.yandex.net (Want to use Yandex.Mail for your domain? Visit http://pdd.yandex.ru)
helo host
250 sas1-fa9d05dd56ad.qloud-c.yandex.net
mail from: sapr-m@yandex.ru
250 2.1.0 <sapr-m@yandex.ru> ok
rcpt to: sapr-m@yandex.ru
250 2.1.5 <sapr-m@yandex.ru> recipient ok
data
354 Enter mail, end with "." on a line by itself
Subject: Test mail
Hello world


Hello world again!


This is me.

.
250 2.0.0 Ok: queued on sas1-fa9d05dd56ad.qloud-c.yandex.net as 1625576207-wFjz8HcUjq-tifeSO9G
quit
221 2.0.0 Closing connection.
Connection closed by foreign host.
serg@quantori:~$
```



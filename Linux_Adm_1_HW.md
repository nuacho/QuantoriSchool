# 1: linux.adm.software:
Скачайте свежую версию исходников git. Скомпилируйте и инсталлируйте в каталог /usr/local. Убедитесь, что свежая версия установлена и готова к использованию.

Идем сюда https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Git

### Устанавливаем зависимости:
```
$ sudo apt-get install dh-autoreconf libcurl4-gnutls-dev libexpat1-dev \
  gettext libz-dev libssl-dev
```
### Для документации в разных форматах устанавливаем зависимости:

$ sudo apt-get install asciidoc xmlto docbook2x


### Устанавливаем пакет install-info:
$ sudo apt-get install install-info


### Компилируем и устанавливаем:
$ tar -zxf git-2.32.0.tar.gz
$ cd git-2.32.0
$ make configure
$ ./configure --prefix=/usr
$ make all doc info
$ sudo make install install-doc install-html install-info

### Переходим в директорию /usr/local. 

sudo git clone git://git.kernel.org/pub/scm/git/git.git

### Имеем

nuacho@VirtualBox:/usr/local$ ls -ald git
drwxr-xr-x 27 root root 20480 июл 21 17:01 git

nuacho@VirtualBox:/usr/local$ git --version
git version 2.32.0
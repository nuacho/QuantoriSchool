# 4 Иногда бывает задача записать stdout в файл, на который у пользователя нет прав:

$ echo “Secret Password” > /root/password.txt 
permission denied
Начинающие пользователи сразу пробуют применить программу sudo:
$ sudo echo “Secret Password” > /root/password.txt
permission denied
Однако sudo здесь не помогает.
*Почему такое использование sudo не срабатывает?*

Потому что потоками управляет шелл, а не sudo, а у нее не хватает прав.

*Как можно обойти?*

Например, так:
```
nuacho@VirtualBox:/var/ftp$ echo 'новая строка' | sudo tee --append /var/ftp/password.txt 
[sudo] password for nuacho: 
новая строка
```

чтобы не выводило в консоль, а только добавлялось в файл, надо вывод отправить на /dev/null

```
nuacho@VirtualBox:/var/ftp$ echo 'новая строка' | sudo tee --append /var/ftp/password.txt > /dev/null
nuacho@VirtualBox:/var/ftp$ vim password.txt 
```

*Как правильно собрать такой pipeline с sudo?*

Например, так:
```
nuacho@VirtualBox:/var/ftp$ ls -lah
total 24K
drwxrwsr-x  5 nuacho ftp-admin 4,0K июл 17 20:58 .
drwxr-xr-x 15 root   root      4,0K июл 17 18:28 ..
drwxrwsr-x  2 ivan   ftp-admin 4,0K июл 17 20:00 ivan
drwxrwsr-x  2 maxim  ftp-admin 4,0K июл 17 20:17 maxim
-r--------  1 nuacho ftp-admin    6 июл 17 21:06 password.txt
drwxrwsr-x  2 sergey ftp-admin 4,0K июл 17 18:37 sergey
nuacho@VirtualBox:/var/ftp$ sudo echo "Hello" > password.txt 
bash: password.txt: Permission denied
*nuacho@VirtualBox:/var/ftp$ sudo echo "Hello" | sudo dd of=/var/ftp/password.txt*
0+1 records in
0+1 records out
6 bytes copied, 0,00154828 s, 3,9 kB/s
nuacho@VirtualBox:/var/ftp$ cat password.txt 
Hello
nuacho@VirtualBox:/var/ftp$ 

```
# 3. linux.files:
### В папке /var/ftp/ - есть подпапки пользователей (**/var/ftp/ivan, /var/ftp/aleksei, etc.**), куда они складывают свои файлы. Есть пользователь и группа **ftp-admin** - они используются администратором ftp сервера, и он может управлять содержимым всех подпапок всех пользователей. При этом обычные пользователи могут управлять только своими файлами. Начинающий администратор случайно поломал права на папки и файлы, а также сменил пользователей владельцев и групп владельцев у некоторых файлов. Вам предстоит починить и привести систему к рабочему состоянию.Используя команды **find, chown, chmod** восстановите правильный порядок.

### Имеем такую структуру после шаловливых ручек:
```
nuacho@VirtualBox:/var/ftp$ ls -lahR
.:
total 20K
drwxr-xr-x  5 root root 4,0K июл 17 18:34 .
drwxr-xr-x 15 root root 4,0K июл 17 18:28 ..
drwxr-xr-x  2 root root 4,0K июл 17 18:37 ivan
drwxr-xr-x  2 root root 4,0K июл 17 18:37 maxim
drwxr-xr-x  2 root root 4,0K июл 17 18:37 sergey

./ivan:
total 8,0K
drwxr-xr-x 2 root root 4,0K июл 17 18:37 .
drwxr-xr-x 5 root root 4,0K июл 17 18:34 ..
-rw-r--r-- 1 root root    0 июл 17 18:37 ivan.txt

./maxim:
total 8,0K
drwxr-xr-x 2 root root 4,0K июл 17 18:37 .
drwxr-xr-x 5 root root 4,0K июл 17 18:34 ..
-rw-r--r-- 1 root root    0 июл 17 18:37 maxim.txt

./sergey:
total 8,0K
drwxr-xr-x 2 root root 4,0K июл 17 18:37 .
drwxr-xr-x 5 root root 4,0K июл 17 18:34 ..
-rw-r--r-- 1 root root    0 июл 17 18:37 sergey.txt

```
### Устанавливаем права так, чтобы все созданное внутри наследовало группу директории, а не ее создателя

```
nuacho@VirtualBox:/var/ftp$ sudo chmod 2775 /var/ftp
```

### Ищем в папке директории с владельцем root и меняем владельца на пользователя ftp-admin
```
nuacho@VirtualBox:/var/ftp$ sudo find /var/ftp -type d -group root -print | sudo xargs chgrp ftp-admin
```

### Ищем в папке файлы с владельцем root и меняем владельца на пользователя ftp-admin
```
nuacho@VirtualBox:/var/ftp$ sudo find /var/ftp -type f -group root -print | sudo xargs chgrp ftp-admin
```

### Меняем владельца папок и файлов на соответствующих пользователей
```
nuacho@VirtualBox:/var/ftp$ sudo chown ivan /var/ftp/ivan
nuacho@VirtualBox:/var/ftp$ sudo chown maxim /var/ftp/maxim
nuacho@VirtualBox:/var/ftp$ sudo chown sergey /var/ftp/sergey

nuacho@VirtualBox:/var/ftp$ sudo chown ivan /var/ftp/ivan/ivan.txt
nuacho@VirtualBox:/var/ftp$ sudo chown maxim /var/ftp/maxim/maxim.txt
nuacho@VirtualBox:/var/ftp$ sudo chown sergey /var/ftp/sergey/sergey.txt
```

### В результате имеем такую структуру. Пользователи могут шкодничать только в своих директориях, ftp-admin - во всех папках.  
```
nuacho@VirtualBox:/var/ftp$ ls -lahR
.:
total 20K
drwxrwsr-x  5 nuacho ftp-admin 4,0K июл 17 19:13 .
drwxr-xr-x 15 root   root      4,0K июл 17 18:28 ..
drwxrwsr-x  2 ivan   ftp-admin 4,0K июл 17 20:00 ivan
drwxrwsr-x  2 maxim  ftp-admin 4,0K июл 17 20:17 maxim
drwxrwsr-x  2 sergey ftp-admin 4,0K июл 17 18:37 sergey

./ivan:
total 8,0K
drwxrwsr-x 2 ivan   ftp-admin 4,0K июл 17 20:00 .
drwxrwsr-x 5 nuacho ftp-admin 4,0K июл 17 19:13 ..
-rw-rw-r-- 1 ivan   ftp-admin    0 июл 17 18:37 ivan.txt

./maxim:
total 8,0K
drwxrwsr-x 2 maxim  ftp-admin 4,0K июл 17 20:17 .
drwxrwsr-x 5 nuacho ftp-admin 4,0K июл 17 19:13 ..
-rw-rw-r-- 1 maxim  ftp-admin    0 июл 17 18:37 maxim.txt

./sergey:
total 8,0K
drwxrwsr-x 2 sergey ftp-admin 4,0K июл 17 18:37 .
drwxrwsr-x 5 nuacho ftp-admin 4,0K июл 17 19:13 ..
-rw-rw-r-- 1 sergey ftp-admin    0 июл 17 18:37 sergey.txt
nuacho@VirtualBox:/var/ftp$ stat /var/ftp/
  File: /var/ftp/
  Size: 4096      	Blocks: 8          IO Block: 4096   directory
Device: 805h/2053d	Inode: 1196034     Links: 5
Access: (2775/drwxrwsr-x)  Uid: ( 1000/  nuacho)   Gid: ( 1004/ftp-admin)
Access: 2021-07-17 19:49:15.445178634 +0400
Modify: 2021-07-17 19:13:39.462242565 +0400
Change: 2021-07-17 19:49:13.581188373 +0400
 Birth: -

```

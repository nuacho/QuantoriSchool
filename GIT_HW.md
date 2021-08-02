# Склонировать один и тот же репозиторий к себе на компьютер в две разные папки. 
Сделать одни и те же изменения в обеих копиях репозитория, закоммитить и сделать push, pull. 
Добиться одинаковых hash сумм для обоих коммитов за счет идентичности коммитов. Сделать push pull.

Взял свой репозиторий с домашками. 

Склонировал в 2 папки:
```
nuacho@VirtualBox:~/Documents/quantoridemo1$ git clone https://github.com/nuacho/QuantoriSchool.git
Cloning into 'QuantoriSchool'...
remote: Enumerating objects: 94, done.
remote: Counting objects: 100% (94/94), done.
remote: Compressing objects: 100% (92/92), done.
remote: Total 94 (delta 40), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (94/94), 41.37 KiB | 756.00 KiB/s, done.
Resolving deltas: 100% (40/40), done.
nuacho@VirtualBox:~/Documents/quantoridemo1$ cd ~/Documents/quantoridemo2/
nuacho@VirtualBox:~/Documents/quantoridemo2$ git clone https://github.com/nuacho/QuantoriSchool.git
Cloning into 'QuantoriSchool'...
remote: Enumerating objects: 94, done.
remote: Counting objects: 100% (94/94), done.
remote: Compressing objects: 100% (92/92), done.
remote: Total 94 (delta 40), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (94/94), 41.37 KiB | 756.00 KiB/s, done.
Resolving deltas: 100% (40/40), done.

```

Скопировал в обе папки измененный **README.md**

Сделал git add .
Сделал git commit с принудительным указанием даты с авторством коммита, чтобы дата обоих коммитов точно совпадала:

```
nuacho@VirtualBox:~/Documents/quantoridemo2$ cd QuantoriSchool/
nuacho@VirtualBox:~/Documents/quantoridemo2/QuantoriSchool$ git add .
nuacho@VirtualBox:~/Documents/quantoridemo2/QuantoriSchool$ git commit --date "Tue Aug 02 14:00 2021 +0300" -m "first commit"
[main 439b486] first commit
 Date: Mon Aug 2 14:00:00 2021 +0300
 1 file changed, 1 insertion(+), 1 deletion(-)
nuacho@VirtualBox:~/Documents/quantoridemo2/QuantoriSchool$ cd ~/Documents/quantoridemo1/
nuacho@VirtualBox:~/Documents/quantoridemo1$ cd QuantoriSchool/
nuacho@VirtualBox:~/Documents/quantoridemo1/QuantoriSchool$ git add .
nuacho@VirtualBox:~/Documents/quantoridemo1/QuantoriSchool$ git commit --date "Tue Aug 02 14:00 2021 +0300" -m "first commit"
[main 14219e4] first commit
 Date: Mon Aug 2 14:00:00 2021 +0300
 1 file changed, 1 insertion(+), 1 deletion(-)

```
Однако получил все равно разный хэш:

```
nuacho@VirtualBox:~/Documents/quantoridemo1/QuantoriSchool$ git show
commit 14219e4a54ace0ab4f24a99e7efcd4d757a7e1cb (HEAD -> main)
Author: Sergey Borisov <sapr_m@mail.ru>
Date:   Mon Aug 2 14:00:00 2021 +0300

    first commit

diff --git a/README.md b/README.md
index 8e7c22e..cdb99c5 100644
--- a/README.md
+++ b/README.md
@@ -1 +1 @@
-# QuantoriSchool
\ No newline at end of file
+# QuantoriSchool Hello
nuacho@VirtualBox:~/Documents/quantoridemo1/QuantoriSchool$ cd ~/Documents/quantoridemo2/QuantoriSchool/
nuacho@VirtualBox:~/Documents/quantoridemo2/QuantoriSchool$ git show
commit 439b486d96564a12c90471a0d0b7f5a50d24b577 (HEAD -> main)
Author: Sergey Borisov <sapr_m@mail.ru>
Date:   Mon Aug 2 14:00:00 2021 +0300

    first commit

diff --git a/README.md b/README.md
index 8e7c22e..cdb99c5 100644
--- a/README.md
+++ b/README.md
@@ -1 +1 @@
-# QuantoriSchool
\ No newline at end of file
+# QuantoriSchool Hello

```

Посмотрим содержимое блоба нашего коммита:
```
git cat-file -p 0dee9b10c79b57e4116c61d89d697ac87685f474
tree 17b7aba3017c7b7d1ba58dbab74183974a459582
parent 7784a322bd24f88c79d55009ccdc0e1ad10b034b
author Sergey Borisov <sapr_m@mail.ru> 1627902000 +0300
committer Sergey Borisov <sapr_m@mail.ru> 1627919420 +0400

first commit

```
Имеем отличающуюся дату у комиттера от дата автора.
Исправляем:
```
nuacho@VirtualBox:~/Documents/quantoridemo1/QuantoriSchool$ GIT_COMMITTER_DATE="Mon Aug 2 14:00:00 2021 +0300" git commit --amend --no-edit
[main f912d8d] first commit
 Date: Mon Aug 2 14:00:00 2021 +0300
 1 file changed, 1 insertion(+), 1 deletion(-)

```
Проверяем:

```
nuacho@VirtualBox:~/Documents/quantoridemo1/QuantoriSchool$ git cat-file commit HEAD
tree 17b7aba3017c7b7d1ba58dbab74183974a459582
parent 7784a322bd24f88c79d55009ccdc0e1ad10b034b
author Sergey Borisov <sapr_m@mail.ru> 1627902000 +0300
committer Sergey Borisov <sapr_m@mail.ru> 1627902000 +0300

```

Проделываем процедуры для второй папки. И смотрим хэш коммитов. Одинаковый!


```
nuacho@VirtualBox:~/Documents/quantoridemo1/QuantoriSchool$ git show
commit f912d8d6ca7cd2ee4c3e60653961c70c4696e1cd (HEAD -> main)
Author: Sergey Borisov <sapr_m@mail.ru>
Date:   Mon Aug 2 14:00:00 2021 +0300

    first commit

diff --git a/README.md b/README.md
index 8e7c22e..cdb99c5 100644
--- a/README.md
+++ b/README.md
@@ -1 +1 @@
-# QuantoriSchool
\ No newline at end of file
+# QuantoriSchool Hello
nuacho@VirtualBox:~/Documents/quantoridemo1/QuantoriSchool$ cd ~/Documents/quantoridemo2/QuantoriSchool
nuacho@VirtualBox:~/Documents/quantoridemo2/QuantoriSchool$ git show
commit f912d8d6ca7cd2ee4c3e60653961c70c4696e1cd (HEAD -> main)
Author: Sergey Borisov <sapr_m@mail.ru>
Date:   Mon Aug 2 14:00:00 2021 +0300

    first commit

diff --git a/README.md b/README.md
index 8e7c22e..cdb99c5 100644
--- a/README.md
+++ b/README.md
@@ -1 +1 @@
-# QuantoriSchool
\ No newline at end of file
+# QuantoriSchool Hello

```


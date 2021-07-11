
# 2. linux.utils:


### 1. Используя bash и программы из пакетов util-linux и core-utils, составить pipeline, который считает количество файлов, в полном имени (включая путь) которых есть подстрока “root”, но нет подстроки “proc”.

```
nuacho@nuacho-VirtualBox:/$ find / -iname *root* 2>/dev/null |  grep -v proc
/home/nuacho/.local/share/gvfs-metadata/root
/usr/lib/recovery-mode/options/root
/usr/src/linux-headers-5.8.0-59-generic/include/config/usb/ehci/root
/usr/src/linux-headers-5.8.0-43-generic/include/config/usb/ehci/root
/root
/snap/core20/1026/root
/snap/core18/1988/root
/snap/core18/2074/root
/snap/core/11316/root

```


### 2. Используя bash и программы из пакетов util-linux и core-utils, составить pipeline, который выводит значящие (не закомментированные и не пустые) строки файла конфигурации сервиса. Например из файла /etc/ssh/sshd_config.

```
nuacho@nuacho-VirtualBox:/$ cat | grep "^[^#*/;]" /etc/ssh/ssh_config 
Include /etc/ssh/ssh_config.d/*.conf
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
```
или так:

```
nuacho@nuacho-VirtualBox:/$ cat | awk '$1 ~ /^[^;#]/' /etc/ssh/ssh_config 
Include /etc/ssh/ssh_config.d/*.conf
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
```

### 3. Выбрать все уникальные оболочки из файла /etc/passwd и сравнить со списком оболочек из файла /etc/shells.

```
nuacho@nuacho-VirtualBox:~$ grep "[a-z]*sh" /etc/passwd>pass.txt | grep "[a-z]*sh" /etc/shells>shells.txt | diff shells.txt pass.txt
1,8c1,2
< # /etc/shells: valid login shells
< /bin/sh
< /bin/bash
< /usr/bin/bash
< /bin/rbash
< /usr/bin/rbash
< /bin/dash
< /usr/bin/dash
---
> root:x:0:0:root:/root:/bin/bash
> nuacho:x:1000:1000:nuacho,,,:/home/nuacho:/bin/bash

```
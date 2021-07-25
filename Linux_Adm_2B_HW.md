# 2b: linux.adm.gpgvolume
Прислать мне бинарный файл защищенный паролем, объемом не более 2 мегабайт. И сам пароль. Используя программы из пакета GNUPG и пароль, 
я должен иметь возможность смонтировать полученный файл через /dev/loop в свое дерево каталогов. Внутри полученного каталога рассчитываю 
увидеть текстовый файл с контрольной фразой.


```
dd if=/dev/zero of=~/file.img bs=1024k count=2
losetup --find --show ~/file.img
/dev/loop10
mkfs -t ext2 /dev/loop10
mount /dev/loop10 /mnt/loop100
 ...
umount /dev/loop10
losetup --detach /dev/loop10

gpg -c file.img

Пароль - SaratoV

Файл в корне  - file.img.gpg
```

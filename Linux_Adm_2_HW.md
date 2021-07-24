# 2: linux.adm.volumes
Рассчитать вероятность потерять данные при использовании дисков в raid массиве, для разных raid level и разных количествах дисков. Считать вероятность выхода из строя одного диска - 1%.
Рассчитать насколько уменьшится суммарный объем памяти при использовании дисков в raid массиве, для разных raid level и разном количестве дисков, по сравнению с использованием дисков как независимых.


### Решение
```
S = 1% = 0.01 - вероятность отказа 1 диска
K - количество дисков
N - вероятность выхода из строя массива

```
Массив **RAID 0** будет продолжать работать пока работают все его диски, следовательно
*Использование памяти - 100%*

```
N(RAID 0) = S * K

Для массива из 2 дисков N = 2%
Для массива из 5 дисков N = 5%
```

Массив **RAID 1** работоспособен, пока в каждой паре работают хотя бы один диск, поэтому его вероятность безотказной работы равна
*Использование памяти - 50%*

```
N(RAID 1) = S ^ K
Для массива из 2 дисков N = 0.001
Для массива из 4 дисков N = 0.00000001
```

Массив **RAID 5** работоспособен, пока работают все его диски или все кроме одного любого из них:
*Использование памяти - 67-94%*

```
N(RAID 5) = S * (K - 1)

Для массива из 5 дисков N = 0.01 * (5 - 1) = 4%

```

Массив **RAID 6** сохраняет работоспособность при потере не более двух любых своих жёстких дисков
*Использование памяти - 50-88%*

```
N(RAID 6) =  S * (K - 2)

Для массива из 4 дисков N = 0.01 * (4 - 2) = 2%

```
Массив **RAID 01** - зеркало из страйпов. Работоспособен, пока работают все его диски или все кроме одного любого из любого страйпа:
*Использование памяти - 50%*

```
N(RAID 01) = (K / 2) / (K — 1)

Для массива из 4 дисков N = (4 / 2) / (4 - 1) = 66 %
```

Массив **RAID 10** - страйп из зеркал. Работоспособен, пока работают все его диски или не потеряны все диски в любом зеркале:
*Использование памяти - 50%*
```
N(RAID 01) = 1 / (K — 1)

Для массива из 4 дисков N = 1 / (4 - 1) = 33 %
```
## Собрать несколько lv поверх md (raid5). Смонтировать с разными опциями в дерево каталогов.

Имеем 3 диска sdb, sdc, sdd:

```
nuacho@VirtualBox:~$ lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0    7:0    0 55,5M  1 loop /snap/core18/1988
loop1    7:1    0 55,5M  1 loop /snap/core18/2074
loop2    7:2    0  219M  1 loop /snap/gnome-3-34-1804/66
loop3    7:3    0  219M  1 loop /snap/gnome-3-34-1804/72
loop4    7:4    0 64,8M  1 loop /snap/gtk-common-themes/1514
loop5    7:5    0 65,1M  1 loop /snap/gtk-common-themes/1515
loop6    7:6    0 31,1M  1 loop /snap/snapd/11036
loop7    7:7    0   51M  1 loop /snap/snap-store/518
loop8    7:8    0 32,3M  1 loop /snap/snapd/12398
loop9    7:9    0   51M  1 loop /snap/snap-store/547
sda      8:0    0   25G  0 disk 
├─sda1   8:1    0  512M  0 part /boot/efi
├─sda2   8:2    0    1K  0 part 
└─sda5   8:5    0 24,5G  0 part /
sdb      8:16   0  4,1G  0 disk 
sdc      8:32   0  4,1G  0 disk 
sdd      8:48   0  4,1G  0 disk 
sr0     11:0    1 1024M  0 rom  

```
Разбиваем на партиции командой **fdisk**. Решил отдать все досупное пространство на каждом диске:

```
nuacho@VirtualBox:~$ sudo fdisk /dev/sdb

Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): 

Using default response p.
Partition number (1-4, default 1): 
First sector (2048-8541119, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-8541119, default 8541119): 

Created a new partition 1 of type 'Linux' and of size 4,1 GiB.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

nuacho@VirtualBox:~$ sudo fdisk /dev/sdc

Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x52ed9c26.

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): 

Using default response p.
Partition number (1-4, default 1): 
First sector (2048-8541119, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-8541119, default 8541119): 

Created a new partition 1 of type 'Linux' and of size 4,1 GiB.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

nuacho@VirtualBox:~$ sudo fdisk /dev/sdd

Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0xdc3c5c73.

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): 

Using default response p.
Partition number (1-4, default 1): 
First sector (2048-8541119, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-8541119, default 8541119): 

Created a new partition 1 of type 'Linux' and of size 4,1 GiB.

Command (m for help): 


Command (m for help): w

The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

nuacho@VirtualBox:~$ lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0    7:0    0 55,5M  1 loop /snap/core18/1988
loop1    7:1    0 55,5M  1 loop /snap/core18/2074
loop2    7:2    0  219M  1 loop /snap/gnome-3-34-1804/66
loop3    7:3    0  219M  1 loop /snap/gnome-3-34-1804/72
loop4    7:4    0 64,8M  1 loop /snap/gtk-common-themes/1514
loop5    7:5    0 65,1M  1 loop /snap/gtk-common-themes/1515
loop6    7:6    0 31,1M  1 loop /snap/snapd/11036
loop7    7:7    0   51M  1 loop /snap/snap-store/518
loop8    7:8    0 32,3M  1 loop /snap/snapd/12398
loop9    7:9    0   51M  1 loop /snap/snap-store/547
sda      8:0    0   25G  0 disk 
├─sda1   8:1    0  512M  0 part /boot/efi
├─sda2   8:2    0    1K  0 part 
└─sda5   8:5    0 24,5G  0 part /
sdb      8:16   0  4,1G  0 disk 
└─sdb1   8:17   0  4,1G  0 part 
sdc      8:32   0  4,1G  0 disk 
└─sdc1   8:33   0  4,1G  0 part 
sdd      8:48   0  4,1G  0 disk 
└─sdd1   8:49   0  4,1G  0 part 
sr0     11:0    1 1024M  0 rom  

```

Создаем RAID 5 массив при помощи утилиты **mdadm**

```
nuacho@VirtualBox:~$ sudo mdadm --create /dev/md0 -l5 --raid-devices=3 /dev/sdb1 /dev/sdc1 /dev/sdd1
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.
nuacho@VirtualBox:~$ lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
loop0     7:0    0 55,5M  1 loop  /snap/core18/1988
loop1     7:1    0 55,5M  1 loop  /snap/core18/2074
loop2     7:2    0  219M  1 loop  /snap/gnome-3-34-1804/66
loop3     7:3    0  219M  1 loop  /snap/gnome-3-34-1804/72
loop4     7:4    0 64,8M  1 loop  /snap/gtk-common-themes/1514
loop5     7:5    0 65,1M  1 loop  /snap/gtk-common-themes/1515
loop6     7:6    0 31,1M  1 loop  /snap/snapd/11036
loop7     7:7    0   51M  1 loop  /snap/snap-store/518
loop8     7:8    0 32,3M  1 loop  /snap/snapd/12398
loop9     7:9    0   51M  1 loop  /snap/snap-store/547
sda       8:0    0   25G  0 disk  
├─sda1    8:1    0  512M  0 part  /boot/efi
├─sda2    8:2    0    1K  0 part  
└─sda5    8:5    0 24,5G  0 part  /
sdb       8:16   0  4,1G  0 disk  
└─sdb1    8:17   0  4,1G  0 part  
  └─md0   9:0    0  8,1G  0 raid5 
sdc       8:32   0  4,1G  0 disk  
└─sdc1    8:33   0  4,1G  0 part  
  └─md0   9:0    0  8,1G  0 raid5 
sdd       8:48   0  4,1G  0 disk  
└─sdd1    8:49   0  4,1G  0 part  
  └─md0   9:0    0  8,1G  0 raid5 
sr0      11:0    1 1024M  0 rom   

```

Имеем:
```
nuacho@VirtualBox:~$ ls -ld /dev/md*
brw-rw---- 1 root disk 9, 0 июл 24 16:47 /dev/md0

nuacho@VirtualBox:~$ sudo !!
sudo cat /proc/mdstat /dev/md0
Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10] 
md0 : active raid5 sdd1[3] sdc1[1] sdb1[0]
      8527872 blocks super 1.2 level 5, 512k chunk, algorithm 2 [3/3] [UUU]

```
Создадим файловую систему на устройстве **md0**:

```
nuacho@VirtualBox:~$ mkfs /dev/md0
mke2fs 1.45.5 (07-Jan-2020)
Could not open /dev/md0: Permission denied
nuacho@VirtualBox:~$ sudo !!
sudo mkfs /dev/md0
[sudo] password for nuacho: 
mke2fs 1.45.5 (07-Jan-2020)
Creating filesystem with 2131968 4k blocks and 533280 inodes
Filesystem UUID: f4cdeb76-cb4b-44a0-b3dc-cd7eba017457
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done                            
Writing inode tables: done                            
Writing superblocks and filesystem accounting information: done 
```

Получили **ext2**. Хочу переделать ее в **ext4**:

```
nuacho@VirtualBox:/mnt$ sudo mkfs.ext4 /dev/md0
mke2fs 1.45.5 (07-Jan-2020)
/dev/md0 contains a ext2 file system
	created on Sat Jul 24 17:39:30 2021
Proceed anyway? (y,N) y
Creating filesystem with 2131968 4k blocks and 533280 inodes
Filesystem UUID: 392a2a9b-a7cc-4d03-891f-227db8fa8f1b
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done 

```
Создаем директорию **/mnt/md0** и монтируем в нее новый девайсЖ

```
uacho@VirtualBox:~$ mkdir /mnt/md0
mkdir: cannot create directory ‘/mnt/md0’: Permission denied
nuacho@VirtualBox:~$ sudo !!
sudo mkdir /mnt/md0
nuacho@VirtualBox:/mnt$ sudo mount /dev/md0 /mnt/md0
nuacho@VirtualBox:/mnt$ lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
loop0     7:0    0 55,5M  1 loop  /snap/core18/1988
loop1     7:1    0 55,5M  1 loop  /snap/core18/2074
loop2     7:2    0  219M  1 loop  /snap/gnome-3-34-1804/66
loop3     7:3    0  219M  1 loop  /snap/gnome-3-34-1804/72
loop4     7:4    0 64,8M  1 loop  /snap/gtk-common-themes/1514
loop5     7:5    0 65,1M  1 loop  /snap/gtk-common-themes/1515
loop6     7:6    0 31,1M  1 loop  /snap/snapd/11036
loop7     7:7    0   51M  1 loop  /snap/snap-store/518
loop8     7:8    0 32,3M  1 loop  /snap/snapd/12398
loop9     7:9    0   51M  1 loop  /snap/snap-store/547
sda       8:0    0   25G  0 disk  
├─sda1    8:1    0  512M  0 part  /boot/efi
├─sda2    8:2    0    1K  0 part  
└─sda5    8:5    0 24,5G  0 part  /
sdb       8:16   0  4,1G  0 disk  
└─sdb1    8:17   0  4,1G  0 part  
  └─md0   9:0    0  8,1G  0 raid5 /mnt/md0
sdc       8:32   0  4,1G  0 disk  
└─sdc1    8:33   0  4,1G  0 part  
  └─md0   9:0    0  8,1G  0 raid5 /mnt/md0
sdd       8:48   0  4,1G  0 disk  
└─sdd1    8:49   0  4,1G  0 part  
  └─md0   9:0    0  8,1G  0 raid5 /mnt/md0
sr0      11:0    1 1024M  0 rom   
nuacho@VirtualBox:/mnt$ ls /mnt/md0
lost+found

```
Для сохранения монтирования в файлик **fstab** дописываем:
```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda5 during installation
UUID=da67a81d-9163-479d-9b1c-076472827b9f /               ext4    errors=remount-ro 0       1
# /boot/efi was on /dev/sda1 during installation
UUID=45DA-998A  /boot/efi       vfat    umask=0077      0       1
/swapfile                                 none            swap    sw              0       0

/dev/md0 /mnt/md0 ext4 rw,relatime,noexec,stripe=256 0 0
```

Создадим физический том:
```
root@VirtualBox:~# pvcreate /dev/md0
WARNING: ext4 signature detected on /dev/md0 at offset 1080. Wipe it? [y/n]: y
  Wiping ext4 signature on /dev/md0.
  Physical volume "/dev/md0" successfully created.

root@VirtualBox:~# pvdisplay
  "/dev/md0" is a new physical volume of "8,13 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/md0
  VG Name               
  PV Size               8,13 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               Xj9kUt-ta2U-oTGx-GWG2-da7Y-XGX0-Sdcci7

```
Создадим группу 

```
root@VirtualBox:~# vgcreate nuacho1 /dev/md0
  Volume group "nuacho1" successfully created

root@VirtualBox:~# vgdisplay
  --- Volume group ---
  VG Name               nuacho1
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               <8,13 GiB
  PE Size               4,00 MiB
  Total PE              2081
  Alloc PE / Size       0 / 0   
  Free  PE / Size       2081 / <8,13 GiB
  VG UUID               zcgdUz-b9cF-dEED-jd29-NX3C-iqXz-IBBfY4


```
Создаем логический том на 500Мб внутри

```
root@VirtualBox:~# lvcreate nuacho1 -L 500M
  Logical volume "lvol0" created.
root@VirtualBox:~# lvdisplay
  --- Logical volume ---
  LV Path                /dev/nuacho1/lvol0
  LV Name                lvol0
  VG Name                nuacho1
  LV UUID                3n2mP4-ZZGO-OolT-yKs7-hjeb-1qNj-UO2Qsn
  LV Write Access        read/write
  LV Creation host, time VirtualBox, 2021-07-24 20:03:52 +0400
  LV Status              available
  # open                 0
  LV Size                500,00 MiB
  Current LE             125
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     4096
  Block device           253:0

```
И еще 2 таких. Итого 3 логических тома.
Создаем для них директории в папке /mnt. Создаем на логических томах файловую систему. И монтируем их в только что созданные папки. 

```
root@VirtualBox:~# mkfs.ext4 /dev/nuacho1/lvol0
mke2fs 1.45.5 (07-Jan-2020)
Creating filesystem with 128000 4k blocks and 128000 inodes
Filesystem UUID: fac14e4d-5d1a-4a64-9f9a-03e51e6aba9d
Superblock backups stored on blocks: 
	32768, 98304

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (4096 blocks): done
Writing superblocks and filesystem accounting information: done

root@VirtualBox:~# mkdir /mnt/nuacho_1
root@VirtualBox:~# mount /dev/nuacho1/lvol0 /mnt/nuacho_1/
root@VirtualBox:~# df -h
Filesystem                 Size  Used Avail Use% Mounted on
udev                       1,4G     0  1,4G   0% /dev
tmpfs                      288M  1,4M  287M   1% /run
/dev/sda5                   24G   11G   13G  45% /
tmpfs                      1,5G     0  1,5G   0% /dev/shm
tmpfs                      5,0M  4,0K  5,0M   1% /run/lock
tmpfs                      1,5G     0  1,5G   0% /sys/fs/cgroup
/dev/loop0                  56M   56M     0 100% /snap/core18/1988
/dev/loop1                  56M   56M     0 100% /snap/core18/2074
/dev/loop2                 219M  219M     0 100% /snap/gnome-3-34-1804/66
/dev/loop3                 219M  219M     0 100% /snap/gnome-3-34-1804/72
/dev/loop4                  65M   65M     0 100% /snap/gtk-common-themes/1514
/dev/loop5                  66M   66M     0 100% /snap/gtk-common-themes/1515
/dev/loop7                  52M   52M     0 100% /snap/snap-store/518
/dev/loop6                  32M   32M     0 100% /snap/snapd/11036
/dev/loop8                  33M   33M     0 100% /snap/snapd/12398
/dev/loop9                  51M   51M     0 100% /snap/snap-store/547
/dev/sda1                  511M  4,0K  511M   1% /boot/efi
tmpfs                      288M   24K  288M   1% /run/user/1000
/dev/mapper/nuacho1-lvol0  469M  768K  433M   1% /mnt/nuacho_1

```
Пробуем скопировать в только что созданные и примонтированные тома 200 файликов по 2 Мб. Работает! 

```
oot@VirtualBox:~# dd if=/dev/zero of=/mnt/nuacho_1/zerofile bs=2M count=200 
200+0 records in
200+0 records out
419430400 bytes (419 MB, 400 MiB) copied, 0,767618 s, 546 MB/s
root@VirtualBox:~# df -h
Filesystem                 Size  Used Avail Use% Mounted on
udev                       1,4G     0  1,4G   0% /dev
tmpfs                      288M  1,4M  287M   1% /run
/dev/sda5                   24G   11G   13G  45% /
tmpfs                      1,5G     0  1,5G   0% /dev/shm
tmpfs                      5,0M  4,0K  5,0M   1% /run/lock
tmpfs                      1,5G     0  1,5G   0% /sys/fs/cgroup
/dev/loop0                  56M   56M     0 100% /snap/core18/1988
/dev/loop1                  56M   56M     0 100% /snap/core18/2074
/dev/loop2                 219M  219M     0 100% /snap/gnome-3-34-1804/66
/dev/loop3                 219M  219M     0 100% /snap/gnome-3-34-1804/72
/dev/loop4                  65M   65M     0 100% /snap/gtk-common-themes/1514
/dev/loop5                  66M   66M     0 100% /snap/gtk-common-themes/1515
/dev/loop7                  52M   52M     0 100% /snap/snap-store/518
/dev/loop6                  32M   32M     0 100% /snap/snapd/11036
/dev/loop8                  33M   33M     0 100% /snap/snapd/12398
/dev/loop9                  51M   51M     0 100% /snap/snap-store/547
/dev/sda1                  511M  4,0K  511M   1% /boot/efi
tmpfs                      288M   24K  288M   1% /run/user/1000
/dev/mapper/nuacho1-lvol0  469M  401M   33M  93% /mnt/nuacho_1
/dev/mapper/nuacho1-lvol1  485M  396K  459M   1% /mnt/nuacho_2
/dev/mapper/nuacho1-lvol2  485M  396K  459M   1% /mnt/nuacho_3

```
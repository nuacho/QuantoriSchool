# 4: linux.adm.init
Написать systemV init script и systemd service unit для filesharing service. В качестве транспорта для передачи файлов использовать протокол http. 
Номер tcp порта и папку для раздачи файлов можно вынести в файл с параметрами, можно оставить в скрипте, на ваше усмотрение (предлагаю 8080 и /opt/share). 
В качестве web сервера предлагаю использовать python -m http.server (или python -m SimpleHTTPServer для python2).
Продемонстрировать работоспособность: start, stop, restart, status.


## systemd. :

nuacho@VirtualBox:/etc/systemd/system$ ls -l fileshare.service 
-rwxrwxrwx 1 root root 192 июл 31 22:45 fileshare.service

```
[Unit]
Description=File sharing
After=network.target

[Service]
Type=simple
ExecStart=python3 -m http.server 8080 --directory /opt/share/
TimeoutStartSec=0

[Install]
WantedBy=default.target
```
## Работоспособность

```
nuacho@VirtualBox:/etc/systemd/system$ systemctl start fileshare.service
nuacho@VirtualBox:/etc/systemd/system$ systemctl status fileshare.service
● fileshare.service - File sharing
     Loaded: loaded (/etc/systemd/system/fileshare.service; disabled; vendor preset: enabled)
     Active: active (running) since Sun 2021-08-01 00:11:52 +04; 10s ago
   Main PID: 5914 (python3)
      Tasks: 1 (limit: 3378)
     Memory: 8.1M
     CGroup: /system.slice/fileshare.service
             └─5914 /usr/bin/python3 -m http.server 8080 --directory /opt/share/

авг 01 00:11:52 VirtualBox systemd[1]: Started File sharing.
nuacho@VirtualBox:/etc/systemd/system$ systemctl stop fileshare.service
nuacho@VirtualBox:/etc/systemd/system$ systemctl status fileshare.service
● fileshare.service - File sharing
     Loaded: loaded (/etc/systemd/system/fileshare.service; disabled; vendor preset: enabled)
     Active: inactive (dead)

июл 31 22:48:34 VirtualBox systemd[1]: fileshare.service: Succeeded.
июл 31 22:48:34 VirtualBox systemd[1]: Stopped File sharing.
июл 31 23:25:56 VirtualBox systemd[1]: Started File sharing.
июл 31 23:26:12 VirtualBox systemd[1]: Stopping File sharing...
июл 31 23:26:12 VirtualBox systemd[1]: fileshare.service: Succeeded.
июл 31 23:26:12 VirtualBox systemd[1]: Stopped File sharing.
авг 01 00:11:52 VirtualBox systemd[1]: Started File sharing.
авг 01 00:12:17 VirtualBox systemd[1]: Stopping File sharing...
авг 01 00:12:17 VirtualBox systemd[1]: fileshare.service: Succeeded.
авг 01 00:12:17 VirtualBox systemd[1]: Stopped File sharing.
nuacho@VirtualBox:/etc/systemd/system$ systemctl restart fileshare.service
nuacho@VirtualBox:/etc/systemd/system$ systemctl status fileshare.service
● fileshare.service - File sharing
     Loaded: loaded (/etc/systemd/system/fileshare.service; disabled; vendor preset: enabled)
     Active: active (running) since Sun 2021-08-01 00:12:35 +04; 2s ago
   Main PID: 5938 (python3)
      Tasks: 1 (limit: 3378)
     Memory: 8.1M
     CGroup: /system.slice/fileshare.service
             └─5938 /usr/bin/python3 -m http.server 8080 --directory /opt/share/

авг 01 00:12:35 VirtualBox systemd[1]: Started File sharing.

```



## system V

```
#!/bin/bash

### BEGIN INIT INFO
# Provides:          share folder
# Required-Start:    
# Required-Stop:
# Should-Start:      
# Should-Stop:       
# X-Start-Before:    
# X-Stop-After:      
# Default-Start:     
# Default-Stop:
### END INIT INFO

SCRIPTNAME=/etc/init.d/fileshare
PORT=8080
SHARE_FOLDER=~/opt/share/
PID_FILE=/var/run/pidshare.pid


case "$1" in
  start)
        cd $SHARE_FOLDER
        python3 -m http.server $PORT --directory ~/opt/share 1>/dev/null &
        echo $!>$PID_FILE
        echo "HTTP Server started!"

        ;;
  stop)
        kill -9 `cat $PID_FILE`
        echo "HTTP Server stopped!"
        ;;
 restart)
        $0 stop
        $0 start &
        ;;
 status)
         if  ps -auxf | fgrep -f $PID_FILE
                 then
                        echo "Sharing started" 
                 else
                        echo "Sharing stopped" 
         fi
         ;;
  *)
        echo "Usage: $SCRIPTNAME start" >&2
        exit 3
        ;;
esac

```
## Работоспособность

```
nuacho@VirtualBox:/etc/init.d$ ./fileshare start
HTTP Server started!
nuacho@VirtualBox:/etc/init.d$ ./fileshare stop
HTTP Server stopped!
nuacho@VirtualBox:/etc/init.d$ ./fileshare status
Sharing stopped
nuacho@VirtualBox:/etc/init.d$ ./fileshare restart
./fileshare: line 36: kill: (4040) - No such process
HTTP Server stopped!
nuacho@VirtualBox:/etc/init.d$ HTTP Server started!

nuacho@VirtualBox:/etc/init.d$ ./fileshare status
root        1120  0.0  0.0 304056  2852 ?        Sl   13:16   0:04 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
nuacho      1609  0.0  0.8 349604 24056 ?        Ssl  13:16   0:00  \_ /usr/libexec/gsd-wacom
nuacho      4056  0.7  0.5  35416 16576 pts/0    S    21:48   0:00  \_ python3 -m http.server 8080 --directory /home/nuacho/opt/share
Sharing started
nuacho@VirtualBox:/etc/init.d$ 


```

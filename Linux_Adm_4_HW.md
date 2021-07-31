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

SCRIPTNAME=/etc/init.d/fileshare &
PORT=8080
SHARE_FOLDER=~/opt/share/

case "$1" in
  start)
        cd $SHARE_FOLDER
        python3 -m http.server $PORT
        echo "HTTP Server started!"
        ;;
  stop)
        pkill -15 python
        echo "HTTP Server stopped!"
        ;;
 restart)
        $0 stop
        $0 start &
        ;;
 status)
         if  ps -auxf | pgrep python
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
nuacho@VirtualBox:/etc/init.d$ ./fileshare start &
[1] 5985
nuacho@VirtualBox:/etc/init.d$ Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...

nuacho@VirtualBox:/etc/init.d$ ps auxf | grep python
root         772  0.0  0.6  47956 20304 ?        Ss   июл31   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         876  0.0  0.7 126656 22620 ?        Ssl  июл31   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
nuacho      5987  0.1  0.5  35412 16476 pts/1    S    00:16   0:00          |   \_ python3 -m http.server 8080
nuacho      5992  0.0  0.0  17676   664 pts/1    S+   00:17   0:00          \_ grep --color=auto python
nuacho@VirtualBox:/etc/init.d$ ./fileshare stop
Terminated
HTTP Server started!
HTTP Server stopped!
[1]+  Done                    ./fileshare start
nuacho@VirtualBox:/etc/init.d$ ps auxf | grep python
root         772  0.0  0.6  47956 20304 ?        Ss   июл31   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         876  0.0  0.7 126656 22620 ?        Ssl  июл31   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
nuacho      5997  0.0  0.0  17676   664 pts/1    S+   00:17   0:00          \_ grep --color=auto python
nuacho@VirtualBox:/etc/init.d$ ./fileshare status
Sharing stopped

```

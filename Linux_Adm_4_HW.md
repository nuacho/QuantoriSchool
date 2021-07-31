# 4: linux.adm.init
Написать systemV init script и systemd service unit для filesharing service. В качестве транспорта для передачи файлов использовать протокол http. 
Номер tcp порта и папку для раздачи файлов можно вынести в файл с параметрами, можно оставить в скрипте, на ваше усмотрение (предлагаю 8080 и /opt/share). 
В качестве web сервера предлагаю использовать python -m http.server (или python -m SimpleHTTPServer для python2).
Продемонстрировать работоспособность: start, stop, restart, status.


systemV. :

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

# 5. linux.scripting:
Программа ping в операционной системе solaris не выводит подробности взаимодействия по icmp, а кратко сообщает о том, доступен ли удаленный сетевой узел:
$ ping google.com
google.com is alive
$ ping eeeerrr.fff.rrr
eeeerrr.fff.rrr is not alive
Написать bash скрипт ping.sh - который будет эмулировать поведение программы ping из ОС Solaris.

### Ответ:

```
#!/bin/sh

ping -q -w1 -c1 "$1" >/dev/null 2>&1 && echo $1 is alive || echo $1 is not alive
```

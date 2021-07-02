# Исследовать работу протокола ICMP и утилит traceroute и ping

### 1. Выяснить количество хопов до крупных сетевых узлов: google, yandex, cisco, aws, microsoft, etc.  

Из полученной картины видно, что хост 188.232.3.252, который второй хоп, не пропускает UDP пакеты, которые **traceroute** использует по дефолту, поэтому вторым пунктом везде звезды, а если запускать **traceroute** с ключом -I, т.е. используя ICMP пакеты вместо UDP, то мы его получим. Однако, некоторые хопы не реагируют и на ICMP пакеты (возможно отключено админом), поэтому мы их никак не увидим. Это видно из последнего листинга **traceroute** Гугла. 

```traceroute to AWS.com (13.33.242.11), 30 hops max, 60 byte packets

 1  _gateway (192.168.1.1)  2.209 ms  2.112 ms  2.061 ms  
 2  * * *  
 3  lag-8-435.bbr01.voronezh.ertelecom.ru (109.195.24.18)  4.857 ms  4.816 ms  4.858 ms  
 4  GW-ERTelecom.retn.net (87.245.228.243)  28.648 ms  28.605 ms  28.563 ms  
 5  ae14.RT.SL.SPB.RU.retn.net (87.245.228.242)  30.037 ms  30.709 ms  30.668 ms  
 6  et002-3.RT.EQ6.HKI.FI.retn.net (87.245.232.87)  39.859 ms  51.830 ms  51.723 ms  
 7  99.83.66.80 (99.83.66.80)  32.474 ms  32.290 ms  32.242 ms  
 8  52.93.81.224 (52.93.81.224)  33.386 ms 52.93.81.216 (52.93.81.216)  33.344 ms 52.93.81.204 (52.93.81.204)  33.704 ms  
 9  52.93.104.61 (52.93.104.61)  33.258 ms 52.93.104.51 (52.93.104.51)  33.218 ms 52.93.104.63 (52.93.104.63)  33.177 ms  
10  * * *  
11  * * *  
12  * * *  
13  * * *  
14  * * *  
15  server-13-33-242-11.hel50.r.cloudfront.net (13.33.242.11)  32.263 ms  32.108 ms  32.059 ms  
```

```
traceroute to cisco.com (72.163.4.185), 30 hops max, 60 byte packets  
 1  _gateway (192.168.1.1)  1.955 ms  1.856 ms  1.805 ms  
 2  * * *  
 3  lag-8-435.bbr01.voronezh.ertelecom.ru (109.195.24.18)  4.018 ms  3.900 ms  3.847 ms  
 4  GW-ERTelecom.retn.net (87.245.243.62)  11.160 ms  11.117 ms  11.075 ms  
 5  ae3-110.RT.ES.VOZ.RU.retn.net (87.245.243.61)  20.211 ms  20.516 ms  20.466 ms  
 6  ae5-10.RT.TC2.AMS.NL.retn.net (87.245.234.113)  57.750 ms  53.276 ms  56.423 ms  
 7  ae69.edge7.Amsterdam1.Level3.net (213.244.164.1)  57.777 ms  54.092 ms  57.600 ms  
 8  ae-4-15.edge5.Dallas3.Level3.net (4.69.208.233)  192.228 ms  191.622 ms ae-3-5.edge5.Dallas3.Level3.net (4.69.208.229)  191.541 ms  
 9  CISCO-SYSTE.edge5.Dallas3.Level3.net (4.59.34.66)  191.383 ms  182.460 ms  182.058 ms  
10  128.107.2.5 (128.107.2.5)  181.976 ms  159.344 ms  159.242 ms  
11  72.163.0.98 (72.163.0.98)  161.555 ms  203.910 ms  201.460 ms  
12  rcdn9-cd2-dmzdcc-gw2-por2.cisco.com (72.163.0.190)  201.076 ms rcdn9-cd1-dmzdcc-gw1-por1.cisco.com (72.163.0.178)  201.296 ms  201.251 ms  
13  rcdn9-br07-fab1-sw3812-dmzdcc2uplink.cisco.com (72.163.3.6)  200.935 ms  201.163 ms rcdn9-bb07-fab1-sw3811-dmzdcc2uplink.cisco.com (72.163.3.2)  201.122 ms  
14  * * *  
15  * * *  
16  * * *  
17  * * *  
18  * * *  
19  * * *  
20  * * *  
21  * * *  
22  * * *  
23  * * *  
24  * * *  
25  * * *  
26  * * *  
27  * * *  
28  * * *  
29  * * *  
30  * * *  
```

```
traceroute to yandex.ru (5.255.255.80), 30 hops max, 60 byte packets  
 1  _gateway (192.168.1.1)  1.634 ms  1.567 ms  1.538 ms  
 2  * * *  
 3  lag-8-435.bbr01.voronezh.ertelecom.ru (109.195.24.18)  4.348 ms  4.321 ms  4.865 ms  
 4  188.234.131.242 (188.234.131.242)  19.591 ms  20.215 ms  20.192 ms  
 5  net131.234.188-243.ertelecom.ru (188.234.131.243)  20.168 ms  21.245 ms  21.220 ms  
 6  10.3.5.1 (10.3.5.1)  27.793 ms 10.4.5.1 (10.4.5.1)  23.174 ms 10.1.3.1 (10.1.3.1)  29.084 ms  
 7  yandex.ru (5.255.255.80)  19.829 ms  19.648 ms  19.597 ms  
```
```
traceroute to live.com (204.79.197.212), 30 hops max, 60 byte packets  
 1  _gateway (192.168.1.1)  2.100 ms  2.004 ms  1.955 ms  
 2  * * *  
 3  lag-8-435.bbr01.voronezh.ertelecom.ru (109.195.24.18)  3.832 ms  3.791 ms  4.483 ms  
 4  104.44.37.212 (104.44.37.212)  20.907 ms  20.865 ms  20.823 ms  
 5  ae64-0.ier01.mow30.ntwk.msn.net (104.44.37.213)  19.858 ms * *  
 6  * ae22-0.ear03.fra30.ntwk.msn.net (104.44.235.1)  63.039 ms *  
 7  be-24-0.ibr03.fra30.ntwk.msn.net (104.44.33.137)  62.906 ms ae28-0.fra-96cbe-1a.ntwk.msn.net (104.44.235.23)  66.180 ms  66.138 ms  
 8  * * *  
 9  ae26-0.fra-96cbe-1b.ntwk.msn.net (104.44.235.25)  63.664 ms * *  
10  * * *  
11  * * *  
12  * * *  
13  * * *  
14  * * *  
15  * * *  
16  * * *  
17  * * *  
18  * * *  
19  * * *  
20  * * *  
21  * * *  
22  * * *  
23  * * *  
24  * * *  
25  * * *  
26  * * *  
27  * * *  
28  * * *  
29  * * *  
30  * * *  
```
```
traceroute to google.com (173.194.220.101), 30 hops max, 60 byte packets  
 1  _gateway (192.168.1.1)  1.833 ms  2.115 ms  2.204 ms  
 2  * * *  
 3  lag-8-435.bbr01.voronezh.ertelecom.ru (109.195.24.18)  5.644 ms  5.632 ms  7.607 ms  
 4  72.14.215.165 (72.14.215.165)  20.505 ms  21.048 ms  20.478 ms  
 5  72.14.215.166 (72.14.215.166)  21.021 ms  24.577 ms  22.767 ms  
 6  108.170.250.51 (108.170.250.51)  23.689 ms  18.723 ms 108.170.250.34 (108.170.250.34)  18.399 ms  
 7  142.250.239.64 (142.250.239.64)  29.008 ms * *  
 8  108.170.235.204 (108.170.235.204)  32.836 ms 216.239.48.224 (216.239.48.224)  29.147 ms 172.253.66.110 (172.253.66.110)  33.320 ms  
 9  172.253.51.241 (172.253.51.241)  32.258 ms 172.253.51.239 (172.253.51.239)  31.063 ms 172.253.51.243 (172.253.51.243)  30.396 ms  
10  * * *  
11  * * *  
12  * * *  
13  * * *  
14  * * *  
15  * * *  
16  * * *  
17  * * *  
18  * * *  
19  lk-in-f101.1e100.net (173.194.220.101)  30.757 ms *  31.913 ms  
```

### To Google via ICMP:
```
traceroute to google.com (173.194.220.100), 30 hops max, 60 byte packets  
 1  _gateway (192.168.1.1)  2.322 ms  2.267 ms  2.318 ms  
 2  188x232x3x252.dynamic.saratov.ertelecom.ru (188.232.3.252)  3.605 ms  5.640 ms  5.630 ms  
 3  lag-8-435.bbr01.voronezh.ertelecom.ru (109.195.24.18)  7.962 ms  8.072 ms  8.066 ms  
 4  72.14.215.165 (72.14.215.165)  21.306 ms  21.300 ms  21.868 ms  
 5  72.14.215.166 (72.14.215.166)  28.166 ms  28.161 ms  28.154 ms  
 6  * * *  
 7  142.251.49.158 (142.251.49.158)  29.677 ms  29.603 ms *  
 8  108.170.235.204 (108.170.235.204)  30.672 ms  30.661 ms  30.650 ms  
 9  172.253.51.189 (172.253.51.189)  32.462 ms  32.450 ms  32.439 ms  
10  * * *  
11  * * *  
12  * * *  
13  * * *  
14  * * *  
15  * * *  
16  * * *  
17  * * *  
18  * * *  
19  lk-in-f100.1e100.net (173.194.220.100)  30.300 ms  30.289 ms  30.278 ms  
```

### 2. Попробовать определить ОС которая управляет доступными серверами этих сетевых узлов.

Для определения ОС узла можно пользоваться знанием TTL пакета, но это очень неточно. Более точный способ - утилита **nmap**. Но тоже, конечно, не со 100% уверенностью. Т.к. администратор по идее должен всячески скрывать версию ОС сервера для усложнения совершения атаки на него. 

Пробуем определить ОС на сервере Гугла:  
```
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-01 22:40 Na?aoia (ceia)  

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.  

Nmap scan report for google.com (142.251.1.101)  

Host is up (0.031s latency).  

Other addresses for google.com (not scanned): 142.251.1.139 142.251.1.138 142.251.1.100 142.251.1.102 142.251.1.113  

Not shown: 998 filtered ports  

PORT    STATE SERVICE  

80/tcp  open  http  

443/tcp open  https  

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port  

Device type: general purpose  

Running (JUST GUESSING): FreeBSD 11.X (85%)  

OS CPE: cpe:/a:xigmanas:xigmanas cpe:/o:freebsd:freebsd:11.2  

Aggressive OS guesses: XigmaNAS (FreeBSD 11.2-RELEASE) (85%)  


No exact OS matches for host (test conditions non-ideal).  

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 29.63 seconds
```

Утилитка говорит, что с 85% вероятностью там FreeBSD 11.

### 3. При помощи утилиты mtr определить узкие места в сети по маршруту до этих узлов.

Использовал WinMTR.

Тот же google.com. Узкие места:

1. 209.85.249.158 - 72% потерянных запросов
2. 74.125.253.94  - 100мс наихудшее время задержки
|------------------------------------------------------------------------------------------|
|                                      WinMTR statistics                                   |
|                       Host              -   %  | Sent | Recv | Best | Avrg | Wrst | Last |
|------------------------------------------------|------|------|------|------|------|------|
|                           KEENETIC-4194 -    0 |   28 |   28 |    1 |    2 |   10 |    2 |
|188x232x3x252.dynamic.saratov.ertelecom.ru -    0 |   28 |   28 |    2 |    3 |   10 |    2 |
|   lag-8-435.bbr01.voronezh.ertelecom.ru -    0 |   28 |   28 |    2 |    3 |   10 |    2 |
|                           72.14.215.165 -    5 |   24 |   23 |   16 |   18 |   47 |   17 |
|                           72.14.215.166 -    0 |   28 |   28 |   16 |   18 |   41 |   16 |
|                         108.170.250.146 -    0 |   28 |   28 |   16 |   20 |   37 |   21 |
|                          209.85.249.158 -   75 |    8 |    2 |    0 |   31 |   31 |   31 |
|                           74.125.253.94 -    0 |   28 |   28 |   30 |   35 |  100 |   31 |
|                         142.250.238.179 -    0 |   28 |   28 |   32 |   32 |   41 |   32 |
|                   No response from host -  100 |    6 |    0 |    0 |    0 |    0 |    0 |
|                   No response from host -  100 |    6 |    0 |    0 |    0 |    0 |    0 |
|                   No response from host -  100 |    6 |    0 |    0 |    0 |    0 |    0 |
|                   No response from host -  100 |    6 |    0 |    0 |    0 |    0 |    0 |
|                   No response from host -  100 |    6 |    0 |    0 |    0 |    0 |    0 |
|                   No response from host -  100 |    6 |    0 |    0 |    0 |    0 |    0 |
|                           142.251.1.139 -    0 |   28 |   28 |   30 |   31 |   38 |   31 |
|________________________________________________|______|______|______|______|______|______|
   WinMTR v0.92 GPL V2 by Appnor MSP - Fully Managed Hosting & Cloud Provider

# Исследовать работу протокола ICMP и утилит traceroute и ping

### 1. Выяснить количество хопов до крупных сетевых узлов: google, yandex, cisco, aws, microsoft, etc.

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

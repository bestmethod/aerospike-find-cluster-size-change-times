# aerospike-find-cluster-size-change-times
Find times where cluster-size changed on any node from each log file given. Because pipe-grep-pipe-etc was waaaay to slow.

```
$ python find-cluster-size-change.py *log
---------------- Processing file: 1.log ----------------
Nov 30 2017 17:17:09 GMT: INFO (info): (ticker.c:167) NODE-ID bb9d3877282f50e CLUSTER-SIZE 3
Dec 01 2017 20:05:46 GMT: INFO (info): (ticker.c:167) NODE-ID bb9d3877282f50e CLUSTER-SIZE 2
Dec 01 2017 20:15:17 GMT: INFO (info): (ticker.c:167) NODE-ID bb9d3877282f50e CLUSTER-SIZE 3
---------------- Processing file: 2.log ----------------
Dec 02 2017 08:17:08 GMT: INFO (info): (ticker.c:167) NODE-ID bb9edc6ab475112 CLUSTER-SIZE 3
Dec 02 2017 09:27:53 GMT: INFO (info): (ticker.c:167) NODE-ID bb9edc6ab475112 CLUSTER-SIZE 2
Dec 02 2017 09:28:03 GMT: INFO (info): (ticker.c:167) NODE-ID bb9edc6ab475112 CLUSTER-SIZE 3
---------------- Processing file: 3.log ----------------
Dec 01 2017 00:00:05 GMT: INFO (info): (ticker.c:167) NODE-ID bb95f0265530c0a CLUSTER-SIZE 3
Dec 06 2017 02:47:19 GMT: INFO (info): (ticker.c:167) NODE-ID bb95f0265530c0a CLUSTER-SIZE 2
Dec 06 2017 03:18:00 GMT: INFO (info): (ticker.c:167) NODE-ID bb95f0265530c0a CLUSTER-SIZE 3
Dec 06 2017 12:54:22 GMT: INFO (info): (ticker.c:167) NODE-ID bb95f0265530c0a CLUSTER-SIZE 2
Dec 07 2017 08:16:36 GMT: INFO (info): (ticker.c:167) NODE-ID bb95f0265530c0a CLUSTER-SIZE 3
```

---
title: PreFormattedText
marp: true
paginate: true
---

# Logging

```console
2022-02-09 06:47:02.607 [pool-3-thread-2] INFO  com.github.obiwanlansi.alfredsearch.database.AlfredDatabase - Insert Bookmark: httpX://www.howtogeek.com/198615/how-to-check-if-your-linux-system-is-32-bit-or-64-bit/
2022-02-09 06:47:02.664 [pool-3-thread-2] INFO  com.github.obiwanlansi.alfredsearch.database.AlfredDatabase - Timespan (insertBookmark): 57 ms
2022-02-09 06:47:11.201 [pool-3-thread-1] ERROR com.github.obiwanlansi.alfredsearch.indexer.AlfredBookmarkIndexer - Connect timed out
java.net.SocketTimeoutException: Connect timed out
    at sun.nio.ch.NioSocketImpl.timedFinishConnect(NioSocketImpl.java:546) ~[?:?]
    at sun.nio.ch.NioSocketImpl.connect(NioSocketImpl.java:597) ~[?:?]
    at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:333) ~[?:?]
    at java.net.Socket.connect(Socket.java:648) ~[?:?]
    at sun.security.ssl.SSLSocketImpl.connect(SSLSocketImpl.java:290) ~[?:?]
    at sun.net.NetworkClient.doConnect(NetworkClient.java:177) ~[?:?]
    at sun.net.www.http.HttpClient.openServer(HttpClient.java:474) ~[?:?]
    at sun.net.www.http.HttpClient.openServer(HttpClient.java:569) ~[?:?]
    at com.github.obiwanlansi.alfredsearch.indexer.AlfredBookmarkIndexer.readBookmarkContent(AlfredBookmarkIndexer.java:182) ~[AlfredSearch.jar:?]
    at com.github.obiwanlansi.alfredsearch.indexer.AlfredBookmarkIndexer.lambda$runIndexer$(AlfredBookmarkIndexer.java:256) ~[AlfredSearch.jar:?]
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1130) [?:?]
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:630) [?:?]
    at java.lang.Thread.run(Thread.java:832) [?:?]
2022-02-09 06:47:11.262 [pool-3-thread-1] INFO  com.github.obiwanlansi.alfredsearch.database.AlfredDatabase - Insert Bookmark: httpx://picockpit.com/raspberry-pi/de/ultimative-liste-ungewohnlicher-aber-wirklich-nutzlicher-linux-shell-befehle/
2022-02-09 06:47:11.272 [pool-3-thread-1] INFO  com.github.obiwanlansi.alfredsearch.database.AlfredDatabase - Timespan (insertBookmark): 10 ms
2022-02-09 06:47:11.272 [Thread-3] INFO  com.github.obiwanlansi.alfredsearch.indexer.AlfredBookmarkIndexer - Timespan: 28833 ms
2022-02-09 06:47:42.225 [Thread-4] INFO  com.github.obiwanlansi.alfredsearch.database.AlfredDatabase - Timespan (getAllFiles): 1367 ms
```

---

# Metrics

```console
http_requests_total{method="post",code="200"} 1027 1395066363000
http_requests_total{method="post",code="400"}    3 1395066363000

# Escaping in label values:
msdos_file_access_time_seconds{path="C:\\DIR\\FILE.TXT",error="Cannot find file:\n\"FILE.TXT\""} 1.458255915e9

# Minimalistic line:
metric_without_timestamp_and_labels 12.47

# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{le="0.05"} 24054
http_request_duration_seconds_bucket{le="0.1"} 33444
http_request_duration_seconds_sum 53423
http_request_duration_seconds_count 144320

# TYPE rpc_duration_seconds summary
rpc_duration_seconds{quantile="0.01"} 3102
rpc_duration_seconds{quantile="0.05"} 3272
rpc_duration_seconds_sum 1.7560473e+07
rpc_duration_seconds_count 2693
```

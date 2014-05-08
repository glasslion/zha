Title: Appscale——Google App Engine的开源克隆/替代
Date: 2013-08-26 14:13:20
Author: Leonardo Zhou
Category: Others
Slug: post/59374017369/appscale-google-app-engine
Save_as: post/59374017369/appscale-google-app-engine/index.html
Tags: google
Summary: 完全利用开源项目, 就能在自己的设备上搭建 一套和 Google App Engine 的 API 兼容的 PaaS

这个项目其实出来以及很久了，只是前几天才在HackerNews引起关注，github上的 star,
watch数也随之飙升。我之前苦苦搜寻GAE的替代时，都没发现这个项目。

使用界面:
![appscale1][]

Appscale 在底层使用了大量知名的开源软件， 包括并不限于：

 - Apache Cassandra,
 - Apache Hadoop,
 - Apache HBase,
 - Apache Thrift,
 - Apache Zookeeper,
 - Celery,
 - ejabberd,
 - HAProxy,
 - Hypertable,
 - Nginx,
 - RabbitMQ,

Appscale 在这些开源项目 之上实现了一套和 Google App Engine 兼容的 API。而且该项目得到了 Google 官方支持，不愁未来 Google App Engine 更新后的兼容性。

无论是编程语言，db, 搜索，map reduce 还是IaaS, 各层都是 pluggable 的，开发者可以自由选择自己最熟悉的 tech stack， 目测是一个很灵活的 PaaS.


![appscale2][]


架构图:


![appscale3][]

</p>

![appscale4][]


[view on Github][]


  [appscale1]: http://ww2.sinaimg.cn/large/6c3391c1gw1eeea3r5v0tj20dw0a6gm9.jpg
  [appscale2]: http://ww4.sinaimg.cn/large/6c3391c1gw1eeea43yhwlj20dw07t3zi.jpg
  [appscale3]: http://ww2.sinaimg.cn/large/6c3391c1gw1eeea4is7soj20dw09r75b.jpg
  [appscale4]: http://ww2.sinaimg.cn/large/6c3391c1gw1eeea5087p2j20do0fwmym.jpg
  [view on Github]: https://github.com/AppScale/appscale

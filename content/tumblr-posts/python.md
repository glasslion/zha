Title: Python的双层循环可以这么玩
Date: 2013-07-15 00:33:00
Author: Leonardo Zhou
Category: Python
Slug: post/55431622560/python
Save_as: post/55431622560/python/index.html
Summary: I love generators. 

![images/python_vs_ java_loop.png](http://ww4.sinaimg.cn/large/6c3391c1gw1eecwl0oosej20dw0dw3z7.jpg)


把对循环的控制，过滤拆分到一个generator中，在主循环中只存放对循环对象操作的逻辑，不仅是代码更加清晰，也避免了从内层循环退出的麻烦事

参考 [Loop like a native: while, for, iterators, generators (PyCon US
2013 Talk)](http://nedbatchelder.com/text/iter/iter.html)

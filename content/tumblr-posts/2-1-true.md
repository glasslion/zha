Title: "2" < 1 == True
Date: 2013-06-21 11:45:16
Author: Leonardo Zhou
Category: Python
Slug: post/53490665799/2-1-true
Save_as: post/53490665799/2-1-true/index.html
Tags: fail

![python_compare][]


## Python比较规则浅析 ##


今天为了捉一个臭虫耗废了近一个小时，最后发现是 `if foo > 1:`这里的foo实际是字符串，导致`foo`是`"0"`时，`"0" > 1`为真。于是便花了点时间研究了下`Python`比较运算规则。


在`Python2`中，比较运算遵循以下规则:


1.  数字和数字按大小排序 （数字类型包括 int, float, long, complex,
    **bool**）
2.  字符串按字符串按字典序排序(str, unicode)
3.  数字类型和非数字类型比较，除None外,数字类型总是小于非数字类型。
4.  两个非数字不同类型，按其类型名的字典与排序
5.  第4点有一个特例，老式类的实例总是小于新式类
6.  非数字/字符串类型的同一类型的不同实例的比较，如果类定义了`__cmp__()`方法，则用该方法比较
7.  同上，若类型没定义`__cmp__()`方法， 则按实例在内存中的地址排序
8.  None < None
9.  3，4，5，7 是CPython的实现，不是Python语言自身的标准，参见[CPython
    implementation detail][]。
    Python语言只要求对非数字和字符串类型的不同对象的比较，总是不想等的，比较结果可以是任意的，但必须是一致的（即多次比较，结果恒定）。


`Python3`终于修了这个bug ( [What’s New In Python 3.0][] ), 规则如下：


1.  incomparable类型对象比较 \<, \<=, \>=, \> 会 raise `TypeError`
2.  incomparable类型对象比较 ！=, == 仍是合法的，但总为`False`
3.  `cmp()`和`__cmp__()`方法被弃置了，取而代之的是`__lt__()`，`__eq__()`，`__hash__()`
    ...


`Python2` 当初会设计这种比较规则，可能是为了便于对包含不同类型对象的容器排序。`list.sort()`和`sorted()`都仿照了C/C++里的`sort`。`Python2.4`后`sort`使用`key`来比较不同对象显然更Pythonic

更多例子，参见[Sorting Mini-HOW TO][]


  [python_compare]: http://ww4.sinaimg.cn/large/6c3391c1gw1eef2607ezbj20dw0dwq3j.jpg
  [CPython implementation detail]: http://docs.python.org/2/library/stdtypes.html#comparisons
  [What’s New In Python 3.0]: http://docs.python.org/3.0/whatsnew/3.0.html?highlight=incomparable#ordering-comparisons
  [Sorting Mini-HOW TO]: http://wiki.python.org/moin/HowTo/Sorting/

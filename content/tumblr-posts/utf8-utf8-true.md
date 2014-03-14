Title: 为什么有些网址中使用“utf8=✓”而不是“utf8=true”?
Date: 2013-01-18 01:11:00
Author: Leonardo Zhou
Category: 分享链接
Slug: post/40769640185/utf8-utf8-true
Save_as: post/40769640185/utf8-utf8-true/index.html
Tags: 冷知识, 黑魔法

IE又中枪了。 老版本的IE浏览器 (< IE9) 提交 form 数据时，会尽可能地使用`Latin-1`编码， 而不是群众喜闻乐见的 `utf-8` 编码。

✓这个无法用`Latin-1`编码的字符会迫使IE使用 `utf-8`，从而简化了server端的实现。

同理，Ruby on Rails 是在 form 里插入 一个 值为 ☃ 的 hidden input field。


Stackexchange 上的问答: [Is the use of “utf8=✓” preferable to “utf8=true”?](http://programmers.stackexchange.com/questions/168751/is-the-use-of-utf8-preferable-to-utf8-true?newsletter=1&nlcode=44917%7c4830)

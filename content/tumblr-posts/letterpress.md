Title: Letterpress
Date: 2013-08-18 23:17:41
Author: Leonardo Zhou
Category: Others
Slug: post/58607609189/letterpress
Save_as: post/58607609189/letterpress/index.html
Tags: tool

Letterpress是 [墨客][] 的作者 Wang Ling
用Python开发的一款静态博客生成器。


![image/letterpress.png][]

Letterpress的风格十分简洁，使用Markdown语法。作者由于习惯用iPad写作，在设计时也特别考虑了在移动平台上的使用体验。

服务器端的Letterpress 后台进程通过 [pyinotify][],监控服务器指定目录下的Markdown文件的增改删，然后将相同的动作作用于对静态博客文件上。

配合上dropbox,可以轻易得将本地文件变化，推送到服务器端。管理博客也就是用Markdown编辑器里增改删文件的事。


Letterpress还支持使用[Pygments][]高亮Markdown文件里的代码块。


  [墨客]: http://moke.com/
  [image/letterpress.png]: http://ww2.sinaimg.cn/large/6c3391c1gw1eee5qg3a1jj20dw09o3yx.jpg
  [pyinotify]: https://github.com/seb-m/pyinotify/
  [Pygments]: http://pygments.org/

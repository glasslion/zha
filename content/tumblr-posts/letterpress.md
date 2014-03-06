Title: Letterpress
Date: 2013-08-18 23:17:41
Author: glasslion
Category: text
Slug: post/58607609189/letterpress

Letterpress是 [墨客][] 的作者 Wang Ling
用Python开发的一款静态博客生成器。

</p>

![][]

</p>

Letterpress的风格十分简洁，使用Markdown语法。作者由于习惯用iPad写作，在设计时也特别考虑了在移动平台上的使用体验。服务器端的
Letterpress 后台进程通过 [pyinotify][]
,监控服务器指定目录下的Markdown文件的增改删，然后将相同的动作作用于对静态博客文件上。配合上dropbox,
可以轻易得将本地文件变化，推送到服务器端。
管理博客也就是用Markdown编辑器里增改删文件的事。

</p>

Letterpress还支持使用[Pygments][]高亮Markdown文件里的代码块。

</p>

  [墨客]: http://moke.com/
  []: http://media.tumblr.com/61f52fa35e169960c2663d5d306f0e65/tumblr_inline_miyp02s0uH1qz4rgp.png
  [pyinotify]: https://github.com/seb-m/pyinotify
  [Pygments]: http://pygments.org/

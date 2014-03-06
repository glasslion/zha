Title: 为 Github for Windows 设置代理
Date: 2013-01-21 15:02:00
Author: glasslion
Category: text
Slug: post/41087594715/github-for-windows

![](http://media.tumblr.com/db9859f4cabcd6dadacaf2252f4409d0/tumblr_inline_mi9vwpAoAt1qz4rgp.jpg)
今天在公司电脑上安装了Github for Windows， 但一直无法顺利登陆。由于公司电脑必须通过HTTP代理才能连上外网，而Github for Windows自己又不提供设置代理的界面，就只能求助Google了。

Google `github for windows proxy` 到的前几个link都说要设置 `.gitconfig`, 加入下列内容:
<code>
[http]

proxy = host:port

[https]

proxy = host:port
</code>

很不幸，添加后依旧登陆不上。

之后又排除了Github for Windows 会自动适应IE的代理设置的可能。恰好，今天开始github成为了gfw敏感词，于是又怀疑到了方校长头上。

最后换了搜索关键词`github for windows login failed`,才在这个链接里发现了正解 。[](https://github.com/heroku/heroku/issues/319)


打开命令行

`SET HTTPS_PROXY=host:port`

`SET HTTP_PROXY=host:port`

就行了

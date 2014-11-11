Title: Python Packaging 编年史
Author: Leonardo Zhou
Category: Python
Date: 2014-04-16 20:57:00
Slug: post/python-packaging-timeline
save_as: post/python-packaging-timeline/index.html
Tags: packaging

<div id="cd-timeline" class="cd-container" style="display:body" markdown='1'>
## distutils-sig 工作组成立
最初，Python 并没有自带的包管理器。 纯 Python 的模块（module）往往是通过直接拷贝源代码到相应目录来安装的。 如果要发布的模块包含 C extension ，那么还要写一个冗长的 `Makefile`。 导致程序员之间想要共享模块很不方便。

在 1998年的 Pycon 上， 终于有人 hold 不住了， Greg Ward 作了一场名为 "Building Extensions Considered Painful" 的演讲，引起了很多与会者的共鸣。 于是会后他们建立了 distutils-sig 工作组和同名的邮件列表，专门用来讨论开发 Python 包管理系统的相关事宜。

*1998年*

## disutils 被纳入 Python 标准库
历时2年的开发后，distutils 终于修成正果，被添加到 Python 1.6 的标准库中。从此 Python 社区有了自己的 包管理库。

`Disutils` 使用 `setup.py` 作为 模块的配置文件， 并通过 `python setup.py CMD` 的形式， 提供了一套用于编译 C extension, 打包 ... 的命令

尽管用今天的眼光来看，`Disutils` 有很多不足 。但在当时 `Disutils` 确实是一个十分出色的包管理系统。由于吸取了Perl 社区1在`Makefile.PL` 上的教训，且为了更好地跨平台， `Disutils` 没有基于当时盛行的 Makefile。`Disutils` 充分运用了 Python 简明而又强大的特性， 没有为了 Packaging 去单独研发一套 DSL， `setup.py` 就是一个 普通的 Python 文件。

*2000年*

## catalog-sig 工作组成立
当时 Perl 社区 的 CPAN 运营的非常成功。 眼红的 Pythonista 们也开始着手创建 Python 的公共第三方模块库

*2000年*

## PEP 241 Metadata for Python Software Packages
`A.M. Kuchling` 起草了 PEP 241,用于规范 Python Package 的元信息

*2001年*

## PEP 301 Package Index and Metadata for Distutils
`PEP 301` 是 `PEP 241` 的补充。约定了元信息 该以怎样的格式被存储在 `setup.py` 中， 来让 `disutils` 和 `PyPI` 识别。

*2002年*

## PyPI 正式上线
Python Package Index(PyPI) 最初也被叫做 Cheeseshop。时至今日， PyPI 已经收录近 5万个 第三方开源模块。
`Disutils` 也做了相应的升级，以支持元数据和上传 Python Package 到 PyPI。

*2003年*

## setuptools 发布

 `setuptools` 是由 Phillip Eby 开发的。

*2004年*

## virtualenv 发布
最初， 所有的 Python Package 都是安装在系统的全局 `site-packages` 目录下。开发者要安装第三方库，常常要有 `root` 权限。不同项目安装的第三方库也容易导致版本冲突。Ian Bicking 开发了 `virtualenv ` 用于创建独立的 Python 运行环境。virtualenv 和 pip 应该是每个 Python 程序员熟知的工具， 这里就不再赘述了。

*2007年*

## pip 发布

`pip` 同样是由 Ian Bicking 开发。

*2008年*

## distribute

`setuptools` 很快就成为 Python 社区中首选的包管理库。但是正当 `setuptools` 如日中天的时候，它的开发却嘎然而止。 明明有一大堆 pull request 在等待 merge, 开发者却杳无音信。Python 3 的支持也迟迟不加。 最终 Tarek Ziade 从 `setuptools` fork 出了 `distribute`。

虽然 `distribute` 在各方面都优于 `setuptools`， 但 `setuptools` 毕竟盛名在外，Python 社区 从  `setuptools` 转移到 `distribute` 上话了很长时间， 并造成了一定的社区分裂。

`2008年`

## PyPA 成立

`2011年 2月 28日`


## Distutils2 的开发被终止
曾被寄予厚望的 `disutils2`，没能按原计划在随 Python 3.3. 发布。

`disutils2` 项目失败的原因有很多。 `disutils2` 的开发者人数只有 1-2 名，而且都是在用业余时间开发, 由于开发者没有足够的精力， 开发经常陷入停滞。项目也十分缺少 beta 用户，也很少得到用户的反馈。

`2011年 2月 28日`

## Pycon 2013 - Directions for Packaging
由于 `disutils2` 项目被放弃，对开发者而言， 未来的 Python Packaing 会是怎么样是个未知数。

 于是趁着 Python 程序员的年度盛会 Pycon 的召开，PyPA 设法让 `distributue`,  `virtualenv`, `pip`, `wheel`,  `PyPI`,  `zc.buildout` 等项目的开发者们齐聚一堂, 共同讨论和规划 Python Packaging 未来的开发路线。
[Youtube 视频](https://www.youtube.com/watch?v=ePFWp3oSfyU)

`2013年 3月 15日`


## PyPI 有了 CDN 加速
Fastly 公司很慷慨地为 PyPI 提供了免费的 CDN 加速。

天朝用户应该对此印象十分深刻， 这倒不是因为有了 CDN 之后访问速度变快了。2014年上半年有一段时间 PyPI无法正常访问就是拜某墙所赐。

`2013年 5月 26日`

## Distribute 项目被 merge 回了 setuptools

`2013年 6月 9日`

## pip 成为 Python 3.4 自带的包管理库
让我们看个冷笑话吧：

甲： Python 的包管理工具是什么？ 

乙：`pip`

甲：pip` 是 Python 自带的吗？

乙：不是。 甲：那么我应该怎么安装 pip ? 

乙： `easy_install pip`

甲：`easy_install` 是什么？

乙：一个 Python 包管理工具

甲：...

`2013年 8月 10日`
</div>
<style type="text/css">

*, *:after, *:before {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

.entry-content {
  color: #7f8c97;
  background-color: #e9f0f5;
}

.cd-container a {
  color: #acb7c0;
  text-decoration: none;
  font-family: "Open Sans", sans-serif;
}

.cd-container img {
  max-width: 100%;
}

.cd-container h1, .cd-container h2 {
  font-family: "Open Sans", sans-serif;
  font-weight: bold;
  margin-top: 0 !important;
}

.cd-container {
  /* this class is used to give a max-width to the element it is applied to, and center it horizontally when it reaches that max-width */
  width: 90%;
  max-width: 1170px;
  margin: 0 auto;
}
.cd-container::after {
  /* clearfix */
  content: '';
  display: table;
  clear: both;
}

#cd-timeline {
  position: relative;
  padding: 2em 0;
  margin-top: 2em;
  margin-bottom: 2em;
}
#cd-timeline::before {
  /* this is the vertical line */
  content: '';
  position: absolute;
  top: 0;
  left: 18px;
  height: 100%;
  width: 4px;
  background: #d7e4ed;
}

@media only screen and (min-width: 1170px) {
  #cd-timeline {
    margin-top: 3em;
    margin-bottom: 3em;
  }
  #cd-timeline::before {
    left: 50%;
    margin-left: -2px;
  }
}

.timeline-block {
  position: relative;
  margin: 2em 0;
  *zoom: 1;
}
.timeline-block:before, .timeline-block:after {
  content: " ";
  display: table;
}
.timeline-block:after {
  clear: both;
}
.timeline-block:first-child {
  margin-top: 0;
}
.timeline-block:last-child {
  margin-bottom: 0;
}
@media only screen and (min-width: 1170px) {
  .timeline-block {
    margin: 4em 0;
  }
  .timeline-block:first-child {
    margin-top: 0;
  }
  .timeline-block:last-child {
    margin-bottom: 0;
  }
}

.cd-timeline-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  box-shadow: 0 0 0 4px #ffffff, inset 0 2px 0 rgba(0, 0, 0, 0.08), 0 3px 0 4px rgba(0, 0, 0, 0.05);
}
.cd-timeline-img .genericon {
  color: white;
  font-size: 36px;
  margin-left: 14px;
  margin-top: 14px;
}
.cd-timeline-img.cd-green {
  background: #75ce66;
}
.cd-timeline-img.cd-red {
  background: #c03b44;
}
.cd-timeline-img.cd-yellow {
  background: #f0ca45;
}
@media only screen and (min-width: 1170px) {
  .cd-timeline-img {
    width: 60px;
    height: 60px;
    left: 50%;
    margin-left: -30px;
    /* Force Hardware Acceleration in WebKit */
    -webkit-transform: translateZ(0);
    -webkit-backface-visibility: hidden;
  }
  .cssanimations .cd-timeline-img.is-hidden {
    visibility: hidden;
  }
  .cssanimations .cd-timeline-img.bounce-in {
    visibility: visible;
    -webkit-animation: cd-bounce-1 0.6s;
    -moz-animation: cd-bounce-1 0.6s;
    animation: cd-bounce-1 0.6s;
  }
}

@-webkit-keyframes cd-bounce-1 {
  0% {
    opacity: 0;
    -webkit-transform: scale(0.5);
    -moz-transform: scale(0.5);
    -ms-transform: scale(0.5);
    -o-transform: scale(0.5);
    transform: scale(0.5);
  }
  60% {
    opacity: 1;
    -webkit-transform: scale(1.2);
    -moz-transform: scale(1.2);
    -ms-transform: scale(1.2);
    -o-transform: scale(1.2);
    transform: scale(1.2);
  }
  100% {
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transform: scale(1);
  }
}
@-moz-keyframes cd-bounce-1 {
  0% {
    opacity: 0;
    -webkit-transform: scale(0.5);
    -moz-transform: scale(0.5);
    -ms-transform: scale(0.5);
    -o-transform: scale(0.5);
    transform: scale(0.5);
  }
  60% {
    opacity: 1;
    -webkit-transform: scale(1.2);
    -moz-transform: scale(1.2);
    -ms-transform: scale(1.2);
    -o-transform: scale(1.2);
    transform: scale(1.2);
  }
  100% {
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transform: scale(1);
  }
}
@-o-keyframes cd-bounce-1 {
  0% {
    opacity: 0;
    -webkit-transform: scale(0.5);
    -moz-transform: scale(0.5);
    -ms-transform: scale(0.5);
    -o-transform: scale(0.5);
    transform: scale(0.5);
  }
  60% {
    opacity: 1;
    -webkit-transform: scale(1.2);
    -moz-transform: scale(1.2);
    -ms-transform: scale(1.2);
    -o-transform: scale(1.2);
    transform: scale(1.2);
  }
  100% {
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transform: scale(1);
  }
}
@keyframes cd-bounce-1 {
  0% {
    opacity: 0;
    -webkit-transform: scale(0.5);
    -moz-transform: scale(0.5);
    -ms-transform: scale(0.5);
    -o-transform: scale(0.5);
    transform: scale(0.5);
  }
  60% {
    opacity: 1;
    -webkit-transform: scale(1.2);
    -moz-transform: scale(1.2);
    -ms-transform: scale(1.2);
    -o-transform: scale(1.2);
    transform: scale(1.2);
  }
  100% {
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transform: scale(1);
  }
}
.timeline-content {
  position: relative;
  margin-left: 60px;
  background: #ffffff;
  border-radius: 0.25em;
  padding: 1em;
  box-shadow: 0 3px 0 #d7e4ed;
  *zoom: 1;
}
.timeline-content:before, .timeline-content:after {
  content: " ";
  display: table;
}
.timeline-content:after {
  clear: both;
}
.timeline-content h2 {
  color: #303e49;
}
.timeline-content p, .timeline-content .cd-date {
  font-size: 13px;
  font-size: 0.8125rem;
}
.timeline-content .cd-date {
  display: inline-block;
}
.timeline-content p {
  margin: 1em 0;
  line-height: 1.6;
}
.timeline-content .cd-date {
  float: left;
  padding: .8em 0;
  opacity: .7;
}
.timeline-content::before {
  content: '';
  position: absolute;
  top: 16px;
  right: 100%;
  height: 0;
  width: 0;
  border: 7px solid transparent;
  border-right: 7px solid #ffffff;
}
@media only screen and (min-width: 768px) {
  .timeline-content h2 {
    font-size: 20px;
    font-size: 1.25rem;
  }
  .timeline-content p {
    font-size: 16px;
    font-size: 1rem;
  }
 .timeline-content .cd-date {
    font-size: 14px;
    font-size: 0.875rem;
  }
}
@media only screen and (min-width: 1170px) {
  .timeline-content {
    margin-left: 0;
    padding: 1.6em;
    width: 45%;
  }
  .timeline-content::before {
    top: 24px;
    left: 100%;
    border-color: transparent;
    border-left-color: #ffffff;
  }
  .timeline-content .cd-date {
    position: absolute;
    width: 100%;
    left: 132%;
    top: 6px;
    font-size: 16px;
    font-size: 1rem;
  }
  .timeline-block:nth-child(even) .timeline-content {
    float: right;
  }
  .timeline-block:nth-child(even) .timeline-content::before {
    top: 24px;
    left: auto;
    right: 100%;
    border-color: transparent;
    border-right-color: #ffffff;
  }

  .timeline-block:nth-child(even) .timeline-content .cd-date {
    left: auto;
    right: 132%;
    text-align: right;
  }
  .cssanimations .timeline-content.is-hidden {
    visibility: hidden;
  }
  .cssanimations .timeline-content.bounce-in {
    visibility: visible;
    -webkit-animation: cd-bounce-2 0.6s;
    -moz-animation: cd-bounce-2 0.6s;
    animation: cd-bounce-2 0.6s;
  }
}

@media only screen and (min-width: 1170px) {
  /* inverse bounce effect on even content blocks */
  .cssanimations .timeline-block:nth-child(even) .timeline-content.bounce-in {
    -webkit-animation: cd-bounce-2-inverse 0.6s;
    -moz-animation: cd-bounce-2-inverse 0.6s;
    animation: cd-bounce-2-inverse 0.6s;
  }
}
@-webkit-keyframes cd-bounce-2 {
  0% {
    opacity: 0;
    -webkit-transform: translateX(-100px);
    -moz-transform: translateX(-100px);
    -ms-transform: translateX(-100px);
    -o-transform: translateX(-100px);
    transform: translateX(-100px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateX(20px);
    -moz-transform: translateX(20px);
    -ms-transform: translateX(20px);
    -o-transform: translateX(20px);
    transform: translateX(20px);
  }
  100% {
    -webkit-transform: translateX(0);
    -moz-transform: translateX(0);
    -ms-transform: translateX(0);
    -o-transform: translateX(0);
    transform: translateX(0);
  }
}
@-moz-keyframes cd-bounce-2 {
  0% {
    opacity: 0;
    -webkit-transform: translateX(-100px);
    -moz-transform: translateX(-100px);
    -ms-transform: translateX(-100px);
    -o-transform: translateX(-100px);
    transform: translateX(-100px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateX(20px);
    -moz-transform: translateX(20px);
    -ms-transform: translateX(20px);
    -o-transform: translateX(20px);
    transform: translateX(20px);
  }
  100% {
    -webkit-transform: translateX(0);
    -moz-transform: translateX(0);
    -ms-transform: translateX(0);
    -o-transform: translateX(0);
    transform: translateX(0);
  }
}
@-o-keyframes cd-bounce-2 {
  0% {
    opacity: 0;
    -webkit-transform: translateX(-100px);
    -moz-transform: translateX(-100px);
    -ms-transform: translateX(-100px);
    -o-transform: translateX(-100px);
    transform: translateX(-100px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateX(20px);
    -moz-transform: translateX(20px);
    -ms-transform: translateX(20px);
    -o-transform: translateX(20px);
    transform: translateX(20px);
  }
  100% {
    -webkit-transform: translateX(0);
    -moz-transform: translateX(0);
    -ms-transform: translateX(0);
    -o-transform: translateX(0);
    transform: translateX(0);
  }
}
@keyframes cd-bounce-2 {
  0% {
    opacity: 0;
    -webkit-transform: translateX(-100px);
    -moz-transform: translateX(-100px);
    -ms-transform: translateX(-100px);
    -o-transform: translateX(-100px);
    transform: translateX(-100px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateX(20px);
    -moz-transform: translateX(20px);
    -ms-transform: translateX(20px);
    -o-transform: translateX(20px);
    transform: translateX(20px);
  }
  100% {
    -webkit-transform: translateX(0);
    -moz-transform: translateX(0);
    -ms-transform: translateX(0);
    -o-transform: translateX(0);
    transform: translateX(0);
  }
}
@-webkit-keyframes cd-bounce-2-inverse {
  0% {
    opacity: 0;
    -webkit-transform: translateX(100px);
    -moz-transform: translateX(100px);
    -ms-transform: translateX(100px);
    -o-transform: translateX(100px);
    transform: translateX(100px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateX(-20px);
    -moz-transform: translateX(-20px);
    -ms-transform: translateX(-20px);
    -o-transform: translateX(-20px);
    transform: translateX(-20px);
  }
  100% {
    -webkit-transform: translateX(0);
    -moz-transform: translateX(0);
    -ms-transform: translateX(0);
    -o-transform: translateX(0);
    transform: translateX(0);
  }
}
@-moz-keyframes cd-bounce-2-inverse {
  0% {
    opacity: 0;
    -webkit-transform: translateX(100px);
    -moz-transform: translateX(100px);
    -ms-transform: translateX(100px);
    -o-transform: translateX(100px);
    transform: translateX(100px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateX(-20px);
    -moz-transform: translateX(-20px);
    -ms-transform: translateX(-20px);
    -o-transform: translateX(-20px);
    transform: translateX(-20px);
  }
  100% {
    -webkit-transform: translateX(0);
    -moz-transform: translateX(0);
    -ms-transform: translateX(0);
    -o-transform: translateX(0);
    transform: translateX(0);
  }
}
@-o-keyframes cd-bounce-2-inverse {
  0% {
    opacity: 0;
    -webkit-transform: translateX(100px);
    -moz-transform: translateX(100px);
    -ms-transform: translateX(100px);
    -o-transform: translateX(100px);
    transform: translateX(100px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateX(-20px);
    -moz-transform: translateX(-20px);
    -ms-transform: translateX(-20px);
    -o-transform: translateX(-20px);
    transform: translateX(-20px);
  }
  100% {
    -webkit-transform: translateX(0);
    -moz-transform: translateX(0);
    -ms-transform: translateX(0);
    -o-transform: translateX(0);
    transform: translateX(0);
  }
}
@keyframes cd-bounce-2-inverse {
  0% {
    opacity: 0;
    -webkit-transform: translateX(100px);
    -moz-transform: translateX(100px);
    -ms-transform: translateX(100px);
    -o-transform: translateX(100px);
    transform: translateX(100px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateX(-20px);
    -moz-transform: translateX(-20px);
    -ms-transform: translateX(-20px);
    -o-transform: translateX(-20px);
    transform: translateX(-20px);
  }
  100% {
    -webkit-transform: translateX(0);
    -moz-transform: translateX(0);
    -ms-transform: translateX(0);
    -o-transform: translateX(0);
    transform: translateX(0);
  }
}
</style>
<script type="text/javascript" src="//upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.3.min.js"></script>
<script type="text/javascript">
$(function () {
    $('#cd-timeline > h2').each(function(){
      var $this = $(this);
      // use .add() and .nextUntil() to get both the .section-header
      // and .section-item elements into a single set for our .wrapAll() call
      $this.add($this.nextUntil('#cd-timeline > h2', '#cd-timeline > p'))
        .wrapAll('<div class="timeline-content"/>');
    });

    $('#cd-timeline > .timeline-content').wrap('<div class="timeline-block"/>');

    $('#cd-timeline .timeline-content').each(function(){
        var $this = $(this);
        date_text = $this.children('p:last').text();
        $this.children('p:last').remove();
        $this.append('<span class="cd-date"/>')
        $this.children('.cd-date').text(date_text);
    });

    $('#cd-timeline .timeline-block').each(function(){
        var $this = $(this);
        $this.prepend('<div class="cd-timeline-img"></div>');
        colors = ['cd-green', 'cd-red', 'cd-yellow'];
        rand_color = colors[Math.floor(Math.random()*colors.length)];
        $this.children('.cd-timeline-img').addClass(rand_color);
        $this.children('.cd-timeline-img').append('<span class="genericon"/>')
        icons = ['genericon-pinned', 'genericon-week', 'genericon-day','genericon-month', 'genericon-time', 'genericon-user'];
        rand_icon = icons[Math.floor(Math.random()*icons.length)];
        $this.find('.genericon').addClass(rand_icon);
 
    });
});

</script>
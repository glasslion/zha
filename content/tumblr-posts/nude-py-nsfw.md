Title: 无节操的nude.py识别哔～～～～图评测[NSFW]
Date: 2013-08-12 23:15:46
Author: Leonardo Zhou
Category: Python
Slug: post/58062234806/nude-py-nsfw
Save_as: post/58062234806/nude-py-nsfw/index.html
Tags: image-processing 

发个无节操的： [nude.py][]


故名思意，nude.py就是一个Python实现的，判断一张图片是否是nude的library.

安装很简单：

    pip install nudepy


nude.py的图片识别/处理是依赖于`PIL`或`Pillow`的，由于`Pillow`的安装过程比`PIL`简单很多，强烈推荐用`Pillow`。


    # 让Pillow支持jpeg
    # 若未安装libjpeg,用Pillow处理JPEG 图片，会报 IOError: decoder jpeg not available
    # 此时要先pip uninstall Pillow, 安装好 libjpeg,再重新 pip instal  Pillow
    sudo apt-get install libjpeg8-dev pip install Pillow

nude的API很简单：

<div class="monokai">
    import nudefrom nude import Nudeprint(nude.is_nude('./nude.rb/spec/images/damita.jpg'))n = Nude('./nude.rb/spec/images/damita.jpg')n.parse()print("damita :", n.result, n.inspect())

</div>

实测结果：


先来几张吾王的:

![][]

  

![][1]

  

![][2]

  

![][3]

  

![][4]

这几张~~玉照~~御照被nude.py毫无异议得判为nude，就连下面这张不怎么犯规的的，也没能幸免


![][5]

不过下面这种尺度的，就不会被错杀了。


![][6]

这让我想起了当年让小朋友们闻风丧胆的绿坝娘。坝娘横行马勒戈壁，最后竟是栽在了这几只喵星人头上。

![][7]

  

![][8]

  

![][9]

  

![][10]

  

![][11]

Nude.py表现相当不错，这几只肥猫都没能蒙混过去。


来个2.5次元的，这只吾王的手办，也被判为Nude。


![][12]

最后二次元的情况不容乐观，不知道是不是现在男孩子太可爱的缘故，这几张都没能识别出来


![][13]

  

![][14]

  

![][15]

 

就这两张识别出了：


![][16]

  

![][17]

金闪闪惹不起，也识别出了：


![][18]

在节操掉尽前，再多说一句，二次元的图片，如果用的是XXX的话，识别率蹭得就上去了。对看了本文心动手痒的诸位绅士来说，这是好事吧。


  [nude.py]: https://github.com/hhatto/nude.py
  []: http://media.tumblr.com/78778acedb2305cbd79003008f1b00ae/tumblr_inline_mrf8wjG8HN1qz4rgp.jpg
  [1]: http://media.tumblr.com/524aafe22924acddd00eabe31d350038/tumblr_inline_mrf8v3lwGW1qz4rgp.jpg
  [2]: http://media.tumblr.com/535de630e6eaebb9bfd20f55463a8860/tumblr_inline_mrf8w4AtkC1qz4rgp.jpg
  [3]: http://media.tumblr.com/556ec753ceebb1ae5df81978163c95ff/tumblr_inline_mrf8vkubN21qz4rgp.jpg
  [4]: http://media.tumblr.com/55ff2ee98ba04615da1a246a3aec9881/tumblr_inline_mrf9253mQo1qz4rgp.jpg
  [5]: http://media.tumblr.com/2e0c3ff5d1ab31357639e7af959580b9/tumblr_inline_mrf970fWhB1qz4rgp.jpg
  [6]: http://media.tumblr.com/7a11db311e00a79163ce3b17bff18320/tumblr_inline_mrf97eY3r91qz4rgp.jpg
  [7]: http://media.tumblr.com/1df2c502d11bbc43c5893bd47a1a9f6d/tumblr_inline_mrf9ttMz1N1qz4rgp.jpg
  [8]: http://media.tumblr.com/fb6ed82541d7ba9355022ae035a8b12f/tumblr_inline_mrf9wl6hbB1qz4rgp.jpg
  [9]: http://media.tumblr.com/170ead7a60b2dda420ae7817c5cf9246/tumblr_inline_mrf9wdh3tI1qz4rgp.jpg
  [10]: http://media.tumblr.com/57ed24a240cf72c39a04931205d54fce/tumblr_inline_mrf9x3cqP91qz4rgp.jpg
  [11]: http://media.tumblr.com/45e42407010a2ab9a0264210b23f9f00/tumblr_inline_mrf9xdarCw1qz4rgp.jpg
  [12]: http://media.tumblr.com/e9e1f536565c21f75d4128a122fea8b6/tumblr_inline_mrfbi6KHlJ1qz4rgp.jpg
  [13]: http://media.tumblr.com/ce637c35e1cf3a7b075c0d973c32d1c3/tumblr_inline_mrfbinTBrr1qz4rgp.jpg
  [14]: http://media.tumblr.com/6acbb4306f1a4663108b8299434d017c/tumblr_inline_mrfbizf6xE1qz4rgp.jpg
  [15]: http://media.tumblr.com/3ace6e5a165e0a7b1c3dc8eb7f19c09d/tumblr_inline_mrfbk4KG2H1qz4rgp.jpg
  [16]: http://media.tumblr.com/0e61cf196183f1f9a42d0597c5ca1b6c/tumblr_inline_mrfbljwSnb1qz4rgp.jpg
  [17]: http://media.tumblr.com/06604f51563b2096010643e517107d77/tumblr_inline_mrfbmdjcIz1qz4rgp.jpg
  [18]: http://media.tumblr.com/381c49041a5b51db3077723d30cd9a63/tumblr_inline_mrfbn1dP8g1qz4rgp.jpg

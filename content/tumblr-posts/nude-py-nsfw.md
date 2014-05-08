Title: 无节操的nude.py识别哔～～～～图评测[NSFW]
Date: 2013-08-12 23:15:46
Author: Leonardo Zhou
Category: Python
Slug: post/58062234806/nude-py-nsfw
Save_as: post/58062234806/nude-py-nsfw/index.html
Tags: image-processing 
Summary: 前方高能

发个无节操的东东： [nude.py][]


故名思意，nude.py就是一个Python实现的，判断一张图片是否是nude的library.

安装很简单：

    pip install nudepy

nude.py的图片识别/处理是依赖于`PIL`或`Pillow`的，由于`Pillow`的安装过程比`PIL`简单很多，强烈推荐用`Pillow`。

    # 让Pillow支持jpeg
    # 若未安装libjpeg,用Pillow处理JPEG 图片，会报 IOError: decoder jpeg not available
    # 此时要先pip uninstall Pillow, 安装好 libjpeg,再重新 pip instal  Pillow
    sudo apt-get install libjpeg8-dev pip install Pillow

nude的API很简单：

    :::python
    import nude
    from nude import Nude
    
    print(nude.is_nude('./nude.rb/spec/images/damita.jpg'))
    
    n = Nude('./nude.rb/spec/images/damita.jpg')
    n.parse()
    print("damita :", n.result, n.inspect())

实测结果：


先来几张吾王的:

![nudepy1][]

![nudepy2][]

![nudepy3][]

![nudepy4][]

![nudepy5][]

这几张~~玉照~~御照被nude.py毫无异议得判为nude，就连下面这张不怎么犯规的的，也没能幸免

![nudepy6][]

不过下面这种尺度的，就不会被错杀了。

![nudepy7][]

这让我想起了当年让小朋友们闻风丧胆的绿坝娘。坝娘横行马勒戈壁，最后竟是栽在了这几只喵星人头上。

![nudepy8][]

![nudepy9][]

![nudepy10][]

![nudepy11][]

![nudepy12][]

Nude.py表现相当不错，这几只肥猫都没能蒙混过去。

来个2.5次元的，这只吾王的手办，也被判为Nude。

![nudepy13][]

最后二次元的情况不容乐观，不知道是不是现在男孩子太可爱的缘故，这几张都没能识别出来

![nudepy14][]

![nudepy15][]

![nudepy16][]

就下面这两张识别出了：

![nudepy17][]

![nudepy18][]

金闪闪惹不起，也识别出了：

![nudepy19][]

在节操掉尽前，再多说一句，二次元的图片，如果用的是XXX的话，识别率蹭得就上去了。对看了本文心动手痒的诸位绅士来说，这是好事吧。


  [nude.py]: https://github.com/hhatto/nude.py
  [nudepy1]: http://ww4.sinaimg.cn/large/6c3391c1gw1eefnud176lj20dw0ijn01.jpg
  [nudepy2]: http://ww2.sinaimg.cn/large/6c3391c1gw1eefnvfxncuj206904owel.jpg
  [nudepy3]: http://ww3.sinaimg.cn/large/6c3391c1gw1eefnwh3jgjj207705e0so.jpg
  [nudepy4]: http://ww3.sinaimg.cn/large/6c3391c1gw1eefo1rx5vyj20dm0i7wf4.jpg
  [nudepy5]: http://ww3.sinaimg.cn/large/6c3391c1gw1eefo23dy0cj206b06oa9y.jpg
  [nudepy6]: http://ww3.sinaimg.cn/large/6c3391c1gw1eefo2ie38wj20c10go0w1.jpg
  [nudepy7]: http://ww2.sinaimg.cn/large/6c3391c1gw1eefo2vp9cfj20ao0e8t9c.jpg
  [nudepy8]: http://ww4.sinaimg.cn/large/6c3391c1gw1eefo39ta6kj209f0dcjs2.jpg
  [nudepy9]: http://ww1.sinaimg.cn/large/6c3391c1gw1eefo5l9x5dj20dw0d8t9n.jpg
  [nudepy10]: http://ww4.sinaimg.cn/large/6c3391c1gw1eefo5yg3n3j20dw0afacx.jpg
  [nudepy11]: http://ww1.sinaimg.cn/large/6c3391c1gw1eefo67osgtj20dw0af755.jpg
  [nudepy12]: http://ww2.sinaimg.cn/large/6c3391c1gw1eefo6exmwsj20dw0itgmn.jpg
  [nudepy13]: http://ww3.sinaimg.cn/large/6c3391c1gw1eefo6txssqj20cg0jg402.jpg
  [nudepy14]: http://ww1.sinaimg.cn/large/6c3391c1gw1eefo77220gj20dw07tmxz.jpg
  [nudepy15]: http://ww2.sinaimg.cn/large/6c3391c1gw1eefo7dr55kj20dw07taa4.jpg
  [nudepy16]: http://ww1.sinaimg.cn/large/6c3391c1gw1eefo7o3feej20dw07tdge.jpg
  [nudepy17]: http://ww2.sinaimg.cn/large/6c3391c1gw1eefo7vl7xqj207906yq3u.jpg
  [nudepy18]: http://ww2.sinaimg.cn/large/6c3391c1gw1eefo83gaqaj20dw07tq3h.jpg
  [nudepy19]: http://ww1.sinaimg.cn/large/6c3391c1gw1eefo8le2x0j20dw07tjs0.jpg

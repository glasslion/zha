Title: Python的双层循环可以这么玩
Date: 2013-07-15 00:33:00
Author: glasslion
Category: text
Slug: post/55431622560/python

![][]

把对循环的控制，过滤拆分到一个generator中，在主循环中只存放对循环对象操作的逻辑，不仅是代码更加清晰，也避免了从内层循环退出的麻烦事

via [Loop like a native: while, for, iterators, generators (PyCon US
2013 Talk)][]

  []: http://media.tumblr.com/e658ef57242b435f01208793e0ae23e2/tumblr_inline_mpxpxs64a11qz4rgp.png
  [Loop like a native: while, for, iterators, generators (PyCon US 2013
  Talk)]: http://nedbatchelder.com/text/iter/iter.html

Title: Chrome Logger
Date: 2013-08-07 13:57:00
Author: Leonardo Zhou
Category: Others
Slug: post/57590624308/chrome-logger
Save_as: post/57590624308/chrome-logger/index.html
Tags: tool, chrome

安装好Chrome Logger的[Chrome扩展][]，并在服务器端安装对应语言（目前支持[Ruby][], [PHP][], [Python][], [Node.js][], [.NET][]）的Chrome Logger库后，就可以在服务器端用类似`console.(variable)`的语句log变量，然后在Chrome Dev Tools上查看变量的实际值。


以`Django`为例, 配置十分简单：

    :::python
    # django middleware
    MIDDLEWARE_CLASSES = (
        'chromelogger.DjangoMiddleware'
    )

    # views
    import chromelogger as console
    console.log('Hello console!')
    console.get_header()



gif 演示:

![chrome-logger1][]

![chrome-logger2][]

[Project Homepage][]


  [Chrome扩展]: https://chrome.google.com/webstore/detail/chromephp/noaneddfkdjfnfdakjjmocngnfkfehhd
  [Ruby]: http://github.com/cookrn/chrome_logger
  [PHP]: http://github.com/ccampbell/chromephp
  [Python]: http://github.com/ccampbell/chromelogger-python
  [Node.js]: http://github.com/yannickcr/node-chromelogger
  [.NET]: http://github.com/ChrisMissal/chromelogger
  [chrome-logger1]: http://ww4.sinaimg.cn/large/6c3391c1gw1eef8b0wyixg20hq06vkcf.gif
  [chrome-logger2]: http://ww3.sinaimg.cn/large/6c3391c1gw1eef8bi0n3bg2076055mz3.gif
  [Project Homepage]: http://craig.is/writing/chrome-logger/

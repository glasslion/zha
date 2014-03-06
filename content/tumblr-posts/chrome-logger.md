Title: Chrome Logger
Date: 2013-08-07 13:57:00
Author: glasslion
Category: text
Slug: post/57590624308/chrome-logger

安装好Chrome Logger的[Chrome扩展][]，并在服务器端安装对应语言（目前支持
[Ruby][], [PHP][], [Python][], [Node.js][], [.NET][]）的Chrome
Logger库后，就可以在服务器端用类似`console.(variable)`的语句log变量，然后在Chrome
Dev Tools上查看变量的实际值。

</p>

下面以`Django`为例：

</p>

<div class="monokai">
    # django exampleimport chromelogger as consolefrom django.http import HttpResponsedef index(request):    response = HttpResponse("Hello, world. You're at the poll index.")    console.log('Hello console!')    console.log(request.user)    return response

</div>
</p>

![][]

![][1]

[Project Homepage][]

</p>

  [Chrome扩展]: https://chrome.google.com/webstore/detail/chromephp/noaneddfkdjfnfdakjjmocngnfkfehhd
  [Ruby]: http://github.com/cookrn/chrome_logger
  [PHP]: http://github.com/ccampbell/chromephp
  [Python]: http://github.com/ccampbell/chromelogger-python
  [Node.js]: http://github.com/yannickcr/node-chromelogger
  [.NET]: http://github.com/ChrisMissal/chromelogger
  []: http://cdn.craig.is/img/chromelogger/console.gif
  [1]: http://media.tumblr.com/b0e30d91489d7d45d905287cb536dce8/tumblr_inline_mr56b4r8kx1qz4rgp.gif
  [Project Homepage]: http://craig.is/writing/chrome-logger/

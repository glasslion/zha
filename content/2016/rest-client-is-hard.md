Title: REST Client 拾遗
Author: Leonardo Zhou
Category: Python
Date: 2015-02-27 20:15:00
Slug: post/rest-client-tips
save_as: post/rest-client-tips/index.html
Tags: rest
Summary: Restful Service 早已不是什么新鲜玩意。 国内很多公司都提供基于 REST 的服务， 其中不少还有官方提供的 多语言 SDK。先不论这些 REST API 的设计， 那些SDK/REST Client 往往并不好用， 在 github 上也能找到大量改良的 fork。这里就分享一些我关于写好 REST Client 的愚见。

Restful Service 早已不是什么新鲜玩意。 国内很多公司都提供基于 REST 的服务， 其中不少还有官方提供的 多语言 SDK。先不论这些 REST API 的设计， 那些SDK/REST Client 往往并不好用， 在 github 上也能找到大量改良的 fork。这里就分享一些我关于写好 REST Client 的愚见。

###  REST Client 不是 url 拼接器

相当多的 REST Client 说简单了，就做一件事:
```python
import request
class Client(object):
    def post(self, url, data):
        r = request.post(url, data)
        return r.json()
```

REST Client 返回给用户的应该是解析好的，有意义的对象， 而不是原始的 JSON。这些对象应该提供一些数据操作接口，可以方便地修改对象所对应的数据。 

以新浪微博 API 为例， 官方推荐的 [Python SDK](https://github.com/michaelliao/sinaweibopy) 只是把 `HTTP GET： statuses/user_timeline` 这个请求包装成了 `client.statuses.user_timeline.get()` 这样的函数调用。这样的 Client 写起来很简单， 单个文件就可以搞定， 但对用户却不友好。譬如收藏评论这样简单的操作， 用户也要不断去翻 新浪微博 API 文档， 并手动拼接出正确的 API URL。

相比之下， 另一个微博 [Client](https://github.com/wuyuntao/weibopy)， 只对 API 返回的实体做了简单的抽象，就已经极大提高 Client 的易用性。扫一眼下面的代码， 不看文档， 我也知道怎样用代码刷微博了。
 Anyway， REST API 是给机器用的， REST Client 是给人用的。

e.g.
```
# https://github.com/wuyuntao/weibopy
class Comments(Model):
    def destroy(self):
        return self._api.destroy_status(self.id)

    def retweet(self):
        return self._api.retweet(self.id)

    def retweets(self):
        return self._api.retweets(self.id)

    def favorite(self):
        return self._api.create_favorite(self.id)

class User(Model):

    def timeline(self, **kargs):
        return self._api.user_timeline(user_id=self.id, **kargs)

    def friends(self, **kargs):
        return self._api.friends(user_id=self.id, **kargs)

    def followers(self, **kargs):
        return self._api.followers(user_id=self.id, **kargs)

    def follow(self):
        self._api.create_friendship(user_id=self.id)
        self.following = True

    def unfollow(self):
        self._api.destroy_friendship(user_id=self.id)
        self.following = False

    def lists_memberships(self, *args, **kargs):
        return self._api.lists_memberships(user=self.screen_name, *args, **kargs)

    def lists_subscriptions(self, *args, **kargs):
        return self._api.lists_subscriptions(user=self.screen_name, *args, **kargs)

    def lists(self, *args, **kargs):
        return self._api.lists(user=self.screen_name, *args, **kargs)
```


### 没有充分利用缓存
成熟的 REST 服务往往会利用缓存来提高响应速度。许多多 REST 服务（例如 github， heroku, 阿里云 OSS）使用 `If-Modified-Since`(Last-Modified) 和 `If-None-Match `(ETag) 这两个 HTTP 头来标示缓存信息。一个好的 REST Client 应当在请求时向 Server 端提供这些 HTTP 头。

e.g
```
# https://github.com/sigmavirus24/github3.py
def refresh(self, conditional=False):
    headers = {}
    if conditional:
        if self.last_modified:
            headers['If-Modified-Since'] = self.last_modified
        elif self.etag:
            headers['If-None-Match'] = self.etag

```

### 跨域问题

出于安全考虑， 浏览器会限制脚本中发起的跨站请求。绕过这个限制的方法也不少，比如 iframe, JSONP, CORS... 其中[跨源资源共享](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS)（Cross-Origin Resource Sharing / CORS) 是比较主流的， 也是 W3C 推荐的一种做法。本文篇幅有限， 其细节可以参考前文所给的链接，接下来让我们专心黑 IE。
其他浏览器都是在 `XMLHttpRequest` 对象上实现了 CORS。 唯独微软在 IE8-IE9 里引入了一个新的对象 `XDomainRequest`， 专门处理CORS 请求。 这还是个小坑， 前端可以很容易绕过。最要命的是在 IE10 以前，`XDomainRequest` 只支持 GET 和 POST 方法, 而且无法自定义 HTTP Header。于是 PUT， DELETE 方法是不能用了， 要设置 `Content-type` 为 `application/json` 也不行了。当然解决办法是有的， 比如使用 [XDomain](https://github.com/jpillora/xdomain)。但这些方法都需要对 Server 端做一定的更改，无法完全在 Client 端加以解决。

值得一提的是， Django REST Framework 为此原生提供了一种很简单的 [workaround](http://www.django-rest-framework.org/topics/browser-enhancements/)。 只要设置了 `X-HTTP-Method-Override` 头，DRF 就会将那些本来是 POST 的请求，当作指定的方法处理。

e.g.
```javascript
$.ajax({
    url: '/myresource/',
    method: 'POST',
    headers: {'X-HTTP-Method-Override': 'PATCH'},
    ...
});
```

尽管跨域问题只存在浏览器端， 但所有的 Client 也会面临类似的问题： 一些企业内部网络由于代理，防火墙的限制， 无法使用某些特定的 HTTP 方法。 因此 REST Client 在这方面下点功夫还是很有必要。

 
## Finally
在写 REST Client 时会遇到的那些痛点, 很多时候是无法光靠 Client 自身去解决的, 需要服务器端的配合。换个角度看的话，那么Server 端的实现可只能称之为失败。因此我建议那些负责 REST 服务端程序员也去亲自写一下对应 Client 端的代码。对于后端程序员来说， 这并不需要多少前端知识， 你完全可以使用和 Server 端相同的编程语言，我信心这会 带来不少启发。
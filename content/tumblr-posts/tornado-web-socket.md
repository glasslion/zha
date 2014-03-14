Title: A simple demo for tornado web socket
Date: 2013-08-04 17:29:00
Author: Leonardo Zhou
Category: Python
Slug: post/57321962100/tornado-web-socket
Save_as: post/57321962100/tornado-web-socket/index.html
Tags: tornado

[Python Code]

![images/tornado_websocket_python.png](http://ww2.sinaimg.cn/large/6c3391c1gw1eecw1ldxobj20dw0dw3yx.jpg)


[JS Code]

![images/tornado_websocket_js.png](http://ww2.sinaimg.cn/large/6c3391c1gw1eecw1x8oxlj20dw0dwmyk.jpg)

Subclass `WebSocketHandler` to create a basic WebSocket handler.

Override `on_message` to handle incoming messages, and use
`write_message` to send messages to the client. You can also override
`open` and `on_close` to handle opened and closed connections.



The only communication methods available to you are `write_message()`,
`ping()`, and `close()`. Likewise, your request handler class should
implement `open()` method rather than `get(`) or `post()`.


参考: [tornado.websocket — Bidirectional communication to the browser](http://www.tornadoweb.org/en/stable/websocket.html)

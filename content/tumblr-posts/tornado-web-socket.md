Title: 用tornado实现一个web socket
Date: 2013-08-04 17:29:00
Author: glasslion
Category: text
Slug: post/57321962100/tornado-web-socket

[Python]

![][]

  

[JS]

![][1]

Subclass `WebSocketHandler` to create a basic WebSocket handler.

</p>

Override `on_message` to handle incoming messages, and use
`write_message` to send messages to the client. You can also override
`open` and `on_close` to handle opened and closed connections.

</p>

The only communication methods available to you are `write_message()`,
`ping()`, and `close()`. Likewise, your request handler class should
implement `open()` method rather than `get(`) or `post()`.

</p>

摘自 [tornado.websocket — Bidirectional communication to the browser][]

</p>

  []: http://media.tumblr.com/02f66a55db7441110d55c10a37eb0746/tumblr_inline_mr01ymaV121qz4rgp.png
  [1]: http://media.tumblr.com/5f386529c08b38f0f406bfdbfdc61e7d/tumblr_inline_mr01zbDeZx1qz4rgp.png
  [tornado.websocket — Bidirectional communication to the browser]: http://www.tornadoweb.org/en/stable/websocket.html

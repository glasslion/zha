Title: The ignored decorater
Date: 2013-06-14 14:16:00
Author: Leonardo Zhou
Category: Python
Slug: post/52930265558/ignored-ignored-context
Save_as: post/52930265558/ignored-ignored-context/index.html


![images/ignore_decorator.png][]

**@ignored**

再介绍一个关于Python的冷知识， 可以用 *@ignored* context manager来显式地声明要忽略的无关紧要的异常

虽然 try except后再pass掉的做法更常见，
但其含义比较隐晦。阅读者往往要把代码块读到最后才能知道那些错误是要忽略的。然后再回过来检查这些异常是否该被忽略。

可惜Python3.4+才支持

-----------------------------------
**Upates**:

最新的Python3.4 dev 又把这个 decorator 被改名为 @suppress

  [images/ignore_decorator.png]: http://ww3.sinaimg.cn/large/6c3391c1gw1eee6peof5tj20e80e83z5.jpg
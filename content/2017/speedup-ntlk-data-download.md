Title: 加速 NLTK 数据包 (NLTK Data) 的下载速度的几种方法
Author: Leonardo Zhou
Category: Python
Date: 2017-05-06 17:27:00
Slug: post/speedup-ntlk-data-download
save_as: post/speedup-ntlk-data-download/index.html

NLTK 是一个在 Python 自然语言处理领域里非常流行的的一个包。NLTK 本身的安装比较简单 (如果是缺少编译环境的 Windows 系统， 推荐用 conda 安装 )，教程也比较多， 这里不再赘述。

然而要让 NLTK 真正工作起来，我们还需要去网上下载各种语料库、语法库和训练模型。由于网络原因，这个下载过程可能比较耗时，或经常失败。下面就简要介绍几个小技巧来加速这一过程。

**只下载你需要的数据包**

NLTK 提供了十分丰富的自然语言数据包， 其中大多数体积都比较小，也有少数体积比较大, 会有几个G。 通常你并不需要所有的数据包，只下载那些你需要的， 显然可以快很多。

完整的 NLTK Data 列表可以访问 http://www.nltk.org/nltk_data/ 得到。

通过 Python shell 下载:
```python
import nltk
# nltk.download() 不指定数据包的名字时， 默认下载全部数据
nltk.download('stopwords')
```

或者在命令行里运行 `python -m nltk.downloader <数据包名>`

如果是在桌面环境下执行上述命令的话, NLTK 会弹出一个用 Tkinter 写的 图形化窗口， 可以更加方便地选择要下载的数据包。
![nltk_data_path](http://wing2south.qiniudn.com/images/nltk_data_path.png)

**通过代理下载**

现在 NLTK 的数据是托管在 Github 上的。 由于一些众做周知的原因， Github 在天朝的网络下时常不太稳定。 考虑到很多程序员都会自备*梯子*，我们可以让 NLTK 通过代理来下载软件包。 一个稳定的代理不仅能避免连接被重置而导致的下载失败， 往往也能提高下载速度。

在 Python shell 里指定代理：
```python
nltk.set_proxy('http://proxy', ('USERNAME', 'PASSWORD'))
nltk.download()
```
如果是在命令行里通过 ``python -m` 的方式下载的话， 可以通过设置 `HTTP_PROXY` 环境变量来指定代理。

**通过其他工具下载**

当你确实需要某些体积很大的数据包时, 光靠 NLTK 自己提供的下载功能可能就捉襟见肘了(仅针对国内网络而言)。这种情况下， 我们可以借助于 wget/aria2c 这类支持多线程， 断点续传的下载工具。 相关数据包的下载链接可以在 上文中提到  http://www.nltk.org/nltk_data/ 里找到。

例如 Brown Corpus 这个数据包 就可以通过 `wget https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/brown.zip` 的方式下载下来。 下载下来 zip 包需要解压到 NLTK 指定的 data 目录的某个子目录下。
如果是桌面环境， 下载窗口上就会显示 data 目录的路径。 
![nltk_packages](http://wing2south.qiniudn.com/images/nltk_packages.png)


如果是命令行环境,可通过下面的代码查看:
```python
import nltk
nltk.data.path
```

在我的机器为例，NLTK 的 data 目录是 `~/nltk_data` 。 注意刚才的下载 url 是以 `corpora/brown.zip` 结尾的， 暗示这是一个 corpora (语料)， 因此这个 zip 文件就要解药到  `~/nltk_data/corpora` 目录下。 同理， Grammars from NLTK Book(`https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/grammars/book_grammars.zip`) 就要解压到 `~/nltk_data/grammars` 目录下。


有少数包的下载地址不符合上述规则，如 PanLex Lite Corpus(https://db.panlex.org/panlex_lite-20170401.zip)， 这类数据包一般都是体积较大， 不能托管在 Github 上的， 这类包一般都属于 corpora。
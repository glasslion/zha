Title: Virtual box 共享文件夹下运行 python setup.py sdist 报 Operation not permitted 错误的解决方法
Author: Leonardo Zhou
Category: Python
Date: 2014-03-18 14:05:00
Slug: post/virtuak-box-shared-folder-run-setuppy-stdist
save_as: post/virtuak-box-shared-folder-run-setuppy-stdist/index.html
Tags: vagrant

我 PC 上的开发环境是 Windows + Vagrant ( VirtualBox )。常用的编辑器则是 sublime, pycharm 之类的图形化工具。为了方便在 windows 上编辑 vm 中的文件，代码都是放在 virtual box 的 shared folder 下的。

前不久，在我打包  [django-qiniu-storage][1] 并发布到 pypi 时， 遇到了点麻烦。

当我运行 `python setup.py sdist` 时，出现了如下错误：

    >>> python setup.py sdist
    
    running sdist
    running egg_info
    ...
    hard linking xxx -> xxx
    error: Operation not permitted

还好错误信息还算是比较明了的: 因为脚本是在 Ubuntu 虚拟机下运行， Python 假设操作系统支持 hardlink, 于是 setup.py 会尝试在工作目录下建立 hardlink,  但是virtualbox 目前还不支持在 shared folder下建立 hard link, 从而引发了  Operation not permitted。

用 Google 和 stackoverflow 搜索之后，发现这个 bug 已经分别被人反馈给 [Python][2] 和 [virtualbox][3] 的开发者了，但是在 Python 和 virtualbox 任何一方都不太可能在短时间内被修复。

幸运的是，在 python 的 bug 讨论列表里， 有人给出了一个可行的解决方案:

> A dirty hack is to include this line at the top of your setup.py: del os.link

因为 `disutils` 是通过检查 os.link 是否为 None 来决定是否使用 hardlink, 那么将 os.link monkey patch 为 None 就行了 。这么做除了多占用些微不足道的磁盘空间，不会有任何副作用。

我做了个小改动，通过检查环境变量， 只有当 `setup.py` 在 vagrant 下运行时， 才会 `del os.link`.

    :::Python
    # put the following code at the beginning of your setup.py
    # if you are not using vagrant, just delete os.link directly,
    # The hard link only saves a little disk space, so you should not care
    if os.environ.get('USER','') == 'vagrant':
        del os.link


  [1]: https://github.com/glasslion/django-qiniu-storage
  [2]: http://bugs.python.org/issue8876
  [3]: https://www.virtualbox.org/ticket/818
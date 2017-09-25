Title: devpi —— 架设私有 pypi 的最佳选择
Author: Leonardo Zhou
Category: Python
Date: 2014-05-03 22:31:00
Slug: post/devpi-best-private-pypi-server
save_as: post/devpi-best-private-pypi-server/index.html


## 引言

[PyPI][1] 可以说是 Python 程序员几乎每天都要用到的工具 （当然由于众所周知的原因， 在国内使用[豆瓣][2]，[阿里云][3] 等公司/组织提供的 PyPI 镜像会更加快捷，稳定）。但是在每个公司内部都会有一些的闭源的，私有的 Python Package 。 为了让这些私有的 Python Package 的安装流程能和 PyPI 一致， 架设一个私有的 PyPI 就很有必要了。

## 寻寻觅觅

目前，在各大搜索引擎上，无论是去搜索 “how to build a private pypi” 还是 “怎样搭建私有的pypi”，都能找到大量的解决方法和工具。 其中比较常见的 "类 PyPI Server" 就有： [DjangoPyPI][4]， [chishop][5]， [pypiserver][6]， [Cheese Shop][7]， [localshop][8], [mypypi][9], [proxypypi](https://bitbucket.org/r1chardj0n3s/proxypypi),  [Flask-PyPi-Proxy][10] ... 就算不是你“选择困难症患者”, 面对如此众多的选择， 心里恐怕也要发毛了。

其实在搭建私有 pypi 这个问题上，Python 官方是有一个推荐工具的： [devpi](http://doc.devpi.net/)。我在试用过上述工具后， 也觉得无论是在功能上，还是代码质量上 devpi 都遥遥领先于其他候选工具。可惜的是，由于devpi 是 一个在2013 年才起步的新项目， 目前 Python 中文圈里还没有人对 devpi 做过详细的介绍， 希望本文能起到个抛砖引玉的作用， 让更多 Pythonista 知道这个工具。

## 为什么选择 devpi ?
我以表格的形式对做了常见的 PyPI Server 做了一个对比，总结：

| PyPI Server      | PyPI代理镜像 | 本地缓存 | 单元测试 | 系统测试 | 搜索               | 项目最后更新时间       |
|------------------|--------------|----------|----------|----------|--------------------|------------------------|
| devpi            | 支持         | 支持     | ★★★★     | ★★★★★    | 支持 Web + XML RPC | 2014-05-03(本文截稿时) |
| DjangoPyPI       | 支持         | 不支持   | ★        | 无       | 支持 Web + XML RPC | 2012-04-19             |
| chishop          | 不支持       | 不支持   | 无       | 无       | 不支持             | 2011-04-02             |
| pypiserver       | 支持         | 不支持   | ★★★★★    | 无       | 不支持             | 2014-04-21             |
| Cheese Shop      | 不支持       | 不支持   | ★★       | 无       | 支持Web + XML RPC  | 已终止开发             |
| localshop        | 支持         | 支持     | ★★★★     | 无       | 只支持XML RPC      | 2014-03-12             |
| mypypi           | 不支持       | 不支持   | ★★       | 无       | 不支持             | 2013-05-31             |
| proxypypi        | 支持         | 支持     | 无       | 无       | 不支持             | 2013-12-06             |
| Flask-Pypi-Proxy | 支持         | 支持     | 无       | 无       | 不支持             | 2014-01-08             |


对上表中各列的详细解释：

#### PyPI 代理镜像
一些比较“古老”的 PyPI Server 只实现了 官方PyPI 上已有功能，即允许用户上传, 下载，搜索 Python Packages。 
换而言之， 对于每个 Python Package， 都要先上传到私有的 PyPI，然后才能下载 。可是在实际开发中， 要安装的各种公共的 Python Package 的数量往往要远远多余自己公司内部的 私有 Package 的数量， 一一手动上传显然并不是及。所以， 大部分“现代”的 PyPI Server 无法在本地找到一个 Python Package 时，会自动去 官方PYPI 查找一次， 并从 官方PYPI 下载对应版本的 Python Package。

#### 本地缓存
这项功能是以 “PyPI 代理镜像” 为前提的。对于公开的的 Python Package，从 PyPI上下载回来后。如果能在本地做一个缓存，下次请求就不必再去访问外网了。这不仅提高了下载速度，也保证了 PyPI Down掉后不会影响你网站/软件的部署。此外在某些生产环境下可能要禁止访问外网，再者现在不少程序员带着笔记本去喜欢去星巴克，公园之类的场合码代码, 这些地方的网速往往不是很稳定，这项功能就更加实用了。

#### 单元测试
单元测试的数量和覆盖率显然是衡量软件质量的指标。 devpi 的单元测试非常完善， 其测试用例多达 200 多个。 值得一提的是， Python 社区里两大著名测试工具 `pytest` 和 `tox` 也是出自 devpi 的作者 holger krekel 笔下。 因此， 对于 devpi 的代码质量， 我们大可打五星好评。

#### 系统测试
除了完善的单元测试外， devpi 还有着一个看似疯狂的系统测试。 `devpi/server/extra/compare_pypi_devpi.py` 这个脚本会去抓取 PyPI 上所有 3 万 多个 package 的链接， 并和 devpi 的本地缓存比较， 从而保证了所有 PyPI 上的 Python Package 都是能被 devpi 处理的。 据 devpi 的作者透露， 他用这个测试脚本发现了不少古怪的，需要特殊处理的 package。 可见这个看似变态的系统测试还是很有必要的。 由于其他 PyPI Server 都没有做过这类测试， 其可靠性不由让人怀疑。

搜索这块没有多少可讲的，略过不谈。

#### 项目的开发活跃度
如果项目长期得不到更新，不仅用户渴望的新功能不会被实现， 那些困扰用户的 bug 也不会被修复。1-2年的不到得不到更新对一个开源项目往往是致命的。 devpi 的开发十分活跃，几乎每天都有提交。 考虑到，再过不久， [Warehouse](https://warehouse.python.org/) 就要取代现有的基于 Cheese Shop 的 PYPI了。届时 新的 PyPI 会新增一些功能和API, 我们自然也希望 私有的 PyPI Server 能实现这些功能。 我在 twitter 上同时 fololow 了 pip 和 PYPI 的主要维护者 @dstufft 和 devpi 的作者 @hpk42， 常见到两人讨论如何在 devpi 上实现 warehouse 的新功能。

---------------------------------------

不难看出， 对于每一指标， devpi 在同类竞争者中都是最优秀的。

### devpi 特有的功能

#### Index 继承
这是前面提到的 “PyPI 代理镜像” 功能的加强版。像 pypiserver， proxypypi 等实现只支持两个Index： 私有的和共有的。 在私有 Index 上找不到用户请求的 Python Package时， 就会 fallback 去 Public PyPI。 devpi 对这一功能做了扩展， devpi可以支持多个 Index， 这些Index可以像面向对象编程里的类一样， 存在继承关系。 

举个实际一点的使用例子。在我司还有少量系统是运行在老旧的 FreeBSD 和 Pythohn 2.5 上。，不少 library 是无法直接工作的， 要打 patch。所以我司会维护两个 Index， 一个放公司内部开发的库(Internal Index)， 一个放专门为老系统适配修改的后的 Package(Legacy Patched Index), 继承关系如下：

`Public PyPI --> Internal Index --> Legacy Patched Index` 

这样老系统使用 Legacy Patched Index ，新系统使用 Internal Index， 互不干扰。那些同时兼容新老系统的 Package 就上传到 Internal Index， Legacy Patched Index 因为继承的原因， 也可以使用。

#### 集成 Jenkins
#### 数据导入/导出
用户上传到 devpi 的 package 是可以被统一导出和导入的。 这项功能除了用于数据备份外， 也被用于 devpi 升级时的数据迁移。

#### replication
devpi 原生支持 replication 和 failover， 保证高可用。


  [1]: https://pypi.python.org/pypi
  [2]: http://pypi.douban.com/simple/
  [3]: http://mirrors.aliyun.com/pypi/simple/
  [4]: https://github.com/benliles/djangopypi
  [5]: https://github.com/ask/chishop
  [6]: https://github.com/schmir/pypiserver
  [7]: https://svn.python.org/packages/trunk/pypi/
  [8]: https://github.com/mvantellingen/localshop
  [9]: https://pypi.python.org/pypi/mypypi
  [10]: https://github.com/tzulberti/Flask-PyPi-Proxy
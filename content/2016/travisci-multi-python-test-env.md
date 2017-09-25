Title: 用 Travis CI 定制多样化的 Python 测试环境
Author: Leonardo Zhou
Category: Python
Date: 2014-11-13 20:06:00
Slug: post/travisci-multi-python-test-env
save_as: post/travisci-multi-python-test-env/index.html

[Travis CI](https://travis-ci.org/) 是一项面向 GitHub 用户的持续集成即测试服务。只要是在 GitHub 上开源的项目，经过简单配置， 便可以利用 Travis CI 来进行自动化测试。

做过 Python 开源项目开发的大概都曾被和特定 Python 版本相关的 bug 叮过。  现在比较主流的 Python 运行环境就有: Python 2.6, Python 2.7, Python 3.3 和 Python 3.4 这四种。 此外由于 CPython 有GIL 的限制,  近两年来，pypy 也得到了越来越多的关注。尽管目前 Python 3， pypy 在实际产品中还用得比较少， 但对 Python3 的支持已经成为大家在选择第三方库时需要考量的一个相当重要指标。

如果是做 Django 开发的话， 测试环境多样化的问题就更加严重了。现在大部分 Django 第三方库都会支持 Django 1.4 -1.7 这 4个版本。和上面提到的 4个 Python 版本组合起来，就有 16种之多( 由于 Django 1.5 以上才支持 Python3, 实际有效的组合会略少）。对于某些项目， 甚至要考虑不同数据库 （MySQL, PostgreSQL, SQLite) 的差异， 那么总的测试环境数又要 X3。

尽管通过 [pyenv](https://github.com/yyuu/pyenv) 和 [tox](http://tox.readthedocs.org/en/latest/) 这些工具,  在本地安装和测试多版本的 Python 的流程已经被简化了很多。但光是在十几个环境里把测试一一跑一遍就要花费不少时间。从而导致了我们在平时的开发过程中不会经常去运行这些测试。缺乏测试又会让我们无法尽早发现bug。像 unicode/string 相关 bug， 常常是牵一发而动全身， 后期修复的代价比较高。


Travis CI 使用 GitHub 项目根目录下的 `.travis.yml` 作为其配置文件。从后缀名就可以看出， 其配置文件是 `YAML` 格式的。

一个简单的例子：
```yaml
language: python
python:
- '2.7'
- '2.6'
- '3.3'
- '3.4'
# command to install dependencies
install: "pip install -r requirements.txt"
# command to run tests
script: py.test
```

上面的 `.travis.yml`  会创建 Python 2.6 - Python 3.4  这 4 个 独立的 Python 测试环境。 在每个环境里，通过 `pip install -r requirements.txt` 安装项目所依赖的 Python Package。 

`script` 用于指定用来执行单元测试的命令。这里我们使用的是  `py.test`， 根据个人喜好，你也可以选择 `nosetest`, `make test`, `python setup.py tetst` ... 对于 Python 项目， Travis CI 会自动安装 `nose`, `pytest`, `mock` 这几个常用的测试库。 

对于更加复杂的项目， 我们也可以指定多个 `install`  命令。
例如：
```yaml
install:
- pip install django==$DJANGO_VERSION
- pip install -r requirements.txt
- pip install -e .
env： DJANGO_VERSION=1.7 SECRET_KEY="XXXXXXX" FOO="foo"
```
上面的配置除了安装 requirements.txt 所罗列的 Python Package 外， 还会以 `develop` 模式 安装项目根目录下的 `setup.py`， 并根据 `DJANGO_VERSION` 这个环境变量，安装指定版本的 Django 。

如果， `env` 指定了多组环境变量， Travis CI 会将 各个版本的 Python 和环境变量组 一一组合。 下面的配置就会生成  4X3， 共12个测试环境。
```yaml
python:
- '2.7'
- '2.6'
- '3.3'
- '3.4'
install:
- pip install -r requirements.txt
- pip install django==$DJANGO_VERSION
- pip install -e .
env:
 - DJANGO_VERSION=1.7
 - DJANGO_VERSION=1.6
 - DJANGO_VERSION=1.5
```

**注**： 在 `env` 列表里， 每一行代表一组环境变量。多个环境变量间用空格隔开。

当我们想在每个测试环境中都设置一些环境变量时， 我们就要把 `env` 列表显式地拆分成 `matrix` 和 `global` 两个子列表。 `global` 子列表 里的环境变量不参与测试环境的组合。
 例：
```yaml
env:
  matrix:
  - DJANGO_VERSION=1.7
  - DJANGO_VERSION=1.6
  - DJANGO_VERSION=1.5
  global:
  - SECRET_KEY="XXXXXXX"
```

有时， 难免会遇到一些无效的测试环境组合， 比如 Django 1.7 就不支持 Python 2.6。 这种情况下， 可以用 `matrix.exclude` 来排除某些特殊的组合：

```yaml
matrix:
  exclude:
  - python: '2.6'
    env: DJANGO_VERSION=1.7
```
总的来说，`.travis.yml` 的配置还是简明又不失灵活的， 用的也是标准的 `YAML` 语法。如果对 `YAML` 不熟， 建议上手Travis CI前，可以先找一份简明的 `YAML` 语法说明学习一下， 会起到事半功倍的效果。如果你的 `.travis.yml` 存在语法错误，可以用 [Travis WebLint](http://lint.travis-ci.org/) 来作调试和语法检查。

最后 ， 附上我在 [django-qiniu-storage](https://github.com/glasslion/django-qiniu-storage) 项目中所使用 `.travis.yml` 以资参考。

```yaml
language: python
python:
- '2.7'
- '2.6'
- '3.3'
- '3.4'
install:
- pip install -r requirements.txt
- pip install django==$DJANGO_VERSION
- pip install -e .
script: py.test tests/test_storage.py
env:
  matrix:
  - DJANGO_VERSION=1.7
  - DJANGO_VERSION=1.6
  - DJANGO_VERSION=1.5
  global:
  - USING_TRAVIS=YES
  - QINIU_BUCKET_NAME=django-qiniu-storage
  - QINIU_BUCKET_DOMAIN=django-qiniu-storage.qiniudn.com
  - secure: QVYe9vITrCQw924X7h0vYfHwSDGs6QTaHitM2M31hVkYdBWnYMQZcyW1b5DUcXIOot/Z9+1av77tHgh2nXPA34uR7OIzO+LTtmByEE4fOQwJPDkWvJmF63z6B3eRwH20RPg7sBhzQqEK8KPApTiVjRxw5qsf8yp3+V5aozrKAOg=
matrix:
  exclude:
  - python: '2.6'
    env: DJANGO_VERSION=1.7
```
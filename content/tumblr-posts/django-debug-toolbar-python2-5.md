Title: 让django-debug-toolbar支持Python2.5
Date: 2013-08-22 14:27:00
Author: Leonardo Zhou
Category: Python
Slug: post/58990039224/django-debug-toolbar-python2-5
Save_as: post/58990039224/django-debug-toolbar-python2-5/index.html
Tags: django
Summary: 

`django-debug-toolbar` 从 0.9.x 开始就放弃对 Python 2.5 的支持了。最简单的做法是将那些 仍深陷在 Python 2.5 泥沼里的 Django 项目的 `django-debug-toolbar` 版本指定为 0.8.x。遗憾的是，作为最受欢迎的 Django 第三方 package, `django-debug-toolbar` 本身也有不少很有用的第三方 plugin ，而这些 plugin 为了使用 `django-debug-toolbar` 的 new features 往往就不再支持 0.8.x 版的 `django-debug-toolbar` 了。比如 [django-debug-toolbar-template-timings][] 这个用来 profile Django templates 渲染时间的插件。


这种情况下，只能手动去给 `django-debug-toolbar` 的源码打 patch了。好在截至目前的 0.9.4 版本，让 `django-debug-toolbar` 支持 Python 2.5, 所要做的改动很小。

在8个月前，曾有人提交了的一个支持 Python 2.5 的 [patch][] 到 master 上，但之后由于 Django 1.5 明确放弃 support Python 2.5, 现在的 master 已经再次不支持（而且这次是永久不再支持） Python 2.5了。但对上面的 patch 稍作修改，就能让 pypi 上 `django-debug-toolbar` 最新的正式版本0.9.4， 在 Python 2.5 下工作.

patch( [pygments生成的diff highlight html效果不是很好，可以去看 gist][]):

    :::diff
    diff --git a/debug_toolbar/panels/sql.py b/debug_toolbar/panels/sql.py
    index 18fffdc..a0bfce8 100644
    --- a/debug_toolbar/panels/sql.py
    +++ b/debug_toolbar/panels/sql.py
    @@ -193,8 +193,14 @@ class SQLDebugPanel(DebugPanel):
                     stacktrace = []
                     for frame in query['stacktrace']:
                         params = map(escape, frame[0].rsplit('/', 1) + list(frame[1:]))
    +                    params_dict = dict((unicode(idx), v) for idx, v in enumerate(params))
                         try:
    -                        stacktrace.append(u'<span class="path">{0}/</span><span class="file">{1}</span> in <span class="func">{3}</span>(<span class="lineno">{2}</span>)\n  <span class="code">{4}</span>'.format(*params))
    +                        stacktrace.append(u'<span class="path">%(0)s/</span>'
    +                              u'<span class="file">%(1)s</span>'
    +                              u' in <span class="func">%(3)s</span>'
    +                              u'(<span class="lineno">%(2)s</span>)\n'
    +                              u'  <span class="code">%(4)s</span>'
    +                              % params_dict)
                         except IndexError:
                             # This frame doesn't have the expected format, so skip it and move on to the next one
                             continue

  [django-debug-toolbar-template-timings]: https://github.com/orf/django-debug-toolbar-template-timings
  [patch]: https://github.com/django-debug-toolbar/django-debug-toolbar/commit/3013b5a6e4c682004207e944ebea172a39e52e8c
  [pygments生成的diff highlight html效果不是很好，可以去看 gist]: https://gist.github.com/glasslion/6303816

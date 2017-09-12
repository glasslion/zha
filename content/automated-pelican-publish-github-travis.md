Title: 利用 Travis CI + Github 给静态博客加上草稿和编辑预览功能
Author: Leonardo Zhou
Category: Python
Date: 2016-12-25 14:36:00
Slug: post/advanced-pelican-publish-github-travis
save_as: post/automated-pelican-publish-github-travis/index.html
Tags: pelican

最近几年，静态博客超越 wordpress。 在程序员社区， 利用 Github Pages 来托管静态博客更是风靡一时。 其中不少人也开始使用持续集成工具 Travis CI 来自动构建和发布博客。

本文介绍了一种使用持续集成工具 Travis CI 来实现自动化发布 Pelican 静态博客到 Github Page.s 的方法。在完成本文所述的配置后，你可以抛开 Python、命令行, 只通过 Github 就能编辑， 发布自己的博客。 通过 git branch 和 Pull request还能实现传统动态博客的草稿和预览功能。


想不予， 如今静态博客。
dao到。






**Travis CI 是什么？**
Travis CI 是一款和 Github 紧密结合的持续集成(CI) 工具。 当你的代码被提交到 Github 后， 会触发 Travis CI 的 webhook, Travis CI 就会自动去执行一些操作， 通常是运行单元测试。当然这种操作并不仅限于单元测试， 实际上你可以用它来执行几乎任何命令。 由于很多静态博客的源文件(例如 markdown) 就是托管在 Github 上， 并使用 Github Pages 发布的， 利用 Travis CI 来自动生成静态博客文件并上传到 Github Pages 就成了一件很自然的事情。通过搜索引擎， 我们可以搜到这方面大量的使用案例。本文碍于篇幅， 这里就不介绍从头搭建一个 Travis CI+ Github 博客的步骤了。 下面推荐的几篇教程都还不错不错， 可以参考: [手把手教你使用Travis CI自动部署你的Hexo博客到Github上](http://www.jianshu.com/p/e22c13d85659)、 [用 Travis CI 自動化發佈 Pelican blog 到 GitHub Pages 上](https://blog.m157q.tw/posts/2016/05/08/use-travis-ci-to-publish-pelican-blog-on-github-pages-automatically/)、[Publish your Pelican blog on Github pages via Travis-CI](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html)。不同的静态博客工具的配置过程会略有不同， 你也可以用。

然而我还是觉得有必要要强调下网上这类教程普遍存在的一个问题: **忽视安全!!!**
把博客发布到 Github Page 上的过程说白了就是把 html 文件提交到某个 Github repo 的 gh-page 分支。 要让 Travis CI 能提交文件
- 不加密。
- 把使用



## 在线预览
实在有些*鸡肋*。 如果你的本机已经有了 Pelican 的构建环境的话， 构建静态博客并上传到 Github 应该会非常容易。 只要运行 `make github` 就行了，速度也比去 Travis CI 绕一圈快的多。
， 这种情况下

这种情况下， 你无法。 虽然 Markdown 格式， 语法十分简单。

由于每个 Github repo 只能拥有一个 Github Pages 分支(gh-pages), 我们需要新建一个新的 repo 来存放预览分支。

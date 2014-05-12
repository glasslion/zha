Title: 小硬盘伤不起-将Vagrant移出系统盘的方法
Date: 2013-03-02 22:55:00
Author: Leonardo Zhou
Category: Devops
Slug: post/44371306891/vagrant
Save_as: post/44371306891/vagrant/index.html
Summary:

最近用上vagrant，叹为神器的同时，它将所有文件全存系统盘的做法，也让我很伤脑筋。很多开发者系统盘用了SSD，相信为此头疼的不只是我一个。

![images/vagrant-logo.jpg](http://ww3.sinaimg.cn/large/6c3391c1gw1eecwatrftaj2069069747.jpg)

在万能的Google的加持下，最终还是找打了解决[办法](http://emptysquare.net/blog/moving-virtualbox-and-vagrant-to-an-external-drive/)。

# 更改VirtualBox虚拟机映像文件的位置

* 打开 VirtualBox 程序，点击`管理/全局设定`菜单项(Ctrl+G), 将`常规`栏里的`默认虚拟电脑位置(M)`改为其他磁盘下的路径
* 将原路径 `C:\Users\user_name\.VirtualBox\VirtualBox VMs` 下的文件移动到新路径下。
* 重新启动VirtualBox程序，在虚拟机列表里，以前建立的虚拟机虽然都还在，但已经不可用了，将他们全部删除。
* 双击打开新路径各个文件夹里的vbox文件，将建立的虚拟机重新导入。

VirtualBox虚拟机映像文件是vagrant最多的一块, 上述方法应该能显著减少vagrant对系统盘的空间占用。只是如果添加的vagrant box数量比较多，其占用的空间也是很可观的，可以用下面的方法将其移出系统盘。

# 更改vagrant配置文件的位置

* 将 `C:\Users\user_name\.vagrant.d` 移动到新的位置
* 新建环境变量`VAGRANT_HOME`，并指向新路径

最后吐槽一句无关的，我第一次知道 vagrant 居然是在Pycon上，而不是RubyConf上

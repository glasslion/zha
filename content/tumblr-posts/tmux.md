Title: 用tmux提高工作效率 配置篇
Date: 2013-01-16 16:04:00
Author: glasslion
Category: text
Slug: post/40670260768/tmux

_本文中很多内容都是摘自《tmux Productive Mouse-Free Development》一书。书的篇幅也不长，只有80多页，感兴趣的话，推荐一读。_ [豆瓣](http://book.douban.com/subject/10541112/)

![](http://media.tumblr.com/75a7236ddb0139d52cff7b615771b013/tumblr_inline_mi9w2jiyxA1qz4rgp.png)

###tmux配置文件的地址
* /etc/tmux.conf 存储的是系统中所有用户的全局配置
* ~/.tmux.conf 存储的时用户个人的配置

###更改键位
* `set -g prefix C-a` 将prefix键设为Ctrl+a  
	prefix键在tmux中使用十分频繁，几乎所有的都需要先按prefix键，而tmux默认的prefix键是C-b(Ctrl+b),十分难按，非常坑爹。

	很多tmux用户曾使用过GNU screen, screen的prefix键 C-a显然比C-b更加便捷，也减少了学习成本

	对于prefix键重度使用者，可以用键位映射工具，将CapsLock大小写锁定键映射成Ctrl键，C-a就更加容易按了。

	添加了新的的prefix键位后，将C-b与prefix键解绑，留作他用。 `unbind C-b` 

	`source-file ~/.tmux.conf` 之后，更改的配置才会生效

	`bind C-a send-prefix` 由于prefix按键被tmux拦截，Emacs,VIm等软件可能会不能正常工作，这个设置可以让用户连按两次C-a,来向第三方软件发送prefix按键

* `bind r source-file ~/.tmux.conf` 按r可以让更改后的tmux设置生效

*  `bind | split-window -h` 

	`bind - split-window -v`

	纵向和横向切分面板。切分面板本来是tmux的一大杀器，但默认的命令太过繁琐，而且|和-更直观得表明了切割方向

* `bind h select-pane -L`
	
	`bind j select-pane -D`

	`bind k select-pane -U`

	`bind l select-pane -R`

	在不同面板间切换。也是比较常用的，用LDUR表示方向在按键时很不方便，改为vim风格的。

* `bind -r H resize-pane -L 5`
	
	`bind -r J resize-pane -D 5`

	`bind -r K resize-pane -U 5`

	`bind -r L resize-pane -R 5`

	改变面板的大小。四个方向还是使用vim风格的方向键，不过这里用的是大写。

	这里-r的作用是，如果要窗口向上扩展一大段空间，按了prefix键后，连着按H就行了。 

*  `bind -r C-h select-window -t :-`
	`bind -r C-l select-window -t :+`
	切换窗口。这里的按键和切换面板的对应。

### 基本设置

* `set -sg escape-time 1` tmux，会有一个延时，以方便用户输入按键组合，但默认的有点长，1秒钟足矣

* `set -g base-index 1` 有些用户习惯让窗口的编号从1开始（默认是0）

* `setw -g pane-base-index 1` 类似的可以设置面板的开始编号

### 鼠标设置

*  `setw -g mode-mouse on`
	
*  `set -g mouse-select-pane on`
	
* `set -g mouse-resize-pane on`
	
* `set -g mouse-select-window on`

	即使在命令行下，鼠标有时也是能提高工作效率的

###色彩设置
* set -g default-terminal "screen-256color" 让tmux支持256色
* 设置底部状态条的颜色
	`set -g status-fg white`
	
	`set -g status-bg black`
	
	`setw -g window-status-fg cyan`
	
	 `setw -g window-status-bg default`
	
	`setw -g window-status-attr dim`
	
	`setw -g window-status-current-fg white`
	
	`setw -g window-status-current-bg red`
	
	`setw -g window-status-current-attr bright`

*  设置面板间分割线的颜色
	`set -g pane-border-fg green`
	
	`set -g pane-border-bg black`
	
	`set -g pane-active-border-fg red`
	
	`set -g pane-active-border-bg black`

* 设置命令出错后提醒的颜色
	`set -g message-fg white`
	`set -g message-bg black`
	`set -g message-attr bright`

###状态条设置
* `set -g status-left-length 40`

 	`set -g status-left "#[fg=green]Session: #S #[fg=yellow]#I #[fg=cyan]#P"`

	状态栏左侧的长度和文字颜色

* `set -g status-right "#[fg=cyan]%d %b %R"` 右侧

* `set -g status-utf8 on`

* `set -g status-interval 60` 每60秒更新一次显示的时间。默认是15秒

* `setw -g monitor-activity on`

	`set -g visual-activity on`
	
	非当前窗口中有事件发生时（比如一个耗时的命令跑完了），状态栏上会有高亮提醒

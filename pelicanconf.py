#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import os
import sys

BASE_DIR = os.path.dirname(__file__)

# Clone the official plugin repo to the `official_plugins` dir
# (https://github.com/getpelican/pelican-plugins)
sys.path.append(os.path.join(BASE_DIR, "official_plugins"))

import summary, assets

AUTHOR = u'Leonardo Zhou'
SITENAME = u'翼图南'
SITESUBTITLE = u'Wings towards the south'
SITETAGLINE = u'有鸟焉 其名为鹏 背若泰山 翼若垂天之云 ... 然后图南 且适南冥也'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/glasslion'),
    ('envelope', 'mailto:glasslion@gmail.com'),
    ('github', 'https://github.com/glasslion'),
    ('stack-overflow', 'http://stackoverflow.com/users/1093020/leonardo-z'),
    ('google-plus', 'https://google.com/+LeonardoZhou'),
)


LOCALE = ('usa', 'en_US.utf8')

DEFAULT_DATE_FORMAT = '%b %d, %Y'

DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
PAGINATED_DIRECT_TEMPLATES = (('blog',))

PLUGINS = [summary, assets]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Static content
STATIC_PATHS = ['images', 'extra/CNAME',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Url
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Custom theme
THEME = '../pelican-zha'
MENUITEMS = (
    ('blog', '/blog.html'),
)
CURRENT_DATETIME = datetime.now()

QINIU_BUCKET_URL = 'http://wing2south.qiniudn.com'

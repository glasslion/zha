#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Leonardo Zhou'
SITENAME = u'\u7ffc\u56fe\u5357'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Python.org', 'http://python.org/'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/glasslion'),
    ('github', 'https://github.com/glasslion'),
    ('google-plus', 'https://google.com/+LeonardoZhou'),
    ('envelope', 'mailto:glasslion@gmail.com'),
    ('stack-overflow', 'http://stackoverflow.com/users/1093020/leonardo-z'),
)

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
THEME = 'themes/BT3-Flat-4zha'

# BT3-Flat-4zha settings
TEMPLATE_PAGES = {'blog.html': 'blog.html'}
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'blog-index', 'blog')
PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
POST_LIMIT = 10
STOCK_PHOTO = 'http://ww2.sinaimg.cn/large/6c3391c1gw1eef9wv6doyj212w0jetc6.jpg'
BLOG_LOGO = 'http://static.tumblr.com/5483bdcce6a32349f096604033a96608/k03pzap/ziWmplna8/tumblr_static_char-leo.png'

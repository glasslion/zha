#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import os
import sys
import time

BASE_DIR = os.path.dirname(__file__)

# Clone the official plugin repo to the `official_plugins` dir
# (https://github.com/getpelican/pelican-plugins)
sys.path.append(os.path.join(BASE_DIR, "official_plugins"))

AUTHOR = u'Leonardo Zhou'
SITENAME = u'翼图南'
SITE_DESCRIPTION = u'故九萬里，則風斯在下矣，而後乃今培風；背負青天而莫之夭閼者，而後乃今將圖南'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


GOOGLE_ANALYTICS = "UA-42951023-1"

LOCALE = ('usa', 'en_US.utf8')

DEFAULT_DATE_FORMAT = '%b %d, %Y'

# DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')
# PAGINATED_DIRECT_TEMPLATES = (('blog',))

PLUGINS = ['summary', 'neighbors']


# Assets
ASSET_BUNDLES = ()
ASSET_CONFIG = (('sass_bin', 'sass'), )

SUMMARY_MAX_LENGTH = 20

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Static content
STATIC_PATHS = [
    'images',
    'files',
    'extra/CNAME',
    'extra/robots.txt',
    'extra/cv.htm',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/cv.htm': {'path': 'cv.htm'},
}


READERS = {'htm': None}

# Url
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'


# Archive
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'


# Custom theme
THEME = '../pelican-zha'

CURRENT_DATETIME = datetime.now()
TIMESTAMP = time.mktime(CURRENT_DATETIME.timetuple())

CDN_URL = SITEURL

AUTORELOAD_IGNORE_CACHE = True

# Hacks to make teh asset plugin work with Pelican 3.5
# https://github.com/getpelican/pelican/issues/1523
# https://github.com/iKevinY/iKevinY.github.io/commit/872a2b3
ASSET_SOURCE_PATHS = ['static']

LINKS = (
    ('CV', '/cv.htm'),
)

SOCIAL = (
    ('Twitter', 'https://twitter.com/glasslion'),
    ('GitHub', 'https://github.com/glasslion'),
    ('StackOverflow', 'http://stackoverflow.com/users/1093020/leonardo-z'),
    (u'微信二维码', '/images/wechat.jpg'),

)


# Pelican plugin for Jupyter/IPython Notebooksls

MARKUP = ('md', 'ipynb')
PLUGINS.append('pelican-ipynb.markup')

MD_EXTENSIONS = ['codehilite(css_class=highlight snippet)','extra']
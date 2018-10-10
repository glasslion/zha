#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

if os.environ.get('TRAVIS_BRANCH') != 'draft':
    SITEURL = 'https://wing2south.com'
else:
    SITEURL = 'https://glasslion.github.io/zha-beta'

CDN_URL = SITEURL

RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_MAX_ITEMS = 100

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "wing2south"
#GOOGLE_ANALYTICS = ""

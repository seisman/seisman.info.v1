#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://seisman.info'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

BAIDU_SITE_VERIFICATION = 'bH1LL8vy2G'
BAIDU_ANALYTICS = '65542808c7a590c2137aef85e1116ace'
DISQUS_SITENAME = 'seisman'
COMMENTS_INTRO = 'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

SHARE_POST_INTRO = 'Share on:'

GOOGLE_ANALYTICS = ''
STAT_COUNTER_PROJECT = ''
STAT_COUNTER_SECURITY = ''

SOCIAL_PROFILE_LABEL = 'Contact Me'
SOCIAL = (
    ('Email', 'mailto:seisman.info@gmail.com'),
    ('GitHub', 'http://github.com/seisman'),
    ('RSS', FEED_DOMAIN + '/' + FEED_ATOM),
    ('CNY', SITEURL + '/donations.html'),
)

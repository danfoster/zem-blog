#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pilkit.processors import *

AUTHOR = u'Dan Foster'
SITENAME = u'Zem'
SITEURL = 'http://www.zem.org.uk'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  ()

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = ''

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/zem"
GITHUB_URL = "https://github.com/danfoster"
TWITTER_USERNAME = "DanF42"
GOOGLE_ANALYTICS = "UA-44620677-1"

PLUGIN_PATH = '..'
PLUGINS = ['pelican-picasa'] 

PICASA_USER = 'dan@zem.org.uk'

JINJA_EXTENSIONS= ['jinja2.ext.loopcontrols']

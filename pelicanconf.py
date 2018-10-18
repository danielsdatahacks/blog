#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel'
SITENAME = "Daniel's Data Hacks"
SITEURL = ''

SITESUBTITLE = 'Articles about my data science projects'

SITEIMAGE = '/images/test.svg width=130 height=140'

HIDE_AUTHORS = True

PYGMENTS_STYLE = 'lovelace'

DIRECT_TEMPLATES = ['index']
#SITEMAP_SAVE_AS = 'sitemap.xml'

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_PAGES_ON_MENU = True

PATH = 'content/'

TIMEZONE = 'Europe/Berlin'

#IPYNB_FIX_CSS = True

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = [(('LinkedIn','https://www.linkedin.com/in/daniel-borcherding-653656161'))]
LINKS = [(('LinkedIn','https://www.google.de'))]

# Social widget
#SOCIAL = (('LinkedIn', '#'))

DEFAULT_PAGINATION = 10

LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']

#pelican-bootstrapify is used for alchemy theme
PLUGINS = ['ipynb.markup','pelican-bootstrapify','render_math']

#'pelican-bootstrapify'
#This as well
BOOTSTRAPIFY = {
        'table': ['table', 'table-striped', 'table-hover'],
        'img': ['img-fluid'],
        'blockquote': ['blockquote'],
    }

THEME = '/Users/danielborcherding/Documents/Studium/DataScience/jupyter-blog/themes/alchemy_custom'

IGNORE_FILES = ['.ipynb_checkpoints']

#CSS_FILE = 'bootstrap.css'

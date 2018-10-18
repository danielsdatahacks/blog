#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel'
SITENAME = "Daniel's Blog"
SITEURL = ''

PATH = 'content/'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']

#pelican-bootstrapify is used for alchemy theme
PLUGINS = ['ipynb.markup','pelican-bootstrapify']

#'pelican-bootstrapify'
#This as well
BOOTSTRAPIFY = {
        'table': ['table', 'table-striped', 'table-hover'],
        'img': ['img-fluid'],
        'blockquote': ['blockquote'],
    }


THEME = '/Users/danielborcherding/Documents/Studium/DataScience/jupyter-blog/themes/alchemy'

#CSS_FILE = 'main.css'

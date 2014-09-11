#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
AUTHOR = 'SeisMan'
SITENAME = 'SeisMan'
SITEURL = ''
TIMEZONE = 'Asia/Shanghai'
TYPOGRIFY = True

# Date
LOCALE = ['zh_CN', 'en_US']
DEFAULT_DATE = 'fs' # 若metadata中未指定日期，则使用File System Timestamp
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DATE_FORMAT = {
    'zh': ('zh_CN', '%Y-%m-%d'),
}

# Category
USE_FOLDER_AS_CATEGORY = False # 不以目录名为默认分类名
DEFAULT_CATEGORY = '其他'
DISPLAY_CATEGORIES_ON_MENU = False

# Pages
DISPLAY_PAGES_ON_MENU = True # 在菜单栏显示pages
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = []

# Articles
ARTICLE_PATHS = ['']
ARTICLE_EXCLUDES = ['images', 'draft', 'pdfs', 'theme']

# Metadata
SLUGIFY_SOURCE = 'basename' # use basename as slug
DEFAULT_METADATA = ()
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
PATH_METADATA = ''
EXTRA_PATH_METADATA = {}
SUMMARY_MAX_LENGTH = 50

# Output
DELETE_OUTPUT_DIRECTORY = False # Do not delete output directory
OUTPUT_RETENTION = ()
OUTPUT_PATH = 'output/'
OUTPUT_SOURCE = False
OUTPUT_SOURCES_EXTENSION = '.text'
WRITE_SELECTED = []

# Cache
CACHE_CONTENT = True
CONTENT_CACHING_LAYER = 'reader'
CACHE_PATH = 'cache'
GZIP_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'
LOAD_CONTENT_CACHE = True
AUTORELOAD_IGNORE_CACHE = True

# Jinja2
JINJA_EXTENSIONS = []
JINJA_FILTERS = {}

# Markdown
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']

# Pygments
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Others
LOG_FILTER = []
READERS = {}
IGNORE_FILES = ['.#*']
WITH_FUTURE_DATES = False
RELATIVE_URLS = False
INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]''}]'

# Paths
STATIC_PATHS = [
    'images',
    'theme/images',
    'CNAME',
    'pdfs',
]
PATH = 'content'

# Plugins
PLUGIN_PATHS = ['plugins', ]
PLUGINS = []

# Templates
TEMPLATE_PAGES = None
DIRECT_TEMPLATES = ('index', 'tags', 'categories','archives', 'search', '404')
PAGINATED_DIRECT_TEMPLATES = ('index',)
EXTRA_TEMPLATES_PATHS = []

# URL settings
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
YEAR_ARCHIVE_SAVE_AS = False
MONTH_ARCHIVE_SAVE_AS = False
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = ''
TAG_URL = '{slug}.html'
TAG_SAVE_AS = 'tags.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'authors.html'
ARCHIVES_SAVE_AS = 'archives.html'
LUG_SUBSTITUTIONS = ()

# Feed settings
# Feed generation is usually not desired when developing
FEED_DOMAIN = None
FEED_RSS = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TAG_FEED_RSS = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
FEED_MAX_ITEMS = ''

# Pagination
DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = [
    (0, '{name}{number}.html', '{name}{number}.html'),
]

# Tag Cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# Translations
DEFAULT_LANG = 'zh'
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Order
NEWEST_FIRST_ARCHIVES = True
REVERSE_CATEGORY_ORDER = False

# Theme
THEME = "themes/Elegant"
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

# Theme options

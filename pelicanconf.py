#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
AUTHOR = 'SeisMan'
SITENAME = 'SeisMan'
SITEURL = 'http://localhost:8000'
TIMEZONE = 'Asia/Shanghai'
TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = []

# Date
LOCALE = ['zh_CN', 'en_US']
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DATE_FORMATE = {
    'zh': ('zh_CN', '%Y-%m-%d'),
}

# Category
USE_FOLDER_AS_CATEGORY = False   # 不以目录名为默认分类名
DEFAULT_CATEGORY = '其他'
DISPLAY_CATEGORIES_ON_MENU = False

# Pages
DISPLAY_PAGES_ON_MENU = True  # 在菜单栏显示pages
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = []

# Articles
ARTICLE_PATHS = ['']
ARTICLE_EXCLUDES = ['images', 'draft', 'pdfs', 'theme', 'trash']

# Metadata
SLUGIFY_SOURCE = 'basename'  # use basename as slug
DEFAULT_METADATA = ()
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
PATH_METADATA = ''
EXTRA_PATH_METADATA = {}
SUMMARY_MAX_LENGTH = 50

# Output
DELETE_OUTPUT_DIRECTORY = False  # Do not delete output directory
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

# Jinja2
JINJA_EXTENSIONS = []
JINJA_FILTERS = {}

# Markdown
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']

# Pygments
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Math
DOCUTILS_SETTINGS = {'math_output': 'mathjax'}

# Others
LOG_FILTER = []
READERS = {}
IGNORE_FILES = ['.#*']
WITH_FUTURE_DATES = True
RELATIVE_URLS = False
INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'

# Paths
STATIC_PATHS = [
    'images',
    'theme/images',
    'CNAME',
]
PATH = 'content'

# Templates
TEMPLATE_PAGES = {}
DIRECT_TEMPLATES = ('index', 'tags', 'categories',
                    'archives', 'search', '404')
PAGINATED_DIRECT_TEMPLdATES = ('index',)
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
TAG_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
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

# Plugins
PLUGIN_PATHS = ['plugins', ]
PLUGINS = [
     'assets',               # 压缩CSS、JS
     'extract_toc',          # 将toc从content提取出来，单独处理
     'neighbors',            # 上一篇，下一篇
     'related_posts',        # 相关博文
     'sitemap',
     'tipue_search',         # 搜索工具
]

# asset
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
    ('cache', False),
    ('manifest', False),
    ('url_expire', False),
    ('versions', False),
]

# sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# # Theme
THEME = "themes/Elegant"
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

# Theme options
SITE_DESCRIPTION = '关注和分享地震学相关知识、软件、代码。'
SITE_LICENSE = '2013-2015 Copyright &copy; by <a href="http://seisman.info">SeisMan</a>; Licensed under <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a>'
SITESUBTITLE = '学会整理自己的经验是科研的第一步。'
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'
RECENT_ARTICLES_COUNT = 15
USE_SHORTCUT_ICONS = True
RELATED_POSTS_LABEL = 'Related Posts:'

GOOGLE_PLUS_PROFILE_URL = ''
TWITTER_USERNAME = ''
LANDING_PAGE_ABOUT = {}
PROJECTS = []

QINIU = "http://seisman.qiniudn.com"
GITHUB = "http://github.com/seisman/seisman.info"

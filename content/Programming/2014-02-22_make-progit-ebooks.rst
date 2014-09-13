制作Pro Git电子书
#################

:date: 2014-02-22 10:39
:author: SeisMan
:category: 编程
:tags: 书籍, Ruby, Pandoc, PDF
:slug: make-progit-ebooks

.. contents::

Pro Git
=======

Pro Git是一本关于Git的开源书籍，其源文件为MarkDown格式，目前已被翻译为近20种语言。

- 项目主页: https://github.com/progit/progit
- 中文网页版: http://git-scm.com/book/zh

官方网站仅提供英文版的PDF、EPUB和Mobi格式的电子书，因而想要看中文版的电子书就需要自己编译了。

根据项目主页README的解释，要编译生成三种格式的电子书，需要先安装Ruby、calibre、pandoc、LaTeX。

安装Ruby
========

使用RVM来管理Ruby的多版本环境。前面介绍的plenv和pyenv好像都是在模仿Ruby的rvm的功能。因而plenv、pyenv、rvm的用法基本是一致的。

rvm以及ruby的安装参考了\ `RVM实用指南 <http://ruby-china.org/wiki/rvm-guide>`_ \，实际安装过程中有修改。

下载并安装rvm::

    curl -L https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer | bash -s stable

这里不采用原文的\ ``curl -L get.rvm.io | bash -s stable``\ ，是因为该网址一直无法连接。

rvm安装后会自动在\ ``.bashrc``\ , \ ``.bash_profile``\ , \ ``.zshrc``\ , \ ``.zlogin``\ 等文件中加入环境变量信息，需要手动删除或修改以符合自己的需求。

列出可安装的ruby版本::

    rvm list known

安装最新版本ruby::

    rvm install 2.1.0

安装的时候下载速度比较慢，查看了一下，发现rvm首先检测出我的系统是CentOS6，然后从\ ``https://rvm.io/binaries/centos/6/x86_64/ruby-2.1.0.tar.bz2``\ 下载软件包到\ ``~/.rvm/archives/bin-ruby-2.1.0.tar.bz2``\ 。手动实现这一步骤，重新用rvm安装，rvm检测到安装包的完整性便直接使用，加速不少。

设置当前版本为默认版本::

    rvm use 2.1.0 --default

由于国内网络原因，ruby的官方源会出现间歇性连接失败，因而需要修改rvm的ruby安装源到国内的\ `淘宝镜像服务器 <http://ruby.taobao.org/>`_\ ，以提高安装速度::

    $ gem sources --remove https://rubygems.org/
    $ gem sources -a http://ruby.taobao.org/
    $ gem sources -l
    *** CURRENT SOURCES ***

    http://ruby.taobao.org
    # 请确保只有 ruby.taobao.org
    $ sed -i 's!cache.ruby-lang.org/pub/ruby!ruby.taobao.org/mirrors/ruby!' $rvm_path/config/db

安装ruby相关包
==============

gem是ruby的包管理器，类似于perl下的cpan和python下的pip。

官方使用yum来安装相关包::

    yum install ruby rubygems ruby-devel rubygem-ruby-debug rubygem-rdiscount

通过rvm已经安装了\ ``ruby rubygems ruby-devel rubygem-ruby-debug``\ 这四个，\ ``rubygem-rdiscount``\ 需要通过gem来安装::

    gem install rdiscount

安装calibre
===========

`calibre <http://calibre-ebook.com/>`_\ 是一个开源的电子书软件套装，可以用来组织、存放、以及管理电子书，支持大多数的电子书格式。同时也支持与许多流行的电子书阅读器进行同步。

官方强烈不推荐使用系统自带的软件包管理器来安装calibre，其给出的安装方法如下::

    sudo python -c "import sys; py3 = sys.version_info[0] > 2; u = __import__('urllib.request' if py3 else 'urllib', fromlist=1); exec(u.urlopen('http://status.calibre-ebook.com/linux_installer').read()); main()"

下载相当慢，所以还是手动下载。从 http://download.calibre-ebook.com/ 下载合适的版本，然后将其保持到\ ``/tmp/calibre-installer-cache``\ ，再次执行上面的命令就安装完成啦。

calibre不仅是一个电子书管理器，也是一个电子书阅读器，更是一个电子书格式转换器。这里仅用到格式转换的功能，其他功能尚待挖掘。其支持的格式可以在\ `这里 <http://manual.calibre-ebook.com/faq.html#what-formats-does-app-support-conversion-to-from>`__\看到。

安装Pandoc
==========

CentOS 6的官方源中貌似是没有Pandoc的，不过EPEL源中有Pandoc::

    yum install pandoc

`Pandoc <http://johnmacfarlane.net/pandoc/>`_\ 是一个用于从一种标记格式转换为另一种的Haskell库，号称标记格式界的瑞士军刀。其支持markdown, rST, textile, HTML, DocBook, LaTeX, MediaWiki markup, OPML, Haddock markup之间的互相转换。


安装LaTeX
==========

安装过程参考《\ `Linux下安装TeXLive 2013 <{filename}/Programming/2013-07-11_install-texlive-under-linux.rst>`_\ 》并配置中文字体。

获取Pro Git源码
===============

::

    git clone git://github.com/progit/progit.git

制作电子书
==========

Pro Git的源码中提供了脚本\ ``makeebooks``\ 以制作电子书，其首先将markdown格式做简单处理生成了html文件，然后利用calibre的ebook-convert命令实现html到指定格式的转换。

制作mobi格式中文文档::

    FORMAT=mobi ruby makeebooks zh

制作epub格式中文文档::

    FORMAT=epub ruby makeebooks zh

制作PDF
=======

ebook-convert支持输出为PDF格式，但是其生成的PDF效果很差，完全不及mobi和epub格式。

Pro Git 提供了脚本\ ``makepdfs``\ ，本质上是使用了pandoc的格式转换功能，pandoc提供LaTeX模板，并利用LaTeX来更好地实现markdown到PDF的转换。

在latex目录下，template.tex提供了生成LaTeX所需要的模板，主要是LaTeX的导言区；config.yml为配置文件，需要修改中文字体。

查看当前系统下的中文字体::

    $ fc-list :lang=zh
    YouYuan,幼圆:style=Regular
    AR PL UMing TW:style=Light
    AR PL UMing HK:style=Light
    NSimSun,新宋体:style=Regular
    FangSong,仿宋:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
    AR PL UMing CN:style=Light
    KaiTi,楷体:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
    Adobe Kaiti Std,Adobe 楷体 Std,Adobe Kaiti Std R,Adobe 楷体 Std R:style=R,Regular
    SimSun,宋体:style=Regular
    AR PL UKai TW MBE:style=Book
    AR PL UKai CN:style=Book
    AR PL UKai HK:style=Book
    AR PL UKai TW:style=Book
    WenQuanYi Zen Hei,文泉驛正黑,文泉驿正黑:style=Regular
    SimHei,黑体:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
    Adobe Heiti Std,Adobe 黑体 Std,Adobe Heiti Std R,Adobe 黑体 Std R:style=R,Regular
    Adobe Song Std,Adobe 宋体 Std,Adobe Song Std L,Adobe 宋体 Std L:style=L,Regular
    WenQuanYi Zen Hei Mono,文泉驛等寬正黑,文泉驿等宽正黑:style=Regular
    LiSu,隶书:style=Regular
    AR PL UMing TW MBE:style=Light
    Adobe Fangsong Std,Adobe 仿宋 Std,Adobe Fangsong Std R,Adobe 仿宋 Std R:style=R,Regular
    WenQuanYi Zen Hei Sharp,文泉驛點陣正黑,文泉驿点阵正黑:style=Regular

修改如下::

    font: WenQuanYi Zen Hei
    bold: WenQuanYi Zen Hei Mono
    mono: WenQuanYi Zen Hei Mono

制作::

    ./makepdfs zh

参考
====

#. Pro Git README: https://github.com/progit/progit/blob/master/README.md
#. RVM实用指南 : http://ruby-china.org/wiki/rvm-guide
#. 淘宝镜像服务器: http://ruby.taobao.org/
#. Calibre Wiki: http://zh.wikipedia.org/zh-cn/Calibre
#. Pandoc: http://johnmacfarlane.net/pandoc/

GMT 4在Mac下的安装
##################

:date: 2015-09-05
:author: SeisMan
:category: GMT
:tags: 安装, 编译, GMT4
:slug: install-gmt4-under-mac

.. contents::

GMT官方没有为Mac提供GMT4的安装包，因而只能通过其他方式安装。Mac下有很多第三方软件管理工具，比如MacPorts和Homebrew。MacPorts和Homebrew中自带最新版本的GMT，可以直接安装，是比较推荐的使用方式。某些情况下可能会希望自己手动编译，比如自己修改了GMT源码。

因而，本文会介绍四种安装GMT4的方法，列举如下

#. 用Homebrew安装GMT4
#. 用MacPorts安装GMT4
#. 基于Homebrew安装GMT4
#. 基于MacPorts安装GMT4

安装命令行开发工具
==================

在开始之前，先要安装Mac下的命令行开发工具。因为全新的Mac默认是没有自带的::

    $ xcode-select --install

使用Homebrew安装
================

#. 到\ `Homebrew <http://brew.sh/>`_\ 首页，复制首页上的安装代码到终端，执行即可安装Homebrew。

#. 使用Homebrew安装GMT4::

     $ brew install homebrew/science/gmt4

使用MacPorts安装
================

#. 到\ `MacPorts <https://www.macports.org/install.php>`_\ 网站，下载当前系统对应的pkg文件并安装
#. 使用MacPorts安装GMT4::

    $ sudo port install gmt4

手动编译GMT
===========

手动编译GMT需要如下几步：

#. 下载
#. 解决依赖关系
#. 编译GMT源码
#. 安装海岸线数据
#. 修改环境变量

具体操作参考\ `Linux下安装GMT4 <{filename}/GMT/2013-11-07_install-gmt4-under-linux.rst>`_\ 一文，Linux与Mac唯一的不同仅仅是“解决依赖关系”这一步。

解决依赖关系
------------

GMT4依赖于netCDF，必须安装；不依赖于gdal，但gdal在转换数据格式时经常用到，推荐安装。

可以用Homebrew安装依赖包::

   $ brew install gdal
   $ brew install homebrew/science/netcdf

也可以用MacPorts安装依赖包::

   $ sudo port install netcdf +gdal +curl +geos +hdf5

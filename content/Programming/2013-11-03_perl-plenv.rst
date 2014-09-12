Perl多版本共存之plenv
#####################

:date: 2013-11-03 01:24
:author: SeisMan
:category: 编程
:tags: 安装, 版本, Perl
:slug: perl-plenv
:summary: 使用plenv管理多个Perl版本。

.. contents::

前面写了两篇相关的文章。

`《Perl多版本共存之Perlbrew》`_\ 中介绍了如何用Perlbrew实现多个Perl版本的共存。

`《Python多版本共存之pyenv》`_\ 中介绍了如何使用pyenv实现多个Python版本的共存。

plenv和PerlBrew是相同功能的工具，不过，感觉plenv比perlbrew要更方便好用。

官方网站：https://github.com/tokuhirom/plenv

安装plenv
=========

.. code-block:: bash

 $ git clone git://github.com/tokuhirom/plenv.git ~/.plenv
 $ echo 'export PATH="$HOME/.plenv/bin:$PATH"' >> ~/.bashrc
 $ echo 'eval "$(plenv init -)"' >> ~/.bashrc
 $ exec $SHELL -l

安装plenv的build插件
====================

.. code-block:: bash

 $ git clone git://github.com/tokuhirom/Perl-Build.git ~/.plenv/plugins/perl-build/

查看所有可以安装的版本
======================

.. code-block:: bash

 $ plenv install --list

Perl的版本格式为\ ``5.xx.x``\ ，其中\ ``xx``\ 为偶数的版本为稳定版。

安装指定版本
============

.. code-block:: bash

 $ plenv install 5.18.1

更新数据库
==========

.. code-block:: bash

 $ plenv rehash

修改全局Perl版本
================

.. code-block:: bash

 $ plenv versions
 $ plenv global 5.18.1

安装cpanm
==========
Perl的cpan工具可以方便的安装和管理众多模块。cpanm与cpan类似，其功能更强大，其可以根据当前的Perl版本，将模块安装到对应的路径中，而不会对系统自带的Perl模块以及其他Perl版本的模块进行任何修改。

.. code-block:: bash

 $ plenv install-cpanm

.. _《Perl多版本共存之Perlbrew》: http://seisman.info/perlbrew-for-multiple-versions-of-perl.html
.. _《Python多版本共存之pyenv》: http://seisman.info/python-pyenv.html

SAC源代码安装
#############

:date: 2013-07-08 22:06
:modified:       
:author: SeisMan
:category: SAC
:tags: 编译
:slug: install-sac-from-source-code

说明
====

本文不再维护，关于如何安装二进制版的SAC，在《\ `SAC参考手册中文版 <{filename}/SAC/2013-07-06_sac-manual.rst>`_\ 》中有详细说明。

SAC提供了源代码版，可以自主编译安装。安装方法在\ ``Readme.buildsac``\ 中有详细说明。

简单列出如下：

.. code-block:: bash

 tar -zxvf sac-101.6_source.tar.gz
 cd sac-101.6
 ./configure --prefix=/usr/local/sac
 make
 sudo make install


接下来是修改环境变量，参考博文《`SAC二进制版的安装 <{filename}/SAC/2013-07-08_install-sac-from-binary-package.rst>`_》。

安装过程中可能出现的如下错误：

**错误1：**

::

 checking for tgetent in -lcurses... no
 checking for tgetent in -lncurses... no
 configure: error: libtermcap, libcurses or libncurses are required!
 make[1]: *** [lib/libedit.a] 错误 1
 make[1]:正在离开目录 `/home/seisman/Document/sac-101.6/libedit'
 make: *** [all-recursive] 错误 1

问题：缺少相关库libtermcap, libcurses or libncurses

解决办法：搜索相关库文件，并安装。不同系统上库文件名不同，可以直接搜索cureses等，安装其中类似libcurses-dev或者libcurses-devel的包。

**错误2：**

::

 In file included from ../inc/gdm.h:14,
 from ./msg/outmsg.c:14:
 ../inc/gd5.gui.h:66:27: error: X11/Intrinsic.h: 没有那个文件或目录

问题：缺少Xt头文件
解决办法：安装libxt-dev或者libxt-devel

**备注：**

每次安装新的软件包，最好重新解压，configure，make，这样可以保证前面错误的编译不会再次影响接下来的编译。

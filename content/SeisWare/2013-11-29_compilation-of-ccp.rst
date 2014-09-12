CCP1.0编译
##########

:date: 2013-11-29 16:37
:author: SeisMan
:category: 地震学软件
:tags: 接收函数, 编译
:slug: compilation-of-ccp

.. contents::

Prof. Lupei Zhu最近又在网上公开了两个程序包，CCP和CAP。

CCP，即Common-Conversion-Point，用于共转换点地震数据的叠加，这个程序主要与\ `hk1.3 <{filename}/SeisWare/2013-09-08_compilation-of-hk.rst>`_\ 一起使用，用于接收函数的研究。

安装方法以及一些修改与hk1.3类似：

下载与解压
==========

.. code-block:: bash

 $ wget http://www.eas.slu.edu/People/LZhu/downloads/ccp1.0.tar
 $ tar -xvf ccp1.0.tar
 $ cd ccp
 $ make clean

修改Makefile
============

在Makefile中加入如下两行，定义变量GMT\_INC和GMT\_LIB：

.. code-block:: make

    GMT_INC = -I/opt/GMT/include -I/opt/netcdf/include
    GMT_LIBS = -L/opt/GMT/lib -lgmt -lpsl -L/opt/netcdf/lib -lnetcdf -lm -s

编译
====

::

 $ make

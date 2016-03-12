CCP1.0编译
##########

:date: 2013-11-29 16:37
:modified: 2016-03-12
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

在Makefile中加入如下两行，定义变量 ``GMT_INC`` 和 ``GMT_LIB`` ：

.. code-block:: make

    GMT_INC = -I/opt/GMT/include
    GMT_LIBS = -L/opt/GMT/lib -lgmt -lpsl -lnetcdf -lm -s

编译
====

::

    $ make

BUG及其解决办法
===============

在按照CCP包里的说明文档执行程序3Dslice时，会出现如下信息及错误::

    interpolation order = 1
    GMT Warning: scale_factor should not be 0. Reset to 1.
    段错误 (核心已转储)

这个错误是由于3Dslice中调用 ``GMT_write_grd`` 导致的。具体原因尚不清楚，可能是由于GMT不同版本之间该函数的定义有变化导致的。

整个程序的作用在于从一个3D的网格文件中提取一个切片，然后将该切片上的数据写到2D网格文件中，调用 ``GMT_write_grd`` 的目的就是将2D的网格数据以netCDF格式写入到文件中。

因而，解决这个问题的思路有三个：

#. 读GMT源码，了解 ``GMT_write_grd`` 这个函数，找到可能出错的原因
#. 尝试安装稍老版本的GMT4，比如GMT 4.5.5，也许可以用
#. 在3Dslice源码的最后，删除对 ``GMT_write_grd`` 的调用，自己写代码，直接输出XYZ数据。然后在外部调用 ``xyz2grd`` 生成netCDF即可

推荐使用方法3。当然，如果有人用方法1解决了问题，可以告诉我。

hk1.3编译
#########

:date: 2013-09-08 19:22
:author: SeisMan
:category: 地震学软件
:tags: 接收函数, 编译
:slug: compilation-of-hk

.. contents::

hk是Prof. Lupei Zhu写的一个程序包，利用接收函数方法计算Moho厚度以及地壳波速比。整个程序包包含了接收函数所需的关键代码，但是想要高效地用于接收函数研究，还需要自己写一些代码作为补充。正由于程序本身的简洁，因而有助于理解接收函数的原理。

下载与解压
==========

.. code-block:: bash

 $ wget http://www.eas.slu.edu/People/LZhu/downloads/hk1.3.tar
 $ tar -xvf hk1.3.tar
 $ cd hk
 $ make clean

修改Makefile
============

在Makefile中设置变量GMT_INC和GMT_LIB：

::

    GMT_INC = -I/opt/GMT/include -I/opt/netcdf/include
    GMT_LIBS = -L/opt/GMT/lib -lgmt -lpsl -L/opt/netcdf/lib -lnetcdf -lm -s

修改代码
========

直接make进行编译可能会出现类似

::

    k_stack.c:30: 错误：‘BOOLEAN’未声明(在此函数内第一次使用)

这样的错误。

解决办法是将k_stack.c和grdmin.c中的BOOLEAN改成GMT_LONG。

编译
====

::
 
 $ make

其他
====

与hk相关的另一个程序包是CCP，用于共转换点地震数据的叠加，安装过程在\ `这里 <{filename}/SeisWare/2013-11-29_compilation-of-ccp.rst>`_\ 。

修订历史
========

-  2013-09-08：初稿；
-  2013-11-29：加入了CCP编译博文的链接；

pssac2的安装
############

:date: 2013-08-09 00:01
:modified: 2015-04-01
:author: SeisMan
:category: 地震学软件
:tags: pssac2, 编译
:slug: install-pssac2
:summary: 安装pssac2.

pssac2是由Brian Savage基于Lupei Zhu的pssac修改得到的，其继承了pssac的优质特性，同时在很多方面又有了进一步的提高。比如选项更加符合GMT的风格，且支持直接在地图上绘制地震图（这个在pssac中很困难），目前pssac2有两个版本，分别支持GMT4和GMT5。

GMT4版
======

下载
----

GMT4下的pssac2貌似没有更官方的下载地址，specfem3d中包含了pssac2的源码：

.. code-block:: bash

   $ git clone --recursive https://github.com/geodynamics/specfem3d.git
   $ mv specfem3d/utils/ADJOINT_TOMOGRAPHY_TOOLS/measure_adj/UTIL/pssac2 .
   $ cd pssac2

修改
----

在\ ``pssac2.c``\ 中\ ``#include <gmt.h>``\ 语句后添加如下语句::

    typedef GMT_LONG BOOLEAN;

编译
----

.. code-block:: bash

   $ ./configure --with-gmt=/opt/GMT-4.5.13
   $ make

GMT5版
======

下载
----

.. code-block:: bash

   git clone https://github.com/savage13/pssac2.git

编译
----

.. code-block:: bash

   $ ./configure --with-gmt=/opt/GMT-5.1.1

修订历史
========

- 2013-08-09：初稿；
- 2015-01-03：添加了pssac2的GMT5版本并简化了GMT4版本的说明；
- 2015-04-01：更新了pssac2的GMT4版本的地址；

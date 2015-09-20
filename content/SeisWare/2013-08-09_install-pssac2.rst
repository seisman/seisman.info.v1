pssac2的安装
############

:date: 2013-08-09 00:01
:modified: 2015-07-17
:author: SeisMan
:category: 地震学软件
:tags: pssac2, 编译
:slug: install-pssac2

``pssac2``\ 是由Brian Savage基于Lupei Zhu的\ ``pssac``\ 修改得到的，其继承了\ ``pssac``\ 的优质特性，同时在很多方面又有了进一步的提高。

``pssac2``\ 目前有两个版本，一个支持GMT4，一个支持GMT5。

GMT4版
======

GMT4版本的\ ``pssac2``\ 没有官方下载地址，目前只在\ `specfem3d <https://github.com/geodynamics/specfem3d/tree/master/utils/ADJOINT_TOMOGRAPHY_TOOLS/measure_adj/UTIL/pssac2>`_\ 程序包中找到有\ ``pssac2``\ 的源码。

由于specfem3d中的pssac2下载起来有些麻烦，这里我整理了一个版本供读者下载：

下载地址：http://7j1zxm.com1.z0.glb.clouddn.com/downloads/pssac2_GMT4.tar.gz

本文提供的版本在specfem3d给的源码的基础上做了如下操作与修改：

#. 将源码压缩成\ ``tar.gz``\ 格式，方便下载；
#. ``configure``\ 文件的第2467行原为::

        LDFLAGS+=" -L${withval}/lib "

   修改为::

        LDFLAGS+=" -L${withval}/lib -L${withval}/lib64"

   修改后的版本同时考虑了GMT库文件在\ ``lib``\ 和\ ``lib64``\ 的两种可能性。

安装方法如下：

.. code-block:: bash

   $ tar -xvf pssac2_GMT4.tar.gz
   $ cd pssac2_GMT4
   $ ./configure --with-gmt=/opt/GMT-4.5.13
   $ make

如果成功执行，则会在当前目录生成可执行文件\ ``pssac2``\ ，即可直接使用。

GMT5版
======

GMT5版本的pssac2似乎有不少bug，谨慎使用。

.. code-block:: bash

   $ git clone https://github.com/savage13/pssac2.git
   $ ./configure --with-gmt=/opt/GMT-5.1.2
   $ make

修订历史
========

- 2013-08-09：初稿；
- 2015-01-03：添加了pssac2的GMT5版本并简化了GMT4版本的说明；
- 2015-04-01：更新了pssac2的GMT4版本的地址；
- 2015-07-17：为GMT4版本的pssac2提供了新的下载链接；

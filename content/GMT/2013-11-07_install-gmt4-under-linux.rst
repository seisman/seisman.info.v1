GMT 4.5.14在Linux下的安装
#########################

:date: 2013-11-07 00:17
:author: SeisMan
:modified: 2015-11-01
:category: GMT
:tags: 安装, GMT4, 编译
:slug: install-gmt4-under-linux

.. contents::

说明
====

本文介绍如何在Linux下编译GMT4的最新版本：GMT 4.5.14。

很多Linux发行版的源中带有GMT软件包，但是版本一般较老，因而这里假定想要自己编译GMT4的读者，下载和编译的都是GMT4的最新版本，因而本文会随着GMT4新版本的发行而不断作出修改。

注意：GMT 4.5.14的官方文档中漏了很重要的一章，所以不建议以此版本的文档作为参考。

下载
====

官方ftp：ftp://ftp.soest.hawaii.edu/gmt

需要下载的包包括：

- `gmt-4.5.14-src.tar.bz2 <ftp://ftp.soest.hawaii.edu/gmt/gmt-4.5.14-src.tar.bz2>`_
- `gshhg-gmt-2.3.4.tar.gz <ftp://ftp.soest.hawaii.edu/gmt/gshhg-gmt-2.3.4.tar.gz>`_

注：GMT中的 ``triangulate`` 命令有两个不同的源码，其中一个遵循GPL协议，另一个不遵循GPL协议。GMT的src包中包含了前者。若有特殊需求，需要使用后者源码的功能，可以下载 `gmt-4.5.14-non-gpl-src.tar.bz2 <ftp://ftp.soest.hawaii.edu/gmt/gmt-4.5.14-non-gpl-src.tar.bz2>`_ ，并将解压后的triangulate源码覆盖 ``gmt-4.5.14-src.tar.bz2`` 中的相应源码。

下载完成后，可以用 ``md5sum`` 检查压缩文件的md5值，以保证该文件是完整且未被篡改的::

    $ md5sum gmt-4.5.14.src.tar.bz2 gshhg-gmt-2.3.4.tar.gz
    2d5bad3aaf593c46f0ff57264c2d3a47  gmt-4.5.14-src.tar.bz2
    80947a92cc88927aff070556ca5ab133  gshhg-gmt-2.3.4.tar.gz

依赖关系
========

基础依赖包
----------

编译GMT时需要一些开发工具（ ``gcc`` 、 ``g++`` 和 ``make`` ）以及底层的库文件 ``libc.so`` 和 ``libm.so`` 。

对于Ubuntu/Debian::

    sudo apt-get update
    sudo apt-get install gcc g++ make libc6

对于CentOS/RHEL/Fedora::

    sudo yum install gcc gcc-c++ make glibc

netCDF库
--------

GMT4主要依赖于netCDF4，可以直接使用Linux发行版官方源中提供的netCDF包。除了netCDF之外，建议还安装gdal包。虽然GMT不依赖于gdal，但gdal可以轻松地将其他数据格式转换为GMT可识别的格式。

对于Ubuntu/Debian::

    sudo apt-get update
    sudo apt-get install libnetcdf-dev libgdal-dev python-gdal

备注： ``libgdal-dev`` 在某些版本的Ubuntu下叫 ``libgdal1-dev``

对于RHEL/CentOS/Fedora::

    sudo yum install netcdf netcdf-devel gdal gdal-devel gdal-python

注意：

#. 一定不要试图自己手动编译netCDF。如果在阅读本文之前曾经手动编译过，一定要将原来手动编译生成的文件删除干净。通常可以使用 ``locate netcdf`` 找到 ``/usr/local`` 目录下的与netCDF相关的文件，直接删除即可。
#. CentOS和RHEL的官方源中没有netCDF，需要首先添加EPEL源再安装netCDF；Fedora官方源中自带netCDF；

X相关库
-------

GMT4中的 ``xgridedit`` 命令是一个很简易的带GUI的网格文件编辑器，其依赖于一堆图形界面相关库文件::

    libICE.so   libSM.so   libX11.so  libXaw.so
    libXext.so  libXmu.so  libXt.so

对于Ubuntu/Debian::

    sudo apt-get update
    sudo apt-get install libxaw7-dev
    sudo apt-get install libice-dev libsm-dev libx11-dev
    sudo apt-get install libxext-dev libxmu-dev libxt-dev

对于CentOS/RHEL/Fedora::

    sudo yum install libXaw-devel
    sudo yum install libICE-devel libSM-devel libX11-devel
    sudo yum install libXext-devel libXmu-devel libXt-devel

安装GMT
=======

编译GMT源码
-----------

.. code-block:: bash

   $ tar -xvf gmt-4.5.14-src.tar.bz2
   $ cd gmt-4.5.14
   $ ./configure --prefix=/opt/GMT-4.5.14
   $ make
   $ sudo make install-all       # 注意：这里是install-all不是install

其中 ``--prefix`` 指定了GMT安装路径，你可以指定为其他路径，但要注意后面其他步骤要与这里的路径统一。

安装海岸线数据
--------------

.. code-block:: bash

   $ tar -xvf gshhg-gmt-2.3.4.tar.gz
   $ sudo mv gshhg-gmt-2.3.4 /opt/GMT-4.5.14/share/coast


修改环境变量
------------

向 ``~/.bashrc`` 中加入GMT4的环境变量，并使环境变量生效：

.. code-block:: bash

   $ echo 'export GMT4HOME=/opt/GMT-4.5.14' >> ~/.bashrc
   $ echo 'export PATH=${GMT4HOME}/bin:$PATH' >> ~/.bashrc
   $ echo 'export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${GMT4HOME}/lib64' >> ~/.bashrc
   $ exec $SHELL -l

说明：

- 第一个命令向 ``~/.bashrc`` 中添加环境变量 ``GMT4HOME``
- 第二个命令修改 ``~/.bashrc`` ，将GMT4的bin目录加入到 ``PATH`` 中
- 第三个命令将GMT4的lib目录加入到动态链接库路径中，若为32位系统，则为 ``lib`` ；64位系统则为 ``lib64``
- 第四个命令是重新载入bash，相当于 ``source ~/.bashrc``

命令测试
========

在终端键入 ``psxy -`` ，若出现如下输出，则安装成功::

    $ psxy -
    psxy 4.5.14 [64-bit] - Plot lines, polygons, and symbols on maps

个人笔记
========

#. 查看GMT需要哪些动态链接库::

       $ cd /opt/GMT-4.5.14/bin
       $ readelf -d * | grep 'Shared library' | sort -u

#. Ubuntu下查找哪个软件包提供某个特定库文件： http://packages.ubuntu.com/
#. CentOS下查找哪个软件包提供某个特定库文件： ``yum provides libICE.so.6``

修订历史
========

- 2013-11-07：针对GMT 4.5.11发布初稿
- 2014-03-02：针对GMT 4.5.12进行更新
- 2014-03-08：``make install``->``make install-all``
- 2014-07-10：更新gshhg为2.3.1版；GMT4不依赖 ``gdal``
- 2014-09-14：更新gshhg为2.3.2版
- 2014-09-26：Ubuntu下 ``libxaw-dev`` 应为 ``libxaw7-dev``
- 2014-10-14：修正了若干细节
- 2014-11-04：修改环境变量 ``LD_LIBRARY_PATH``
- 2015-01-01：更新至GMT 4.5.13
- 2015-09-06：推荐安装GDAL的Python绑定（内含 ``gdal_merge.py`` ）
- 2015-09-18：下载后检查压缩文件的md5值
- 2015-10-11：重新整理了软件的依赖关系
- 2015-11-01：更新至GMT 4.5.14

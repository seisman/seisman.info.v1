GMT 4.5.12在Linux下的安装
#########################

:date: 2013-11-07 00:17
:author: SeisMan
:modified: 2014-09-14
:category: GMT
:tags: 安装, GMT4, 编译
:slug: install-gmt4-under-linux

.. contents::

说明
====

本文介绍如何Linux下如何编译安装GMT 4.5.12，不保证其适用于GMT的其他版本。

很多Linux发行版的源中带有GMT软件包，但是版本一般较老，因而这里假定想要自己编译GMT4的读者，下载和编译的都是GMT4的最新版本，因而本文会随着GMT4新版本的发行而不断作出修改。

下载
====

官方ftp：ftp://ftp.soest.hawaii.edu/gmt

需要下载的包包括\ [*]_\ ：

- `gmt-4.5.12-src.tar.bz2 <ftp://ftp.soest.hawaii.edu/gmt/gmt-4.5.12-src.tar.bz2>`_
- `gshhg-gmt-2.3.2.tar.gz <ftp://ftp.soest.hawaii.edu/gmt/gshhg-gmt-2.3.2.tar.gz>`_

.. [*] 对于GMT中的\ ``triangulate``\ 命令，其源码有两个版本，一个遵循GPL协议，一个不遵循GPL协议。GMT的src包中包含了前者，若有特殊需求，需要使用后者源码的功能，可以下载\ ``gmt-4.5.12-non-gpl-src.tar.bz2``\ 。


依赖关系
========

基础依赖包
----------

GMT编译过程需要C编译器，以及一些系统级别的库文件。

对于Ubuntu/Debian::

    sudo apt-get install g++ libxt-dev libxaw7-dev libxmu-dev libSM-dev

对于CentOS/RHEL/Fedora::

    sudo yum install gcc-c++ libXt-devel libXaw-devel libXmu-devel libSM-devel

软件依赖包
----------

GMT4主要依赖于netCDF，可以直接使用官方源中自带的netCDF包\ [*]_\ 。

对于Ubuntu/Debian::

    sudo apt-get install libnetcdf-dev libgdal1-dev

对于RHEL/CentOS/Fedora\ [*]_\ ::

    sudo yum install netcdf-devel gdal-devel

.. [*] GMT4可以使用netCDF3或netCDF4，但新版本的GMT正在逐渐放弃对netCDF3的支持，因而建议\ **使用netCDF4**\ ，且建议\ **不要自行编译netCDF4**\ 。

.. [*] CentOS的官方源中没有netCDF，需要首先添加EPEL源再安装netCDF。

安装GMT
=======

编译GMT源码
-----------

.. code-block:: bash

 $ tar -jxvf gmt-4.5.12-src.tar.bz2
 $ cd gmt-4.5.12
 $ ./configure --prefix=/opt/GMT-4.5.12
 $ make
 $ sudo make install-all

安装海岸线数据
--------------

.. code-block:: bash

   $ tar -zxvf gshhg-gmt-2.3.2.tar.gz
   $ sudo cp -r gshhg-gmt-2.3.2 /opt/GMT-4.5.12/share/coast

修改环境变量
------------

向\ ``~/.bashrc``\ 中加入GMT4的环境变量，并使环境变量生效：

.. code-block:: bash

   $ echo 'export GMT4HOME=/opt/GMT-4.5.12' >> ~/.bashrc
   $ echo 'export PATH=${GMT4HOME}/bin:$PATH' >> ~/.bashrc
   $ echo 'export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${GMT4HOME}/lib64' >> ~/.bashrc
   $ exec $SHELL -l

说明：

- 第一个命令向\ ``~/.bashrc``\ 中添加环境变量\ ``GMT4HOME``\ ；
- 第二个命令修改\ ``~/.bashrc``\ ，将GMT4的bin目录加入到\ ``PATH``\ 中；
- 第三个命令将GMT4的lib目录加入到动态链接库路径中，若为32位系统，则为\ ``lib``\ ；64位系统则为\ ``lib64``\ ；
- 第四个命令是重新载入bash，相当于\ ``source ~/.bashrc``\ 。

修订历史
========

- 2013-11-07：针对GMT 4.5.11发布初稿；
- 2014-03-02：针对GMT 4.5.12进行更新；
- 2014-03-08：``make install``->``make install-all``；
- 2014-07-10：更新gshhg为2.3.1版；GMT4不依赖\ ``gdal``\ ；
- 2014-09-14：更新gshhg为2.3.2版；
- 2014-09-26：Ubuntu下\ ``libxaw-dev``\ 应为\ ``libxaw7-dev``\ ；
- 2014-10-14：修正了若干细节；
- 2014-11-04：修改环境变量\ ``LD_LIBRARY_PATH``\ ；

GMT 4.5.12 安装
###############

:date: 2013-11-07 00:17
:author: SeisMan
:modified: 2014-09-14
:category: GMT
:tags: 安装, GMT4, 编译
:slug: install-gmt4-under-linux

.. contents::

说明
====

本文介绍GMT 4在Linux下如何编译安装，只针对\ **GMT 4.5.10**\ 及其之后的版本。

很多Linux发行版的源中带有GMT软件包，但是版本一般较老，因而这里假定想要自己编译GMT4的读者，下载和编译的都是GMT4的最新版本，因而本文会随着GMT4新版本的发行而不断作出修改。

下载
====

官方ftp：ftp://ftp.soest.hawaii.edu/gmt

需要下载的包包括\ [*]_\ ：

- `gmt-4.5.12-src.tar.bz2 <ftp://ftp.soest.hawaii.edu/gmt/gmt-4.5.12-src.tar.bz2>`_
- `gshhg-gmt-2.3.2.tar.gz <ftp://ftp.soest.hawaii.edu/gmt/gshhg-gmt-2.3.2.tar.gz>`_

.. [*] 对于GMT中的triangulate命令，其源码有两个版本，一个遵循GPL协议，一个不遵循GPL协议。GMT的src包中包含了前者，若有特殊需求，需要使用后者源码的功能，可以下载\ ``gmt-4.5.12-non-gpl-src.tar.bz2``\ 。


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

GMT4主要依赖于netCDF。虽然GMT4可以使用netCDF3，但是建议使用netCDF4。\ [*]_\

netCDF4的包依赖关系相对比较复杂，因而非常不建议自己编译netCDF4！最好使用官方源中自带的netCDF4444包。

对于Ubuntu/Debian::

    sudo apt-get install libnetcdf-dev libgdal1-dev

对于RHEL/CentOS/Fedora\ [*]_\ ::

    sudo yum install netcdf-devel

.. [*] GMT4可以使用netCDF3包，此时下载GSHHS数据时必须选择2.2.4之前的版本，且文件名中应包含\ ``nc3``\ 。

.. [*] CentOS的官方源中没有netCDF，需要首先添加EPEL源再安装netCDF。

安装GMT
=======

编译GMT源码
-----------

.. code-block:: bash

 $ tar -jxvf gmt-4.5.12-src.tar.bz2
 $ ./configure --prefix=/usr/local/GMT-4.5.12
 $ make
 $ sudo make install-all

安装海岸线数据
--------------

.. code-block:: bash

   $ tar -zxvf gshhg-gmt-2.3.2.tar.gz
   $ sudo cp -r gshhg-gmt-2.3.2 /usr/local/GMT-4.5.12/share/coast

修改环境变量
------------

在\ ``~.bashrc``\ 中加入如下语句：

.. code-block:: bash

   export GMTHOME=/usr/local/GMT-4.5.12
   export PATH=${GMTHOME}/bin:$PATH

修订历史
========

- 2013-11-07：针对GMT 4.5.11发布初稿；
- 2014-03-02：针对GMT 4.5.12进行更新；
- 2014-03-08：``make install``->``make install-all``；
- 2014-07-10：更新gshhg为2.3.1版；GMT4不依赖\ ``gdal``\ ；
- 2014-09-14：更新gshhg为2.3.2版；
- 2014-09-26：Ubuntu下\ ``libxaw-dev``\ 应为\ ``libxaw7-dev``\ ；

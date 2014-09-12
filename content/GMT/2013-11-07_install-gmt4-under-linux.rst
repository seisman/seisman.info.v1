GMT 4.5.12 安装
###############

:date: 2013-11-07 00:17
:author: SeisMan
:modified: 2014-07-10
:category: GMT
:tags: 安装, GMT4
:slug: install-gmt4-under-linux

.. contents::

说明
====

本文介绍GMT4系列在Linux下如何编译安装，只针对GMT 4.5.10之后的版本。

很多Linux发行版的源中带有GMT软件包，但是其版本一般较老，因而这里假定想要自己编译GMT4的读者，下载和编译的都是GMT4的最新版本，因而本文会随着GMT4新版本的发行而不断作出修改。

下载
====

官方网站：http://gmt.soest.hawaii.edu/gmt4/

官方ftp：ftp://ftp.soest.hawaii.edu/gmt

需要下载的包包括：

- \ ``gmt-4.5.12-src.tar.bz2``
- \ ``gshhg-gmt-2.3.0.tar.gz``

PS：对于GMT中的triangulate命令，其源码有两个版本，一个遵循GPL协议，一个不遵循GPL协议。GMT的src包中包含了前者，若有特殊需求，需要使用后者源码的功能，可以下载\ ``gmt-4.5.12-non-gpl-src.tar.bz2``\ 。

依赖关系
========

基础依赖包
----------

GMT编译过程需要C编译器，以及一些系统级别的库文件。

对于Ubuntu/Debian::

    sudo apt-get install g++ libxt-dev libxaw-dev libxmu-dev libSM-dev

对于CentOS/RHEL/Fedora::

    sudo yum install gcc-c++ libXt-devel libXaw-devel libXmu-devel libSM-devel

软件依赖包
----------

GMT4主要依赖于netcdf包，虽然GMT4可以使用netCDF3，但是建议使用netCDF4版本。

netCDF4的包依赖关系相对比较复杂，因而非常不建议自己编译！最好使用源中自带的netCDF包。

对于Ubuntu/Debian::

    sudo apt-get install libnetcdf-dev libgdal1-dev

对于RHEL/CentOS/Fedora::

    sudo yum install netcdf-devel 

PS1：CentOS有些特殊，其base源中没有netCDF，因而需要首先添加EPEL源，再安装netCDF。

PS2：对于GMT4，如果执意要使用netcdf3也没有问题，在下载海岸线数据时需要选择gshhg-2.2.4以下的文件名包含\ ``nc3``\ 的数据。

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

   $ tar -zxvf gshhg-gmt-2.3.1.tar.gz
   $ sudo cp -r gshhg-gmt-2.3.1 /usr/local/GMT-4.5.12/share/coast

修改环境变量
------------

在.bashrc中加入如下语句：

.. code-block:: bash    
   
   export GMTHOME=/usr/local/GMT-4.5.12
   export PATH=${GMTHOME}/bin:$PATH

修订历史
========

- 2013-11-07：针对GMT 4.5.11发布初稿；
- 2014-03-02：针对GMT 4.5.12进行更新；
- 2014-03-08：``make install``->``make install-all``；
- 2014-07-10：更新gshhg为2.3.1版；GMT4不依赖\ ``gdal``\ ；

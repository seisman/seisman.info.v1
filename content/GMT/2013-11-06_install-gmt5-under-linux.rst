GMT5.1.1在Linux下的安装
#######################

:date: 2013-11-06 00:53
:modified: 2014-03-02
:author: SeisMan
:category: GMT
:tags: 编译, GMT5
:slug: install-gmt5-under-linux

.. contents::

GMT5的第一个正式版5.1.0于2013年11月05日正式发布了。GMT5相对于GMT4的变化还是相当大的（幸好提供了兼容模式），对于用惯了GMT4的人来说，估计一时半会没法适应GMT5。不管怎样，先把GMT5安装上再说。

下载
====

GMT 5.1.1 需要下载三个文件：

#. GMT源码： http://gmtrac.soest.hawaii.edu/files/download?name=gmt-5.1.1-src.tar.gz
#. 全球海岸线数据GSHHG： ftp://ftp.soest.hawaii.edu/gshhg/gshhg-gmt-2.3.1.tar.gz
#. 全球数字图表DCW： ftp://ftp.soest.hawaii.edu/dcw/dcw-gmt-1.1.1.tar.gz

喜欢使用svn的，也可以利用下面的命令获取GMT源码::

    svn checkout svn://gmtserver.soest.hawaii.edu/gmt5/trunk gmt-dev

解决依赖关系
============

基础依赖包
----------

GMT编译过程需要C编译器，以及一些系统级别的库文件。

对于Ubuntu/Debian::

    sudo apt-get install g++ libxt-dev libxaw-dev libxmu-dev libSM-dev
    
对于CentOS/RHEL/Fedora::    
    
    sudo yum install gcc-c++ libXt-devel libXaw-devel libXmu-devel libSM-devel

软件依赖包
----------

GMT5的依赖包，相对来说要复杂很多。

必须的包包括：

- 看ps文件需要ghostscript；
- 编译需要cmake(>=2.8.5)；
- 网格文件需要netCDF(>=4.0,且需要支持netCDF-4/HDF5)。

其他可有可无的依赖包括：

- Perl兼容正则表达式库\ `PCRE`_\ ；
- 地理空间数据抽象库\ `GDAL`_\ ；
- Fourier变换库\ `FFTW`_ ；
- 如果想要自行编译文档的话还需要\ `Sphinx`_\ 。


对于Ubuntu/Debian::

    sudo aptitude install ghostscript build-essential cmake libnetcdf-dev libgdal1-dev

对于RHEL/CentOS/Fedora::

    sudo yum install cmake28 netcdf-devel gdal-devel

一些需要注意的地方:

#. CentOS官方源中cmake的版本为2.6.4，不满足要求，需要先安装EPEL源，再安装EPEL源中的\ ``cmake28``\ ，并且在编译过程中要使用\ ``cmake28``\ 命令，而不是\ ``cmake``\ 命令。
#. CentOS官方源中不带有netcdf，需要先安装EPEL源。需要安装的包包括\ ``netcdf``\ , \``netcdf-devel``\，其他包（尤其是hdf5包）会根据依赖关系自动安装。
#. GDAL包是非必须的，但是在数据格式转换时非常有用，建议安装。同样，CentOS需要先安装EPEL源；
#. PCRE以及FFTW请自行搜索；这里的sphinx是python的一个用于制作文档的模块，不是某个数据库查询软件；
#. 其他发行版很久不用了，不清楚细节，读者可以在使用过程中补充。


安装GMT
=======

解决了依赖关系之后，就可以安装了。

.. code-block:: bash

 $ ls
 dcw-gmt-1.1.1.tar.gz gmt-5.1.1-src.tar.gz gshhg-gmt-2.3.1.tar.gz
 $ tar -zxvf gmt-5.1.1-src.tar.gz
 $ tar -zxvf dcw-gmt-1.1.1.tar.gz
 $ tar -zxvf gshhg-gmt-2.3.1.tar.gz
 $ cd gmt-5.1.1
 $ cp cmake/ConfigUserTemplate.cmake cmake/ConfigUser.cmake
 $ vi cmake/ConfigUser.cmake # 修改Config文件

修改ConfigUser.cmake以满足用户自定义的需求，将需要修改的行最前面的“#”去掉，并根据实际情况修改，一个基本的示例如下::

    set (CMAKE_INSTALL_PREFIX "/opt/GMT-5.1.1")
    set (GMT_INSTALL_MODULE_LINKS FALSE)
    set (GSHHG_ROOT "/home/seisman/Datas/gshhg-gmt-2.3.1")
    set (COPY_GSHHG TRUE)
    set (DCW_ROOT "/home/seisman/Datas/dcw-gmt-1.1.1")
    set (COPY_DCW TRUE)

- CMAKE_INSTALL_PREFIX设置GMT的安装路径；
- GSHHG_ROOT为GSHHG数据的位置，需要对下载下来的压缩文件进行解压，并给定绝对路径；COPY_GSHHG为TRUE会将GSHHG数据复制到GMT/share/coast下；
- DCW_ROOT设置DCW数据的位置，需给定绝对路径，COPY_DCW将数据复制到GMT/share/dcw下；
- 也可以设置GMT_INSTALL_MODULE_LINKS为FALSE，这样做的原因可以参考\ `GMT多版本共存 <{filename}/GMT/2013-11-09_multiple-versions-of-gmt.rst>`_

PS: 如果系统中存在多个GMT的版本，按照上面的做法会存在多个GSHHG和DCW数据的副本。可以将这些数据放置在系统中固定的位置（比如我把这些数据都放在\ ``/home/seisman/Datas``\ 目录下），然后有两种处理方式：其一，设置COPY_GSHHG为FALSE，此时GMT在编译时会到GSHHG_ROOT指定的目录中寻找数据；其二，使用默认的GSHHG_ROOT以及COPY_GSHHG，在安装完成之后，到GMT/share目录下设置一个target为\ ``/home/seisman/Datas/gshhg-gmt-2.3.0``\ ，link name为coast的软链接即可。对于DCW数据，同理。

修改完毕后，进行编译::

 $ mkdir build
 $ cd build/
 $ cmake ..

在某些系统下\ ``cmake``\ 的版本是2.6，此时命令需要改成\ ``cmake28 ..``\ 。

\ ``cmake ..``\ 会检查GMT对软件的依赖关系，我的检查结果如下::

    *  Options:
    *  Found GSHHG database       : /home/seisman/Datas/gshhg-gmt-2.3.1 (2.3.1)
    *  Found DCW-GMT database     : /home/seisman/Datas/dcw-gmt-1.1.0
    *  NetCDF library             : /usr/lib64/libnetcdf.so
    *  NetCDF include dir         : /usr/include
    *  GDAL library               : /usr/lib64/libgdal.so
    *  GDAL include dir           : /usr/include/gdal
    *  FFTW library               : /usr/lib64/libfftw3f.so
    *  FFTW include dir           : /usr/include
    *  Accelerate Framework       : 
    *  Regex support              : PCRE (/usr/lib64/libpcre.so)
    *  File locking               : TRUE
    *  License restriction        : no
    *  Triangulation method       : Shewchuk
    *  Build mode                 : shared
    *  Build GMT core             : always [libgmt.so]
    *  Build PSL library          : always [libpsl.so]
    *  Build GMT supplements      : yes [supplements.so]
    *  Build proto supplements    : none
    *
    *  Locations:
    *  Installing GMT in          : /opt/GMT-5.1.1
    *  GMT_DATADIR                : /opt/GMT-5.1.1/share
    *  GMT_DOCDIR                 : /opt/GMT-5.1.1/share/doc
    *  GMT_MANDIR                 : /opt/GMT-5.1.1/share/man
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /export/home/seisman/backup/seisware/GMT/5.1.1/gmt-5.1.1/build

检查完毕，开始编译和安装::

 $ make
 $ sudo make install

自行编译文档
============

如果系统中安装了sphinx和LaTeX，则可以自行编译文档。（其实直接用官方已经编译好的文档即可）

::

 $ make docs_man
 $ make docs_html
 $ make docs_pdf
 $ sudo make install

修改环境变量
============

在.bashrc中加入如下语句

.. code-block:: bash

 export GMTHOME=/opt/GMT-5.1.1
 export PATH=${GMTHOME}/bin:$PATH

参考来源
========

#.  http://gmtrac.soest.hawaii.edu/projects/gmt/wiki/BuildingGMT
#.  `GMT4.5.12在Linux下的安装 <{filename}/GMT/2013-11-07_install-gmt4-under-linux.rst>`_

修订历史
========

- 2013-11-06: 初稿；
- 2014-02-22: cmake版本需要2.8以上；
- 2014-03-02: 更新至GMT 5.1.1；

.. _PCRE: http://www.pcre.org/
.. _GDAL: http://www.gdal.org/
.. _FFTW: http://www.fftw.org/
.. _Sphinx: http://sphinx-doc.org/

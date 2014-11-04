GMT 5.1.1在Linux下的安装
########################

:date: 2013-11-06 00:53
:modified: 2014-09-14
:author: SeisMan
:category: GMT
:tags: 编译, GMT5, 安装
:slug: install-gmt5-under-linux

.. contents::

本文介绍如何在Linux下编译安装GMT5。对于想要自己编译安装GMT5的读者而言，我默认读者下载并想要安装的是最新的GMT5版本，因而本文会随着GMT5新版本的发布而不断更新。

若新版本的安装方式与旧版本的安装方式有区别，则本文只介绍新版本的安装方式（也许会提几句与旧版本的区别）。执意要安装旧版本GMT5的读者，需要自己解决所遇到的问题。

下载
====

GMT 5.1.1 需要下载三个文件：

#. GMT源码： http://gmtrac.soest.hawaii.edu/files/download?name=gmt-5.1.1-src.tar.gz
#. 全球海岸线数据GSHHG： ftp://ftp.soest.hawaii.edu/gshhg/gshhg-gmt-2.3.2.tar.gz
#. 全球数字图表DCW： ftp://ftp.soest.hawaii.edu/dcw/dcw-gmt-1.1.1.tar.gz


解决依赖关系
============

基础依赖包
----------

GMT编译过程需要C编译器，以及一些系统级别的库文件。

对于Ubuntu/Debian::

    sudo apt-get install g++ libxt-dev libxaw7-dev libxmu-dev libSM-dev

对于CentOS/RHEL/Fedora::

    sudo yum install gcc-c++ libXt-devel libXaw-devel libXmu-devel libSM-devel

软件依赖包
----------

GMT5的依赖包，相对来说要复杂很多。

必须的包包括：

- 看ps文件需要\ ``ghostscript``\ ；
- 编译需要\ ``cmake``\ （>=2.8.5）；
- 网格文件需要\ ``netCDF``\ （>=4.0,且需要支持netCDF-4/HDF5）。

其他可有可无的依赖包括：

- Perl兼容正则表达式库\ `PCRE`_\ ；
- 地理空间数据抽象库\ `GDAL`_\ ；
- Fourier变换库\ `FFTW`_ ；
- 如果想要自行编译文档的话还需要\ `Sphinx`_\ 。

对于Ubuntu/Debian::

    sudo apt-get install ghostscript build-essential cmake libnetcdf-dev libgdal1-dev

对于RHEL/CentOS/Fedora::

    sudo yum install ghostscript cmake netcdf-devel gdal-devel

一些需要注意的地方:

#. CentOS 6官方源中cmake的版本为2.6.4，版本过低。需要先安装EPEL源，再安装EPEL源中的\ ``cmake28``\ ，并且在接下来的编译过程中要将\ ``cmake``\ 命令改成\ ``cmake28``\ ；
#. CentOS 7官方源中cmake版本为2.8.11，可以直接安装使用；
#. CentOS官方源中不带有netCDF，需要先安装EPEL源。需要安装的包包括\ ``netcdf``\ , \ ``netcdf-devel``\ ，其他包（尤其是hdf5包）会根据依赖关系自动安装。
#. GDAL包是非必须的，但是在数据格式转换时非常有用，建议安装。同样，CentOS需要先安装EPEL源；
#. PCRE以及FFTW等其他非必须包，如有需要，可以自行搜索安装；
#. 其他发行版很久不用了，不清楚细节，读者可以在使用过程中补充。

安装GMT
=======

解决了依赖关系之后，就可以安装了。

.. code-block:: bash

 $ ls
 dcw-gmt-1.1.1.tar.gz gmt-5.1.1-src.tar.gz gshhg-gmt-2.3.2.tar.gz
 $ tar -zxvf gmt-5.1.1-src.tar.gz
 $ tar -zxvf dcw-gmt-1.1.1.tar.gz
 $ tar -zxvf gshhg-gmt-2.3.2.tar.gz
 $ cd gmt-5.1.1
 $ cp cmake/ConfigUserTemplate.cmake cmake/ConfigUser.cmake
 $ vi cmake/ConfigUser.cmake # 修改Config文件

修改\ ``ConfigUser.cmake``\ 以满足用户自定义的需求，将需要修改的行最前面的“#”去掉，并根据实际情况修改，一个基本的示例如下::

    set (CMAKE_INSTALL_PREFIX "/opt/GMT-5.1.1")
    set (GMT_INSTALL_MODULE_LINKS FALSE)
    set (GSHHG_ROOT "/home/seisman/Datas/gshhg-gmt-2.3.2")
    set (COPY_GSHHG TRUE)
    set (DCW_ROOT "/home/seisman/Datas/dcw-gmt-1.1.1")
    set (COPY_DCW TRUE)

- ``CMAKE_INSTALL_PREFIX``\ 设置GMT的安装路径；
- ``GSHHG_ROOT``\ 为GSHHG数据的位置，需要对下载下来的压缩文件进行解压，并给出文件夹的绝对路径；\ ``COPY_GSHHG``\ 为TRUE会将GSHHG数据复制到\ ``GMT/share/coast``\ 下；
- ``DCW_ROOT``\ 设置DCW数据的位置，需给出DCW数据所在文件夹的绝对路径，\ ``COPY_DCW``\ 将数据复制到\ ``GMT/share/dcw``\ 下；
- 设置GMT_INSTALL_MODULE_LINKS为FALSE，这样做的原因可以参考\ `GMT多版本共存 <{filename}/GMT/2013-11-09_multiple-versions-of-gmt.rst>`_

PS: 如果系统中存在多个GMT的版本，按照上面的做法会存在多个GSHHG和DCW数据的副本。可以将这些数据放置在系统中固定的位置（比如我把这些数据都放在\ ``/home/seisman/Datas``\ 目录下），然后有两种处理方式：其一，设置COPY_GSHHG为FALSE，此时GMT在编译时会到GSHHG_ROOT指定的目录中寻找数据；其二，使用默认的GSHHG_ROOT以及COPY_GSHHG，在安装完成之后，到GMT/share目录下设置一个target为\ ``/home/seisman/Datas/gshhg-gmt-2.3.2``\ ，link name为coast的软链接即可。对于DCW数据，同理。

修改完毕后，进行编译::

 $ mkdir build
 $ cd build/
 $ cmake ..

``cmake ..``\ 会检查GMT对软件的依赖关系，我的检查结果如下::

    *  Options:
    *  Found GSHHG database       : /home/seisman/Datas/gshhg-gmt-2.3.2 (2.3.2)
    *  Found DCW-GMT database     : /home/seisman/Datas/dcw-gmt-1.1.1
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
    -- Build files have been written to: /home/seisman/backup/seisware/GMT/5.1.1/gmt-5.1.1/build

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

修改环境变量并使其生效

.. code-block:: bash

   $ echo 'export GMT5HOME=/opt/GMT-5.1.1' >> ~/.bashrc
   $ echo 'export PATH=${GMT5HOME}/bin:$PATH' >> ~/.bashrc
   $ echo 'export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${GMT5HOME}/lib64' >> ~/.bashrc
   $ exec $SHELL -l

说明

- 第一个命令向\ ``~/.bashrc``\ 中添加环境变量\ ``GMT4HOME``\ ；
- 第二个命令修改\ ``~/.bashrc``\ ，将GMT4的bin目录加入到\ ``PATH``\ 中；
- 第三个命令将GMT4的lib目录加入到动态链接库路径中，若为32位系统，则为\ ``lib``\ ；64位系统则为\ ``lib64``\ ；
- 第四个命令是重新载入bash，相当于\ ``source ~/.bashrc``\ 。


参考来源
========

#.  http://gmtrac.soest.hawaii.edu/projects/gmt/wiki/BuildingGMT
#.  `GMT4.5.12在Linux下的安装 <{filename}/GMT/2013-11-07_install-gmt4-under-linux.rst>`_

修订历史
========

- 2013-11-06：初稿；
- 2014-02-22：cmake版本需要2.8以上；
- 2014-03-02：更新至GMT 5.1.1；
- 2014-09-14：更新GSHHG至2.3.2；
- 2014-09-26：Ubuntu下\ ``libxaw-dev``\ 应为\ ``libxaw7-dev``\ ；
- 2014-11-04：修改环境变量\ ``LD_LIBRARY_PATH``\ ；

.. _PCRE: http://www.pcre.org/
.. _GDAL: http://www.gdal.org/
.. _FFTW: http://www.fftw.org/
.. _Sphinx: http://sphinx-doc.org/

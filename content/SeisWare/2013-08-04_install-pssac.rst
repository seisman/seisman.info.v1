安装pssac
#########

:date: 2013-08-04
:modified: 2015-07-16
:author: SeisMan
:category: 地震学软件
:tags: pssac, 编译, GMT4
:slug: install-pssac

.. contents::

``pssac``\ 是Prof. Lupei Zhu根据GMT的\ ``psxy``\ 命令修改得到，用于绘制SAC格式的波形数据的一个小程序。

该程序调用了GMT的绘图库，因而安装该程序之前需要首先安装GMT4。需要注意，该程序不支持GMT5。

下载
====

.. code-block:: bash

   # 下载基于GMT4.0的pssac包
   $ wget http://www.eas.slu.edu/People/LZhu/downloads/pssac.tar
   $ tar -xvf pssac.tar      # 解压

   # 下载基于GMT4.5的pssac源码
   $ wget http://www.eas.slu.edu/People/LZhu/downloads/pssac.c

   $ mv pssac.c pssac/       # 用基于GMT4.5的pssac.c替换基于GMT 4.0的pssac.c
   $ cd pssac

修改Makefile
============

源码中的Makefile有些问题，需要进一步修改。修改之后的Makefile内容如下：

.. code-block:: makefile

   GMTHOME=/opt/GMT-4.5.13
   GMT_INC=-I${GMTHOME}/include
   GMT_LIBS=-L${GMTHOME}/lib -lgmt -lpsl -lgmtps -lnetcdf -lm

   CFLAGS = -O ${GMT_INC}

   pssac: pssac.o sacio.o
        $(LINK.c) -o $@ $@.o sacio.o $(GMT_LIBS)

   clean:
        rm -f pssac *.o

- ``GMTHOME``\ 是当前系统中GMT4的安装路径，需要根据自己的情况修改
- ``GMT_INC``\ 指定了GMT的头文件的位置
- ``GMT_LIBS``\ 指定了编译过程中所需要的库文件
- ``-L``\ 指定了在编译过程中要在哪些路径下寻找库文件

通常情况下，只需要根据自己的情况修改\ ``GMTHOME``\ 即可。若netCDF包不是通过系统自带的软件包管理器安装而是手动编译的，则需要在\ ``GMT_INC``\ 和\ ``GMT_LIBS``\ 中加上netCDF所对应的路径。

编译
====

编译过程就是简单的make，正常情况下的输出如下：

.. code-block:: bash

   $ make
   cc -O -I/opt/GMT-4.5.13/include   -c -o pssac.o pssac.c
   cc -O -I/opt/GMT-4.5.13/include   -c -o sacio.o sacio.c
   cc -O -I/opt/GMT-4.5.13/include    -o pssac pssac.o sacio.o -L/opt/GMT-4.5.13/lib -lgmt -lpsl -lgmtps -lnetcdf -lm

编译会生成可执行文件\ ``pssac``\ ，将该可执行文件复制到PATH中即可，比如\ ``/usr/local/bin```\ 、\ ``/opt/GMT-4.5.13/bin``\ 或\ ``${HOME}/bin``\ 。

执行
====

终端直接执行\ ``pssac``\ 就会出现命名的语法说明。

修订历史
========

- 2013-04-17：初稿；
- 2013-04-19：加入了对旧版本pssac.c的讨论；
- 2014-06-24：GMT4的最近几个版本，都不再建议自己安装netcdf3了，最好还是自己利用系统自带的软件包管理器安装netcdf4。在这种情况下，netcdf会被安装到系统默认路径中，因而Makefile中不需要再指明netcdf的安装路径；
- 2014-07-16：在某些系统下，GMT_LIBS需要加上\ ``-lm``\ ；
- 2015-07-16：整理，并删除对旧版本pssac.c的说明；

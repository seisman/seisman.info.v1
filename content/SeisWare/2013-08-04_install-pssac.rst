pssac之安装
###########

:date: 2013-08-04 15:13
:modified: 2014-07-16       
:author: SeisMan
:category: 地震学软件
:tags: pssac, 编译, GMT4
:slug: install-pssac

.. contents::

**注意：** pssac仅支持GMT4。

pssac是Prof. Lupei Zhu根据GMT的psxy命令改写的一个小程序，利用GMT强大的绘图功能来绘制SAC文件。

下载
====

.. code-block:: bash

 $ mkdir pssac
 $ cd pssac
 $ wget http://www.eas.slu.edu/People/LZhu/downloads/pssac.tar
 #下载基于GMT4.0的pssac包
 $ wget http://www.eas.slu.edu/People/LZhu/downloads/pssac.c
 #下载基于GMT4.5的pssac源码
 $ tar xvf pssac.tar
 $ cp pssac.c pssac #用新的pssac.c替换旧的
 $ cd pssac

修改Makefile
============

用你最喜欢的编辑器打开Makefile文件，在文件头部加上1-5行的内容，并根据自己的情况稍作修改：

**注意：** 安装GMT4时必须用系统自带的软件包管理器安装netcdf3或netcdf4。

.. code-block:: bash

 GMTHOME=/usr/local/GMT
 GMT_INC=-I${GMTHOME}/include
 GMT_LIBS=-L${GMTHOME}/lib -lgmt -lpsl -lgmtps -lnetcdf -lm

 CFLAGS = -O ${GMT_INC}

 pssac: pssac.o sacio.o
    $(LINK.c) -o $@ $@.o sacio.o $(GMT_LIBS)

 clean:
    rm -f pssac *.o

-  ``GMTHOME``\ 为你安装的GMT的路径，需要根据自己的情况修改
-  ``GMT_INC``\ 指定了GMT的头文件位置
-  ``GMT_LIBS``\ 指定了编译过程中所需要的库文件
-  ``-L``\ 指定了在编译过程中要在哪些路径下寻找库文件
-  ``-lgmt -lpsl -lgmtps``\ 为\ ``GMT/lib``\ 下的几个库文件
-  ``-lnetcdf``\ 是netcdf的库文件

编译
====

.. code-block:: bash

 $ make
 cc -O -I/usr/local/local/GMT/include -c -o pssac.o pssac.c
 cc -O -I/usr/local/local/GMT/include -c -o sacio.o sacio.c
 cc -O -I/usr/local/local/GMT/include -o pssac pssac.o sacio.o -L/usr/local/local/GMT/lib -lgmt -lpsl -lgmtps -lnetcdf

编译过程就是简单的make，如果没有错误的话应该会出现下面三行。

执行
====

直接./pssac应该就会出来关于pssac的使用说明，如果报其他错，可以向我反馈。

对旧版本的说明
==============

在编译旧版本的pssac的时候，可能会出现类似“BOOLEAN类型未定义”这样的错误，这是因为在C99标准之前是没有bool类型的定义，C99标准中增加了_Bool类型作为布尔类型，而BOOLEAN应该是用户自己定义的。具体可以参考下面两个维基条目：

http://zh.wikipedia.org/wiki/%E5%B8%83%E7%88%BE_%28%E6%95%B8%E6%93%9A%E9%A1%9E%E5%9E%8B%29#C

http://zh.wikipedia.org/wiki/C%E8%AF%AD%E8%A8%80#C99

可以通过在pssac.c重定义数据类型来修正整个错误。在pssac.c代码的前部加上如下两个typedef语句中的任何一个都可以：

.. code-block:: C

 typedef _Bool BOOLEAN;
 typedef GMT_LONG BOOLEAN;

其中GMT_LONG是Prof. Zhu 的新pssac.c代码中的用法。

修订历史
========

- 2013-04-17：初稿；
- 2013-04-19：加入了对旧版本pssac.c的讨论。
- 2014-06-24：GMT4的最近几个版本，都不再建议自己安装netcdf3了，最好还是自己利用系统自带的软件包管理器安装netcdf4。在这种情况下，netcdf会被安装到系统默认路径中，因而Makefile中不需要再指明netcdf的安装路径。
- 2014-07-16：在某些系统下，GMT_LIBS需要加上\ ``-lm``\ 。  

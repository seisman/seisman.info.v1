fk3.1编译
#########

:date: 2013-09-01 11:03
:author: SeisMan
:category: 地震学软件
:tags: 理论地震图, 编译, C, Fortran, Perl
:slug: fk-installation

.. contents::

fk是Prof. Lupei Zhu写的一个计算水平分层介质中理论地震图的小程序。

下载
====

下载地址： http://www.eas.slu.edu/People/LZhu/downloads/fk3.1.tar

解压
====

::

 $ tar -xvf fk3.1.tar

修改Makefile
============

程序的大部分代码是用Fortran 77的语法写的，由于Fortran 77规定每行超过第72列的字符会被忽略，而代码中部分行超过了72列。因而要修改编译器选项，加入语句如下::

 FC=gfortran -ffixed-line-length-none

部分代码中调用了SAC提供的子程序，如果已经安装了SAC，那么可以将CFLAGS和SACLIB两行去除注释。

最终修改得到的Makefile的前几行如下所示：

.. code-block:: make

 FC=gfortran -ffixed-line-length-none
 optimize=-O
 FFLAGS=$(optimize)
 CFLAGS=$(optimize)

 CFLAGS=$(optimize) -DSAC_LIB
 SACLIB=-L$(SACHOME)/lib -lsac -lsacio

如果SACHOME在.bashrc中没有定义，此处应根据实际情况修改。

编译
====

::

 $ make

安装
====

几个重要的文件包括fk、fk.pl、st\_fk、syn、trav，将这几个文件复制到$HOME/bin或者其他可搜索的路径中即可。

说明
====

-  fk：程序的核心，负责计算格林函数；
-  st_fk：与fk相似，负责计算静态位移；
-  trav：计算到时；
-  syn：利用fk计算出的格林函数合成最终地震图；
-  fk.pl：fk的Perl封装，相对fk来说更易于使用，其调用了fk和trav；
-  fk.pl中调用了另一个命令sachd，该命令将到时写入SAC头段中，但是这个命令没给源码，不过不太重要；

fk 3.2的一些变化
================

fk 3.2发布了，该版本的唯一变化是加入了3.1中缺失的sachd的源码，Makefile中多加入了两行。

按照上面所说进行修改，make之后出现如下错误：

::

    cc -O    -o sachd sachd.o sacio.o
    sacio.o: In function `read_sac2':
    sacio.c:(.text+0x831): undefined reference to `rintf'
    sacio.c:(.text+0x8e0): undefined reference to `rintf'
    collect2: ld 返回 1
    make: *** [sachd] 错误 1

只要将Makefile中

::

    sachd: sachd.o sacio.o
        ${LINK.c} -o $@ $^

改成

::

    sachd: sachd.o sacio.o
        ${LINK.c} -o $@ $^ -lm

即可。

修订历史
========

-  2013/09/01：初稿；
-  2013/10/07：关于fk 3.2的一点修改；

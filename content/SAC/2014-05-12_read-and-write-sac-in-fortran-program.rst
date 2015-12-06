在Fortran程序中读写SAC文件
##########################

:date: 2014-05-12 15:55
:author: SeisMan
:category: SAC
:tags: Fortran, SAC基础
:slug: read-and-write-sac-in-fortran-program

.. contents::

序言
====

SAC是进行地震数据预处理的好工具，但是无法实现所有的数据分析功能，这就需要能够在自己的程序中读写SAC文件。这篇博文介绍如何在Fortran程序中读写SAC文件。

子函数库
========

SAC自带了读写函数库，并且提供了相关的示例程序，这些可以在\ `《SAC参考手册》 <{filename}/SAC/2013-07-06_sac-manual.rst>`_\ 中的相关章节中找到。

SAC自带的读写子函数实际上并不好用，因而就有很多人自己重新实现了SAC读写函数库，其中之一就是Prof. Lupei Zhu所写的 ``sacio.c`` 。

\ `Prof. Lupei Zhu <http://www.eas.slu.edu/People/LZhu/home.html>`_\ 的 ``fk`` 或者  ``gCAP`` 中都包含了SAC读写函数库， ``sacio.c`` 和 ``sac.h`` 。这是一个用C语言实现的SAC读写函数库，同时提供了一些Fortran接口，因而也可以直接在Fortran程序中使用。


子函数
======

``sacio.c`` 中定义了如下Fortran接口：

- rdsac0：读取SAC二进制文件
- my_brsac：读取SAC二进制文件的另一个Fortran接口
- wrtsac0：写SAC二进制文件
- wrtsac2：将两个1维数组写成XY形式的SAC数据
- wrtsac3：与wrtsac0类似，但向头段中加入了分量信息

读和写一个SAC文件
=================

最常见的需求是读取一个SAC二进制文件，对数据进行处理，并将处理后的数据写回到原文件中。

.. code-block:: fortran

          program main
          implicit none
          integer MAX
          parameter (MAX=10000)
          real array
          dimension array(MAX)
          real b, delta, dist
          integer npts, j
          character(len=80) kname, kout
          kname = 'seis.SAC'
          call rdsac0(trim(kname), delta, npts, b, array)
    !     Process
          do j=1, npts
            array(j) = array(j)+1
          end do
          dist = 10.0  ! distance
          kout = 'seis.SAC.out'
          call wrtsac0(trim(kout), delta, npts, b, dist, array)
          end program

需要注意的几个事项包括：

- 调用子函数前需要使用 ``trim`` 将文件名中的多余空白字符去除
- 只能返回头段变量delta、npts和b的值，无法获取其它头段变量
- 对数据进行处理后，可以直接写回到原文件中，或写入到新文件中
- 写数据时，需要提供表示距离的变量 ``dist`` （这完全是个人的需求，所以该子函数并不那么好用）

说明
====

此SAC函数库的Fortran接口，基本是完全根据个人需求而写的，因而没有太高的通用性。且Fortran中不包含结构体，无法一次性获取全部头段变量的信息。有需要在Fortran中读写SAC的可以考虑使用SAC自带的函数库，或者重新定义该函数。

编译方法
========

::

    $ gfortran prog.c  sacio.c

修订历史
========

- 2014-05-11：mars_cfeng原稿；
- 2014-05-12：SeisMan修订稿；

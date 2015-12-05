hk1.3编译
#########

:date: 2013-09-08 19:22
:modified: 2015-07-13
:author: SeisMan
:category: 地震学软件
:tags: 接收函数, 编译
:slug: compilation-of-hk

.. contents::

hk是Prof. Lupei Zhu写的一个程序包，利用接收函数方法计算Moho厚度以及地壳波速比。整个程序包包含了接收函数所需的关键代码，但是想要高效地用于接收函数研究，还需要自己写一些代码作为补充。而网络上实际上有很多更加成熟和高效的接收函数代码，所以此程序的实际用途不大。但该程序的代码比较简单，可以帮助理解接收函数的原理与实现。

下载与解压
==========

.. code-block:: bash

   $ wget http://www.eas.slu.edu/People/LZhu/downloads/hk1.3.tar  # 下载
   $ tar -xvf hk1.3.tar     # 解压
   $ cd hk
   $ make clean
   $ rm .gmtcommands4       # 删除临时文件

修改Makefile
============

hk依赖于GMT，但只支持GMT4，不支持GMT5。

在Makefile的最前面新增如下两行定义环境变量 ``GMT_INC`` 和\ ``GMT_LIBS``\ 。

通常情况下，新增的两行如下::

    GMT_INC = -I/opt/GMT-4.5.13/include
    GMT_LIBS = -L/opt/GMT-4.5.13/lib -lgmt -lpsl -lnetcdf -lm -s

如果在安装GMT时，netCDF是通过手动编译并指定 ``--prefix`` 安装的，则需要额外指定netCDF的路径::

    GMT_INC = -I/opt/GMT-4.5.13/include -I/opt/netcdf/include
    GMT_LIBS = -L/opt/GMT-4.5.13/lib -lgmt -lpsl -L/opt/netcdf/lib -lnetcdf -lm -s

修改代码
========

修改完Makefile后执行make进行编译可能会出现如下错误::

    k_stack.c: In function ‘main’:
    k_stack.c:29:3: error: unknown type name ‘BOOLEAN’
       BOOLEAN error = FALSE, addmore=FALSE;
       ^
    make: *** [k_stack.o] Error 1

解决办法是将 ``k_stack.c`` 的29行和\ ``grdmin.c``\ 的18行中的\ ``BOOLEAN``\ 替换成\ ``GMT_LONG``\ 。

编译
====

修改完Makefile和BOOLEAN后，执行如下命令::

    $ make

其他
====

``README`` 中介绍了程序的具体用法，具体示例位于目录 ``examples``\ 。

直接执行 ``README`` 中的示例代码，可能会出现如下错误::

    $ ./iter_decon -F1/3/-5 -N100 -C-2/-10/80 -T0.1 example/KUL.z example/KUL.[r,t]
    example/KUL.z
    Error in allocating memory for reading example/KUL.z n=0
    fail to get data from example/KUL.z

出现这个错误的原因是：日常使用的大部分机器的字节序是Little Endian的，而软件包中自带数据的字节序是Big Endian。即数据与当前机器的字节序不匹配。可以通过将数据读入SAC再写回到磁盘来完成字节序的转换::

   SAC> r KUL.* pp.*
   SAC> w over

``hk_plt.pl`` 脚本中第13行， ``-JX4/2``\ 应改成\ ``-JX4i/2i``\ ，这样画出来的图的尺寸才是对的。

修订历史
========

- 2013-09-08：初稿；
- 2015-07-13：示例及脚本中的若干问题；

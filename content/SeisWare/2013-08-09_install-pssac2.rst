pssac2的安装
############

:date: 2013-08-09 00:01
:author: SeisMan
:category: 地震学软件
:tags: pssac2, 编译
:slug: install-pssac2
:summary: 安装pssac2.

pssac2是由Brian Savage基于Lupei Zhu的pssac修改得到的，其继承了pssac的优质特性，同时在很多方面又有了进一步的提高。比如选项更加符合GMT的风格，且支持直接在地图上绘制地震图（这个在pssac中很困难）。同时，Brain Savage也是当前SAC的主要维护者之一。

Brain Savage的个人主页： http://seismolab.gso.uri.edu/~savage/

下载
====

pssac2貌似没有更官方的下载地址，现在只能找到下面这个

.. code-block:: bash

 $ mkdir pssac2
 $ cd pssac2
 $ wget -r -np -nd http://geodynamics.org/svn/cig/seismo/3D/ADJOINT_TOMO/measure_adj/UTIL/pssac2/
 $ rm index.html robots.txt

编译前的配置
============

.. code-block:: bash

 $ chmod +x configure
 $ ./configure --with-gmt=/usr/local/GMT-4.5.9 --with-netcdf=/usr/local/netcdf-3.6.3 
 checking whether to enable maintainer-specific portions of Makefiles... no
 checking build system type... x86_64-unknown-linux-gnu
 checking host system type... x86_64-unknown-linux-gnu
 checking target system type... x86_64-unknown-linux-gnu
 checking for a BSD-compatible install... /usr/bin/install -c
 checking whether build environment is sane... yes
 checking for a thread-safe mkdir -p... /bin/mkdir -p
 checking for gawk... gawk
 checking whether make sets $(MAKE)... yes
 checking for gcc... gcc
 checking whether the C compiler works... yes
 checking for C compiler default output file name... a.out
 checking for suffix of executables...
 checking whether we are cross compiling... no
 checking for suffix of object files... o
 checking whether we are using the GNU C compiler... yes
 checking whether gcc accepts -g... yes
 checking for gcc option to accept ISO C89... none needed
 checking for style of include used by make... GNU
 checking dependency style of gcc... none
 checking for library containing sin... -lm
 checking for library containing nc_create... -lnetcdf
 checking for library containing GMT_begin... -lgmt
 checking for library containing ps_line... -lpsl
 checking for library containing GMT_fill... -lgmtps
 checking whether gcc and cc understand -c and -o together... yes
 configure: creating ./config.status
 config.status: creating Makefile
 config.status: executing depfiles commands

出于安全的考虑，从网络上下载的文件的可执行权限都被去除了，所以需要chmod命令给configure文件赋予可执行权限。

configure需要给出GMT和netcdf的安装路径。

编译及修改
==========

直接编译会出现下面这样的情况：

.. code-block:: bash

 $ make
 gcc -DPACKAGE_NAME=\"pssac2\" -DPACKAGE_TARNAME=\"pssac2\" -DPACKAGE_VERSION=\"v2.1\" 
   -DPACKAGE_STRING=\"pssac2\ v2.1\" -DPACKAGE_BUGREPORT=\"savage@uri.edu\" -DPACKAGE_URL=\"\" 
   -I.  -I/usr/local/GMT-4.5.9/include  -I/usr/local/netcdf-3.6.3//nclude  -c pssac2.c
 在包含自 /usr/local/GMT-4.5.9/include/gmt.h：636 的文件中，
                  从 pssac2.c：25:
 /usr/local/GMT-4.5.9//include/gmt_version.h:5:1: 警告：“PACKAGE_VERSION”重定义
 <命令行>: 警告：这是先前定义的位置
 pssac2.c: 在函数‘main’中:
 pssac2.c:205: 错误：‘BOOLEAN’未声明(在此函数内第一次使用)
 pssac2.c:205: 错误：(即使在一个函数内多次出现，每个未声明的标识符在其
 pssac2.c:205: 错误：所在的函数内也只报告一次。)
 pssac2.c:205: 错误：expected ‘;’ before ‘negative_distances’
 pssac2.c:206: 错误：expected ‘;’ before ‘error’
 pssac2.c:207: 错误：expected ‘;’ before ‘norm’
 pssac2.c:208: 错误：expected ‘;’ before ‘reduce’
 pssac2.c:209: 错误：expected ‘;’ before ‘window_cut’
 pssac2.c:210: 错误：expected ‘;’ before ‘phase_paint’
 pssac2.c:211: 错误：expected ‘;’ before ‘neg_phase_paint’
 pssac2.c:212: 错误：expected ‘;’ before ‘rmean’
 pssac2.c:213: 错误：expected ‘;’ before ‘sin_scaling’
 pssac2.c:214: 错误：expected ‘;’ before ‘body_wave_scaling’
 pssac2.c:215: 错误：expected ‘;’ before ‘positioning’
 pssac2.c:216: 错误：expected ‘;’ before ‘vertical_trace’
 pssac2.c:217: 错误：expected ‘;’ before ‘plot_timescale’
 pssac2.c:218: 错误：expected ‘;’ before ‘option_M_specified’
 pssac2.c:219: 错误：expected ‘;’ before ‘option_L_specified’
 pssac2.c:220: 错误：expected ‘;’ before ‘clipping_on’
 pssac2.c:221: 错误：expected ‘;’ before ‘window_cut_use_headers_0’
 pssac2.c:222: 错误：expected ‘;’ before ‘window_cut_use_headers_1’
 pssac2.c:223: 错误：expected ‘;’ before ‘user_defined_shifts’
 pssac2.c:232: 错误：‘error’未声明(在此函数内第一次使用)
 pssac2.c:248: 错误：‘norm’未声明(在此函数内第一次使用)
 pssac2.c:253: 错误：‘body_wave_scaling’未声明(在此函数内第一次使用)
 pssac2.c:258: 错误：‘sin_scaling’未声明(在此函数内第一次使用)
 pssac2.c:264: 错误：‘option_M_specified’未声明(在此函数内第一次使用)
 pssac2.c:268: 错误：‘clipping_on’未声明(在此函数内第一次使用)
 pssac2.c:273: 错误：‘user_defined_shifts’未声明(在此函数内第一次使用)
 pssac2.c:281: 错误：‘phase_paint’未声明(在此函数内第一次使用)
 pssac2.c:286: 错误：‘neg_phase_paint’未声明(在此函数内第一次使用)
 pssac2.c:291: 错误：‘window_cut_use_headers_0’未声明(在此函数内第一次使用)
 pssac2.c:298: 错误：‘window_cut_use_headers_1’未声明(在此函数内第一次使用)
 pssac2.c:302: 错误：‘window_cut’未声明(在此函数内第一次使用)
 pssac2.c:313: 错误：‘reduce’未声明(在此函数内第一次使用)
 pssac2.c:332: 错误：‘negative_distances’未声明(在此函数内第一次使用)
 pssac2.c:350: 错误：‘plot_timescale’未声明(在此函数内第一次使用)
 pssac2.c:353: 错误：‘option_L_specified’未声明(在此函数内第一次使用)
 pssac2.c:357: 错误：‘rmean’未声明(在此函数内第一次使用)
 pssac2.c:363: 错误：‘vertical_trace’未声明(在此函数内第一次使用)
 pssac2.c:443: 错误：‘positioning’未声明(在此函数内第一次使用)
 make: *** [pssac2.o] 错误 1


警告信息为“PACKAGE_VERSION”重定义，这个警告出现的原因在于GMT和pssac2都同时使用了这个宏定义，所以出现了重复定义。实际上pssac2只是在编译的时候加了这个宏定义而已，代码中并没有使用，这个警告可以忽略。

错误信息是‘BOOLEAN’未声明，这个错误在《\ `pssac的安装 <{filename}/SeisWare/2013-08-04_install-pssac.rst>`_\ 》中有解释，只要在pssac2.c的前部加上如下语句即可：

::

 typedef GMT_LONG BOOLEAN;

修改完之后重新编译：

.. code-block:: bash

 $ make clean
 $ make

执行
====

::

 $ ./pssac2

如果在执行的过程中，出现了类似下面这样动态库找不到的情况::

 ./pssac: error while loading shared libraries: libnetcdf.so.4:
 cannot open shared object file: No such file or directory

可以参考《\ `pssac之安装 <{filename}/SeisWare/2013-08-04_install-pssac.rst>`_\ 》文末关于动态链接的讨论。

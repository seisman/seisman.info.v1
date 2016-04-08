gCAP和gCAP3D的安装
##################

:author: SeisMan
:date: 2014-06-13
:modified: 2016-04-07
:category: 地震学软件
:tags: 震源机制解
:slug: install-gcap

gCAP是Prof. Lupei Zhu发展的一种反演震源机制解的一种方法。目前该代码已经开源。

gCAP3D是在gCAP的基础上修改得到的，与gCAP的区别在于其可以使用三维格林函数。该代码也已经开源。

gCAP和gCAP3D之间没有本质区别，本文的介绍以gCAP为准，在最后会介绍安装方法上gCAP3D与gCAP的不同。

.. contents::

gCAP安装步骤
============

#. 下载gCAP源码： http://www.eas.slu.edu/People/LZhu/downloads/gcap1.0.tar

#. 解压::

      tar -xvf gcap1.0.tar

#. 清理垃圾文件

   软件包在发布的时候，没有做一些清理，遗留了一些没有用的临时文件，看起来很碍眼::

       rm junk.ps junk.out .gmtcommands

#. 下载辅助代码

   gCAP使用了Numerical Recipes（简称NR）中的一些函数，包括 ``matrix`` 、 ``free_matrix`` 、 ``free_convert_matrix`` 、 ``jacobi`` 、 ``eigsrt`` 。由于NR是非开源非免费的软件，所以gCAP并没有将NR相关的代码放在包里。

   网络上可以下载到NR的完整代码，这里仅给出gCAP所需的代码（注：此处存在版本问题！）。下载该压缩包，解压，并将解压后的源代码放到gCAP的目录中。

   gCAP_util下载：http://seisman.qiniudn.com/downloads/gcap_utils.tar.gz

#. 新的Makefile

   软件包自带的Makefile无法使用，因而对其进行了一些修改。修改幅度稍大，几乎算是重写了。

   新Makefile下载地址： http://seisman.qiniudn.com/downloads/Makefile.gCAP

   下载之后，将其重命名为 `Makefile` ，替换原目录中的同名文件，并根据自身情况修改 ``SACHOME`` 、 ``FC`` 、 ``CC`` 。

#. 编译::

      make

#. 修改环境变量

   要能够正确运行gcap，首先需要系统能够正确找到二进制文件 ``cap`` 、 ``cap_dir`` 、 ``mtdcmp`` 、 ``radpttn`` 。有两种方式可以选择：

   #. 直接将gcap的源码路径加入到PATH环境变量中，即在 ``~/.bashrc`` 中加入类似如下语句::

          export PATH=/path/to/gcap:${PATH}

   #. 直接将这几个二进制文件复制到 ``/usr/local/bin`` 或 ``${HOME}/bin`` 等已经在PATH环境变量中的目录内

#. 修改绝对路径

   ``cap.pl`` 中第15行与第19行包含了两个绝对路径，分别包含了绘图脚本 ``cap_plt.pl`` 和Green函数库 ``Glib`` 的路径，需要根据自身情况修改。

#. 运行

   直接执行::

      $ perl cap.pl

   就会出现软件的用法说明。

   软件包中自带了一个示例数据，因而可以通过如下命令来尝试运行::

      $ perl cap.pl -H0.2 -P0.3 -S2/5/0 -T35/70 -F -D2/1/0.5 -C0.05/0.3/0.02/0.1 -W1 -X10 -Mcus_15/5.0 20080418093700

   更多用法见软件的用法说明。

   需要注意：直接运行二进制文件 ``cap`` 时会出现段错误::

      $ ./cap
      [1]    12763 segmentation fault  ./cap

   看看源码 ``cap.c`` 即可知道为何会出现这个错误。只要记住，直接使用 ``cap.pl`` 即可，不要直接使用 ``cap``

#. 对 ``cap_plt.pl`` 的微小修改

   完全使用默认的脚本运行并绘图后，可能会发现整个图片都缩在图片的左下角的一个小区域内，与文章中的图片相比有较大差别。出现这个错误的主要原因是，Prof. Zhu的GMT默认使用了US单位制，脚本中所有未显式指定单位的值使用的都是inch，而其他人通常使用的都是SI单位制，会将这些未显式指定单位的值使用默认单位cm。

   解决办法是，在 ``cap_plt.pl`` 的第6行之后加上如下语句::

      system "gmtset MEASURE_UNIT inch";
      system "gmtset PAGE_ORIENTATION portrait";

   这两句的作用是设置默认单位为英寸，并设置纸张方向为portrait模式。

gCAP3D安装步骤
==============

gCAP3D的安装与gCAP的步骤几乎完全相同（部分文件名以及行号可能不一致，读者自行判断），区别列出如下：

- 下载地址： http://www.eas.slu.edu/People/LZhu/downloads/gCAP3D1.0.tar
- Makefile下载地址： http://seisman.qiniudn.com/downloads/Makefile.gCAP3D

修订历史
========

- 2014-06-13：初稿；
- 2016-03-12：加入了对gCAP3D的说明；
- 2016-04-07：微调文章结构，加入了对段错误的说明；

gCAP的安装
##########

:author: SeisMan
:date: 2014-06-13 09:00
:category: 地震学软件
:tags: 震源机制解
:slug: compile-gcap

gCAP是Prof. Lupei Zhu发展的一种反演震源机制解的一种方法。目前该代码已经开源。

#. 下载gCAP源码

   下载地址： http://www.eas.slu.edu/People/LZhu/downloads/gcap1.0.tar

#. 解压::

       tar -xvf gcap1.0.tar

#. 清除垃圾文件

   软件包在发布的时候，没有做一些清理，遗留了一些没有用的临时文件，看起来很碍眼。

   ::

       rm junk.ps junk.out .gmtcommands

#. 下载辅助代码

   gCAP使用了Numerical Recipes（简称NR）中的一些函数，包括matrix、free_matrix、free_convert_matrix、jacobi、eigsrt。由于NR是非开源非免费的软件，所以gCAP并没有将NR相关的代码放在包里。

   网络上可以下载到NR的完整代码，这里仅给出gCAP所需的代码。下载该压缩包，解压，并将解压后的源代码放到gCAP的目录中。

   gCAP_util下载：http://seisman.qiniudn.com/downloads/gcap_utils.tar.gz

#. 新的Makefile

   Makefile的修改幅度稍大，几乎算是重写了。下载之后，将其重命名为\ `Makefile`\ ，替换原目录中的同名文件。并根据自身情况修改SACHOME、FC、CC。

   Makefile下载地址： http://seisman.qiniudn.com/downloads/Makefile.gCAP

#. 编译::

       make

#. 要能够正确运行gcap，需要将编译生成的二进制文件\ ``cap``\ 、``cap_dir``\ 、\ ``mtdcmp``\ 、\ ``radpttn``\ 加入到PATH中，使得SHELL可以找到这几个命令。一种方法是把这几个二进制文件都复制到\ ``/usr/loca/bin``\ 或\ ``${HOME}/bin``\ 中，另一种做法是直接把gcap的源码路径加入到PATH环境变量中。

#. 其它

   `cap.pl`\ 中第15行与第19行包含了两个绝对路径，分别包含了绘图脚本\ `cap_plt.pl`\ 和Green函数库\ `Glib`\ 的路径，需要根据自身情况修改。

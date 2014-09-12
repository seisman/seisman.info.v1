GMT 5与4:如何兼得？
###################

:date: 2013-11-09 00:13
:author: SeisMan
:category: GMT
:tags: GMT技巧, GMT4, GMT5, 版本
:slug: multiple-versions-of-gmt

.. contents::

想要看具体的解决办法，可以直接跳转至\ `第4部分`_\ 。

2013年11月05日，GMT 4以及GMT 5同时发布了最新版本。GMT 4.5.11在经历了4系列的不断升级后，其稳定性值得信任。而5系列相对于4系列的变化非常之大，几乎重写或重整了全部代码，功能更丰富，bug“可能”会多一些。

一个是已经用习惯的老版本，一个是必须去适应的新版本，该怎么选择是个问题。官方声称GMT 4系列会继续维护更新直到GMT6出来，按照现在的速度，GMT4应该还会维护至少4-5年，即便4-5年之后GMT4不再更新，使用GMT4语法也不是问题。

对于新手来说，使用GMT5是必然的趋势也是最好的选择；对于老手来说，是该固守GMT4还是该学习GMT5呢？

下面分几个情况讨论，GMT4和GMT5的选择问题：

只安装GMT4
==========

这一类是保守派。毕竟GMT4用习惯了，以前的所有脚本都是用GMT4的语法写的，重新学习GMT5的成本太大。对于这一类，老老实实用GMT4就好，不必理会GMT5。

只安装GMT5
==========

这一类是改革派。又分为两种情况：

GMT5兼容GMT4语法
----------------

GMT5完全可以“兼容”GMT4的用法。兼容的好处在于可以帮助用户实现GMT4到GMT5的无痛过渡；不好的地方在于为了实现兼容，需要写更多的代码，或使用不合适的特性。

维基百科在\ `向下兼容`_\ 词条中举例：

    通常更新一个软件时，应该为向下兼容性做出一定的考虑，这往往能给用户带来方便并更好地留住用户。Microsoft
    特别强调维持软件的向下兼容性。为了实现此一目标，有时微软甚至不惜支持使用了非官方乃至误用的
    API 的软件。

    但情况并不总是这样，有时为了考虑向下兼容会带来一些累赘，尤其是进行过较多升级后。Python
    3.0 便是放弃向下兼容的一个例子。

前面说过，GMT5与GMT4的一个最大区别是，GMT5中只有一个唯一的可执行文件：\ ``gmt``\ 。GMT4中的所有命令在GMT5中都作为命令\ ``gmt``\ 的一个模块来调用。比如GMT4的\ ``pscoast``\ 命令在GMT5中应该使用\ ``gmt pscoast``\ 来调用。

为了兼容GMT4，GMT5除了在代码上下了很多功夫外，还有两个事情是一般用户值得注意的：

-  GMT5的默认参数文件位于GMT/share/conf/gmt.conf，其中GMT\_COMPATIBILITY=4代表当前的GMT5在源代码级别上兼容GMT4；
-  GMT5的bin目录下，提供了众多指向二进制文件gmt的符号链接。因而当用户输入命令\ ``pscoast``\ ，实际上是在执行\ ``gmt pscoast``\ ；这保证了在兼容模式下用GMT4语法写的脚本不必修改也可直接使用；

GMT5不兼容GMT4语法
------------------

对于新手来说，学习GMT4过时的语法反而是个累赘。这个时候最好不要让GMT5兼容GMT4语法。

将GMT/share/conf/gmt.conf中的

::

    GMT_COMPATIBILITY = 4

改成

::

    GMT_COMPATIBILITY = 5

即可。

同时安装GMT4和GMT5
==================

这个算是什么派呢？安装GMT5是为了顺应潮流，安装GMT4是为了其他程序的兼容性问题，比如地震学常用的pssac目前只支持GMT4，Prof. Zhu不知道有没有心思让pssac支持GMT5。两个版本同时存在，具体怎么搞？

GMT manual的第5章给出了两种解决办法，下面简要介绍，并重点给出我的第三种办法。

用gmtswitch切换GMT版本
----------------------

在安装完全部需要的GMT版本之后，运行\ ``gmtswitch``\ ，该命令会搜索当前系统中所有可用GMT版本，并将搜索结果保存在文件=/.gmtversions中，该文件每行给定一个GMT版本的绝对路径（如/usr/local/GMT-4.5.9），如果搜索结果有误（搜索结果错误的概率好像很大），自己可以手动修改该文件。然后用户需要在.bashrc中修改环境变量::

    export $PATH=${PATH}:$HOME/this_gmt/bin

注意，最好把原来GMT安装时加入的GMT路径删除。

下次运行gmtswitch时，如果没有提供参数，gmtswitch会列出所有可能的GMT版本，供用户选择::

 $ gmtswitch
 1. Version GMT-4.5.9
 2. Version GMT-4.5.11
 3. Version GMT-5.1.0

 Please choose a GMT version (1-3) [1]: 1

选择之后，该命令会在HOME下创建一个指向对应GMT版本根目录的符号链接this_gmt。

::

 $ ll this_gmt
 lrwxrwxrwx. 1 seisman seisman 14 11月 6 18:58 this_gmt -> /opt/GMT-4.5.9

当然，也可以使用下面的方式来切换版本::

 $ gmtswitch 4.5.11
 $ gmtswitch GMT-5.1.0

这个方法实际上是在模拟当前十分流行的多版本切换方法，比如plenv、pyenv、perlbrew都是用类似的方法切换不同版本。这样做的缺点在于需要明确知道自己要使用哪个版本，需要不断地进行切换。

Bash脚本切换版本
----------------

脚本如下:

.. code-block:: bash

 case $1 in
     4)
     function gmt() {
         module=$1; shift; /path/to/gmt4/bin/${module} "$@"
     }
     ;;
     5)
     function gmt() {
         /path/to/gmt5/bin/gmt "$@"
     }
     ;;
     *)
         return
     ;;
 esac
 export -f gmt

将该脚本命名为gmtfun，通过如下命令进行版本切换::

    $ . gmtfun 4 #切换到GMT4
    $ . gmtfun 5 #切换到GMT5

已经无力吐嘲这个版本切换的方法了。。。

个人比较推荐的版本共存方法
==========================

先说怎么做，再解释原因。

修改环境变量
------------

这里，同时添加两个GMT版本的路径，理论上这样做命令会出现多个版本的冲突。

.. code-block:: bash

 # GMT 4
 export GMT4_HOME=/opt/GMT-4.5.11
 export PATH=${GMT4_HOME}/bin:$PATH

 # GMT 5
 export GMT5_HOME=/opt/GMT-5.1.0
 export PATH=${GMT5_HOME}/bin:$PATH

删除GMT5的bin目录下的所有符号链接
---------------------------------

删除GMT5的符号链接以解决这些冲突::

    $ cd /opt/GMT-5.1.0/bin/
    # 建立临时目录，需要Root权限
    $ sudo mkdir temp
    #

GMT5的bin目录，gmt为可执行文件，gmt-config、gmtlogo、gmt_shell_functions.sh、 gmtswitch、isogmt为Bash脚本，其余都是指向可执行文件gmt的符号链接::

    $ sudo mv gmt gmt-config gmtlogo gmt_shell_functions.sh gmtswitch isogmt temp/
    $ sudo rm * # 删除除temp目录之外的全部符号链接
    rm: 无法删除"temp": 是一个目录
    # 将temp目录下的文件复制回bin下
    $ sudo mv temp/* .
    # 删除temp目录
    $ sudo rmdir temp/

修改GMT5为不兼容模式
--------------------

修改GMT5的文件share/gmt.conf，将其中的

::

    GMT_COMPATIBILITY = 4

改成

::

    GMT_COMPATIBILITY = 5

测试一下
--------

::

 $ psxy -
 psxy 4.5.11 [64-bit] - Plot lines, polygons, and symbols on maps
 
 usage: psxy <infiles> -J<params> -R<west>/<east>/<south>/<north>[r] [-A[m|p]] [-B<params>] [-C<cpt>] [-D<dx>/<dy>]
     [-E[x|y|X|Y][n][cap][/[+|-]<pen>]] [-G<fill>] [-H[i][<nrec>]] [-I<intens>] [-K] [-L] [-N] [-O] [-P]
     [-S[<symbol>][<size>]] [-T] [-U[<just>/<dx>/<dy>/]1] [-V] [-W[+|-][<pen>]] [-X[a|c|r]<x_shift>[u]] [-Y[a|c|r]<x_shift>[u]]
     [-c<ncopies>] [-:[i|o]] [-bi[s|S|d|D[<ncol>]|c[<var1>/...]]] [-f[i|o]<colinfo>] [-g[a]x|y|d|X|Y|D|[<col>]z[-|+]<gap>[unit]] [-m[<flag>]]
 
 $ gmt psxy -
 psxy(core) 5.1.0 (r12452) [64-bit] - Plot lines, polygons, and symbols on maps
 
 usage: psxy [<table>] -J<args> -R<west>/<east>/<south>/<north>[/<zmin>/<zmax>][r] [-A[m|p]]
     [-B<args>] [-C<cpt>] [-D<dx>/<dy>] [-E[x|y|X|Y][n][cap][/[+|-]<pen>]] [-G<fill>]
     [-Jz|Z<args>] [-I<intens>] [-K] [-L] [-N] [-O] [-P] [-S[<symbol>][<size>|+s<scale>[unit][/<origin>][l]]]
     [-T] [-U[<just>/<dx>/<dy>/]1] [-V[<level>]] [-W[+|-][<pen>]]
     [-X[a|c|r]<xshift>[<unit>]] [-Y[a|c|r]<yshift>[<unit>]] [-a<col>=<name>[,...]]
     [-bi[<ncol>][t][w][+L|B]] [-c<ncopies>] [-f[i|o]<info>]
     [-g[a]x|y|d|X|Y|D|[<col>]z[-|+]<gap>[<unit>]]
     [-h[i|o][<nrecs>][+c][+d][+r<remark>][+t<title>]] [-i<cols>[l][s<scale>][o<offset>][,...]]
     [-p[x|y|z]<azim>/<elev>[/<zlevel>][+w<lon0>/<lat0>[/<z0>][+v<x0>/<y0>]] [-s[<cols>][a|r]]
     [-t<transp>] [-:[i|o]]


补充说明
--------

删除符号链接的步骤比较麻烦，其实有更简单的办法，在编译GMT5之前，修改cmake/ConfigUser.cmake时，其中有一行::

 #set (GMT_INSTALL_MODULE_LINKS FALSE)

将该行前的“#”去掉，即设置GMT_INSTALL_MODULE_LINKS=FALSE，则在安装过程中就不会创建符号链接了。

原理解释
--------

主要利用的一点是“GMT5中只有gmt这一个可执行文件”。删除了GMT5下的所有符号链接并设置GMT5为不兼容模式后，所有类似\ ``psxy``\ 的命令都会被认为是GMT4的语法，这样以前的GMT4脚本都不需要做任何修改。所有类似\ ``gmt psxy``\ 的命令都会被认为是GMT5的语法，并严格要求必须是GMT5语法，这样有利用用户实现过渡。总之，这样做的好处就是，以前的GMT4脚本不用改，新写的脚本严格遵循GMT5语法。互不干涉，挺好的。

.. _第4部分: http://seisman.info/multiple-versions-of-gmt.html#i
.. _向下兼容: http://zh.wikipedia.org/wiki/%E5%90%91%E4%B8%8B%E5%85%BC%E5%AE%B9

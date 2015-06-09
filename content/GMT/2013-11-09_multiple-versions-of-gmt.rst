GMT4与GMT5双版本共存
####################

:date: 2013-11-09
:modified: 2015-06-09
:author: SeisMan
:category: GMT
:tags: GMT技巧, GMT4, GMT5, 版本
:slug: multiple-versions-of-gmt

.. contents::

随着GMT5的发布，GMT目前存在两个大版本：GMT4和GMT5。

GMT4会继续维护更新直到GMT6的发布，但只修订bug，不会再增加新功能。GMT5在GMT4的基础上重新整理了代码，并加入了不少新功能，语法也与GMT4不兼容，因而，GMT5相对来说bug可能会更多一些。

对于GMT新手来说，建议直接学习GMT5；对于GMT老手来说，可以继续使用GMT4，也可以开始逐渐使用GMT5。

一些旧脚本可能是用GMT4的命令与语法写的，在GMT5下直接运行可能会有问题。把旧脚本从GMT4语法改成GMT5语法比较麻烦且没有必要。因而最好的方式是，在系统中同时安装GMT4和GMT5，旧脚本使用GMT4的语法，新脚本使用GMT5的语法。

GMT官方提供了两种方法，可以实现多版本GMT的切换。但这两种方法，要么需要对绘图脚本做额外修改，要么需要在每次执行脚本前做额外操作，因而比较麻烦，不推荐使用。有兴趣的可以自己看官方文档。

下面介绍的方法可以在不需要额外修改的情况下，指定脚本使用GMT4还是GMT5。

安装GMT4和GMT5
==============

首先，当前系统需要安装GMT4和GMT5两个版本，然后，需要将两个版本的路径都添加到PATH中。

Linux用户可以向\ ``~/.bashrc``\ 中加入如下语句：

.. code-block:: bash

   # GMT 4
   export GMT4_HOME=/opt/GMT-4.5.11
   export PATH=${GMT4_HOME}/bin:$PATH

   # GMT 5
   export GMT5_HOME=/opt/GMT-5.1.0
   export PATH=${GMT5_HOME}/bin:$PATH

Windows用户类似，也要把两个版本的bin目录的路径加到PATH中。

GMT5的命令格式
==============

严格的说，GMT5中只有一个可执行文件：\ ``gmt``\ ，所有的命令都应以\ ``gmt``\ 开头，命令格式如下::

    gmt module -Axxx -Bxxx

GMT4中的所有命令在GMT5中都作为命令\ ``gmt``\ 的一个模块来调用。比如GMT4的\ ``pscoast``\ 命令在GMT5中应该使用\ ``gmt pscoast``\ 来调用。

在使用GMT5时，应严格按照\ ``gmt module``\ 这样的格式调用。这样，随便打开一个脚本，看到\ ``pscoast``\ 就知道是GMT4的语法，看到\ ``gmt pscoast``\ 就知道是GMT5语法。

删除软链接
==========

GMT5为了兼容GMT4的语法，在bin目录下建立了一堆指向\ ``gmt``\ 的软链接。进入GMT5的bin目录，其中gmt为可执行文件，gmt-config、gmtlogo、gmt_shell_functions.sh、 gmtswitch、isogmt为Bash脚本，其余都是指向可执行文件gmt的符号链接，把这些直接删除。

最简单的删除符号链接的办法是在安装GMT的时候就不生成这些符号链接。在编译GMT5之前，修改\ ``cmake/ConfigUser.cmake``\ 时，其中有一行::

    #set (GMT_INSTALL_MODULE_LINKS FALSE)

将该行前的“#”去掉，即设置GMT_INSTALL_MODULE_LINKS=FALSE，则在安装过程中就不会创建符号链接了。

如果安装的过程中创建了符号链接，可以使用如下命令将这些符号链接删除::

    $ cd /opt/GMT-5.1.0/bin/
    # 建立临时目录，需要Root权限
    $ sudo mkdir temp
    $ sudo mv gmt gmt-config gmtlogo gmt_shell_functions.sh gmtswitch isogmt temp/
    $ sudo rm * # 删除除temp目录之外的全部符号链接
    rm: 无法删除"temp": 是一个目录
    # 将temp目录下的文件复制回bin下
    $ sudo mv temp/* .
    # 删除temp目录
    $ sudo rmdir temp/

对于Windows用户，bin目录下会有很多文件，可以将该目录下的所有文件按照大小排序，所有大小为6 KB的都是“符号链接”，直接选中删除就好。

不兼容模式
==========

GMT5提供了兼容模式，可以部分兼容GMT4的语法，但推荐使用不兼容模式。原因如下：

#. 通常来说，兼容模式有更多的bug；
#. GMT5并不能完全兼容GMT4，因而有些用法在一个命令下是有效的，在另一个命令下却是无效的；
#. 使用兼容模式，可能到导致一个命令中既有GMT4语法也有GMT5语法，调试变得困难；
#. 使用不兼容模式，有助于用户熟悉GMT5语法；

要让GMT5不再兼容GMT4，只需要将\ ``GMT5/share/conf/gmt.conf``\ 中的::

    GMT_COMPATIBILITY = 4

改成::

    GMT_COMPATIBILITY = 5

测试一下
========

终端输入\ ``psxy -``\ 会看到命令的版本是GMT 4.5.xx。

终端输入\ ``gmt psxy -``\ 会看到命令版本为GMT 5.1.xx。

修订历史
========

- 2013-11-09：初稿；
- 2015-06-07：重整文章布局；

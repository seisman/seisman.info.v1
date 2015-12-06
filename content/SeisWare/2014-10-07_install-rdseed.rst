rdseed的安装
############

:date: 2014-10-07
:author: SeisMan
:category: 地震学软件
:tags: SAC, 格式转换
:slug: install-rdseed

rdseed用于将SEED格式的数据转换为SAC格式。

软件申请与下载
==============

申请地址： http://www.iris.edu/forms/rdseed_request.htm

简单填写申请信息后，无需等待即可直接下载，目前的最新版本为 ``rdseedv5.3.1.tar.gz`` 。

解压
====

::

    $ tar -zxvf rdseedv5.3.1.tar.gz
    $ cd rdseedv5.3.1

安装
====

rdseed提供了源代码，也提供了在不同平台下编译好的二进制文件。

- 如果是Linux 64位系统，则使用 ``rdseed.rh6.linux_64`` ；
- 如果是Mac 64位系统，则使用 ``rdseed.mac.x86_64`` ；
- 如果是运行在Sun/Sparc平台上的Solaris，则使用 ``rdseed.solaris.sparc_64`` ；
- 如果是运行在Sun/Intel平台上的Solaris，则使用 ``rdseed.solaris.x86_64`` ；
- 如果是在32位Windows 7下运行Cygwin，则使用 ``rdseed.windows.cygwin_32.exe`` ；

以64位Linux为例，应选择二进制文件 ``rdseed.rh6.linux_64`` ，直接执行::

    $ ./rdseed.rh6.linux_64

若输出如下::

    << IRIS SEED Reader, Release 5.3.1 >>
    Input  File (/dev/nrst0) or 'Quit' to Exit:

则表示该二进制在当前系统可以直接使用，将其重命名，并放置到PATH中即可::

    mv rdseed.rh6.linux_64 ~/bin/rdseed

若你的Linux系统为32位，或者其他一些特殊的原因，该二进制可能无法执行，则需要自己手动编译。

编译
====

若二进制文件可以直接使用，则可以忽略这一步。

#. ``make clean``
#. 修改Makefile

   Makefile中默认的CFLAGS为 ``-O -m64 -g`` ，若为32位系统，则应设置CFLAGS的值 ``-O -m32 -g`` 。

#. ``make``
#. 此时生成了可执行文件 ``rdseed`` ，将其复制到PATH中即可::

      mv rdseed ~/bin/

注意：5.3.1版本目前存在bug，使用较新的gcc编译器虽然可以编译通过，但无法正确解压SEED数据，因而不建议自己手动编译。

CentOS7下，gcc编译器的版本为4.8.3，编译通过，但无法解压数据。

如果一定需要手动编译的话，可以将Makefile以及各子目录下的makefile中的CC设置成icc，即使用Intel C编译器。

Jrdseed
=======

rdseed还有一个Java版本，即\ `Jrdseed <http://www.iris.edu/forms/jrdseed_request.htm>`_ 。

由于是Java写的，所以具有很好的跨平台特性，直接下载解压即可使用。

执行方法为::

    java -jar JrdseedVer0.10.1.jar

用法与rdseed类似。

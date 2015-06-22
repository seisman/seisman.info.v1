Linux下安装TeXLive 2015
########################

:date: 2013-07-11
:modified: 2015-06-19
:author: SeisMan
:category: 编程
:tags: 安装, LaTeX
:slug: install-texlive-under-linux

.. contents::

依赖包
======

- 安装过程中需要调用Perl的模块\ ``Digest::MD5``\ 来检测ISO文件的完整性；
- 升级过程中界面需要调用Perl的模块\ ``Tk``\ ；

CentOS::

    $ sudo yum install perl-Digest-MD5 perl-Tk

Ubuntu::

    $ sudo apt-get install libdigest-perl-md5-perl perl-tk

安装
====

下载
----

下载地址：

- 官方镜像: http://mirrors.ctan.org/systems/texlive/Images/texlive2015.iso
- USTC镜像： http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/texlive2015.iso

.. - 阿里云镜像： http://mirrors.aliyun.com/CTAN/systems/texlive/Images/texlive2015.iso

Linux下可以用wget、axel，windows下可以用迅雷，怎么快怎么来。

挂载ISO镜像
-----------

.. code-block:: bash

   $ su
   # mount -o loop texlive2015.iso  /mnt/
   # cd /mnt
   # ./install-tl

出现选项后，输入\ ``I``\ 直接安装（也可以更改选项）。不出意外的话，5分钟应该就OK了，然后退出root用户。

环境变量
--------

在当前用户的\ ``~/.bashrc``\ 中加入如下语句：

.. code-block:: bash

   # TeX Live 2015
   export MANPATH=${MANPATH}:/usr/local/texlive/2015/texmf-dist/doc/man
   export INFOPATH=${INFOPATH}:/usr/local/texlive/2015/texmf-dist/doc/info
   export PATH=${PATH}:/usr/local/texlive/2015/bin/x86_64-linux

卸载ISO镜像
-----------

.. code-block:: bash

   $ cd
   $ sudo umount /mnt/

更新TeXLive
===========

可以使用如下命令更新TeXLive宏包::

.. code-block:: bash

   $ su
   # 更新TeXLive包管理器tlmgr
   # tlmgr update --self
   # 更新TeXLive的全部包
   # tlmgr update --all

默认情况下，会自动搜索合适的镜像来更新，也可以使用\ ``--repository``\ 选项指定了要使用哪一个CTAN镜像。

比如USTC镜像::

   # tlmgr update --self --repository http://mirrors.ustc.edu.cn/CTAN/systems/texlive/tlnet/
   # tlmgr update --all --repository http://mirrors.ustc.edu.cn/CTAN/systems/texlive/tlnet/

比如阿里云镜像::

   # tlmgr update --self --repository http://mirrors.aliyun.com/CTAN/systems/texlive/tlnet/
   # tlmgr update --all --repository http://mirrors.aliyun.com/CTAN/systems/texlive/tlnet/

如果希望在图形界面下升级，可以使用如下命令调出tlmgr的中文图形界面：

.. code-block:: bash

   $ su
   # tlmgr --gui --gui-lang zh_CN

安装额外的字体
==============

TeXLive 2015在使用xeLaTeX处理中文时，有自己的默认字体。大多数Linux发行版下，都使用自带的Fandol字体。

如果想要使用Windows字体，可以将字体文件复制到\ ``~/.fonts``\ 目录下，并在tex源码中指定字体选项即可。

修订历史
========

- 2013-07-11：初稿；
- 2014-07-06：修改为TeXLive2014，并删除中文字体部分；
- 2015-03-08：新增“安装依赖”；
- 2015-03-15：使用命令行更新包；
- 2015-03-20：指定更新源以及GUI更新；
- 2015-06-13：更新至TeXLive 2015；

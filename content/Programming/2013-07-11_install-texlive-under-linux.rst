Linux下安装TeXLive 2014
########################

:date: 2013-07-11 09:00
:modified: 2015-03-08
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

    sudo yum install perl-Digest-MD5 perl-Tk

Ubuntu::

    sudo apt-get install libdigest-perl-md5-perl perl-tk

安装
====

下载
----

下载地址：

- USTC镜像： http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/texlive2014.iso
- 阿里云镜像： http://mirrors.aliyun.com/CTAN/systems/texlive/Images/texlive2014.iso

Linux下可以用wget、axel，windows下可以用迅雷，怎么快怎么来。

挂载ISO镜像
-----------

.. code-block:: bash

   $ su
   # mount -o loop texlive2014.iso  /mnt/
   # cd /mnt
   # ./install-tl

出现选项后，输入\ ``I``\ 直接安装（也可以更改选项）。不出意外的话，5分钟应该就OK了，然后退出root用户；

环境变量
--------

在当前用户的\ ``~/.bashrc``\ 中加入如下语句：

.. code-block:: bash

   # TeX Live 2014
   export MANPATH=${MANPATH}:/usr/local/texlive/2014/texmf-dist/doc/man
   export INFOPATH=${INFOPATH}:/usr/local/texlive/2014/texmf-dist/doc/info
   export PATH=${PATH}:/usr/local/texlive/2014/bin/x86_64-linux

卸载ISO镜像
-----------

.. code-block:: bash

   $ cd
   $ sudo umount /mnt/

更新TeXLive
===========

可以使用如下命令更新TeX包，\ ``--repository``\ 选项指定了要使用哪一个CTAN镜像，这里使用了阿里云的CTAN镜像，也可指定其他CTAN镜像。若不使用该选项，则默认使用官方CTAN镜像，速度较慢。

.. code-block:: bash

   $ su
   # 更新TeXLive包管理器tlmgr
   # tlmgr update --self --repository http://mirrors.aliyun.com/CTAN/systems/texlive/tlnet/
   # 更新TeXLive的全部包
   # tlmgr update --all --repository http://mirrors.aliyun.com/CTAN/systems/texlive/tlnet/

如果希望在图形界面下升级，可以使用如下命令调出tlmgr的中文图形界面：

.. code-block:: bash

   $ su
   # tlmgr --gui --gui-lang zh_CN

安装额外的字体
==============

将字体文件复制到\ ``~/.fonts``\ 目录下即可。

修订历史
========

- 2013-07-11：初稿；
- 2014-07-06：修改为TeXLive2014，并删除中文字体部分；
- 2015-03-08：新增“安装依赖”；
- 2015-03-15：使用命令行更新包；
- 2015-03-20：指定更新源以及GUI更新；

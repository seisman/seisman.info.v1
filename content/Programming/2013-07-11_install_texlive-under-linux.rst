Linux下安装TeXLive 2014
########################

:date: 2013-07-11 09:00
:modified: 2014-07-06
:author: SeisMan
:category: 编程
:tags: 安装, LaTeX
:slug: install-texlive-under-linux

.. contents::

安装
====

下载
----

下载地址：http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/texlive2014.iso

Linux下可以用wget、axel，windows下可以用迅雷，怎么快怎么来。

挂载
----

.. code-block:: bash

 $ su
 # mount -o loop texlive2014.iso  /mnt/
 # cd /mnt
 # ./install-tl

出现选项后，输入\ ``I``\ 直接安装（也可以更改选项）。不出意外的话，5分钟应该就OK了。

环境变量
--------

在\ ``~/.bashrc``\ 中加入如下语句：

.. code-block:: bash

 # TeX Live 2014
 export MANPATH=${MANPATH}:/usr/local/texlive/2014/texmf-dist/doc/man
 export INFOPATH=${INFOPATH}:/usr/local/texlive/2014/texmf-dist/doc/info
 export PATH=${PATH}:/usr/local/texlive/2014/bin/x86_64-linux

卸载
----

.. code-block:: bash

 $ cd /
 # sudo umount /mnt/

修订历史
========

- 2013-07-11：初稿；
- 2014-07-06：修改为TeXLive2014，并删除中文字体部分；  

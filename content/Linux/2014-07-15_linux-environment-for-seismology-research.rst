用CentOS 7打造合适的科研环境
############################

:author: SeisMan
:date: 2014-07-15 13:07
:modified: 2014-11-20
:category: Linux
:tags: CentOS, Perl, Python
:slug: linux-environment-for-seismology-research

这篇博文记录了我用CentOS 7搭建\ **地震学科研环境**\ 的过程，仅供未来重新装机时参考。

.. contents::

准备工作
========

- U盘一个，用于制作CentOS启动盘，U盘容量700M以上；
- 下载CentOS 7的\ `LiveCD ISO镜像文件 <http://mirrors.ustc.edu.cn/centos/7/isos/x86_64/CentOS-7.0-1406-x86_64-livecd.iso>`_
- 下载Windows下的启动盘制作工具\ `Universal USB installer <http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/>`_
- 利用Universal USB installer将CentOS的镜像文件写入U盘
- 插入U盘，重启电脑，进入BIOS选择从U盘启动，进入CentOS的LiveCD

注：

#. Linux下可以通过\ ``dd``\ 命令制作启动盘，但由于对原理不够了解，偶尔会导致制作失败，或制作成功后U盘容量有问题，还是用Windows下的Universal USB installer比较靠谱。

安装过程
========

CentOS 7的安装过程与其他Linux发行版的安装过程差不多，基本就是鼠标点点点，唯一比较麻烦的是分区。

分区
----

CentOS 7的分区似乎比较特别，自认为经验很丰富的我在第一次安装CentOS7时还是在分区上耽误了很多时间。后来找到比较合适的分区方法，如下：

- 先让安装程序帮忙分区，然后再根据需要增删分区以及修改细节；
- 默认的分区方案是使用LVM，一个好处在于“当机器有多块硬盘时，使得看上去只有一块”。
- 默认的文件系统为XFS；
- 分区细节

  - \ ``/boot``\ ：CentOS自动分配了100M；
  - \ ``/``\ ：30G
  - \ ``swap``\ ：64G，与物理内存大小一致
  - \ ``/opt``\ ：70G，用于安装第三方程序
  - \ ``/home``\ ：余下的全部空间

一些原则
--------

为了尽可能地避免因为瞎折腾而导致不得不重装系统，设定如下系统使用原则：

#. 仅使用CentOS官方源以及EPEL源，以避免一个软件包同时存在于多个源可能引起的版本冲突；
#. 个别源只包含一个或几个软件包，可以确保不会与官方源和EPEL源冲突，则允许使用该源；
#. 对于系统级别或较底层的软件包，只使用\ ``yum``\ 安装，绝不自己编译源代码；
#. 对于源中没有的软件包，一律编译并安装至\ ``/opt``\ 目录下；
#. 对于不需要编译，解压即可使用的软件包，一律编译并安装至\ ``/opt/``\ 目录下；
#. 对于编译后只生成一两个二进制文件的小型代码，一律将二进制文件复制到\ ``${HOME}/bin``\ 下；


对系统的一些修改
================

给当前用户root权限
------------------

CentOS默认没有给一般用户root权限，所以安装软件的时候经常需要\ ``su``\ 切换到root用户再进行操作。相对来说很麻烦。因而需要给当前用户root权限。

``su``\ 切换至root用户，用如下命令编辑\ ``sudo``\ 的配置文件::

    sudoedit /etc/sudoers

在其中找到语句\ ``root ALL=(ALL) ALL``\ ，在其下添加如下语句::

    seisman ALL=(ALL)       ALL

其中seisman为当前用户名。

修改主机名
----------

#. 修改\ ``/etc/hostname``\ ,将其中的\ ``localhost.localdomain``\ 改成\ ``saturn.geolab``\ 。（装机过程中若填入了主机名，则可能该文件不需要修改）
#. 修改\ ``/etc/hosts``\ 将其中的::

    127.0.0.1               localhost.localdomain localhost

   改成::

     127.0.0.1               saturn.geolab saturn

#. 重启网络::

    sudo service network restart

添加EPEL源
----------

EPEL即Extra Packages for Enterprise Linux 。CentOS为了保证系统的稳定性，只提供了少量的软件包，无法满足更多的需求。EPEL为CentOS提供了额外10000多个软件包，而且在不替换系统组件方面下了很多功夫，因而可以放心使用。

.. code-block:: bash

   wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm
   sudo rpm -ivh epel-release-7-2.noarch.rpm
   sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

除了EPEL之外，还有很多第三方软件源，如repoforge等，具体可以参考CentOS的\ `wiki页面 <http://wiki.centos.org/zh/AdditionalResources/Repositories>`_\ ，但由于不同软件源之间可能存在相同名称不同版本的软件，因而同时使用多个软件源时可能会造成冲突。根据上面所说原则，应只使用EPEL源。

安装yum-axelget
---------------

`yum-axelget`_\ 是EPEL提供的一个yum插件。使用该插件后用yum安装软件时可以并行下载，大大提高了软件的下载速度。

::

  sudo yum install yum-axelget

第一次全面升级
--------------

::

  sudo yum update

这个升级估计需要一段时间。。

开发环境的安装
==============

GCC系列
-------

::

    yum install gcc                         # C编译器
    yum install gcc-c++                 　  # C++编译器
    yum install gcc-gfortran                # Fortran编译器
    yum install compat-gcc-44               # 兼容gcc 4.4
    yum install compat-gcc-44-c++           # 兼容gcc-c++ 4.4
    yum install compat-gcc-44-gfortran      # 兼容gcc-fortran 4.4
    yum install compat-libf2c-34            # g77 3.4.x兼容库
    yum install gdb                         # 代码调试器

Intel系列
---------

Intel的大部分软件都是非开源且收费的，但同时部分软件也提供了Linux下的非商业免费版。比如icc、ifort、mkl数学库以及代码性能分析工具等。

Intel软件的申请以及安装参考《\ `Intel非商业免费开发工具 <{filename}/Programming/2013-09-10_intel-non-commercial-software.rst>`_\ 》。

Clang系列
---------

Clang是一个C、C++、Objective-C和Objective-C++编程语言的编译器前端，其采用了LLVM作为其后端。它的目标是提供一个GCC的替代品。包括Clang前端和Clang静态分析器两个部分。

::

    yum install clang               # clang编译器
    yum install clang-analyzer      # clang静态分析器

其中clang静态分析器可以用于分析代码中可能出现的bug。

Java环境
--------

::

    yum install java                        # java运行环境

Perl环境
--------

CentOS 7.0自带了perl 5.16.3，大概是两年前发布的版本，基本可以满足日常需求。

perl提供了cpan命令，用于安装模块。当需要安装某模块时应先用yum搜索源中是否有已打包好的模块，若有则直接安装，若无则再考虑用cpan安装模块。

::

    sudo yum install perl-Parallel-ForkManager  # 并行模块

若想要使用最新版本的perl，可以使用\ `plenv <{filename}/Programming/2013-11-03_perl-plenv.rst>`_\ 安装新版本的perl，并使用其提供的cpanm安装模块::

    cpanm install Parallel::ForkManager # 并行模块

Python环境
----------

CentOS 7.0自带Python 2.7.5，基本可以满足需求。与Perl类似，需要相关模块时优先使用yum源中提供的包，尽量避免使用pip安装模块。

由于Python2和Python3的不完全兼容，因而很多时候还需要安装一个Python3，这就需要管理多个Python版本。

- 安装\ `pyenv <{filename}/Programming/2013-10-04_python-pyenv.rst>`_\ 来管理多个Python版本
- 利用pyenv安装anaconda3（即Python 3.4）。
- 申请anaconda的学术版License，并更新anaconda。

其他软件
--------

::

    yum install cmake

驱动安装
========

安装显卡驱动
------------

Linux默认只使用开源的显卡驱动，就目前的情况来看，开源驱动的效果还是不错的，但跟官方的闭源驱动相比还是有一定差距的。最明显的区别是，在使用SAC的ppk功能放大波形时，使用开源驱动会出现延迟，而使用官方闭源则整个过程非常顺畅。

驱动的安装过程参考“\ `安装NVIDIA显卡驱动 <{filename}/Linux/2014-07-13_install-nvidia-drivers-under-linux.rst>`_\ ” 一文。需要注意的是，在安装显卡驱动之后，若更新了kernel，会出现无法进入kernel的情况，即每次更新kernel之后都需要重新安装显卡驱动，这点需要注意。

日常软件安装
============

办公软件
--------

办公软件可以选择大多数Linux发行版都有的LibreOffice::

    sudo yum install libreoffice

LibreOffice与Microsoft Office的兼容性不太好，操作界面与MS Office也有较大差异，让人不太习惯。

如果在Linux对于文档处理有更高一些的要求，可以尝试目前还处于测试版的WPS Office for Linux，安装过程参考\ `CentOS下安装WPS Office <{filename}/Linux/2014-10-01_wps-office-for-centos7.rst>`_\ 一文。WPS Office的兼容性以及界面都比LibreOffice要好很多，值得期待，当然还是不能做到完全兼容MS Office。

Google Chrome浏览器
-------------------

默认的浏览器是Firefox，还是更喜欢Chrome浏览器。

在\ ``/etc/yum.repo.d/``\ 目录下新建文件\ ``google-chrome.repo``\ ，向其中添加Google Chrome源，内容如下::

    [google-chrome]
    name=google-chrome
    baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
    enabled=1
    gpgcheck=1
    gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub

安装::

    sudo yum install google-chrome-stable

中文输入法
----------

刚安装的系统可能是没有中文输入法的，源中带的中文输入法应该是ibus，使用效果一般。fcitex是更好的选择，基于fcitx框架的搜狗输入法或许是更更好的选择。

参考\ `CentOS7安装搜狗输入法 <{filename}/Linux/2014-09-20_fcitx-for-centos-7.rst>`_\ 。

其他软件
--------

::

    yum install nfs-utils       # 挂载NFS文件系统所必须
    yum install p7zip           # 7z格式压缩和解压
    yum install git             # 源码版本控制
    yum install xclip           # 终端的文本复制工具
    yum install ImageMagick     # 其中的import和convert命令很有用
    yum install ntfs-3g         # 用于挂载NTFS格式的硬盘

使用zsh
--------

CentOS以及大多数Linux发行版的默认shell都是bash。zsh基本完全兼容于zsh，并提供了命令补全等方便的特性，且具有很高的可配置性。\ `oh my zsh <https://github.com/robbyrussell/oh-my-zsh>`_\ 是一群人一起维护的一套zsh配置文件。

安装zsh::

    sudo yum install zsh

安装oh my zsh::

    curl -L http://install.ohmyz.sh | sh

安装的过程中，做了如下几件事情：

- 下载\ ``oh my zsh``\ 到\ ``~/.oh-my-zsh``\
- 备份已有的zsh配置文件\ ``~/.zshrc``\ ，并复制新的\ ``.zshrc``\ 文件
- 将当前用户的默认shell由bash改成zsh

第三步中，会报错如下：\ ``chsh: "/usr/bin/zsh" is not listed in /etc/shells.``\ ，因而需要手动修改默认shell::

    chsh -s /bin/zsh

可以选择喜欢的主题，以及适当数量的插件：

#. git

   该插件为git的众多常用命令提供了更简单的别名，比如\ ``git status``\ 的别名是\ ``gst``\ ，大大简写了击键数。但该插件中\ ``git mergetool --no-prompt``\ 的别名是\ ``gmt``\ ，与GMT软件冲突，需要将该插件的目录git复制到custom/plugins下，然后删除其中的gmt别名；

#. 命令补全插件: pip, pyenv

#. sudo：按两下\ ``ESC``\ 即可在当前命令前加上\ ``sudo``\

#. yum：为常见的yum命令提供别名

autojump
--------

`autojump <https://github.com/joelthelion/autojump>`_\ 是一个用于快速切换目录的工具，

安装::

    git clone https://github.com/joelthelion/autojump.git
    cd autojump
    ./install.py
    rm autojump

然后，将如下语句加入到\ ``.zshrc``\ 中::

    [[ -s /home/seisman/.autojump/etc/profile.d/autojump.sh ]] && source /home/seisman/.autojump/etc/profile.d/autojump.sh
    autoload -U compinit && compinit -u

Mendeley
--------

文献管理软件，需要先安装\ ``qtwebkit``\ ，然后基本解压后即可使用。

HostTool
--------

修改Google、twitter、youtube、wikepedia、dropbox等的host文件。该软件用Python写成。

HostTool：https://hosts.huhamhire.com/

安装TeXLive 2014
----------------

参考\ `本文 <{filename}/Programming/2013-07-11_install-texlive-under-linux.rst>`_\ 。

地球物理相关
============

#. 安装SAC，参考《\ `SAC参考手册 <{filename}/SAC/2013-07-06_sac-manual.rst>`_\ 》中的相关章节。
#. \ `安装GMT4 <{filename}/GMT/2013-11-07_install-gmt4-under-linux.rst>`_
#. \ `安装GMT5 <{filename}/GMT/2013-11-06_install-gmt5-under-linux.rst>`_
#. \ `安装TauP <{filename}/SeisWare/2014-10-08_install-taup.rst>`_
#. 安装rdseed（seed格式转SAC格式）
#. 安装win32tools（Hinet自定义的win32格式转SAC格式）
#. 安装pssac

模块、插件等等
==============

Vim插件
-------

- bundle：vim插件管理
- powerline：状态栏增强
- nerdtree：文件浏览器
- vim-colors-solarized：solarized配色
- YouCompleteMe：代码补全
- delimitMate：括号补全
- indentLine：显示缩进对齐

修订历史
========

- 2014-07-15：初稿；
- 2014-09-05：EPEL已经发布正式版；修改了epel-release的下载链接；修订了import步骤的错误；
- 2014-09-20：将小小输入法改为搜狗输入法；
- 2014-11-20：使用zsh；

.. _yum-axelget: https://dl.fedoraproject.org/pub/epel/7/x86_64/repoview/yum-axelget.html

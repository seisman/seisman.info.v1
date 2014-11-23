用CentOS 7打造合适的科研环境
############################

:author: SeisMan
:date: 2014-07-15 13:07
:modified: 2014-11-23
:category: Linux
:tags: CentOS, Perl, Python
:slug: linux-environment-for-seismology-research

这篇博文记录了我用CentOS 7搭建\ **地震学科研环境**\ 的过程，供我个人在未来重装系统时参考。对于其他地震学科研人员，也许有借鉴意义。

需要注意：本文所有操作均在CentOS 7下完成，其他发行版或多或少与CentOS 7不同，因而仅供参考。

.. contents::

安装CentOS
==========

CentOS 7的安装与其他Linux发行版的安装差不多，个别地方稍有不同。

准备工作
--------

- U盘一个，用于制作CentOS启动盘，U盘容量700M以上；
- 下载CentOS 7的\ `LiveCD ISO镜像文件 <http://mirrors.ustc.edu.cn/centos/7/isos/x86_64/CentOS-7.0-1406-x86_64-livecd.iso>`_
- 下载Windows下的启动盘制作工具\ `Universal USB installer <http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/>`_
- 利用Universal USB installer将CentOS的镜像文件写入U盘
- 插入U盘，重启电脑，进入BIOS选择从U盘启动，进入CentOS的LiveCD

注：

#. Linux下可以通过\ ``dd``\ 命令制作启动盘，但由于对原理不够了解，偶尔会导致制作失败，或制作成功后U盘容量有问题，还是用Windows下的Universal USB installer比较靠谱。

分区
----

CentOS 7的分区似乎比较特别，自认为经验很丰富的我在第一次安装CentOS7时还是在分区上耽误了很多时间。后来找到比较合适的分区方法，如下：

- 先让安装程序帮忙分区，然后再根据需要增删分区以及修改细节；
- 默认的分区方案是使用LVM，一个好处在于“当机器有多块硬盘时，使得看上去只有一块”。
- 默认的文件系统为XFS；
- 分区细节

  - ``/boot``\ ：CentOS自动分配了100M；
  - ``/``\ ：30G
  - ``swap``\ ：64G，与物理内存大小一致
  - ``/opt``\ ：70G。个人习惯是将第三方软件都安装在\ ``/opt``\ 下，所以留了很大空间
  - ``/home``\ ：余下的全部空间

对系统的一些修改
================

一些原则
--------

为了搭建一个稳定的系统，尽量避免因为各种瞎折腾而导致的系统问题，订立了一些软件安装的原则。具体参见《\ `CentOS 7下的软件安装方法与策略 <{filename}/Linux/2014-10-23_how-to-install-softwares-under-centos-7.rst>`_\ 》。

给当前用户root权限
------------------

默认情况下，一般用户是没有root权限的，在安装软件时需要\ ``su``\ 。对于习惯了使用\ ``sudo``\ 的人来说，还是有些麻烦。所以，要先给当前用户root权限

假设用户名为seisman，要授予他root权限，则要修改配置文件\ ``/etc/sudoers``\ ::

    $ su
    # echo 'seisman ALL=(ALL) ALL' >> /etc/sudoers # 向配置文件中加入语句
    # tail -1 /etc/sudoers  # 检查一下是否正确
    seisman ALL=(ALL) ALL

其中seisman为当前用户名。

修改主机名
----------

#. 修改\ ``/etc/hostname``\ ,将其中的\ ``localhost.localdomain``\ 改成\ ``saturn.geolab``
#. 修改\ ``/etc/hosts``\ 将其中的::

    127.0.0.1               localhost.localdomain localhost

   改成::

     127.0.0.1               saturn.geolab saturn

#. 重启网络::

    sudo service network restart

添加第三方源
------------

CentOS有很多第三方源，比如EPEL、ATrpms、ELRepo、Nux Dextop、RepoForge等。根据上面提到的软件安装原则，为了尽可能保证系统的稳定性，此处大型第三方源只添加EPEL源。

EPEL即Extra Packages for Enterprise Linux，为CentOS提供了额外的10000多个软件包，而且在不替换系统组件方面下了很多功夫，因而可以放心使用。

.. code-block:: bash

   sudo yum install epel-release

执行完该命令后，在\ ``/etc/yum.repo.d``\ 目录下会多一个\ ``epel.repo``\ 文件。

安装yum-axelget
---------------

`yum-axelget`_\ 是EPEL提供的一个yum插件。使用该插件后用yum安装软件时可以并行下载，大大提高了软件的下载速度，减少了下载的等待时间::

    sudo yum install yum-axelget

第一次全面升级
--------------

在进一步操作之前，先把已经安装的软件包都升级到最新版::

    sudo yum update

要更新的软件包有些多，可能需要一段时间。不过有了yum-axelget插件，速度已经快了很多啦。

开发环境的安装
==============

GCC系列
-------

::

    sudo yum install gcc                     # C编译器
    sudo yum install gcc-c++                 # C++编译器
    sudo yum install gcc-gfortran            # Fortran编译器
    sudo yum install compat-gcc-44           # 兼容gcc 4.4
    sudo yum install compat-gcc-44-c++       # 兼容gcc-c++ 4.4
    sudo yum install compat-gcc-44-gfortran  # 兼容gcc-fortran 4.4
    sudo yum install compat-libf2c-34        # g77 3.4.x兼容库
    sudo yum install gdb                     # 代码调试器

软件开发辅助工具
----------------

::

    sudo yum install make    # make
    sudo yum install cmake   # Cmake
    sudo yum install git

Clang系列
---------

Clang可以认为是GCC的替代品，可以用于编译C、C++、Objective-C和Objective-C++。其提供了更友好的报错信息，在有些方面比GCC更友好，同时其提供了一个代码静态分析器，可以用于分析代码中可能出现的bug和内存溢出问题。

::

    sudo yum install clang             # clang编译器
    sudo yum install clang-analyzer    # clang静态分析器

Intel系列
---------

Intel的大部分软件都是非开源且收费的，但同时部分软件也提供了Linux下的非商业免费版。比如icc、ifort、mkl数学库以及代码性能分析工具等。

Intel软件的申请以及安装参考《\ `Intel非商业免费开发工具 <{filename}/Programming/2013-09-10_intel-non-commercial-software.rst>`_\ 》。

Java环境
--------

Java的一大特色在于跨平台，只有安装了Java运行环境，即可运行Java程序::

    yum install java                        # java运行环境

Perl环境
--------

CentOS 7.0自带了Perl 5.16.3（2013年03月11日发布），目前的最新版本为5.20.1（2014年09月14日发布）。

系统自带Perl
~~~~~~~~~~~~

系统自带Perl，就目前来看，版本不算老，基本够用。官方源和EPEL源中提供了1000多个模块，可以直接用yum安装::

    sudo yum install perl-Parallel-ForkManager  # 并行模块

若源中没有已打包好的模块，也可以使用perl自带的cpan来安装模块。

优先级：yum > cpan。

plenv管理新版本
~~~~~~~~~~~~~~~

若需要使用最新版本的perl，可以使用\ `plenv <{filename}/Programming/2013-11-03_perl-plenv.rst>`_\ 安装新版本的perl，并使用plenv提供的cpanm命令安装模块::

    cpanm install Parallel::ForkManager # 并行模块

Python环境
----------

CentOS 7.0自带Python 2.7.5，目前Python 2的最新版本为2.7.8，Python 3的最新版本为3.4.2。

系统自带Python
~~~~~~~~~~~~~~

系统自带的Python 2.7.5，基本已经够用，Python 2常用的模块在官方源或EPEL源中也有有编译好的包，因而直接通过yum安装即可::

    sudo yum install python-matplotlib  # 2D绘图库
    sudo yum install PyQt4  # Qt4的Python绑定
    sudo yum install numpy  # 数组操作库
    sudo yum install scipy  # 科学计算库
    sudo yum install python-requests  # 网页请求
    sudo yum install python-docopt  # 命令行参数分析器

pyenv管理Python3
~~~~~~~~~~~~~~~~

Python2与Python3之间是不完全兼容的，而我以Python3为主，所以需要安装一个Python3。

首先，安装\ `pyenv <{filename}/Programming/2013-10-04_python-pyenv.rst>`_\ 来管理多个Python版本，然后利用pyenv安装anaconda3（即Python 3.4）。anaconda自带了众多科学计算所需的包，免去了安装的麻烦，对于其他包，则可以利用Python自带的pip进行安装::

    pip install requests
    pip install docopt

驱动安装
========

显卡驱动
--------

Linux默认只使用开源的显卡驱动，就目前的情况来看，开源驱动的效果还是不错的，但跟官方的闭源驱动相比还是有一定差距。最明显的区别是，在使用SAC的ppk功能放大波形时，使用开源驱动会出现延迟，而使用官方闭源则整个过程非常顺畅。

驱动的安装过程参考“\ `安装NVIDIA显卡驱动 <{filename}/Linux/2014-07-13_install-nvidia-drivers-under-linux.rst>`_\ ” 一文。需要注意的是，在安装显卡驱动之后，若更新了kernel，会出现无法进入kernel的情况，即每次更新kernel之后都需要重新安装显卡驱动，这点需要注意。

NTFS驱动
--------

CentOS下默认无法挂载NTFS格式的硬盘。需安装nfts-3g即可实现即插即用::

    sudo yum install ntfs-3g

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

Flash插件
---------

::

    sudo rpm -ivh http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm
    sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux
    sudo yum install flash-plugin

中文输入法
----------

刚安装的系统可能是没有中文输入法的，源中带的中文输入法应该是ibus，使用效果一般。fcitx是更好的选择，基于fcitx框架的搜狗输入法或许是更更好的选择。

参考\ `CentOS7安装搜狗输入法 <{filename}/Linux/2014-09-20_fcitx-for-centos-7.rst>`_\ 。

其他软件
--------

::

    yum install nfs-utils       # 挂载NFS文件系统所必须
    yum install p7zip           # 7z格式压缩和解压
    yum install xclip           # 终端的文本复制工具
    yum install ImageMagick     # 其中的import和convert命令很有用

使用zsh
--------

CentOS以及大多数Linux发行版的默认shell都是bash。zsh基本完全兼容于bash，并提供了命令补全等方便的特性，且具有很高的可配置性。当然，对于一般用户而言，为了配置zsh而去学一堆东西有些过了。\ `oh my zsh <https://github.com/robbyrussell/oh-my-zsh>`_\ 是一群人一起维护的一套zsh配置文件。

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

根据\ `Linux下安装TeXLive <{filename}/Programming/2013-07-11_install-texlive-under-linux.rst>`_\ 一文，从ISO文件中安装TeXLive，安装完成后，更新模块::

    tlmgr update --all

地球物理相关
============

#. SAC

   参考《\ `SAC参考手册 <{filename}/SAC/2013-07-06_sac-manual.rst>`_\ 》中的相关章节。

#. GMT

   - `安装GMT4 <{filename}/GMT/2013-11-07_install-gmt4-under-linux.rst>`_
   - `安装GMT5 <{filename}/GMT/2013-11-06_install-gmt5-under-linux.rst>`_

#. `TauP <{filename}/SeisWare/2014-10-08_install-taup.rst>`_\ ：走时计算工具
#. `rdseed <{filename}/SeisWare/2014-10-07_install-rdseed.rst>`_\ ：SEED转SAC的工具
#. win32tools：Hinet自定义的win32格式转SAC格式
#. `pssac <{filename}/SeisWare/2013-08-04_install-pssac.rst>`_\ ：用GMT绘制SAC文件
#. `distaz <{filename}/SeisWare/2013-07-03_calculate-dist-az-baz.rst>`_\ ：根据两点经纬度计算震中距和方位角

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

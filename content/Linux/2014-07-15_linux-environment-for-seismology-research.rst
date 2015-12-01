用CentOS 7打造合适的科研环境
############################

:author: SeisMan
:date: 2014-07-15 13:07
:modified: 2015-09-18
:category: Linux
:tags: CentOS, Perl, Python
:slug: linux-environment-for-seismology-research

这篇博文记录了我用CentOS 7搭建\ **地震学科研环境**\ 的过程，供我个人在未来重装系统时参考。对于其他地震学科研人员，也许有借鉴意义。

阅读须知：

#. 本文适用于个人电脑，不适用于服务器；
#. **不推荐刚接触Linux的人使用CentOS发行版**\ ；
#. 本文尽量写的浅显易懂，但要求读者掌握Linux基础知识；
#. 本文所有操作均在CentOS 7下完成，其他发行版或多或少与CentOS 7不同，因而仅供参考；
#. 本文所安装的软件纯粹出于个人习惯及喜好，读者应自己判断，按需安装；

.. contents::

安装CentOS
==========

CentOS 7的安装与其他Linux发行版的安装差不多，个别地方稍有不同。

准备工作
--------

#. 准备材料

   - U盘：容量700M以上，用于制作U盘启动盘，因为在制作启动盘时会格式化U盘，所以U盘内不要包含重要资料
   - `CentOS 7.1 LiveCD ISO镜像文件 <http://mirrors.ustc.edu.cn/centos/7.1.1503/isos/x86_64/CentOS-7-x86_64-LiveCD-1503.iso>`_
   - `Universal USB installer <http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/>`_\ ：Windows下的U盘启动盘制作工具
   - 一个已安装Windows的电脑：用于制作U盘启动盘

#. 运行Universal USB installer并制作U盘启动盘
#. 将U盘插入计算机，重启，进入BIOS选择从U盘启动，即可进入CentOS的LiveCD
#. 进入LiveCD后，点击桌面的“Install to Hard Drive”即可安装

注：Linux下可以通过\ ``dd``\ 命令制作启动盘，但由于对原理不够了解，偶尔会导致制作失败，或制作成功后U盘容量有问题，还是用Windows下的Universal USB installer比较靠谱。

安装过程
--------

#. 选择安装过程中使用的语言，这里应\ **使用英语，不要使用汉语**\ 。若安装界面使用汉语，最终安装的系统中会出现两个比较麻烦的问题：

   #. 家目录下的系统文件夹，比如Downloads、Desktop等会以中文表示，这使得在命令行\ ``cd``\ 变得很麻烦；
   #. 终端中某些字符用英文字体，某些字符用中文字体，效果非常差，需要自己修改终端字体方可；

#. 选择区域和城市：Asia和Shanghai
#. 键盘使用English(US)而不是English(UK)
#. Hostname可以改也可以不改，我用\ ``saturn.geolab``\
#. 安装的目的地，选择要使用的硬盘，在“Other Storage Options”处选择“I will configure partioning”，即手动分区

分区
----

CentOS 7的分区似乎比较特别，自认为经验很丰富的我在第一次安装CentOS7时还是在分区上耽误了很多时间。后来找到比较合适的分区方法，如下：

- 点击“Click here to create them automatically”，即让安装程序帮忙分区
- 默认的分区方案是使用LVM，其好处在于“当机器有多块硬盘时，在使用的时候看上去只有一块”
- 默认的文件系统为XFS而不是以前常用的EXT4；
- 自动分区完成后，再根据自己的需求，手动修改分区细节

  - ``/boot``\ ：CentOS自动分配，一定不要乱改；
  - ``/``\ ：根目录，合理使用并及时清理的话15G就够了，不过建议30G以上；
  - ``swap``\ ：与物理内存大小一致即可
  - ``/opt``\ ：个人习惯是将第三方软件都安装在\ ``/opt``\ 下，所以分了70G
  - ``/home``\ ：余下的全部空间

- 点击“Begin to Install”开始安装

真正的安装
----------

#. 设置root密码
#. 创建一般用户
#. 等待安装完成
#. 安装完成，重启
#. 重启后，同意License即可

对系统的若干修改
================

若干原则
--------

为了搭建一个稳定的系统，尽量避免因为各种瞎折腾而导致的系统问题，特订立了一些软件安装的原则。具体参见《\ `CentOS 7下的软件安装方法与策略 <{filename}/Linux/2014-11-23_how-to-install-softwares-under-centos-7.rst>`_\ 》。

给一般账号root权限
------------------

默认情况下，一般账号是没有root权限的。为什么不直接用root账号，而是要给一般账号root权限呢？

- **日常工作中使用root账号，是非常糟糕且危险的习惯！无论是服务器还是个人电脑都是如此。**
- 安装软件时需要root权限，只能\ ``su``\ 切换到root账户再安装。对于习惯使用\ ``sudo``\ 的人来说，还是有些麻烦。

假设账户名为seisman，要授予他root权限，则要修改配置文件\ ``/etc/sudoers``\ ::

    $ su
    # echo 'seisman ALL=(ALL) ALL' >> /etc/sudoers # 向配置文件中加入语句
    # tail -1 /etc/sudoers  # 检查一下是否正确
    seisman ALL=(ALL) ALL

其中seisman为当前用户名。

添加第三方源
------------

CentOS由于很追求稳定性，所以官方源中自带的软件不多，因而需要一些第三方源，比如EPEL、ATrpms、ELRepo、Nux Dextop、RepoForge等。根据上面提到的软件安装原则，为了尽可能保证系统的稳定性，此处大型第三方源只添加EPEL源、Nux Dextop和ELRepo源。

EPEL
~~~~

`EPEL`_\ 即Extra Packages for Enterprise Linux，为CentOS提供了额外的10000多个软件包，而且在不替换系统组件方面下了很多功夫，因而可以放心使用。

.. code-block:: bash

   sudo yum install epel-release

执行完该命令后，在\ ``/etc/yum.repos.d``\ 目录下会多一个\ ``epel.repo``\ 文件。

Nux Dextop
~~~~~~~~~~

`Nux Dextop`_\ 中包含了一些与多媒体相关的软件包，作者尽量保证不覆盖base源。官方说明中说该源与EPEL兼容，实际上个别软件包存在冲突，但基本不会造成影响::

    sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

完成该命令后，在\ ``/etc/yum/repos.d``\ 目录下会多一个\ ``nux-dextop.repo``\ 文件。

ELRepo
~~~~~~

`ELRepo`\ 包含了一些硬件相关的驱动程序，比如显卡、声卡驱动::

    sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
    sudo rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm

完成该命令后，在\ ``/etc/yum.repos.d``\ 目录下会多一个\ ``elrepo.repo``\ 文件。

安装yum-axelget
---------------

`yum-axelget`_\ 是EPEL提供的一个yum插件。使用该插件后用yum安装软件时可以并行下载，大大提高了软件的下载速度，减少了下载的等待时间::

    sudo yum install yum-axelget

安装该插件的同时会安装另一个软件axel。axel是一个并行下载工具，在下载http、ftp等简单协议的文件时非常好用。

第一次全面更新
--------------

在进一步操作之前，先把已经安装的软件包都升级到最新版::

    sudo yum update

要更新的软件包有些多，可能需要一段时间。不过有了yum-axelget插件，速度已经快了很多啦。

重启
----

此处建议重启。

删除多余的kernel
----------------

在前面的\ ``yum update``\ 执行之后，可能会将kernel也一起更新，则在启动CentOS时启动项中会有很多项。

确认当前使用的kernel版本号::

    $ uname -r
    3.10.0-123.9.3.el7.x86_64

查找当前系统安装的所有kernel::

    $ rpm -qa | grep kernel | sort
    kernel-3.10.0-123.8.1.el7.x86_64
    kernel-3.10.0-123.9.2.el7.x86_64
    kernel-3.10.0-123.9.3.el7.x86_64
    kernel-devel-3.10.0-123.8.1.el7.x86_64
    kernel-devel-3.10.0-123.9.2.el7.x86_64
    kernel-devel-3.10.0-123.9.3.el7.x86_64
    kernel-headers-3.10.0-123.9.3.el7.x86_64
    kernel-tools-3.10.0-123.9.3.el7.x86_64
    kernel-tools-libs-3.10.0-123.9.3.el7.x86_64

可以看出有三个版本的kernel，123.8.1、123.9.2和123.9.3。除了最新的kernel外，建议多保留一个旧kernel，以免新kernel出现问题时可以通过旧kernel进入系统。因而此处删除123.8.1版本的kernel::

    sudo yum remove kernel-3.10.0-123.8.1.el7.x86_64
    sudo yum remove kernel-devel-3.10.0-123.8.1.el7.x86_64

基础开发环境
============

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

软件开发辅助工具
----------------

::

    sudo yum install make
    sudo yum install gdb     # 代码调试器
    sudo yum install cmake   # Cmake
    sudo yum install git     # 版本控制
    sudo yum install tig     # git的文本模式接口
    sudo yum install git-svn # git的svn插件

驱动程序
========

显卡驱动
--------

Linux默认只使用开源的显卡驱动，就目前的情况来看，开源驱动的效果还是不错的，但跟官方的闭源驱动相比还是有一定差距。最明显的区别是，在使用SAC的ppk功能放大波形时，使用开源驱动会出现延迟，而使用官方闭源则整个过程非常顺畅。

关于显卡驱动的安装，请参考\ `Linux下安装nvidia显卡驱动 <{filename}/Linux/2014-07-13_install-nvidia-drivers-under-linux.rst>`_\  一文中的“从ELRepo源中安装驱动”部分。

**注意**：目前的显卡驱动似乎有问题，安装后终端有时会出现屏幕闪烁、一屏文字上下重复跳动的情况，稍微有些影响用vim写代码。是否要安装显卡驱动自己决定。

NTFS驱动
--------

CentOS下默认无法挂载NTFS格式的硬盘。需安装nfts-3g即可实现即插即用::

    sudo yum install ntfs-3g

进阶开发环境
============

Java环境
--------

Java的一大特色在于跨平台，安装了Java运行环境，即可运行Java程序::

    sudo yum install java                        # java运行环境

Clang系列
---------

Clang可以认为是GCC的替代品，可以用于编译C、C++、Objective-C和Objective-C++。其提供了更友好的报错信息，在有些方面比GCC更友好，同时其提供了一个代码静态分析器，可以用于分析代码中可能出现的bug和内存溢出问题。

::

    sudo yum install clang             # clang编译器
    sudo yum install clang-analyzer    # clang静态分析器

Intel系列
---------

Intel的大部分软件都是非开源且收费的，但同时部分软件也提供了Linux下的非商业免费版。比如icc、mkl数学库以及代码性能分析工具等。

Intel软件的申请以及安装参考《\ `Intel非商业免费开发工具 <{filename}/Programming/2013-09-10_intel-non-commercial-software.rst>`_\ 》。

还有一点需要注意的是，Intel也提供了并行相关的几个命令，比如mpicc、mpirun。所以openmpi、mpich和intel三者，在并行时只能用其中一个。

并行计算
--------

并行可以用openmpi，也可以用mpich，二者应该是并列的。但是由于二者提供了几乎一样的命令，所以二者可以同时安装，但是不可以同时处于使用状态。

openmpi
~~~~~~~

安装openmpi::

    sudo yum install openmpi openmpi-devel

安装后，二进制文件位于\ ``/usr/lib64/openmpi/bin``\ 下，动态库文件位于\ ``/usr/lib64/openmpi/lib``\ 下，因而实际使用的话还需要额外的配置，在\ ``.bashrc``\ 中加入如下语句::

    export PATH=/usr/lib64/openmpi/bin/:${PATH}
    module load mpi/openmpi-x86_64

PS：要使用\ ``module``\ 命令需要先安装\ ``environment-modules``\ 包。

mpich
~~~~~

安装mpich::

    sudo yum install mpich mpich-devel

安装后，二进制文件位于\ ``/usr/lib64/mpich/bin``\ 下，动态库文件位于\ ``/usr/lib64/mpich/lib``\ 下，因而实际使用的话还需要额外的配置，在\ ``.bashrc``\ 中加入如下语句::

    export PATH=/usr/lib64/mpich/bin/:${PATH}
    module load mpi/mpich-x86_64

脚本语言环境
============

Perl
----

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

Python
------

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
    sudo yum install gdal-python    # gdal的Python绑定

pyenv管理Python3
~~~~~~~~~~~~~~~~

Python2与Python3之间是不完全兼容的，而我以Python3为主，所以需要安装一个Python3。

首先，安装\ `pyenv <{filename}/Programming/2013-10-04_python-pyenv.rst>`_\ 来管理多个Python版本，然后利用pyenv安装anaconda3（即Python 3.4）。anaconda自带了众多科学计算所需的包，免去了安装的麻烦，对于其他包，则可以利用Python自带的pip安装::

    pip install requests
    pip install docopt

编程相关软件
============

编辑器
------

#. vim
#. sublime text 3
#. Visual Studio Code

IDE
----

- Python IDE：\ `PyCharm Community Edition <https://www.jetbrains.com/pycharm/>`_

日常软件
========

Office套件
----------

LibreOffice
~~~~~~~~~~~

大多数Linux发行版都自带LibreOffice::

    sudo yum install libreoffice

LibreOffice与Microsoft Office的兼容性不太好，操作界面与MS Office也有较大差异，让人不太习惯。

WPS Office
~~~~~~~~~~

若在Linux下对于文档处理有更高一些的要求，可以尝试目前还处于测试版的WPS Office for Linux。WPS Office的兼容性以及界面都比LibreOffice要好很多，值得期待，当然还是不能做到完全兼容MS Office。

安装过程参考\ `CentOS下安装WPS Office <{filename}/Linux/2014-10-01_wps-office-for-centos7.rst>`_\ 一文。

PS/PDF阅读器
------------

系统自带的evince阅读器，可以打开PS和PDF文件，基本足够日常的使用了。

zathura
~~~~~~~

zathura可以查看PS、PDF、djvu格式的文件，可以作为evince的替代品::

    sudo yum install zathura zathura-plugins-all

ghostscript
~~~~~~~~~~~

::

    sudo yum install ghostscript

master-pdf-editor
~~~~~~~~~~~~~~~~~

官方网站: https://code-industry.net/free-pdf-editor/

::

    sudo yum localinstall http://get.code-industry.net/public/master-pdf-editor3-3.2.62-1.x86_64.rpm

TeX Live 2015
-------------

系统是自带了TeXLive，版本较老，还是安装最新版比较好。

参考\ `Linux下安装TeXLive <{filename}/Programming/2013-07-11_install-texlive-under-linux.rst>`_\ 一文。

Mendeley
--------

Mendeley是一个跨平台的文献管理软件，其内部自带了一个可以添加注释的PDF阅读器。

下载Generic Linux (64 bits) ：http://www.mendeley.com/download-mendeley-desktop

安装::

    tar -xvf mendeleydesktop-1.12.3-linux-x86_64.tar.bz2  # 解压
    sudo mv mendeleydesktop /opt  # 复制到/opt下
    cd /opt/mendeleydesktop/bin   # cd进去
    ./install-mendeley-link-handler.sh /opt/mendeleydesktop/bin/mendeleydesktop
    sudo yum install qtwebkit  # 安装依赖包

注销重新登陆，在Application->Education下即可看到mendeley的相关项目。不过是没有软件的图标的，强迫症不能忍，用下面的命令解决::

    cp /opt/mendeleydesktop/share/icons/hicolor/128x128/apps/mendeleydesktop.png ~/.local/share/icons/

Google Chrome浏览器
-------------------

默认的浏览器是Firefox，还是更喜欢Chrome浏览器。

Google官方源在国内可能无法正常访问，故而添加Fedora中文社区提供的镜像源::

    sudo wget http://repo.fdzh.org/chrome/google-chrome-mirrors.repo -P /etc/yum.repos.d/

安装::

    sudo yum install google-chrome-stable

.. 在\ ``/etc/yum.repos.d/``\ 目录下新建文件\ ``google-chrome.repo``\ ，向其中添加如下内容::
..    name=google-chrome
..    baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
..    enabled=1
..    gpgcheck=1
..    gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub

.. 导致安装失败或安装后无法正常更新，可以尝试修改\ ``gpgcheck=0``\ 再安装。(Thanks to 徐弥坚)
.. 这个私人镜像似乎已经不再更新了，故而删除。
.. 有人在国内服务器上做了Google官方源的镜像，若你相信该镜像是安全的，则可使用此国内镜像代替Google官方源，\ ``google-chrome.repo``\ 的内容改为::
..  name=google-chrome
..  #baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
..  #gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
..  mirrorlist=http://1dot75cm.tk/mirrorlist
..  gpgkey=http://1dot75cm.tk/src/linux_signing_key.pub
..  gpgcheck=1
..  enabled=1

Opera浏览器
-----------

也可以选择Opera浏览器。

下载地址：http://www.opera.com/download/guide/?os=linux

选择CentOS RPM package进行下载。下载完成后，执行::

    sudo yum localinstall opera-12.16-1860.x86_64.rpm

想要卸载的话，就执行::

    sudo yum remove opera

Flash插件
---------

Flash插件主要是看在线视频的时候要用。Google浏览器自带了Flash插件，所以这里安装的flash插件主要是为了firefox。

::

    sudo rpm -ivh http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm
    sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux
    sudo yum install flash-plugin

解压软件
--------

解压7z或zip格式需要p7zip，由EPEL提供::

    sudo yum install p7zip

解压rar格式需要unrar，该软件由Nux Dextop提供::

    sudo yum install unrar

FTP客户端
---------

FTP客户端，还是有界面的filezilla比较方便些。

::

    sudo yum install filezilla

效率类软件
==========

这一类工具能够在不同方面提高科研的效率，也提高了使用者的体验。

终端模拟器
----------

Gnome自带的终端模拟器是gnome-terminal。经常会需要开十几个终端，切换和管理起来比较麻烦。

terminator
~~~~~~~~~~

terminator有很多功能，我只用到了终端分割的功能。\ ``Ctrl+Shift+O``\ 对终端水平分隔，\ ``Ctrl+Shift+E``\ 对终端垂直分隔，\ ``Alt+上下左右``\ 可以在各子终端中切换。terminator由Nux Dextop提供::

    sudo yum install terminator

guake
~~~~~

有些时候需要临时执行一两个命令，但是又不想额外启动一个终端的情况下，guake是个不错的选择。

::

    sudo yum install guake

安装完成后，在Application->System Tools里找到guake Terminal即可启动。按下F12即可呼出guake，再次按下F12即可隐藏。也可在终端执行\ ``guake-prefs``\ 对gauke进行配置。

zsh与oh my zsh
--------------

Linux下有很多shell，比如最常见的bash，除此之外还有csh、ksh。zsh也是一个shell。

zsh的特点在于：

- 语法基本完全兼容于bash，一般用户完全体会不到其区别
- zsh提供命令补全特性，比bash的补全要更好用
- 可配置性强

完全不经配置的zsh已经很好用了，一般用户也没必要花时间研究配置。\ `oh my zsh <https://github.com/robbyrussell/oh-my-zsh>`_\ 是一群人一起维护的一套zsh配置文件。直接用这个配置文件，稍稍了解一点会有更好的体验。

安装zsh::

    sudo yum install zsh

安装oh my zsh::

    curl -L http://install.ohmyz.sh | sh

上面的命令，做了如下几件事情：

- 下载\ ``oh my zsh``\ 到\ ``~/.oh-my-zsh``\
- 备份已有的zsh配置文件\ ``~/.zshrc``\ ，并复制新的\ ``.zshrc``\ 文件
- 将当前用户的默认shell由bash改成zsh

第三步中，会报错如下：\ ``chsh: "/usr/bin/zsh" is not listed in /etc/shells.``\ ，需要手动修改默认shell::

    chsh -s /bin/zsh

chsh命令修改的是login shell，因而需要退出当前用户并重新登陆，以后用户的默认shell就从bash变成了zsh，所有的配置都不用写到\ ``.bashrc``\ 而要写到\ ``.zshrc``\ 中。

在\ ``.zshrc``\ 中可以选择喜欢的主题，以及适当数量的插件。下面列出我在用的插件:

#. git

   该插件为git的众多常用命令提供了更简单的别名，比如\ ``git status``\ 的别名是\ ``gst``\ ，大大减少了击键数。但该插件中\ ``git mergetool --no-prompt``\ 的别名是\ ``gmt``\ ，与GMT软件冲突，需要将该插件的目录git复制到custom/plugins下，然后删除其中的gmt别名；

#. 命令补全插件: pip, pyenv
#. sudo：按两下\ ``ESC``\ 即可在当前命令前加上\ ``sudo``\
#. yum：为常见的yum命令提供别名

autojump
--------

`autojump <https://github.com/joelthelion/autojump>`_\ 是一个非常智能的目录快速切换的工具。简单演示如下::

    $ pwd
    /home/seisman
    $ cd Desktop
    $ cd /opt
    $ cd /usr/local

    # 用j命令迅速从/usr/local跳转到与des匹配的目录，这里只有Desktop可以匹配
    $ j des
    $ pwd
    /home/seisman/Desktop

用法差不多就这样，具体看项目主页。

安装::

    sudo yum install autojump
    sudo yum install autojump-zsh

中文输入法
----------

刚安装的系统可能是没有中文输入法的，源中带的中文输入法应该是ibus，使用效果一般。fcitx是更好的选择，基于fcitx框架的搜狗输入法或许是更好的选择。

参考\ `CentOS7安装fcitx中文输入法 <{filename}/Linux/2014-09-20_fcitx-for-centos-7.rst>`_\ 。

HostTool
--------

科学上网几乎已经成为每个搞科研的人的必备技能。

科学上网的方式有很多，这里只说HostTool：https://hosts.huhamhire.com/

HostTool科学上网本质上就是用最新的host文件替代了系统自带的host文件。

下载解压后，进入目录，直接\ ``sudo python2 hoststool.py``\ 即可运行，具体的用法自己研究一下。

等宽字体
--------

编程要用等宽字体，这点是常识了。一款适合编程的等宽字体，至少要满足如下几个要求：

#. 易于区分“1”、“i”和“l”
#. 易于区分“0”、“o”和“O”
#. 易于区分中文下的左引号和右引号
#. 美观

目前选择的Source Code Pro。将解压后的字体文件放在\ ``~/.fonts``\ 目录下，并修改终端、gedit以及其他编辑器、IDE等的默认字体。

虚拟机
======

有时候可能需要在Windows下做一些操作，如果机器性能足够好的话，可以安装虚拟机。

VirtualBox虚拟机
----------------

VirtuabBox的安装::

    wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
    sudo mv virtualbox.repo /etc/yum.repos.d/
    sudo yum install VirtualBox-5.0

需要注意两点：

- 若机器性能不够，虚拟机的使用体验会非常差，所以不建议在老机器上使用；
- 更新kernel之后需要执行\ ``sudo /etc/init.d/vboxdrv setup``\ ；
- 在VirtualBox安装虚拟系统后，记得使用“设备”->“安装增强功能”，使用效果会更好；

gnome-boxes
-----------

gnome-boxes是GNOME3开发的一个虚拟机工具，使用体验不如VirtualBox::

    sudo yum install gnome-boxes

Wine
----

Wine是一个可以让Windows程序运行在Linux下的软件。类似虚拟机，但跟虚拟机又不太一样::

    sudo yum install wine


同步网盘
========

网盘根据功能大概可以分为两类：同步网盘和备份网盘。既然是同步网盘，Linux下的客户端必不可少。就目前已知的情况来看，CentOS7下能使用的同步网盘只有三个：Dropbox、MEGA和坚果云。

我主要用同步网盘将Linux机器上的PDF文献同步到iPad上。

Dropbox
-------

又是一个被墙的工具，熟练掌握科学上网技巧的人可以使用，一般人还是不要用了。

::

    wget https://www.dropbox.com/download?dl=packages/fedora/nautilus-dropbox-1.6.2-1.fedora.x86_64.rpm
    sudo rpm -i nautilus-dropbox-1.6.2-1.fedora.x86_64.rpm

MEGA
----

MEGA： https://mega.co.nz/

免费容量50G，作为同步盘来说基本是够用了。

::

    # 下载主程序
    wget https://mega.nz/linux/MEGAsync/CentOS_7/x86_64/megasync-CentOS_7.x86_64.rpm
    # 下载文件管理器扩展（可选）
    wget https://mega.nz/linux/MEGAsync/CentOS_7/x86_64/nautilus-megasync-CentOS_7.x86_64.rpm
    sudo yum localinstall megasync-CentOS_7.x86_64.rpm
    sudo yum localinstall nautilus-megasync-CentOS_7.x86_64.rpm

坚果云
------

国内的全平台同步网盘，不限空间，但限制每月上传流量1G，下载流量3G。

::

    # 坚果云依赖于notify-python
    sudo yum install notify-python
    # 下载
    wget https://jianguoyun.com/static/exe/installer/fedora/nautilus_nutstore_amd64.rpm
    sudo rpm -i nautilus_nutstore_amd64.rpm


工具软件
========

视频下载工具
------------

`you-get <https://github.com/soimort/you-get>`_\ 和\ `youtube-dl <https://github.com/rg3/youtube-dl>`\ 是两个用于从视频网站上下载视频文件的工具。其中，后者支持的网站更多，但前者对国内的视频网站支持更好。

::

    pip install you-get
    pip install youtube-dl
    # EPEL中提供了youtube-dl包，因而也可以使用yum安装。一般来说，pip安装的版本更新一些

PDF处理工具
-----------

`cpdf <http://community.coherentpdf.com/>`_\ 是一个跨平台的PDF处理工具，可以完成常见的PDF合并、切割、加密解密、书签、水印等功能。

下载已编译好的\ `二进制包 <https://github.com/coherentgraphics/cpdf-binaries/archive/master.zip>`_\ ，解压，并将与自己的平台对应的二进制文件复制到\ ``${HOME}/bin``\ 目录下即可使用。

BT软件
------

transmission是Linux下常用的Torrent下载软件::

    sudo yum install transmission

在“Application”->“Internet”->中可以启动transmission。

uGet
----

http://ugetdm.com/

uGet是Linux下的一个下载工具，支持HTTP、HTTPS、FTP、Torrent等，支持多连接，并可以监视剪贴板::

    sudo yum --enablerepo=epel-testing install uget aria2

截图软件shutter
---------------

GNOME自带了截图工具。\ ``PrtScn``\ 为截取整个屏幕；\ ``Alt+PrtScn``\ 为截取当前窗口；\ ``Shift+PrtScn``\ 为自定义截屏区域。

`shutter`_\ 是一个功能更强大的截图工具，支持不同的截图方式、图片格式，还支持图片的简单编辑与注释::

    sudo yum install shutter

可以通过\ `修改快捷键使shutter成为默认的截图工具 <http://shutter-project.org/faq-help/set-shutter-as-the-default-screenshot-tool/>`_\ 。

其他工具
--------

::

    sudo yum install nfs-utils     # 挂载NFS文件系统所必须
    sudo yum install xclip         # 终端的文本复制工具
    sudo yum install ImageMagick   # 其中的import和convert命令很有用
    sudo yum install dos2unix unix2dos  # Windows和Linux换行符互相转换
    sudo yum install meld          # 图形界面下的文件差异比较工具

娱乐
====

影音播放器
----------

Nux Dextop提供了mplayer和VLC，可以用于播放常见格式的音频和视频，二者选其一安装即可::

    sudo yum install mplayer
    sudo yum install vlc

游戏
----

::

    sudo yum install 2048-cli   # 2048命令行版

未完成
======

Google Earth
------------

理论上Google Earth应该可以跟Google Chrome用类似的方法来安装的，但是由于Google Earth的rpm包存在bug，导致无法通过上面的方法安装。

::

    $ cd -
    $ wget https://dl.google.com/dl/earth/client/current/google-earth-stable_current_x86_64.rpm
    $ rpm2cpio google-earth-stable_current_x86_64.rpm | cpio -div
    $ sudo cp -r opt/google/earth /opt/google/
    $ sudo cp etc/cron.daily/google-earth /etc/cron.daily/
    $ rm -rf usr opt etc
    $ sudo ln -s /opt/google/earth/free/googleearth /usr/bin/google-earth

安装完成后，启动后奔溃。。


参考
====

#. `ELRepo官方网站 <http://elrepo.org/tiki/tiki-index.php>`_
#. `ELRepo kmod-nvidia <http://elrepo.org/tiki/kmod-nvidia>`_
#. `CentOS Yum软件库样例 <http://wiki.centos.org/zh/AdditionalResources/Repositories/GoogleYumRepos>`_

修订历史
========

- 2014-07-15：初稿；
- 2014-09-05：EPEL已经发布正式版；修改了epel-release的下载链接；修订了import步骤的错误；
- 2014-09-20：将小小输入法改为搜狗输入法；
- 2014-11-20：使用zsh；
- 2014-11-24：加入了VirtualBox虚拟机；
- 2014-12-01：从ELRepo源中安装显卡驱动；
- 2014-12-02：新增Opera浏览器和unrar；
- 2014-12-27：新增pointdownload下载工具；google chrome采用非官方源镜像；
- 2014-12-28：修订unrar的rpm文件链接；
- 2015-01-03：新增同步网盘Dropbox和坚果云；删除pointdownload；
- 2015-01-05：autojump直接从epel中安装；新增youtube-dl、you-get和2048-cli；
- 2015-01-07：新增terminator和guake；
- 2015-01-27：新增cpdf；
- 2015-03-03：新增filezilla和transmission；
- 2015-03-26：安装过程中不应使用中文安装界面；
- 2015-05-11：新增MEGA同步网盘；
- 2015-05-16：新增gnome-boxes；
- 2015-06-26：新增zathura和ghostscript；
- 2015-07-14：新增Nux Dextop源，uGet、shutter；
- 2015-09-03：删除地球物理相关软件；
- 2015-09-18：删除显卡驱动安装的具体步骤，直接链接到相关博文；

.. _yum-axelget: https://dl.fedoraproject.org/pub/epel/7/x86_64/repoview/yum-axelget.html
.. _EPEL: https://fedoraproject.org/wiki/EPEL
.. _ELRepo: http://elrepo.org/tiki/tiki-index.php
.. _Nux Dextop: http://li.nux.ro/repos.html
.. _shutter: http://shutter-project.org/

Perl多版本共存之Perlbrew
#########################

:date: 2013-07-09 00:41
:author: SeisMan
:category: 编程
:tags: Perl, 安装, 版本
:slug: perlbrew-for-multiple-versions-of-perl

.. contents::

说明
====

推荐使用plenv作为Perl版本管理工具，不再推荐PerlBrew。plenv相比于PerlBrew更加简单也更有优势。关于plenv的介绍，参考博文《`Perl多版本共存之plenv <{filename}/Programming/2013-11-03_perl-plenv.rst>`_》。

缘由
====

目前在使用的Linux发行版是CentOS 6.4，自带的Perl版本为5.10.1，这一版本是2009年发行的，平时随便写点脚本还行，想用点高级的模块实现点高级功能的时候就开始掉链子了。不是这个模块找不到，就是那个模块依赖性搞不定，于是就有了安装新版Perl的想法。Google了一下，有人建议系统自带的Perl还是不要升级比较好，因为各种杂七杂八的东西都依赖于Perl，Perl的升级比glibc的升级还麻烦。试敲了一下\ ``yum remove perl``\ ，哗哗地列出了一堆东西，这些都是因为Perl被删除依赖性无法满足而无法使用的包。想到当初升级glibc导致系统崩溃的惨痛回忆，还是决定不动系统的Perl比较好。于是开始寻找Perl如何实现多版本共存。

Perlbrew
========

Perlbrew模块的作者是台湾人\ `劉康民`_\ 。该模块是以Ruby的RVM概念出发，也就是使用者可以使用Perlbrew將不同版本的Perl安裝在$HOME路径内，并且使用Perlbrew来切换不同版本的Perl。目前Perlbrew的最新版是0.64。（CentOS中epel库的版本是0.28。）

Perlbrew的几个优点：

- 不需要使用sudo来安裝CPAN模块
- 可以使用每个月不断释出的新的Perl
- 可尝试新的程式语言功能
- 可以不再被Vendor Perl限制(平台內建的Perl)
- 可在不同版本的Perl下测试模块
- 可整合至bash,zsh,csh环境变量

安装Perlbrew
============

按照默认的安装方法，会将Perlbrew以及新版本Perl安装在\ ``~/perl5``\ 下。Home是我家，干净整洁很重要，还是换了地方吧。

先声明环境变量\ ``PERLBREW_ROOT``\ ，然后切换到root（使用sudo是没用的），然后下载安装

.. code-block:: bash

 $ export PERLBREW_ROOT=/usr/local/perl5 # 这句直接敲入终端
 $ su # 切换root
 $ wget -O - http://install.perlbrew.pl | bash # 安装

向.bashrc中加入语句：

.. code-block:: bash

 # Perlbrew
 export PERLBREW_ROOT=/usr/local/perl5
 source /usr/local/perl5/etc/bashrc

重新开一个终端使得环境变量生效。由于安装到了/usr/local/下，后面的操作都需要root权限才能完成。

寻找合适的源
============

.. code-block:: bash

 $ perlbrew init
 $ perlbrew mirror
 Fetching mirror list
 [ 1] Africa, South Africa, Cape Town (mirror.ac.za)
 [ 2] Africa, South Africa, Cape Town (wa.co.za)
 [ 3] Africa, South Africa, Gauteng, Johannesburg (is.co.za)
 [ 4] Africa, South Africa, Western Cape, Parow (saix.net)
 [ 5] Africa, Tunisia, Tunis (cpan.mirror.tn)
 [ 6] Africa, Uganda, Mukono (ucu.ac.ug)
 [ 7] Asia, China, AnHui, Hefei (ustc.edu.cn)
 [ 8] Asia, China, Beijing (sohu.com)
 [ 9] Asia, China, Chaoyang, BeiJing (idc.btte.net)
 [ 10] Asia, China, Fujian, Xiamen (xmu.edu.cn)
 [ 11] Asia, China, Hong Kong SAR, Hong Kong (communilink.net)
 [ 12] Asia, China, Hong Kong SAR, Hong Kong (cuhk.edu.hk)
 [ 13] Asia, China, Hong Kong SAR, Hong Kong (devlib.org)
 [ 14] Asia, China, Hubei, Wuhan (hust.edu.cn)
 [ 15] Asia, China, Liaoning, Dalian (neusoft.edu.cn)
 [ 16] Asia, India, Maharashtra, Mumbai (indialinks.com)
 [ 17] Asia, Indonesia, Depok (kambing.ui.ac.id)
 [ 18] Asia, Indonesia, East Java, Surabaya (sby.datautama.net.id)
 [ 19] Asia, Indonesia, Jakarta (mwn-tlkm.archive.or.id)
 [ 20] Asia, Indonesia, Jakarta (pesat.net.id)
 Select a mirror by number or press enter to see the rest (248 more) [q to quit, m for manual entry] 7
 Selected Asia, China, AnHui, Hefei (ustc.edu.cn)(http://mirrors.ustc.edu.cn/CPAN/) as the mirror

查看可用的Perl版本
==================

.. code-block:: bash

 $ perlbrew available
 perl-5.18.1
 perl-5.16.3
 perl-5.14.4
 perl-5.12.5
 perl-5.10.1
 perl-5.8.9
 perl-5.6.2
 perl5.005_04
 perl5.004_05
 perl5.003_07

安装Perl 5.18.1
===============

.. code-block:: bash

 $ perlbrew install perl-5.18.1 --thread --multi --64int --64all
 Fetching perl 5.18.1 as /usr/local/perl5/dists/perl-5.18.1.tar.bz2
 Download http://www.cpan.org/src/5.0/perl-5.18.1.tar.bz2 to /usr/local/perl5/dists/perl-5.18.1.tar.bz2
 Installing /usr/local/perl5/build/perl-5.18.1 into /usr/local/perl5/perls/perl-5.18.1

 This could take a while. You can run the following command on another shell to track the status:

 tail -f /usr/local/perl5/build.perl-5.18.1.log

加入--thread等选项是为了使perl支持并行等特性，perlbrew提供了6种编译选项，根据系统的编译选项选择了如上4种。

某个版本的perlbrew会一直处于Fetching的阶段，无法下载所需版本的perl，目前在perlbrew的新版本中已经解决。

如果觉得perlbrew下载perl包的速度太慢，可以自己用其他方式下载相应的tar.bz2包，比如perl-5.18.1.tar.bz2，然后复制到/usr/local/perl5/dists/再尝试安装。

下面开始就没动静了，不过这个时候真的是在安装，不信的话可以看看build.perl-5.18.1.log，里面的内容一行一行往外冒啊。耐心的等待吧。

使用新版本
==========

.. code-block:: bash

 $ perlbrew switch perl-5.18.1
 $ perl -v
 This is perl 5, version 18, subversion 1 (v5.18.1) built for x86_64-linux

 Copyright 1987-2013, Larry Wall

 Perl may be copied only under the terms of either the Artistic License
 or the GNU General Public License, which may be found in the Perl 5 source kit.

 Complete documentation for Perl, including FAQ lists, should be found on
 this system using "man perl" or "perldoc perl". If you have access to
 the Internet, point your browser at http://www.perl.org/, the Perl Home Page.

也可以仅在当前shell中使用新版perl:

.. code-block:: bash
   
    perlbrew use perl-5.18.1

还可以回到系统自带的perl：

.. code-block:: bash

    perlbrew switch-off

安装cpanm
=========

安装好的新Perl在使用模块时依然是到系统默认的路径中去寻找的，这点可以通过\ ``perl -V``\ 显示的@INC看出来。可以通过安装cpanm来实现将模块安装到新目录中，并在新目录中寻找。

.. code-block:: bash

    perlbrew install-cpanm

重新开一个终端，再看\ ``perl -V``\ 的@INC已经不一样了。cpanm可以代替系统perl的cpan安装各种最新模块，默认安装在perlbrew的那个目录下，在没有权限的情况下会安装到HOME下。也可以通过local::lib模块指定安装路径，我觉得没必要。

参考
====

- Perlbrew主页：\ `http://perlbrew.pl/`_
- Perlbrew中文简介：\ `http://perlbrew.pl/Perlbrew-中文簡介.html`_
- 定制自己的多版本Perl环境：\ `http://www.php-oa.com/2011/02/25/perl-appperlbrew.html`_
- CPAN文档：\ `https://metacpan.org/module/App::perlbrew`_
- 命令文档：perlbrew help

修订历史
========

- 2013-07-09：初稿；
- 2013-08-17：perlbrew更新了，修正了其中下载过程中的一个bug；

.. _劉康民: http://gugod.org/
.. _`http://perlbrew.pl/`: http://perlbrew.pl/
.. _`http://perlbrew.pl/Perlbrew-中文簡介.html`: http://perlbrew.pl/Perlbrew-%E4%B8%AD%E6%96%87%E7%B0%A1%E4%BB%8B.html
.. _`http://www.php-oa.com/2011/02/25/perl-appperlbrew.html`: http://www.php-oa.com/2011/02/25/perl-appperlbrew.html
.. _`https://metacpan.org/module/App::perlbrew`: https://metacpan.org/module/App::perlbrew

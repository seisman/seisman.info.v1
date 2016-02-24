走时计算软件包
##############

:author: SeisMan
:date: 2014-03-29 15:42
:modified: 2016-02-24
:category: 地震学软件
:tags: 走时, TauP
:slug: travel-time-packages

地震波走时的计算是地震学的一个基本问题。下面列出几个目前已知的几个可以计算地震波走时的包。

#. IASPEI Travel Time Software - AK135 version

   网址：http://rses.anu.edu.au/seismology/soft/ttsoft.html

   这个版本的源码比较古老，可能是用Fortran77甚至更老的版本写的。曾经试图编译，发现很多语法编译器已经不再支持，改起来应该不困难，但是有些繁琐，不建议使用。且该版本只支持ak135模型。

#. iaspei-tau

   网址：https://seiscode.iris.washington.edu/projects/iaspei-tau

   原始的ttimes的修改版本，支持ak135和iasp91模型。

#. George Helffrich修改版

   网址：http://www1.gly.bris.ac.uk/~george/sac-bugs.html#ttimes

   Fortran版本，该版本是在ttimes的基础上修改得到，相比ttimes，加入了更多的速度模型，可以直接编译使用。

#. TauP Toolkit

   网址：http://www.seis.sc.edu/taup/

   Java版，具体良好的跨平台能力。包含图形界面和命令行工具，是目前来说最好用的走时计算工具，但是其还是有一些缺憾，最明显的一点是在命令行的输出对于脚本批量处理不算友好。

#. MatTauP

   网址：https://github.com/g2e/seizmo/tree/master/mattaup

   Matlab版，是seiszmo项目的一部分，底层貌似调用了Java版TauP的代码。

#. Cake

   网址： http://emolch.github.io/pyrocko/current/cake_doc.html

   Python版，Pyrocko项目的一部分，支持自定义模型，且可以处理更复杂的震相名。

这几个软件都是基于同一个原理，参考如下：

Buland, R. and C. H. Chapman (1983). The Computation of Seismic Travel Times, Bull. Seism. Soc. Am. 73(5),1271–1302.

修订历史
========

- 2014-03-29：初稿
- 2016-02-24：新增cake

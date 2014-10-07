地球物理相关软件
################

:date: 2014-02-20 10:20
:author: SeisMan
:category: 地球物理相关资源
:tags: 理论地震图, SAC, GMT4, GMT5
:slug: geo-software

.. contents::

通用数据处理
============

Seismic Analysis Code
---------------------

- 版本: 101.6a
- 语言: C
- 网址: http://www.iris.edu/ds/nodes/dmc/forms/sac/
- 说明: 地震学数据处理的常用软件。

Computer Programs in Seismology
-------------------------------

- 语言: Fortran
- 版本: 3.3.0
- 作者: Saint Louis University Earthquake Center
- 网址: http://www.eas.slu.edu/eqc/eqccps.html
- 博文: `CPS330 : Computer Programs in Seismology <{filename}/SeisWare/2014-01-01_cps330-intro.rst>`_

数据格式转换
============

rdseed
------

- 语言: C
- 版本: 5.3.1
- 网址: http://www.iris.edu/ds/nodes/dmc/forms/rdseed/
- 说明: SEED格式转换为SAC格式
- 博文: `rdseed的安装 <{filename}/SeisWare/2014-10-07_install-rdseed.rst>`_

win32tools
----------

- 语言: C
- 网址: http://www.hinet.bosai.go.jp/REGS/manual/dlDialogue.php?r=win32tools
- 说明: Hi-net提供的工具，用于将WIN32格式的数据转换为SAC格式
- 博文: `Hi-net win32tools <{filename}/SeisBasic/2014-09-07_hinet-win32tools.rst>`_

mseed2sac
---------

- 语言: C
- 网址: https://seiscode.iris.washington.edu/projects/mseed2sac
- 说明: 将miniSEED格式转换为SAC格式


绘图类
======

Generic Mapping Tools
---------------------

- 版本: 4.5.12 + 5.1.1
- 语言: C
- 网址: http://gmt.soest.hawaii.edu/
- 说明: 地球物理方向绘制地图必备神器。

pssac
-----

- 语言: C
- 网址: http://www.eas.slu.edu/People/LZhu/home.html
- 说明: 利用GMT强大的绘图库直接绘制地震图

JPlotResp
---------

- 语言: Java
- 网址: http://www.isti2.com/JPlotResp/
- 说明: 绘制RESP仪器响应文件的振幅相位响应谱。可以直接联网查询某台网某台站某个时间的仪器响应，也可以直接处理本地的RESP文件。
- 博文: `JPlotResp：绘制地震仪器响应 <{filename}/SeisWare/2013-07-19_jplotresp.rst>`_

Moment tensor Plotting and Decomposition
----------------------------------------

- 语言: Python
- 作者: Lars Krieger and Sebastian Heimann
- 网址: http://www.larskrieger.de/mopad/
- 说明: 地震矩分析和绘图软件，可以做地震矩的各种分解以及分析，绘制各种类型的震源球，可控性非常强，比GMT的psmeca命令要灵活，且可以与GMT联合使用。
- 博文: `MoPaD:地震矩绘制和分析工具 <{filename}/SeisWare/2013-08-27_mopad-moment-tensor-plotting-and-decomposition.rst>`_

GmtPy
-----

- 语言: Python
- 版本: 0.1
- 作者: Sebastian Heimann
- 网址: http://emolch.github.io/gmtpy/
- 博文: `GMT的Python接口:GmtPy <{filename}/SeisWare/2013-11-16_a-python-interface-to-gmt.rst>`_
- 说明: 该软件已经很久没有更新了，所以不建议使用。GMT5有计划实现Python接口，值得期待一下。


通用辅助类
==========

distaz
------

- 语言: C、Fortran、Java、Python
- 网址: http://www.seis.sc.edu/software/distaz/
- 说明: 给定震中和台站经纬度，计算震中距、方位角和反方位角的经典代码。
- 博文: `震中距、方位角和反方位角的计算 <{filename}/SeisWare/2013-07-03_calculate-dist-az-baz.rst>`_

TauP
----

- 语言: Java
- 版本: 2.1.2
- 网址: http://www.seis.sc.edu/taup/
- 说明: 强大的走时计算器，不过其功能可不仅仅只是计算走时这么简单。射线参数、射线路径、反射点、投射点都可以计算，支持自定义速度模型、支持不常见的震相。
- 博文: `走时计算软件TauP <{filename}/SeisWare/2013-07-10_use-taup-to-calculate-travel-time.rst>`_


理论地震图
==========

fk
--

- 语言: C、Fortran、Perl
- 作者: Lupei Zhu
- 版本: 3.2
- 网址: http://www.eas.slu.edu/People/LZhu/home.html
- 说明: 计算水平分层各向同性介质下理论地震图位移静态解和动态解的常用代码之一。

SHaxi
-----

- 语言: Fortran
- 作者: Gunnar Jahnke, Mike Thorne, Heiner Ige
- 版本: 1.0
- 网址: http://svn.geophysik.uni-muenchen.de/trac/shaxi
- 说明: 用有限差分方法计算全球尺度高精度SH波场。

Mineos
------

- 语言: C + Fortran
- 版本: 1.0.1
- 网址: https://github.com/geodynamics/mineos
- 说明: Normal modes方法计算球对称非旋转地球模型下的合成地震图


特定功能类
==========

hk
--

- 语言: C
- 版本: 1.3
- 作者: Lupei Zhu
- 网址: http://www.eas.slu.edu/People/LZhu/home.html
- 说明: 用于接收函数研究的代码。


Interactive Receiver Functions Forward Modeller
-----------------------------------------------

- 语言: Java + Fortran
- 版本: 1.1
- 作者: Hrvoje Tkalčić
- 网址: http://rses.anu.edu.au/~hrvoje/IRFFMv1.1.html
- 说明: 一个有界面的接收函数包。程序包中包含了respknt和iterdecon两个已编译的二进制文件而没有给出源代码，因而程序的通用性成为一个大问题。在帮助文档方面，给出了界面的使用说明，没有给出文件格式的说明，对用户来说不够友好。还有就是看完manual之后发现没有理解这个软件是如何工作的。

CCP
---

- 语言: C
- 版本: 1.0
- 作者: Lupei Zhu
- 网址: http://www.eas.slu.edu/People/LZhu/home.html
- 说明: 共转换点地震数据叠加，用于接收函数研究。
- 博文: `CCP1.0编译 <{filename}/SeisWare/2013-11-29_compilation-of-ccp.rst>`_

Generalized Cut-and-Paste
-------------------------

- 语言: C + Fortran + Perl
- 版本: 1.0
- 作者: Lupei Zhu
- 网址: http://www.eas.slu.edu/People/LZhu/home.html
- 说明: 用于反演震源机制解的CAP方法，虽然是1.0版，实际上N年前国内就已经有很多人在使用这个代码了。

SAC保存图像小结
###############

:date: 2013-08-13 16:30
:author: SeisMan
:category: SAC
:tags: SAC技巧, 图像
:slug: sac-save-image

.. contents::

数据的处理很重要，数据的可视化更重要，数据可视化之后总会想把图保存起来，这里小结一下SAC中保存图像的方法。

窗口绘图并截图
==============

SAC中的绘图窗口基于XWindows。XWindows大概是Linux下非常常见的视窗系统。在SAC中可以通过plot，plot1，plot2，plotpk等命令实现SAC数据的绘制以及各种交互动作（主要就是标记震相）。最简单粗暴的方法大概就是截屏了。截屏的话gnome下有个screenshot，可以截取整个屏幕；推荐安装ImageMagick，其中的import命令可以通过鼠标拖曳一个区域进行截图，貌似支持保存为很多种格式。

生成SGF文件再转换
=================

SGF是SAC Graphic File的简称，这是SAC自己设计的图像格式，里面包含了SAC图像的基本信息。在SAC中打开SGF设备->绘图产生SGF文件->退出SAC->利用sgftops将sgf文件转换为ps文件->ps2pdf转换为pdf文件。

.. code-block:: bash

 [seisman@info ~]$ sac
 SEISMIC ANALYSIS CODE [02/01/2012 (Version 101.5c)]
 Copyright 1995 Regents of the University of California

 SAC> fg seis
 SAC> bd sgf
 SAC> p
 SAC> q
 [seisman@info ~]$ sgftops f001.sgf f001.ps 2 si
 First translates (x and y), then rotates, then scales:
 [Default] landscape: 8 0 90 1 to prompts
 Sample portrait: 0.5 0.5 0 0.75

 x translation : 0.5
 y translation : 0.5
 rotation angle: 0
 scale........ : 0.75
 [seisman@info ~]$

SAVEIMG直接保存图形文件
=======================

SAC 101.5之后的版本加入了新功能，可以直接保存图形文件，这是个神器～目前支持的格式为ps、pdf、png、xpm。ps和pdf是矢量格式，因而是绘图的首选格式，png和xpm是位图图形格式，绘图精度较差，因而不建议使用。考虑到图像不清晰，且png和xpm需要格外的库文件，在SAC 101.6发布的二进制文件中不再支持png和xpm。

.. code-block:: bash
 [seisman@info ~]$ sac
 SEISMIC ANALYSIS CODE [02/01/2012 (Version 101.5c)]
 Copyright 1995 Regents of the University of California

 SAC> fg seis
 SAC> p
 SAC> saveimg foo.ps
 save file foo.ps [PS]
 SAC> q

pssac绘制ps文件
===============

pssac利用GMT的ps库直接绘制SAC文件，pssac的具体细节可以站内搜索"pssac"。

小结
====

-  Xwindows窗口最快最省事，截图的话平时看看还行，见不了大世面；
-  sgf转换有点麻烦，生成的ps文件线条看上去有点模糊，偶尔会出现bug，ps文件上多出了额外的线条；
-  saveimg是后起之秀，建议使用；
-  pssac功能强大，在需要设计复杂图形时有用，当然用起来需要花点时间学。

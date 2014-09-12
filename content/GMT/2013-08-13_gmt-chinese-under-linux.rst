Linux下的GMT中文显示
####################

:date: 2013-08-13 16:23
:modified: 2013-08-17
:author: SeisMan
:category: GMT
:tags: GMT技巧, 中文, GMT4, GMT5
:slug: gmt-chinese-under-linux
:summary: 讨论了如何让GMT支持中文。

.. contents::

这两天一直在听人讨论这个事情，原来也根据网上的文章试过，无果。这次细细看了一下，算是基本解决了这个问题。想要理解整个问题，需要对字体有更多的了解，比如字体映射、字体嵌入等等，这些有点偏离的太远了。所以这篇文章以这样的方式写：首先简单粗暴的修改配置文件使得问题得以解决，然后再尽量对其中涉及的一些文件格式以及原理进行说明。

我的系统配置
============

-  操作系统：CentOS 6.4 Final
-  ghostscript：8.70
-  GMT：4.5.9

确定相关文件路径
================

-  ghostscript为系统默认安装，其相关文件路径为/usr/share/ghostscript，该目录下有两个文件夹conf.d和8.70。
-  系统自带字体文件位于/usr/share/fonts
-  GMT中与字体有关的配置文件为/usr/local/GMT-4.5.9/share/pslib/PS_font_info.d

修改ghostscript配置文件
=======================================

打开conf.d下的文件cidfmap.zh_CN，可以看到其默认的文件内容为（如果没有看到cidfmap.zh_CN，那是因为没有安装ghostscript中文配置包，在我的系统上包名为cjkuni-fonts-ghostscript.noarch）

::

    /BousungEG-Light-GB     << /FileType /TrueType /Path (/usr/share/fonts/cjkuni/uming.ttc) /CSI [(GB1) 4] >> ;
    /GBZenKai-Medium        << /FileType /TrueType /Path (/usr/share/fonts/cjkuni/ukai.ttc) /CSI [(GB1) 4] >> ;
    /MSungGBK-Light         /BousungEG-Light-GB ;
    /Adobe-GB1              /BousungEG-Light-GB ;

文件可以认为是分为两列，/BousungEG-Light-GB是字体名，这个可以任意取，括号<<>>内包含的内容指定了这个字体名所对应的字体文件，这个例子中字体为/usr/share/fonts/cjkuni/uming.ttc；后面两行的大致意思是将/MSungGBK-Light和/Adobe-GB1都定义成与/BousungEG-Light-GB相同的字体。

查看一下字体文件夹/usr/share/fonts，发现cjkuni/uming.ttc和cjkuni/ukai.ttc在系统中的正确路径分别是cjkuni-ukai/ukai.ttc和cjkuni-uming/uming.ttc。将cidfmap.zh\_CN的前两行根据自己的系统中字体路径修改一下就好。（这两个中文字体可以通过安装cjkuni-uming-fonts和cjkuni-ukai-fonts获得）

如果路径修改正确，理论上这个时候ps文件已经可以使用/BousungEG-Light-G和/GBZenKai-Medium这两个中文字体了。

修改GMT字体配置文件
===================

打开/usr/local/GMT-4.5.9/share/pslib/PS\_font\_info.d，向其中添加如下语句：

::

    BousungEG-Light-GB-UniGB-UTF8-H     0.700           1   
    GBZenKai-Medium-UniGB-UTF8-H       0.700           1

第一列为字体名，第二列为字母A的高度，第三列与编码有关。其中第一列的字体名分为两部分，前面半部分BousungEG-Light-G是第二步中看到的字体名，后半部分是与字体有关的映射。

重建字体缓存
============

可以通过fc-list命令查看当前系统下的中文字体：

::

    $ fc-list :lang=zh
    AR PL UMing TW:style=Light
    AR PL UMing HK:style=Light
    AR PL UMing CN:style=Light
    AR PL UKai TW MBE:style=Book
    AR PL UKai CN:style=Book
    AR PL UKai HK:style=Book
    AR PL UKai TW:style=Book
    文泉驿正黑,文泉驛正黑,WenQuanYi Zen Hei:style=Regular
    文泉驿等宽正黑,文泉驛等寬正黑,WenQuanYi Zen Hei Mono:style=Regular
    AR PL UMing TW MBE:style=Light
    文泉驿点阵正黑,文泉驛點陣正黑,WenQuanYi Zen Hei Sharp:style=Regular

其中UMing就是前面所说的cjkuni-uming，UKai对应前面说的cjkuni-ukai。

如果UMing和UKai不是以前就安装好的，而是在前几步里刚刚安装cjkuni-uming-fonts和cjkuni-ukai-fonts，这个时候fc-list的结果可能如下：

::

    $ fc-list :lang=zh
    文泉驿正黑,文泉驛正黑,WenQuanYi Zen Hei:style=Regular
    文泉驿等宽正黑,文泉驛等寬正黑,WenQuanYi Zen Hei Mono:style=Regular
    文泉驿点阵正黑,文泉驛點陣正黑,WenQuanYi Zen Hei Sharp:style=Regular

这个时候需要重建字体缓存，即可，否则系统无法找到该字体。

::

    $ fc-cache

查看GMT当前支持的字体
=====================

::

    $ pstext -L 
    Font #  Font Name
    ------------------------------------
    0   Helvetica
    1   Helvetica-Bold
    ...    ......
    32  Palatino-BoldItalic
    33  ZapfChancery-MediumItalic
    34  ZapfDingbats
    35  BousungEG-Light-GB-UniGB-UTF8-H
    36  GBZenKai-Medium-UniGB-UTF8-H

0-34为GMT默认支持的西文字体，35和36为新添加的中文字体。

GMT中文测试
===========

.. code-block:: bash

 #!/bin/bash
 gmtset HEADER_FONT 35

 pstext -R0/7/0/7 -JX6i/6i -B1/1:."GMT显示汉字": -P > cn.ps <<EOF
 1.5 5 40 0 35 LM GMT，宋体测试
 1.5 4 35 0 36 LM GMT，楷体测试
 EOF

 rm .gmt*

生成结果如下图：

.. figure:: /images/2013081301.jpg
   :width: 600px
   :alt: gmt chinese

更细致的讨论
============

-  整个修改跟系统关系很大。不同的Linux发行版，字体文件的位置以及预装的字体文件都不同；不同版本的ghostscript，其配置文件cidfmap.zh\_CN的位置也不同；有的版本没有conf.d文件夹，有的版本配置文件直接就是cidfmap，这个需要自己去找；整个修改跟GMT版本的关系不大。
-  ghostscript下有两个文件夹，conf.d和8.70。conf.d下有文件如下：

   ::

       cidfmap.ko     cidfmap.zh_TW   CIDFnmap.zh_TW  FAPIcidfmap.zh_CN
       cidfmap.zh_CN  CIDFnmap.zh_CN  FAPIcidfmap.ko  FAPIcidfmap.zh_TW

   其中ko结尾的可能是指日韩字体，zh\_CN指简体中文，zh\_TW指繁体中文。cidfmap、CIDFnmap和FAPIcidfmap的区别未知，遍历一遍发现只有修改cidfmap.zh\_CN是有效的。

-  在8.70/Resource/Init下也有一个名为cidfmap的文件，其内容如下：

   ::

       %!
       % Don't change following line. We should ensure that the original one is surely loaded.
       (cidfmap.GS) .runlibfile
       % following lines are for CJK fonts.
       (cidfmap.ja) .runlibfileifexists
       (cidfmap.ko) .runlibfileifexists
       (cidfmap.zh_CN) .runlibfileifexists
       (cidfmap.zh_TW) .runlibfileifexists
       % must be at the bottom of line to allow people overriding everything.
       (cidfmap.local) .runlibfileifexists


   它大概是说如果cidfmap.zh\_CN这几个文件存在则包含吧，有些文章说要修改这个文件，但是其文件格式却与cidfmap.zh\_CN相同，所以这应该是版本差异，需要自己判断。

-  cidfmap.zh\_CN中的字体名是可以任意取的，关键是其对应的字体路径要给对，其他一些参数的具体含义不太清楚。
-  修改GMT字体配置文件时给定的字体名为\ ``BousungEG-Light-GB-UniGB-UTF8-H``\ ，其中前部分\ ``BousungEG-Light-GB``\ 为cidfmap.zh\_CN中指定的字体名，后半部分UniGB-UTF8-H为该字体采用的映射，所有的映射方式位于8.70/Resource/CMap中，（不清楚什么叫映射。。。）所有文件名中带有GB的都是与中文显示有关的映射（GB表示国标），结尾为H的代表横向字体，结尾为V的代表纵向字体。按照网上的说法，选择哪种映射与具体字体有关，测试了几个，只发现UniGB-UTF8-H是可用的，因而GMT中给定的字体名为\ ``BousungEG-Light-GB-UniGB-UTF8-H``\ 。（参考中给出的字体名为BousungEG-Light-GB--UniGB-UTF8-H，经测试二者效果一致。）
-  也可以将Windows下常见的中文字体sim\*.tt?字体拷贝到Linux系统下，按照类似的方式修改配置即可以使用windows字体。

可移植性的一些测试
==================

-  本机：用vi打开ps文件，中文正常显示；
-  本机：gs查看正常；
-  本机：ps2pdf转换成pdf文件后用evince查看正常；
-  本机：ps2pdf转换成pdf文件后用Adobe Reader查看正常；
-  其他未经配置的Linux：用vi查看ps文件，中文正常显示，说明文件的编码是对的；
-  其他未经配置的Linux：gs查看乱码（gs找不到相应字体）；
-  其他未经配置的Linux：ps2pdf转换成pdf后，用evince和Adobe Reader均乱码；
-  Windows：用windows下未配置的gs打开乱码；
-  Windows：用Windows版Adobe Reader打开正常。
-  Windows：当初使用的是windows下的字体，测试发现用Adobe
   Reader打开正常，本文直接用的linux字体，不确定是否正常。

参考资料
========

#. GMT软件显示汉字的技术原理与实现\ *，赵桂儒，《测绘通报》*
#. ghostscript中文打印经验：http://guoyoooping.blog.163.com/blog/static/13570518320101291442176
#. GMT中文支持 http://xxqhome.blog.163.com/blog/static/1967330202011112810120598/
#. GMT chinese support http://hi.baidu.com/guyueshuiming/item/0052df53852ee4494fff20c3

更新历史
========

-  2013-05-15：修正了中文测试脚本的一个bug。
-  2013-05-16：系统默认未安装ghostscript的中文字体包，conf.d文件夹为空，通过安装相应中文包解决该问题。
-  2013-08-17：添加了字体以及ghostscript可能需要的几个安装包的信息；以及在新增字体后要重建字体缓存。

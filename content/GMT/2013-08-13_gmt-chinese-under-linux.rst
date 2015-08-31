Linux下的GMT中文支持
####################

:date: 2013-08-13 16:23
:modified: 2015-08-31
:author: SeisMan
:category: GMT
:tags: GMT技巧, 中文, GMT4, GMT5
:slug: gmt-chinese-under-linux
:summary: Linux下可以通过配置ghostscript和GMT，让GMT支持中文。

.. contents::

原生GMT是不支持中文的，想要让GMT支持中文，需要进行一番配置。想要理解整个问题，需要对PostScript、CID字体有更深刻的理解，这未免有些过于复杂。所以这篇博文只介绍一些基本的原理，不一定准确但是却够用。

让GMT支持中文，需要修改ghostscript和GMT的配置文件。由于不同发行版对ghostscript的打包方式不同，不同的ghostscript版本之间的配置文件也有一些差异。因而这里以我在使用的CentOS7来介绍整个原理，\ **其他发行版与CentOS7的差异会在文末列出**\ 。

本文所使用的Linux环境：

- 操作系统：CentOS 7.1
- ghostscript：9.07
- GMT：4.5.13（同样适用于GMT 5.x）

准备工作
========

gs中文配置文件
--------------

大多数发行版都已经默认安装了gs。除此之外，还需要安装简体中文配置文件。CentOS 7下中文配置文件可以通过如下命令安装::

    sudo yum install ghostscript-chinese-zh_CN

安装完成后，中文配置文件的路径为\ ``/usr/share/ghostscript/conf.d/cidfmap.zh_CN``\ ，以下称为ghostscript中文配置文件。

GMT字体配置文件
---------------

假定GMT的安装路径为\ ``/opt/GMT-4.5.13``\ ，则字体配置文件的路径为\ ``/opt/GMT-4.5.13/share/pslib/PS_font_info.d``\ 。

使gs支持中文
============

gs中文配置文件
--------------

CentOS 7中ghostscript中文配置文件的默认内容为::

    /BousungEG-Light-GB << /FileType /TrueType /Path (/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /GBZenKai-Medium    << /FileType /TrueType /Path (/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /MSungGBK-Light     /BousungEG-Light-GB ;
    /Adobe-GB1      /BousungEG-Light-GB ;

其中的细节可能看不懂，但是可以大概总（xia）结（cai）如下：

- 第一行定义了字体名为\ ``/BousungEG-Light-GB``\ ，对应的字体文件为\ ``/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc``\ ，也就是文泉驿正黑；
- 第二行定义了字体名为\ ``/GBZenKai-Medium``\ ，对应的字体文件也是文泉驿正黑；
- 第三行和第四行分别定义了字体名\ ``/MSungGBK-Light``\ 和\ ``/Adobe-GB1``\ ，这两种都对应于\ ``/BousungEG-Light-GB``\ ，相当于给字体定义了别名。

关于配置文件的几点说明：

- 字体名是任意的，比如字体名可以取为\ ``/ABC``\ ；
- 字体文件似乎只能是\ ``ttc``\ 或\ ``ttf``\ 格式的，当然修改参数也有可能可以使用其他格式的字体；
- 要注意确认字体文件是否存在，比如CentOS7下的wqy-zenhei.ttc字体实际上位于软件包\ ``wqy-zenhei-fonts``\ 中。若字体不存在，则需要安装相应软件包。

测试gs对Linux默认字体的支持
---------------------------

CentOS7的ghostscript中文配置文件中，默认有四行，分别定义了四个字体名，尽管本质上这四个字体名都指向同一个字体。下面先测试一下如何让gs显示Linux的默认字体。

用\ **编辑器**\ 新建一个PS文件（是的，PS文件其中就是纯文本，可以直接用编辑器编辑!），名为\ ``linux_fonts.ps``\ ，其内容为::

    %! PS-Adobe-3. 0
    /BousungEG-Light-GB--UniGB-UTF8-H findfont 20 scalefont setfont
    150 400 moveto
    (BousungEG 字体) show

    /GBZenKai-Medium--UniGB-UTF8-H findfont 20 scalefont setfont
    150 375 moveto
    (GBZenKai 字体) show

    /MSungGBK-Light--UniGB-UTF8-H findfont 20 scalefont setfont
    150 350 moveto
    (MSungGBK 字体) show

    /Adobe-GB1--UniGB-UTF8-H findfont 20 scalefont setfont
    150 325 moveto
    (Adobe 字体) show

    showpage
    %%Trailer
    %%EOF

简单解释一下，PS文件中要使用某个中文字体，需要用\ ``FontName--CMap``\ 的格式来调用。其中\ ``FontName``\ 即gs中文配置文件中给定的字体名。CMap可以取\ ``UniGB-UTF8-H``\ 和\ ``GB-EUC-H``\ ，Linux下一般用前者，Windows下一般用后者，应该是用于指定汉字或中文字体的编码，具体原理不知。

用gs查看该PS文件，正常情况下显示如下图，表明gs可以正常显示Linux下的默认中文字体。

.. figure:: /images/2013081301.png
   :width: 300px
   :alt: gs-linux-fonts

添加Windows中文字体
-------------------

Linux的中文字体较少，所以这里使用Windows下中的中文字体，这里只考虑Windows下的宋体、仿宋、黑体和楷体四个基本字体。将这四个字体文件复制到\ ``/usr/share/fonts/winfonts/``\ 目录下，然后对gs的中文配置文件做如下修改::

    % 原内容保持不变
    /BousungEG-Light-GB << /FileType /TrueType /Path (/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /GBZenKai-Medium    << /FileType /TrueType /Path (/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /MSungGBK-Light     /BousungEG-Light-GB ;
    /Adobe-GB1      /BousungEG-Light-GB ;

    % 新增Windows字体的支持
    /STSong-Light << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simsun.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /STFangsong-Light << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simfang.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /STHeiti-Regular << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simhei.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /STKaiti-Regular << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simkai.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;

这里仅以Windows下的常用四大字体为例。对于Windows下的其他中文字体、Linux的其他中文字体甚至日韩字体来说，方法类似。

测试gs对Windows中文字体的支持
-----------------------------

用\ **编辑器**\ 新建一个PS文件，名为\ ``windows_fonts.ps``\ ，其内容为::

    %! PS-Adobe-3. 0
    /STSong-Light--UniGB-UTF8-H findfont 20 scalefont setfont
    150 400 moveto
    (Song Typeface 宋体) show

    /STFangsong-Light--UniGB-UTF8-H findfont 20 scalefont setfont
    150 375 moveto
    (Fangsong Typeface 仿宋体) show

    /STHeiti-Regular--UniGB-UTF8-H findfont 20 scalefont setfont
    150 350 moveto
    (Hei Typeface 黑体) show

    /STKaiti-Regular--UniGB-UTF8-H findfont 20 scalefont setfont
    150 325 moveto
    (Kai Typeface 楷体) show

    showpage
    %%Trailer
    %%EOF

用gs查看该PS文件，若正确显示中文如下图，则表明gs已支持Windows字体。

.. figure:: /images/2013081302.jpg
   :width: 500px
   :alt: gs-chinese


使GMT支持中文
=============

修改GMT字体配置文件
-------------------

打开GMT字体配置文件\ ``/opt/GMT-4.5.13/share/pslib/PS_font_info.d``\ ，在文件最后加入如下语句（以Windows下的四大常用字体为例）::

    STSong-Light--UniGB-UTF8-H  0.700    1
    STFangsong-Light--UniGB-UTF8-H  0.700    1
    STHeiti-Regular--UniGB-UTF8-H   0.700   1
    STKaiti-Regular--UniGB-UTF8-H   0.700   1

第一列为字体名，第二列为字母A的高度，第三列与编码有关。

查看GMT当前支持的字体
---------------------

用\ ``pstext -L``\ 命令查看GMT当前的字体配置：

.. code-block:: bash

    $ pstext -L
    Font #  Font Name
    ------------------------------------
    0   Helvetica
    1   Helvetica-Bold
    ...    ......
    32  Palatino-BoldItalic
    33  ZapfChancery-MediumItalic
    34  ZapfDingbats
    35 STSong-Light--UniGB-UTF8-H
    36 STFangsong-Light--UniGB-UTF8-H
    37 STHeiti-Regular--UniGB-UTF8-H
    38 STKaiti-Regular--UniGB-UTF8-H

其中0-34为GMT/gs默认支持的西文字体，35至38为新添加的中文字体。

GMT中文测试
-----------

GMT4测试脚本：

.. code-block:: bash

   #!/bin/bash
   gmtset HEADER_FONT 35

   pstext -R0/7/0/7 -JX6i/6i -B1/1:."GMT中文支持": -P > cn.ps <<EOF
   1.5 5 35 0 35 LM GMT宋体
   1.5 4 35 0 36 LM GMT仿宋
   1.5 3 35 0 37 LM GMT黑体
   1.5 2 35 0 38 LM GMT楷体
   EOF

   rm .gmt*

成图效果如下

.. figure:: /images/2013081303.jpg
   :width: 400px
   :alt: gmt4-chinese

GMT5测试脚本：

.. code-block:: bash

   #!/bin/bash
   gmt gmtset FONT_TITLE 40p,35,black

   gmt pstext -R0/7/0/7 -JX6i/6i -Bafg -B+t"GMT中文支持" -F+a+c+f -P > gmt5_cn.ps << EOF
   3.5 5 0 LM 45p,35,red   GMT宋体
   3.5 4 0 LM 45p,36,blue  GMT仿宋
   3.5 3 0 LM 45p,37,black GMT黑体
   3.5 2 0 LM 45p,38,green GMT楷体
   EOF

   rm gmt.*

成图效果如下

.. figure:: /images/2013081304.jpg
   :width: 400px
   :alt: gmt5-chinese

对其他发行版的若干说明
======================

其他发行版与CentOS 7之间或多或少有一些区别，列举如下。

CentOS 6
--------

#. gs中文配置文件需要用如下命令安装::

       sudo yum install cjkuni-fonts-ghostscript

   在安装配置文件的同时会安装中文字体uming和ukai

#. gs中文配置文件中给定的字体路径为\ ``/usr/share/fonts/cjkuni/uming.ttc``\ 是错误的，真实的字体路径是\ ``/usr/share/fonts/cjkui-uming/uming.ttc``\ ，要注意改正。

Ubuntu 14.04/15.04
------------------

#. gs中文配置文件可以用如下命令安装（默认已安装）::

       sudo apt-get install poppler-data

#. gs中文配置文件路径为：``/etc/ghostscript/cidfmap.d/90gs-cjk-resource-gb1.conf``

#. gs中文配置文件中默认使用的Linux字体为uming和ukai，需要通过如下命令安装::

       sudo apt-get install fonts-arphic-uming fonts-arphic-ukai

#. gs中文配置文件的默认内容为::

       /BousungEG-Light-GB << /FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/uming.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
       /GBZenKai-Medium    << /FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/ukai.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
       /Song-Medium /GBZenKai-Medium ;
       /STSong-Light /BousungEG-Light-GB ;
       /STFangsong-Light /BousungEG-Light-GB ;
       /STHeiti-Regular /BousungEG-Light-GB ;
       /STKaiti-Regular /BousungEG-Light-GB ;
       /Adobe-GB1      /BousungEG-Light-GB ;
       /Adobe-GB1-Bold /GBZenKai-Medium ;

   需要将该文件改成::

       % 原配置文件的内容，与STSong-Light等相关的四行必须删除
       /BousungEG-Light-GB << /FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/uming.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
       /GBZenKai-Medium    << /FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/ukai.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
       /Song-Medium /GBZenKai-Medium ;
       /Adobe-GB1      /BousungEG-Light-GB ;
       /Adobe-GB1-Bold /GBZenKai-Medium ;

       % 新增Windows字体的支持
       /STSong-Light << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simsun.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
       /STFangsong-Light << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simfang.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
       /STHeiti-Regular << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simhei.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
       /STKaiti-Regular << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simkai.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;

   修改完gs中文配置文件后，必须要执行如下命令::

       $ sudo update-gsfontmap

   该命令会将\ ``/etc/ghostscript/cidfmap.d/*.conf``\ 合并成单独的文件\ ``/var/lib/ghostscript/fonts/cidfmap``\ 。gs在需要中文字体时会读取\ ``/var/lib/ghostscript/fonts/cidfmap``\ 而不是\ ``/etc/ghostscript/cidfmap.d/*.conf``\ 。这是Ubuntu/Debian和CentOS的一个很大不同。

Ubuntu 12.04
------------

#. gs中文配置文件需要用如下命令安装::

       sudo apt-get install gs-cjk-resource

#. 其他部分未做测试，估计跟Ubuntu 15.05差不多。

可移植性的测试
==============

- 本机：用vi打开PS文件，中文正常显示；
- 本机：gs查看正常；
- 本机：ps2raster转换为PDF，用evince、zathura查看正常；
- 本机：ps2pdf转换为PDF，用evince、zathura查看正常；
- 复制到Windows：用gs查看正常；

参考资料
========

#. GMT软件显示汉字的技术原理与实现\ *，赵桂儒，《测绘通报》*
#. ghostscript中文打印经验：http://guoyoooping.blog.163.com/blog/static/13570518320101291442176
#. GMT中文支持 http://xxqhome.blog.163.com/blog/static/1967330202011112810120598/
#. GMT chinese support http://hi.baidu.com/guyueshuiming/item/0052df53852ee4494fff20c3
#. 维基词条：PostScript https://en.wikipedia.org/wiki/PostScript
#. Debian Wiki: https://wiki.debian.org/gs-undefoma

更新历史
========

- 2013-05-15：修正了中文测试脚本的一个bug。
- 2013-05-16：系统默认未安装ghostscript的中文字体包，conf.d文件夹为空，通过安装相应中文包解决该问题。
- 2013-08-17：添加了字体以及ghostscript可能需要的几个安装包的信息；以及在新增字体后要重建字体缓存。
- 2014-10-14：重写整个文档，使其更具有普遍性；
- 2015-08-31：Ubuntu下需要使用update-gsfontmap命令来更新中文配置文件；

Linux下的GMT中文支持
####################

:date: 2013-08-13 16:23
:modified: 2014-10-14
:author: SeisMan
:category: GMT
:tags: GMT技巧, 中文, GMT4, GMT5
:slug: gmt-chinese-under-linux
:summary: 讨论了如何让GMT支持中文。

.. contents::

原生GMT是不支持中文的，想要让GMT支持中文，需要进行一番配置。想要理解整个问题，需要对PostScript、CID字体有更深刻的理解，这未免有些过于复杂。所以这篇博文只介绍一些基本的原理，不一定准确但是却够用。

修改配置这个事情本身不难，麻烦的是不同的发行版对ghostscript的打包方式不同，不同的ghostscript版本之间也会有一些差异。这里列出我在使用的系统信息，对于其他发行版以及gs版本，也有一些参考意义。

-  操作系统：CentOS 7.0
-  ghostscript：9.07
-  GMT：4.5.12或5.1.1（以4.5.12为例）

准备工作
========

安装gs
------

对于大多数发行版而言，gs都是默认安装的。相关的文件位于\ ``/usr/share/ghostscript``\ 目录下。

除此之外，还需要安装简体中文配置文件，不同的发行版该中文配置文件的名字也不同。下文仅以CentOS 7为例，读者需要注意与自己的发行版的区别。

CentOS 7 ::

    $ sudo yum install ghostscript-chinese-zh_CN

CentOS 6 ::

    $ sudo yum install cjkuni-fonts-ghostscript

Ubuntu 14.04::

    $ sudo apt-get install gs-cjk-resource poppler-data

Ubuntu 12.04 ::

    $ sudo apt-get install gs-cjk-resource

安装完中文配置文件之后，不同的发行版配置文件的位置也不同：

- CentOS 7：``/usr/share/ghostscript/conf.d``
- CentOS 6：``/usr/share/ghostscript/conf.d``
- Ubuntu 14.04： ``/etc/ghostscript/cidfmap.d/90gs-cjk-resource-gb1.conf``
- Ubuntu 12.04： ``/etc/ghostscript/cidfmap.d/90gs-cjk-resource-gb1.conf``

安装GMT
-------

这步就不用再多说了。安装后的GMT位于\ ``/opt/GMT-4.5.12``\ ，其中与字体有关的文件为\ ``/opt/GMT-4.5.12/share/pslib/PS_font_info.d``\ 。

使gs支持中文
============

cidfmap
-------

进入\ ``conf.d``\ 目录下，有文件\ ``cidfmap.zh_CN``\ （该目录下还有\ ``CIDFnmap.zh_CN``\ 和\ ``FAPIcidfmap.zh_CN``\ ，不管） ，其内容为::

    /BousungEG-Light-GB << /FileType /TrueType /Path (/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /GBZenKai-Medium    << /FileType /TrueType /Path (/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /MSungGBK-Light     /BousungEG-Light-GB ;
    /Adobe-GB1      /BousungEG-Light-GB ;

其中的细节可能看不懂，但是可以大概总（xia）结（cai）如下：

- 第一行定义了字体名为\ ``/BousungEG-Light-GB``\ ，对应的字体文件为\ ``/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc``\ ，也就是文泉驿正黑；
- 第二行定义了字体名为\ ``/GBZenKai-Medium``\ ，对应的字体文件也是文泉驿正黑；
- 第三行和第四行分别定义了字体名\ ``/MSungGBK-Light``\ 和\ ``/Adobe-GB1``\ ，这两种都对应于\ ``/BousungEG-Light-GB``\ ，相当于给字体定义了别名。

关于这个文件需要说的几点是：

- 字体名是任意的，比如可以把字体名取为\ ``/ABC``\ ；
- 字体文件似乎只能是\ ``ttc``\ 或\ ``ttf``\ 格式的，当然修改参数也有可能可以使用其他格式的字体；
- 由于Linux下中文字体并不统一，所以要注意检查配置文件中的字体文件路径是否正确；

CMap
----

CMap位于\ ``/usr/share/ghostscript/9.07/Resource/CMap``\ 目录下，可以看到其中有很多文件，CMap文件的具体含义不知。暂且留在这里。只需要知道有\ ``UniGB-UTF8-H``\ 和\ ``GB-EUC-H``\ 这两个CMap即可。

测试gs对中文字体的支持
----------------------

Linux的中文字体比较少，可能很多人都会将Windows下的中文字体复制到Linux下使用。假设已经将Windows下的中文字体复制到\ ``/usr/share/fonts/winfonts/``\ 目录下，对gs的配置文件\ ``cidfmap.zh_CN``\ 做一些修改，使gs在Linux下可以使用Windows中文字体::

    % cidfmap.zh_CN的原内容保持不变
    /BousungEG-Light-GB << /FileType /TrueType /Path (/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /GBZenKai-Medium    << /FileType /TrueType /Path (/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /MSungGBK-Light     /BousungEG-Light-GB ;
    /Adobe-GB1      /BousungEG-Light-GB ;

    % 新增Windows字体的支持
    /STSong-Light << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simsun.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /STFangsong-Light << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simfang.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /STHeiti-Regular << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simhei.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
    /STKaiti-Regular << /FileType /TrueType /Path (/usr/share/fonts/winfonts/simkai.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;

用\ **编辑器**\ 新建一个PS文件（是的，PS文件其中就是纯文本，可以直接用编辑器编辑!），名为\ ``gs_test.ps``\ ，其内容为::

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

用gs查看该PS文件，若正确显示中文如下图，则表明gs的中文配置没有问题。

.. figure:: /images/2013081301.jpg
   :width: 500px
   :alt: gs-chinese

需要说明如下几点：

- 这里仅仅以Windows字体为例，对于其他中文甚至日韩字体来说，方法类似；
- PS文件中的中文字体为\ ``CIDFont--CMap``\ ，这里CMap选择的是\ ``UniGB-UTF8-H``\ ，在Windows下似乎应该选择\ ``GB-EUC-H``\ ，尚不清楚原理；

使GMT支持中文
=============

修改配置文件
------------

打开GMT中文配置文件\ ``/opt/GMT-4.5.12/share/pslib/PS_font_info.d``\ ，在文件最后加入如下语句（以Windows字体为例）::

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

.. figure:: /images/2013081302.jpg
   :width: 400px
   :alt: gmt4-chinese

GMT5测试脚本：

.. code-block: bash

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

.. figure:: /images/2013081303.jpg
   :width: 400px
   :alt: gmt5-chinese

可移植性的一些测试
==================

- 本机：用vi打开PS文件，中文正常显示；
- 本机：gs查看正常；
- 本机：ps2raster转换为PDF，用evince、zathura查看正常；
- 本机：ps2pdf转换为PDF，用evince、zathura查看正常；

由于目前无其他机器可用，因而暂时不测试可移植性。

参考资料
========

#. GMT软件显示汉字的技术原理与实现\ *，赵桂儒，《测绘通报》*
#. ghostscript中文打印经验：http://guoyoooping.blog.163.com/blog/static/13570518320101291442176
#. GMT中文支持 http://xxqhome.blog.163.com/blog/static/1967330202011112810120598/
#. GMT chinese support http://hi.baidu.com/guyueshuiming/item/0052df53852ee4494fff20c3

更新历史
========

- 2013-05-15：修正了中文测试脚本的一个bug。
- 2013-05-16：系统默认未安装ghostscript的中文字体包，conf.d文件夹为空，通过安装相应中文包解决该问题。
- 2013-08-17：添加了字体以及ghostscript可能需要的几个安装包的信息；以及在新增字体后要重建字体缓存。
- 2014-10-14：重写整个文档，使其更具有普遍性；

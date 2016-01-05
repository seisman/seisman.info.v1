GMT在Windows下的中文支持
########################

:author: SeisMan
:date: 2014-03-27 16:45
:modified: 2015-01-13
:category: GMT
:tags: GMT技巧, 中文, Windows
:slug: gmt-chinese-support-under-windows
:summary: GMT在Windows下中文支持需要注意的问题。

.. contents::

GMT在Windows下如何支持中文的问题在这篇\ `博文`_\ 里已经说的差不多了。本文会在该博文的基础上做进一步地整理、归纳和补充。

准备工作
========

#. 安装Windows版GMT；
#. 安装ghostscript；

   需要注意在安装的最后，会有一个生成cidmap的选项，选中该选项则表示会为当前系统自动生成中文所需的cidmap文件。默认该选项是被选中的，一定\ **不要**\ 将该选项取消；

#. 安装gsview；

ghostscript的中文支持
=====================

若ghostscript的安装没有问题，则在 ``C:\Program Files\gs\gs9.15\examples\cjk`` 目录下可以找到文件 ``gscjk_ag.ps`` 。

启动cmd，键入如下命令::

   cd "C:\Program Files\gs\gs9.16\bin"
   gswin64.exe ..\examples\cjk\gscjk_ag.ps

该命令用命令行版本的 ``gswin64c`` 打开 ``gscjk_ag.ps`` ，若能看到中文，则说明ghostscript是可以正常支持中文的。

gsview的中文支持
================

安装好gsview之后，PS格式会自动与gsview关联。一般情况下，直接双击PS文件，就会用gsview打开该PS文件。

双击打开 ``gscjk_ag.ps`` ，一般情况下不会正确显示汉字。这是因为gsview在打开PS文件时没有找到汉字所对应的字体文件。

在gsview的“选项”->“高级配置”中，将Ghostscript Options由 ``-dNOPLATFONTS -sFONTPATH="c:\psfonts"`` 改成 ``-dNOPLATFONTS -sFONTPATH="C:\Windows\Fonts"`` ，此时gsview在调用gswin64时会将选项传递给gswin64，gswin64则会在 ``FONTPATH`` 中搜索字体。

配置完毕后，重新打开 ``gscjk_ag.ps`` ，若中文正常显示，则表示gsview已支持中文。

GMT的中文支持
=============

用\ **编辑器**\ 打开 ``gscjk_ag.ps`` ，会看到如下内容::

    /STSong-Light--GB-EUC-H *findfont 20 scalefont setfont
    150 400 moveto
    (Song Typeface 宋体) show
    /STFangsong-Light--GB-EUC-H *findfont 20 scalefont setfont
    150 375 moveto
    (Fangsong Typeface 仿宋体) show
    /STHeiti-Regular--GB-EUC-H *findfont 20 scalefont setfont
    150 350 moveto
    (Hei Typeface 黑体) show
    /STKaiti-Regular--GB-EUC-H *findfont 20 scalefont setfont
    150 325 moveto
    (Kai Typeface 揩体) show
    %
    /Times-Roman findfont 13 scalefont setfont
    50 200 moveto
    (* Chinese translation of "Ghostscript" is merely associative \
    characters of these meanings.) show
    50 200 13 sub moveto
    (In Simplified Chinese articles, customarily we use just "Ghostscript" \
    as it is.) show

其中 ``STSong-Light--GB-EUC-H`` 即为宋体， ``GB-EUC`` 是文字编码方式， ``H`` 表示水平字体， ``V`` 表示垂直向字体，这里给出了四种常见字体的名称

#. ``STSong-Light--GB-EUC-H``
#. ``STFangsong-Light--GB-EUC-H``
#. ``STHeiti-Regular--GB-EUC-H``
#. ``STKaiti-Regular--GB-EUC-H``

将这四种中文字体添加到GMT的字体配置文件中，GMT版本不同，配置文件的位置也不同：

- GMT 5.1.2及其之前版本： ``C:\programs\gmt5\share\pslib\PS_font_info.d``
- GMT 5.2.1及其之后版本： ``C:\programs\gmt5\share\postscriptlight\PSL_standard_fonts.txt``

字体配置文件修改后，最后几行如下::

    ZapfChancery-MediumItalic   0.610       0
    ZapfDingbats            0.700       1
    STSong-Light--GB-EUC-H  0.700    1
    STFangsong-Light--GB-EUC-H  0.700    1
    STHeiti-Regular--GB-EUC-H   0.700   1
    STKaiti-Regular--GB-EUC-H   0.700   1

用 ``gmt pstext -L`` 查看GMT字体，可以看到，新添加的四种中文字体对应的字体编号为35到38。

测试脚本
========

本代码为GMT5语法！

.. code-block:: bash

   gmt gmtset FONT_TITLE 40p,35,black

   echo 3.5 5 0 LM 45p,35,red  GMT宋体 > tmp
   echo 3.5 4 0 LM 45p,36,blue GMT仿宋 >> tmp
   echo 3.5 3 0 LM 45p,37,yellow GMT黑体 >> tmp
   echo 3.5 2 0 LM 45p,38,green GMT楷体 >> tmp

   gmt pstext tmp -R0/7/0/7 -JX6i/6i -Bafg -B+t"GMT中文" -F+a+c+f -P > cn.ps

若生成的PS文件正常显示汉字，则表示GMT已经可以支持中文。

需要注意，若使用记事本编辑bat文件，则保存时应注意编码方式为ANSI、Unicode或Unicode big endian，若使用UTF-8编码则会出现乱码；另外，很多编辑器默认将文本文件以UTF-8编码保存，因而可能需要修改编辑器的默认编码。

图片格式转换
============

使用GMT自带的 ``ps2raster`` 命令可以将PS文件转换为其它图片格式。

在Windows下，对于含中文的PS文件，需要在ps2raster上加上字体路径，如下:

.. code-block:: bash

   ps2raster -C-sFONTPATH=C:\Windows\Fonts test.ps

即可正常使用。

#. GMT 5.1.1存在bug，上面的命令无法与-A选项一起使用；
#. GMT 5.1.2在Windows下存在Bug，主要是由于引号的错误使用导致；

修订历史
========

#. 2014-03-27：初稿；
#. 2016-01-05：GMT 5.2.1中字体配置文件的位置发生变化；

.. _博文: http://xxqhome.blog.163.com/blog/static/1967330202011112810120598/

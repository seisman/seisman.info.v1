GMT之利用ps2raster实现图像格式转换
##################################

:date: 2013-08-15 17:11
:author: SeisMan
:category: GMT
:tags: GMT命令, 图像, GMT4, 格式转换
:slug: format-conversion-using-ps2raster
:summary: ps2raster可以将PS文件转换为多种格式。

.. contents::

前言
====

GMT中与绘图相关的大部分命令的输出都是PS代码，我们一般将输出通过">"或者">>"重定向到ps文件中，然后用gs查看。PS是矢量图像格式，因而可以任意放大而不失真，满足了出版社对高质量图像的要求。有时候在用word随便写点文章或者制作ppt时，ps图像无法直接插入，因而需要将ps文件转换为常见的其他图像格式。格式转换可以使用强大的convert命令，不过GMT提供的ps2raster命令已经足够了。

ps2raster利用ghostscript程序将ps文件转换为多种格式，BMP, EPS, JPEG, PDF, PNG, PPM, TIFF。

命令
====

::

 ps2raster 4.5.9 [64-bit] - Converts one or several [E]PS file(s) toraster formats using GhostScript.
 usage: ps2raster psfile1 psfile2... [-A[u][-]] [-Cgs_command] [-Ddir] [-Eresolution] [-Fout_name]
 [-Gghost_path] [-Llistfile] [-N] [-P] [-Q[g\|t]1\|2\|4] [-S] [-Tb\|e\|f\|g\|G\|j\|m\|t] [-V]
 [-W[+g][+k][+ttitle][+nname][+amode[alt]][+llodmin/lodmax][+fminfade/maxfade][+uURL&]]

选项
====

需要关注的参数为-A、-E、-T和-P：

-  psfiles：要进行转换的ps文件
-  **-A：**\ 一般ps文件的尺寸为一张A4纸的大小（PAPER\_MEDIA），很多时候绘图只占用了纸张的一小部分。这个选项可以重新定义BoudingBox，将空白的部分去除。-Au可以额外去除GMT的时间戳（-U）。（觉得这个选项去空白去得有点过了，图像周围基本一点空白都没有）
-  **-E：**\ 设置位图的精度。默认pdf格式dpi=720，其他格式dpi=300。pdf格式是矢量格式，但是其中的图案填充以及字体是以位图的格式存储的，-E选项对这部分是有效的。
-  **-T：**\ 指定输出格式，默认为jpeg格式。b指bmp，e代表eps，f代表pdf，j代表jpeg，g代表png，G代表透明的png，m代表ppm，t代表tiff。对于bgjt后可加-以产生灰度图。EPS是格式转换过程的中间文件，因而可以和其他格式同时生成，比如可以使用-Tef同时产生pdf和eps文件。
-  **-P：**\ Portrait mode。

比较小众的选项如下：

-  **-C：**\ 传递额外的参数给ghostscript
-  **-D：**\ 输出目录。-D.代表当前目录
-  **-F：**\ 强制修改转换后的文件名，后缀不能改
-  **-G：**\ ghostscript的完整路径，Linux下一般用不到
-  **-L：**\ 内含要转换的ps文件名。
-  **-Q：**
-  **-S：**
-  **-V：**\ verbose
-  **-W：**\ 这个选项有些复杂，可以用于生成geotiff文件以及KMZ文件。

例子
====

最常用的一个例子，将ps文件转换为jpeg文件

::

 ps2raster -A -P test.ps

一些说明
========

-  该命令主要处理GMT生成的PS文件，对于其他程序生成的PS文件不能完美支持；
-  该命令要求GMT生成的PS文件是完整的，即要求用户正确使用-K、-O。若PS文件未正确关闭，可以用gs查看ps文件，但是无法用ps2raster进行转换；
-  如eyou所说，当设置纸张背景色时，该命令的-A选项无法实现切边；
-  如果有更多需要的话可以使用ImageMagick的convert命令。\ `官方说明 <http://www.imagemagick.org/script/command-line-options.php>`_\ 。本站博文在\ `这里 <{filename}/GMT/2013-09-27_convert-and-ps2raster.rst>`_

修订历史
========

-  2013-08-15：初稿；
-  2013-09-26：添加了一些说明，并挑出需要关注的选项；

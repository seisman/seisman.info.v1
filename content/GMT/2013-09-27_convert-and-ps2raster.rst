图像格式转换工具convert
########################

:date: 2013-09-27 00:16
:author: SeisMan
:category: GMT
:tags: GMT技巧, GMT命令, 图像, 格式转换, GMT4
:slug: convert-and-ps2raster

在\ `《GMT之利用ps2raster实现图像格式转换》 <{filename}/GMT/2013-08-15_format-conversion-using-ps2raster.rst>`_\ 中介绍了如何利用ps2raster将GMT的PS文件转换成其他常见的图片格式。

一般情况下，如果只用GMT做图的话，ps2raster基本可以满足需求了。

遇到几个特殊的情况如下：

-  GMT中设置纸张背景色PAGE\_COLOR，此时ps2raster无法实现切边；
-  用其他软件绘图，比如LaTeX的TikZ/PGF包，得到PS或PDF文件，无法使用ps2raster实现格式转换；
-  ...

这个时候就需要使用convert命令。convert命令的选项非常多，学起来比ps2raster要复杂多了。

ps2raster中常用的选项有-A、-E、-T、-P。convert众多选项中与之对应的选项如下：

-  **-trim：**\ 切边，等效于ps2raster的-A选项；其可以解决上面的第一个问题；
-  **-density**
   *width*\ **x**\ *height*\ ：设置图像精度，等效于ps2raster的-E选项；按照GMT的惯例，width=300即可，height可以指定或不指定。注意width和height中间的字符是字母"x"；
-  **-rotate**\ *degree*\ ：实现图像旋转，-rotate
   90等效于ps2raster的-P选项，当然rotate可以旋转各种角度。
-  convert没有与ps2raster中-T相应的选项，因为convert通过识别后缀直接进行转换；\ `这里`_\ 列出了convert支持的上百种图像/动画格式。

下面给出最常用的一个例子：

::

    convert -trim -density 300 -rotate 90 test.ps test.png

其等效于

::

    ps2raster -A -E300 -P -Tg test.ps

.. _这里: http://www.imagemagick.org/script/formats.php

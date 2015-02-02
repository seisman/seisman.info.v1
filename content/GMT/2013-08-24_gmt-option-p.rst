GMT进阶之-P选项
###############

:date: 2013-08-24 14:08
:author: SeisMan
:category: GMT
:tags: GMT选项, GMT技巧
:slug: gmt-option-p

.. contents::

一张标准A4纸的大小为210\*297 mm，我们说其宽度是210 mm，高度为297 mm。

模式介绍
========

一般定义A4纸的左下角那一点为坐标原点，从左向右为x轴增加方向，从下往上为y轴增加方向。如下面的左图所示。这个时候称为Portrait模式。Portrait译为“肖像”，显然一个人的高度要比宽度大很多。

如果将坐标系原点从纸张的左下角平移（translate）至右下角，然后将坐标系逆时针旋转90度，得到下面的右图。这个时候x轴是从下往上为增加方向，看起来不太舒服。如果将右图的纸张顺时针旋转90度，这个时候纸张的宽度为297 mm，高度为210 mm。这种模式称为Landscape模式，因为风景（Landscape）一般都是绵延的山水画，宽度比高度要大多了。

.. figure:: /images/2013082401.jpg
   :align: center
   :alt: mode
   :width: 600 px

GMT默认使用的是Landscape模式，可以通过-P选项强制使用Portrait模式。那么究竟该选哪种模式呢？一般情况下，用GMT绘制的地图都是方方正正的，两种模式基本没有区别；在一些特殊的情况下，比如用pssac绘制地震波形剖面，X轴为时间，Y轴列出了多个地震波形，这个时候Y轴就需要更长一些，以免多个波形重合在一起。

一些测试
========

解释完GMT的两种模式之后，还要再看看如何正确的使用-P选项。

测试脚本如下:

.. code-block:: bash

 #!/bin/bash

 psxy -JX1i/2i -R0/5/0/10 -B1/1 -K -T > 01.ps
 psxy -JX2i/1i -R0/10/0/5 -B1/1 -O -X2i -T >> 01.ps

 psxy -JX1i/2i -R0/5/0/10 -B1/1 -K -P -T > 02.ps
 psxy -JX2i/1i -R0/10/0/5 -B1/1 -O -P -X2i -T >> 02.ps

这个例子绘制了两张图，第一张图的两个psxy命令没有使用-P选项，第二张图的两个psxy命令都使用了-P选项。用evince查看一下这两个文件，可以发现01.ps为landscape模式，02.ps为portrait模式，这个是预料之中的事情。gs默认所有ps文件都是portrait模式，所以查看landscape模式的ps文件会比较别扭。

比较两个ps文件的源码可以发现，两个文件唯一的差别在于文件开头处的一些代码片段：

::

    %%BeginPageSetup
    595 0 T 90 R
    0.24 0.24 scale
    %%EndPageSetup

上面的代码片段是Landscape模式下的，Portrait模式下缺少了\ ``595 0 T 90 R``\ 这一行。这是唯一的区别！！！这意味着-P选项不直接影响单个命令产生的代码片段，而是对整个页面的设置起作用。

下面这个例子可能更有意思一些：

.. code-block:: bash

 #!/bin/bash
 psxy -JX1i/2i -R0/5/0/10 -B1/1 -K -P -T > 03.ps
 psxy -JX2i/1i -R0/10/0/5 -B1/1 -O -X2i -T >> 03.ps

 psxy -JX1i/2i -R0/5/0/10 -B1/1 -K -T > 04.ps
 psxy -JX2i/1i -R0/10/0/5 -B1/1 -O -X2i -P -T >> 04.ps

这两个例子中分别只有一个命令有-P选项。用evince查看一下，03.ps为Portrait模式，与02.ps完全相同；04.ps为Landscape模式，与01.ps完全相同。

小结
====

在\ `GMT进阶之深入理解-K和-O选项 <{filename} /GMT/2013-07-06_gmt-option-ko.rst>`_\ 中已经说到，PS文件的源码包含了头段、正文和尾巴，每个命令产生的代码组成了正文。如果一个命令是产生一个ps文件的第一个命令，则有没有-P选项决定了整个ps文件的模式，后面其他的命令无论有-P或者没有-P都没有任何影响，不可能通过-P选项使得图中一部分呈landscape模式，一部分呈portrait模式。总之，如果需要使用-P选项，只要在第一个绘图命令里使用就可以了，后面的-P完全没有效果。

20131024更新
============

关于-P选项，存在一个很大的误解，多数人认为如果一张图想要使用Portrait模式，则所有的命令都需要加上-P选项。上面的结果表明实际上根本不是这样。一个比较合理的做法是，如果需要portrait模式，则在脚本开始处使用\ ``gmtset PAGE_ORIENTATION  portrait``\ ，最后删除.gmt*即可。这样就真的可以把-P选项给彻底扔了。

吐槽
====

GMT为什么不设计成下面这样：

.. code-block:: bash

 #!/bin/bash
 PS="test.ps"

 GMT_init -P -F$PS;

 # begin plot command
 psxy .....
 pscoast .....
 # end plot command

 GMT_end；

GMT_init和GMT_end是两个单独的命令，其中GMT_init负责初始化GMT，主要是写入PS文件需要的头段信息，-P选项指定PS文件为Portrait模式，-F$PS指定PS文件名；GMT_end负责写入尾巴。这样设计的话中间的所有绘图命令都不再需要-K、-O选项，-P选项也可以废除了。GMT会在当前目录写入临时文件保留前面命令中-J和-R的信息，保留PS文件名应该也不是件难事。GMT的世界一下子就被简化了。

修订历史
========

-  2013-08-24：初稿；
-  2013-10-24：增加“小结”；

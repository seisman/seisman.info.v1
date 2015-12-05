底图边框与网格线
################

:date: 2015-05-19
:author: SeisMan
:category: GMT
:tags: GMT5, GMT技巧
:slug: frame-and-gridline

本文介绍GMT的-B选项的两种稍特殊的用法，以实现只绘制边框和只绘制网格线的目的。

两点说明：

#. 示例采用GMT5语法，但方法对于GMT4也同样适用；
#. 想不起来当初为什么会有只绘制网格线的需求了，所以这里只写如何实现，而不说为什么会有如此奇怪的需求。

绘制边框和网格线
================

使用下面的命令，会得到一个含有边框、标注、刻度和网格线的图::

    gmt psbasemap -R0/10/0/10 -JX10c/10c -Ba1f1g1 > test.ps

效果如下：

.. figure:: /images/2015051901.png
   :width: 500px
   :align: center
   :alt: frame-and-gridline

GMT默认绘制四条边，即虽然命令里没有 ``-BWSEN`` ，但实际上可以认为是有的，所以上面绘制出来的图有四个边框。

只绘制边框
==========

``-BWSEN`` 表示要绘制四条边， ``-B0``\ 设置了四条边的标注、刻度和网格线的间距都是零，即可认为是不绘制标注、刻度和网格线::

    gmt psbasemap -R0/10/0/10 -JX10c/10c -B0 -BWSEN > test.ps

效果图

.. figure:: /images/2015051902.png
   :width: 500px
   :align: center
   :alt: frame-only

只绘制网格线
============

想要只绘制网格线，即：

- 不绘制标注：用 ``-Ba0`` ，或不指定a的间隔，或用\ ``-Bwsen``\
- 不绘制刻度：用 ``-Bf0`` ，或不指定f的间隔；
- 不绘制边框：这是要解决的问题；

想要不绘制边框，关键在于要使用某个选项压制GMT默认的 ``-BWSEN`` 选项，这里使用\ ``-BZ``\ 选项，即只绘制Z轴，而对于二维图来说没有Z轴，所以使用\ ``-BZ``\ 可以覆盖GMT默认的\ ``-BWSEN``\ ::

    gmt psbasemap -R0/10/0/10 -JX10c/10c -Bg1 -BZ > test.ps

效果图：

.. figure:: /images/2015051903.png
   :width: 500px
   :align: center
   :alt: gridline-only

解决这个问题还有另外一个办法，即设置 ``MAP_FRAME_WIDTH`` 与\ ``MAP_GRID_PEN_PRIMARY``\ 为同样的粗细。

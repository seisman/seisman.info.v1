Doule Couple辐射花样可视化
##########################

:date: 2013-09-02 00:09
:author: SeisMan
:category: 地震学软件
:tags: 震源机制解, 震源球, Mathematica
:slug: doule-couple-radition-pattern

Aki & Richards (1980) P118 给出了远场P、SV、SH波的辐射花样。一直想将辐射花样画出来，以更好的理解不同震源机制的辐射花样。无奈各种绘图软件都只知皮毛。

下面给出用Mathematica写的两个辐射花样可视化的程序，可以下载封装好的cdf文件（用免费的\ `cdf-player`_\ 打开）或者nb源文件（用商业软件Mathematica打开）。


网址： http://demonstrations.wolfram.com/RadiationPatternForDoubleCoupleEarthquakeSources/

效果图如下，可以调节strike、rake、dip的值，选择波类型，来获得相应的辐射花样。（有些复杂，没怎么看明白。）

.. figure:: /images/2013090201.jpg
   :width: 600px
   :alt: Figure1

网址： http://demonstrations.wolfram.com/EarthquakeFocalMechanism/

效果图如下，这张图实际是根据P波初动绘制震源球，算是上图的一个简化版，通过修改strike、rake、dip的值，可以很清晰地看到震源球的断层面的移动过程，有助于锻炼“看震源球确定断层机制”的能力。

.. figure:: /images/2013090202.jpg
   :width: 600px
   :alt: Figure 2

.. _cdf-player: http://www.wolfram.com/cdf-player/

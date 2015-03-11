修改Y轴的坐标标注的方向
#######################

:date: 2015-03-11
:author: SeisMan
:category: GMT
:tags: GMT技巧
:slug: change-orientation-of-y-axis-annotations

在用GMT绘制底图时，通常Y轴的标注都是水平的，比如如下绘制底图的命令::

    gmt psbasemap -R0/50/-30/30 -JM10c -Bx10 -By10 > test.ps

效果如下图

.. figure:: /images/2015031101.png
   :width: 400px
   :align: center
   :alt: figure 1

有些时候想要让Y轴的标注逆时针旋转90度，即Y轴的标注方向与Y轴平行而不是与X轴平行。想要实现的效果如下图。

.. figure:: /images/2015031102.png
   :width: 400px
   :align: center
   :alt: figure 2

想要实现上图所示的效果，很简单，只需要修改GMT的参数\ ``MAP_ANNOT_OBLIQUE``\ 即可，代码如下::

    gmt set MAP_ANNOT_OBLIQUE 32
    gmt psbasemap -R0/50/-30/30 -JM10c -Bx10 -By10 > test.ps

几点说明：

#. GMT4下需要修改\ ``OBLIQUE_ANNOTATION``\ 为32；
#. 该参数对\ ``JX``\ 无效，可能只对地理投影有效；

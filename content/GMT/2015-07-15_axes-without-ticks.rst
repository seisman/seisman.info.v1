GMT绘制无刻度轴
###############

:author: SeisMan
:date: 2015-07-15
:category: GMT
:tags: GMT5, GMT技巧
:slug: axes-without-ticks

提出问题
========

要绘制一张底图，要求

#. 左边和下边有标注和刻度；
#. 右边和上边无标注且无刻度；

最直接的想法是使用 ``-BWSen`` ，绘图得到的效果图如左图所示，右边和上边虽然没有了标注，但是刻度线依然存在。实际想要实现的效果是右图。

.. figure:: /images/2015071501.png
   :width: 800 px
   :align: center
   :alt: axes without ticks

解决问题
========

GMT中 ``-B`` 选项可以用\ ``WSENwsen``\ 的组合来设置是否显示某边以及某边是否有标注。也可以分别设置X轴和Y轴的标注/刻度间隔，但却不能为X轴的上边和下边分别设置不同标注/刻度间隔。因而，这个问题没有直接的解决办法。

这里给出的办法是，使用两次 ``psbasemap`` ，分别绘制底图的左、下边和右上边。

.. code-block:: bash

   #!/bin/bash
   R=0/10/0/10
   J=X10c/6c
   PS=map.ps

   gmt psxy -J$J -R$R -T -K > $PS

   # 绘制底图的左边和下边
   gmt psbasemap -J$J -R$R -Bxa2 -Bya2 -BWS -K -O >> $PS
   # 绘制底图的右边和上边
   gmt psbasemap -J$J -R$R -B0 -Ben -K -O >> $PS

   # 其他绘图命令（不要再使用-B选项）
   gmt psxy -J$J -R$R -T -O >> $PS

代码中的第一个 ``psbasemap`` 命令中，\ ``-BWS``\ 表明当前命令只绘制底图的左边和下边；\ ``-Bxa2``\ 和\ ``-Bya2``\ 分别设置了两条边的标注间隔，可以根据自己的需求任意修改。第二个\ ``psbasemap``\ 命令中，\ ``-Ben``\ 表明当前命令只绘制底图的右边和上边，\ ``-B0``\ 表示右边和上边的标注/刻度间隔为零，即刻度线。

本示例中，第一个命令的 ``-BWS`` 和第二个命令的\ ``-Ben -B0``\ 是必须的，其他的选项及参数可以根据自己的需求修改。

另外，需要注意，绘制底图之后的其余绘图命令中都不要再使用 ``-B`` 选项（\ ``psscale``\ 除外）。

GMT中添加注释和标注
###################

:date: 2014-12-28
:author: SeisMan
:category: GMT
:tags: GMT5, GMT技巧
:slug: add-annotations-in-gmt

在日常绘图时经常会需要在已经画好的图上添加一些注释或标注，比如在某个位置加文字、箭头或者连线。一般情况下，若注释或标注出现在单个底图的内部，则可以很容易通过pstext和psxy来实现；若需要在底图外添加注释或标注，则会复杂一些。本文试图解决这个问题。

下图展示了绘图时一个常见的需求：

.. figure:: /images/2014122801.jpg
   :width: 600 px
   :alt: final figure

这里出于演示的目的，用尽可能简单的命令绘制尽可能简单的图形。图中两个底图由psbasemap绘制得到，红色矩形由psxy绘制得到。其命令如下：

.. code-block:: bash

    #!/bin/bash
    PS=test.ps

    R=0/10/0/10
    J=X10c
    gmt psxy -R$R -J$J -T -K > $PS

    # 绘制左边的底图
    gmt psbasemap -R$R -J$J -B2 -BWSen -K -O >> $PS
    # 绘制红色矩形
    gmt psxy -R$R -J$J -W1.5p,red -K -O -L >> $PS << EOF
    6 8
    8 8
    8 6
    6 6
    EOF

    R=6/8/6/8
    J=X8c
    # 绘制右边的底图
    gmt psbasemap -R$R -J$J -B0.5 -BwSEn -K -O -X12c -Y1c >> $PS

    gmt psxy -R$R -J$J -T -O >> $PS

    rm -f gmt.conf gmt.history

至此，整张图的主体已经绘制完成，下面需要向图中添加蓝色的两条连线。

这两条连线加起来并不那么容易，因为其游离在两个底图之间，而GMT是无法在底图之外添加注释和标注的，所以两条连线无法通过简单的方式实现。这里有几个反驳点：

#. pstext的-N选项是允许在底图之外写文本的。

   这一点我无力反驳，但是要注意文本和注释之间的一点点区别。比如，在左底图中（5,5）处画一个五角星表示地震事件，然后在附近写上“20141228”表示事件的ID，这称之为文本；若想在两个底图的中间添加“middle”这样的文本，姑且称为注释，可以使用pstext在左底图的（11,5）或右底图的（5.8,5）位置添加文本；

#. psxy的-N选项允许在底图之外画符号。

   用psxy的-N选项可以将圆、三角之类的符号画在底图之外，但直线无法出现在底图之外。

#. 为嘛不直接使用其他工具，比如Photoshop、Illustrator、GIMP甚至画图工具来添加？

   的确，用这些工具可以更简单的实现。但若经常需要微调图片，则需要重复使用这些工具，反而失去了用脚本画图的优势。另外，其他软件并不总能很好地兼容GMT做的图，所以有时候无法使用其他软件添加注释和标注。

这里的解决办法是，新增一个覆盖整张纸的辅助底图，在辅助底图中添加注释和标注，如下。

.. code-block:: bash

   #!/bin/bash
   PS=test.ps
   R=0/10/0/10
   J=X10c

   gmt psxy -R$R -J$J -T -K > $PS

   # 绘制左底图
   gmt psbasemap -R$R -J$J -B2 -BWSen -K -O >> $PS
   # 绘制红色矩形
   gmt psxy -R$R -J$J -W1.5p,red -K -O -L >> $PS << EOF
   6 8
   8 8
   8 6
   6 6
   EOF

   R=6/8/6/8
   J=X8c
   # 绘制右底图
   gmt psbasemap -R$R -J$J -B0.5 -BwSEn -K -O -X12c -Y1c >> $PS

   # 绘制辅助底图
   R=0/29.7/0/21
   J=x1/1
   B=a1g1
   gmt set MAP_FRAME_TYPE=inside MAP_GRID_PEN_PRIMARY=0p,red,.
   gmt psbasemap -R$R -J$J -B$B -BWSEN -K -O -Xf0c -Yf0c >> $PS

   gmt psxy -R$R -J$J -T -O >> $PS

   rm -f gmt.conf gmt.history

关于辅助底图的几个说明：

#. 默认纸张为A4，纸张大小为210x297mm，则对于Landscape模式：\ ``-R0/29.7/0/21``\ ；对于Portrait模式，\ ``-R0/21/0/29.7``\ 。
#. 投影方式为\ ``-Jx1/1``\ ，即线性投影，且纸张中的1厘米表示数据中的1；则\ ``-R0/29.7/0/21``\ 与\ ``-Jx1/1``\ 一起使用的结果是：辅助底图恰好占据整个纸张。
#. ``-Ba1g1``\ 、\ ``MAP_FRAME_TYPE``\ 以及\ ``MAP_GRID_PEN_PRIMARY``\ 的设置，都是为了增强辅助底图的实用性；
#. ``psbasemap``\ 将辅助底图绘制出来，由于需要注意这里-X和-Y的使用；

最终得到的效果如下图（辅助底图的（0,0）点与纸张左下角重合，（29.7,21）点与纸张右上角重合）：

.. figure:: /images/2014122802.jpg
   :align: center
   :width: 800 px
   :alt: auxiliary basemap

辅助底图的出现，给整个纸张加上了网格，因而我们可以很容易的大概确定出纸张上任意一点的坐标。比如这里需要的四个点的坐标分别为（10.5，10.5）、（14.5,11.5）、（10.5,8.5）和（14.5,3.5）。

.. code-block:: bash

   #!/bin/bash
   PS=test.ps
   R=0/10/0/10
   J=X10c

   gmt psxy -R$R -J$J -T -K > $PS

   # 绘制左底图
   gmt psbasemap -R$R -J$J -B2 -BWSen -K -O >> $PS
   # 绘制红色矩形
   gmt psxy -R$R -J$J -W1.5p,red -K -O -L >> $PS << EOF
   6 8
   8 8
   8 6
   6 6
   EOF

   R=6/8/6/8
   J=X8c
   # 绘制右底图
   gmt psbasemap -R$R -J$J -B0.5 -BwSEn -K -O -X12c -Y1c >> $PS

   # 绘制辅助底图
   R=0/29.7/0/21
   J=x1/1
   B=a1g1
   gmt set MAP_FRAME_TYPE=inside MAP_GRID_PEN_PRIMARY=0p,red,.
   gmt psbasemap -R$R -J$J -B$B -BWSEN -K -O -Xf0c -Yf0c >> $PS

   # 在辅助底图坐标系中绘制两条连线，注意-Xf0c和-Yf0c
   gmt psxy -R$R -J$J -W2p,blue -K -O -Xf0c -Yf0c >> $PS << EOF
   >
   10.5 10.5
   14.5 11.5
   >
   10.5 8.5
   14.5 3.5
   EOF

   gmt psxy -R$R -J$J -T -O >> $PS

   rm -f gmt.conf gmt.history

效果图如下：

.. figure:: /images/2014122803.jpg
   :align: center
   :width: 800 px
   :alt: auxiliary basemap

实际的图件中，肯定是不能有辅助底图以及相关的网格线的，所以在添加注释和标注之后，还需要将辅助底图删除，只需要将上面的脚本中注释或删除掉如下两行即可。

.. code-block:: bash

   # gmt set MAP_FRAME_TYPE=inside MAP_GRID_PEN_PRIMARY=0p,red,.
   # gmt psbasemap -R$R -J$J -B$B -BWSEN -K -O -Xf0c -Yf0c >> $PS

需要强调两点：

#. 绘制连线的时候是使用了辅助底图的，注释掉上面两个命令只是使得辅助底图不显示而已；
#. 使用辅助底图会修改gmt.conf和gmt.history文件，因而辅助底图的相关命令应放在所有命令的最后，且在脚本结束时要记得删除gmt.conf和gmt.history以保证不会干扰到其他绘图命令的效果。

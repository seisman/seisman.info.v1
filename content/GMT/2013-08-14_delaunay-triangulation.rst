GMT之用triangulate进行Delaunay三角剖分
######################################

:date: 2013-08-14 17:07
:author: SeisMan
:category: GMT
:tags: GMT命令
:slug: delaunay-triangulation
:summary: 三角剖分程序

.. contents::

三角剖分简介
============

什么是Delaunay三角剖分？我也不清楚。想要知道细节可以看这篇\ `博文`_\ 、\ `维基百科`_\ 以及一堆相关文献。

不负责任地简单概括一下：平面上有点集P，点集P中任意三个不共线的点就可以连成一个三角形DT(P)。Delaunay三角剖分使得点集P中没有点位于任意三角形DT(P)的外接圆内，同时保证三角形的所有角中的最小角度最大。

下图摘自于维基百科，黑点代表平面上的点集，黑实线为Delaunay三角剖分的结果，灰色圆为三角形的外接圆，红点为外接圆的圆心。通过Delaunay三角剖分，利用平面上的点集构建了新的三角单元。

.. figure:: /images/2013081401.png
   :width: 600px
   :alt: Figure 1


点集的三角剖分，主要运用于数值分析（比如有限元分析中的单元划分）以及图形学。搜索了一下，发现其还可以用于生成Voronoi图、指纹匹配、成像、破洞修复、变电站选址。。。

语法
====

::

 triangulate 4.5.9 [64-bit] - Optimal (Delaunay) triangulation of Cartesian xyz-data [Watson]

 usage: triangulate <infiles> [-Dx|y] [-E<empty>] [-F] [-G<grdfile>]
 [-H[i][<nrec>]] [-I<xinc>[u][=|+][/<yinc>[u][=|+]]] [-J<params>]
 [-R<west>/<east>/<south>/<north>[r]] [-V] [-:[i|o]]
 [-b[i|o][s|S|d|D[<ncol>]|c[<var1>/...]]]
 [-f[i|o]<colinfo>] [-m[i|o][<flag>]]

选项说明
========

-H、-J、-R、-V、-：、-bi、-bo、-f选项与其他命令含义相同或相似。

与文件相关的选项：

-  infile：包含点坐标，每行代表一个点，第一行对应的点编号为0，可以是ASCII或二进制
-  -Z：二进制文件是两列还是三列

默认输出的每个记录是每个三角形的三个顶点的id号（文件中第一个点id=0），可以通过下面两个选项修改输出：

-  -m：将整个三角剖分的结果以多个线段表示，每个线段记录的第一个字符为">"，这样的输出可以用于psxy绘图
-  -Q：输出Voronoi单元的边。（需要-m和-R）

下面的选项可以将三角剖分的结果保存为网格文件：

-  -G：将三角剖分的结果划分为等间距的网格文件（-R，-I）
-  -D：不理解。。。
-  -E：设置网格空node处的值，默认为NaN
-  -F：设置网格为pixel node registration，默认为gridline registration
-  -I：设置网格间距

例子
====

数据在这里：\ `station`_\ ，貌似对应了一个地区的台站位置。

::

 triangulate station.txt > v.list

v.list的内容大概如下：

::

 1 2 5
 12 16 27
 0 6 7
 9 13 15
 9 10 15
 0 3 7

每行三列，代表三角形的三个顶点的id，注意输入文件中第一个点的id为0。

::

 triangulate station.txt -m >v.list

这个时候的输出为线段，如下：

::

 > Edge 0-3
 120.065 30.153
 120.1065 29.8935
 > Edge 0-5
 120.065 30.153
 119.4813 29.9489
 > Edge 0-6
 120.065 30.153
 120.05 30.386
 > Edge 0-7
 120.065 30.153
 120.3765 30.3086

以>开始的行代表一个新记录，Edge 0-3指定了顶点为0和3，然后给出这两个点的坐标。这个文件可以直接用于psxy绘图。

可以利用psxy直接绘制v.list文件：

::

 psxy v.list -m -R118.4/122.5/27.4/30.9 -JM5i -W0.5p -B1 -V> voronoi.ps

当然也可以利用管道，而不生成中间文件v.list：

::

 triangulate station.txt -m | psxy -m -R118.4/122.5/27.4/30.9 -JM5i -W0.5p -B1 -V delaunay.ps

效果如下：

.. figure:: /images/2013081402.jpg
   :width: 600px
   :alt: Figure 2

可以用-Q选项生成Voronoi图：

::

 triangulate zj_stn.txt -m -Q -R118.4/122.5/27.4/30.9 | psxy -m -R -JM6.5i -W0.5p -B1 -V -P> voronoi.ps

.. figure:: /images/2013081403.jpg
   :width: 600px
   :alt: Figure 3

其他
====

-  -Q选项的输出可以用于绘制Voronoi图，但是这个选项依赖于另一个算法，在编译GMT时默认使用Watson[1982]，这个选项需要使用Shewchuk [1996]。
-  关于-G选项生成网格，应该与一般网格没有区别。
-  在使用triangulate命令时可以指定地图投影（-R和-J），这样数据点首先会进行投影，然后再进行三角剖分(这里可能是球面上的三角剖分)。

.. _博文: http://www.cnblogs.com/soroman/archive/2007/05/17/750430.html
.. _维基百科: http://en.wikipedia.org/wiki/Delaunay_triangulation
.. _station: http://seisman.qiniudn.com/downloads/station.txt

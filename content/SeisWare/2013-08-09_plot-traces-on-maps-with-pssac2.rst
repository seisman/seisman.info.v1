pssac2之在地图上绘制地震图
##########################

:date: 2013-08-09 00:10
:author: SeisMan
:category: 地震学软件
:tags: pssac2
:slug: plot-traces-on-maps-with-pssac
:summary: 利用pssac2在地图上绘制地震图。

.. contents::

依然利用《\ `pssac绘图之地震剖面图 <{filename}/SeisWare/2013-08-06_plot-profile-with-pssac.rst>`_\ 》中生成的数据。

看上去pssac可以实现的功能pssac2也都可以实现，有兴趣的可以把前面的那些命令用pssac2试试。这里还是主要把精力放在如何在地图上绘制地震图上吧。

脚本
====

.. code-block:: bash

 #!/bin/bash
 #
 # An simple example bash shell script to show
 # how to use pssac2 to plot traces on maps
 #
 # Author: SeisMan @ seisman.info
 # E-mail: seisman.info@gmail.com
 #

 pscoast -JM6i -R-120/-60/40/65 -B15/5 -Glightblue -W0.01p -A1000 -K -V > a.ps

 psxy -J -R -B -Sa10p -Gblack -K -O -V >> a.ps << EOF
 -114.5917 62.4797
 -74.5300 44.5483
 -93.7022 50.8589
 -104.0362 44.1204
 EOF

 pssac2 -J -R -Ent-5 -M1 -L1000 -D0.1/0.1 -O -V >> a.ps << EOF
 ntkm.z -114.5917 62.4797 0.1p,red
 nykm.z -74.5300 44.5483 0.1p,black
 onkm.z -93.7022 50.8589 0.1p,blue
 sdkm.z -104.0362 44.1204 0.1p,yellow
 EOF

.. figure:: /images/2013080901.jpg
   :alt: Map
   :width: 700 px

简单解释
========

-  pscoast用于绘制背景，-G指定海洋颜色，-W指定海岸线线宽，-A指定只绘制面积1000km^2以上的岛屿（不然就密密麻麻一片黑了）。
-  psxy在四个台站位置分别绘制一个黑色五角星
-  pssac2不再显式指定-J和-R了，直接继承前面命令的参数，pssac中是不能这样的，因为pssac中横轴是时间。
-  通过指定-L1000选项，设定地图上MEASURE\_UNIT长度代表1000s，即给出了地图的经度坐标与地震图的时间坐标之间的对应关系。我的系统中的默认MEASURE\_UNIT是cm，前面-JM6i强制指定了地图大小的单位为6英寸，理论上这个单位只适用于投影方式，不会改变MEASURE\_UNIT的，但是看上去trace的1000s好像长度的确是1 inch，这是个小问题（也许是我看错了），实际画图的时候肯定要不断修改-L的值以达到最好的效果的。
-  在pssac中-E和-M是可选的，但在pssac2中-E和-M好像是必须的，-M指定振幅，-E好像用处不大。
-  本来想使用-l来看看timescale是什么的，但是一直没有调出来，暂时放弃。
-  要绘制的地震图通过给出文件名，x、y位置以及画笔属性来指定。实际应用中x、y通常是台站的经纬度。
-  -D指定了trace相对于给定的x、y位置的偏移量。由于一般x、y是台站经纬度，将trace直接画在台站那里总是不太好看的，稍微偏一点点位置视觉效果会更好。
-  pssac2自己的选项中所有的距离或长度的单位都是MEASURE\_UNIT，你可以指定-D1/1，但是不能像GMT那样指定-D1i/1i。

总结
====

pssac2在绘制单个地震图以及地图剖面上与pssac差不多，用法上稍微多一些，也许掌握起来会麻烦一点；在地图上绘制地震图这一点，pssac必须通过自己手动指定-X和-Y偏移量，或者通过台站位置以及地图范围计算偏移量的方式将trace放在合适的位置，pssac2在这一点上要方便非常多。

等震中距线的绘制
################

:date: 2014-05-21 14:30
:author: SeisMan
:category: GMT
:tags: GMT4, GMT脚本
:slug: plot-equal-distance-lines

等值线法
========

.. code-block:: bash

    #!/bin/bash
    R=g
    J=H25c
    B=60/30
    PS=map.ps
    evlo=160
    evla=20
    
    psxy -R$R -J$J -T -K > $PS
    # 绘制底图
    pscoast -J$J -R$R -B$B -Dc -A10000 -Glightblue -K -O >> $PS
    # 绘制震中位置
    echo $evlo $evla | psxy -J$J -R$R -Sa1c -Gred -K -O >> $PS
    
    # 计算全球每点到震中的距离
    grdmath -R$R -I1 $evlo $evla SDIST 111.19 DIV = dist.nc
    # 绘制等值线
    grdcontour dist.nc -J$J -A15 -L0/60 -K -O >> $PS

    psxy -J$J -R$R -T -O >> $PS
    
    rm dist.nc

此法原理很简单，首先将全球（-Rg）划分为间距为1度（-I1）的网格，对于网格中的每个格点计算其到到震中的距离（单位km），然后除以111.19将单位转换为度，将此值记为该网格点的z值，最终结果保存在网格文件\ ``dist.nc``\ 中，最后使用\ ``grdcontour``\ 绘制等值线。\ ``grdcontour``\ 命令的可空性很强，细致的微调可以得到更好的效果。

.. figure:: /images/2014052101.jpg
   :width: 700 px
   :alt: equal-distance-with-contour

椭圆法
======

.. code-block:: bash

    #!/bin/bash
    R=g
    J=H25c
    B=60/30
    PS=map2.ps
    evlo=160
    evla=20
    
    psxy -R$R -J$J -T -K > $PS
    pscoast -J$J -R$R -B$B -Dc -A10000 -Glightblue -K -O >> $PS
    echo $evlo $evla | psxy -J$J -R$R -Sa1c -Gred -K -O >> $PS

    # 15度等值线
    echo $evlo $evla 0 3335.8 3335.8 | psxy -J$J -R$R -SE -K -O -W1p,red >> $PS 
    # 37.5度等值线
    echo $evlo $evla 0 8339.6 8339.6 | psxy -J$J -R$R -SE -K -O -W1p,blue >> $PS 
    
    psxy -J$J -R$R -T -O >> $PS

该方法使用了\ ``psxy``\ 的\ ``-SE``\ 选项。-SE本是用于绘制椭圆的，这里被用来绘制圆以表示等震中距线。

该命令需要的输入数据有5个，分别是椭圆的中心经度、中心纬度、短轴的方位角、短轴长度（km）、长轴长度（km）。此处另短轴长度与长轴长度相等，即得到特殊的椭圆---圆。

想要绘制一条震中距为15度的等震中距线，需要注意如下几点：

- 对于圆来说，其长轴=短轴=直径=30度；
- 长轴和短轴的单位是km，因而需要将震中距乘以111.19转换为km。

.. figure:: /images/2014052102.jpg
   :width: 700 px
   :alt: equal-distance-with-ellipses

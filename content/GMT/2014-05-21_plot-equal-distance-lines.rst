等震中距线的绘制
################

:date: 2014-05-21 14:30
:modified: 2015-02-26
:author: SeisMan
:category: GMT
:tags: GMT4, GMT脚本
:slug: plot-equal-distance-lines

.. contents::

这里给出两个绘制等震中距线的方法，两种方法各有利弊，按需选取。

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
    gmtset ELLIPSOID Sphere
    grdmath -R$R -I1 $evlo $evla SDIST KM2DEG = dist.nc
    # 绘制等值线
    grdcontour dist.nc -J$J -A15 -L0/60 -K -O >> $PS

    psxy -J$J -R$R -T -O >> $PS

    rm dist.nc

grdmath命令首先将全球（-Rg）划分为间隔为1度（-I1）的网格，并计算每个网格点到固定点evlo、evla的距离（单位为km），然后将KM转换为度。则最终生成的dist.nc中包含了每个网格点到固定点的距离。最好使用grdcontour命令绘制等值线，即等震中距线。grdcontour命令的众多选项可以对具体的等值线效果做微调。

对grdmath的若干说明：

#. GMT 4.5.11及之前的版本中，SDIST的返回值单位为度；
#. GMT 4.5.12及之后的版本中，SDIST的返回值单位为km；
#. GMT 5中，SDIST的返回值单位为km；
#. 从GMT 4.5.12开始，新增了KM2DEG操作，但4.5.12版本的KM2DEG有问题；
#. KM2DEG操作仅适用于球状地球，因而要设置ELLIPSOID为Sphere；
#. KM2DEG近似等效于\ ``111.19 DIV``\ ；

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

修订历史
========

- 2014-05-21：初稿；
- 2015-02-26：grdmath在不同GMT版本下表现不同；

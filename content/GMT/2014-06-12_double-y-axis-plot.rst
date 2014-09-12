GMT绘制双Y轴
############

:author: SeisMan
:date: 2014-06-12 20:20
:category: GMT
:tags: GMT4
:slug: double-y-axis-plot

所谓双Y轴，指的是在一张图中同时使用两个完全不同的Y轴。这种类型的图在某些情况下会用到。

这样一张图的绘制其实很简单，只需要绘制两个basemap即可。第一个basemap只绘制X轴和左Y轴；第二个只绘制右Y轴。

GMT的-B选项中，WESN分别表示在四个坐标轴上显示坐标轴及标注文字、刻度；小写news表示在四个坐标轴上只显示坐标轴和刻度，不标注文字；若某个坐标轴上没有相关参数，则什么都不画。因而第一个basemap使用SW，第二个basemap使用E。

.. figure:: /images/2014061201.jpg
   :width: 800 px
   :alt: double-Y-axis-plot

.. code-block:: bash

    #!/bin/bash

    Rx=0/10
    R1=$Rx/0/1000
    R2=$Rx/0/1
    Jx=15c
    J1=X$Jx/10c
    J2=X$Jx/6c
    PS=doubleAxis.ps
    
    # 写入PS头，这里的J和R可以任意
    psxy -J$J1 -R$R1 -T -K -Xc -Yc > $PS

    # 绘制左Y轴
    psbasemap -J$J1 -R$R1 -Ba2f1:X:/a100f50:"Left   Y":WS -K -O >> $PS

    # 绘制一堆与左Y轴相关的数据
    # ...
    psxy -J$J1 -R$R1 -Sc0.2c -Gred -K -O << EOF >> $PS
    1 100
    3 300
    5 500
    7 700
    9 800
    EOF

    # 绘制右Y轴
    psbasemap -J$J2 -R$R2 -Ba2f1/a0.2f0.1:"Right    Y":E -K -O >> $PS

    # 绘制一堆与右Y轴相关的数据
    # ...
    psxy -J$J2 -R$R2 -Sa0.2c -Gblue -K -O << EOF >> $PS
    1 0.5
    3 0.3
    5 0.7
    7 0.2
    9 0.6
    EOF

    # 写入PS尾，这里的J和R可以任意
    psxy -J$J1 -R$R1 -T -O >> $PS

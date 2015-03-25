GMT5进阶之图层透明效果
######################

:date: 2013-11-10 00:14
:author: SeisMan
:category: GMT
:tags: GMT脚本, GMT选项, GMT5
:slug: gmt5-transparency

.. contents::

设置图层的透明度，大概是GMT5新增的绘图功能中最大的一个亮点。

-t选项
======

-t是一个GMT5通用选项，用于设置图层透明度，其用法很简单。\ ``-ttrans``\ ，其中\ ``trans``\ 可以取0-100的值，0代表完全不透明，100代表完全透明。需要注意的是PS是不支持透明特性的，透明的效果只能在PDF中看到。

一个例子
========

这个脚本严格遵循GMT5的语法。

.. code-block:: bash

 #!/bin/bash
 R=g
 J=H20c
 PS=trans.ps

 # 打开GMT5
 gmt psxy -R$R -J$J -T -K -UBL/0/0 > $PS

 # 绘制海岸线
 gmt pscoast -J$J -R$R -Bpx60 -W1/0.2p -N1 -K -O >> $PS

 # 绘制第一个不透明矩形框
 gmt psxy -J$J -R$R -W1p -L -Gred -K -O << EOF >> $PS
 100 -20
 100 20
 140 20
 140 -20
 EOF

 # 绘制第二个透明矩形框
 gmt psxy -J$J -R$R -W1p -L -Gred -t60 -K -O << EOF >> $PS
 280 -20
 280 20
 320 20
 320 -20
 EOF

 # 关闭GMT
 gmt psxy -R$R -J$J -T -O >> $PS

转换为其他格式
==============

PS格式不支持透明，所以在PS文件中看不到任何透明效果。

ps2raster可以将PS文件转换为bmp、eps、pdf、png、jpeg、ppm、tif格式，但是只有PDF格式中可以看到透明效果。

::

    gmt ps2raster -A -P -Tf trans.ps

如果想要其他格式怎么办？再用convert将PDF转换为其他格式即可::

    convert -density 300 trans.pdf trans.jpg

注意：

- 是两步走，先用ps2raster将PS转换为PDF，再用convert将PDF转换为其他格式。
- 直接用convert将PS转换为其他任何格式（包括PDF），都没有透明效果。

效果图
======

.. figure:: /images/2013111001.jpg
   :align: center
   :alt: fig
   :width: 600 px

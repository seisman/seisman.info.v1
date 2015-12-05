GMT之底图边框类型
#################

:date: 2013-08-25 01:00
:modified: 2014-07-09
:author: SeisMan
:category: GMT
:tags: GMT技巧, GMT4
:slug: gmt-basemap-type

BASEMAP_TYPE是GMT的默认参数中可以修改的一个，其可以取inside、graph、plain和fancy中的任意一个，默认为fancy（也就是GMT画图中常见的火车道边框）。

下面给出例子：

.. code-block:: bash

 #!/bin/bash
 R=0/5/0/5
 PS=test.ps
 # 默认标题太大，影响效果，这里改小一点
 gmtset HEADER_FONT_SIZE 15p

 # 设置类型为plain
 gmtset BASEMAP_TYPE plain
 psbasemap -JX1.8i -R$R -B1/1":.Plain:" -K > $PS

 # 设置类型为fancy，后面的加号使得边框的四角为圆角
 gmtset BASEMAP_TYPE fancy+
 psbasemap -JM1.8i -R$R -B1/1":.Fancy:" -K -O -X2.5i >> $PS

 # 设置类型为inside
 psbasemap -JX1.8i -R$R -B1/1:".inside:" -K -O -X2.5i --BASEMAP_TYPE=inside >> $PS

 # 设置类型为graph
 psbasemap -JX1.8i -R$R -B1/1WS":.graph:" -O -X2.5i --BASEMAP_TYPE=graph >> $PS

 rm .gmt*

可以用gmtset来修改GMT默认参数，也可以通过--PAR=value这样的方式设置。

在GMT4.5.9中，用gmtset设置BASEMAP_TYPE为inside或graph都会出现问题，这是bug，在4.5.10中已经修正。因而对于BASEMAP_TYPE为inside或者graph，目前只能采取--PAR=value这样的方式修改参数。

不同的投影方式，效果可能不同，比如-JX设置BASEMAP\_TYPE=fancy则不起作用。最终效果如下：

.. figure:: /images/2013082501.jpg
   :align: center
   :alt: BASEMAP TYPE

标题的位置没有做修改，是GMT自定义的结果。

备注
====

-  psxyz不支持BASEMAP\_TYPE=graph

修订历史
========

-  2013-08-25：初稿；
-  2013-10-05：gmtset无法设置BASEMAP_TYPE为inside和graph：已确定为Bug；
-  2013-10-05：psxyz支持graph类型；
-  2014-07-09： ``psbasemap`` 命令不需要输入文件，修正了脚本中的错误；

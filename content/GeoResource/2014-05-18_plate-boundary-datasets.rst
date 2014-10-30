板块边界数据集
##############

:date: 2014-05-18 10:00
:author: SeisMan
:category: 地球物理相关资源
:tags: 板块, 数据
:slug: plate-boundary-datasets

.. contents::

NUVEL板块边界数据
=================

下载地址：http://jules.unavco.org/GMT/

该数据集包含了15个主要的板块边界数据。其中：

- ``nuvel_1_plates.orig``\ ：最原始的数据，来自于NUVEL-1A包；
- ``nuvel_1_plates``\ ：在原始数据的基础上修正了一些小的错误；
- ``<plate-name>_plate``\ ：给出了板块plate-name与其它板块的分界线，即多段数据。
- ``<plate-name>.txt``\ ：给出了板块plate-name的轮廓，即相当于将<plate-name>_plate的数据进行整理使其成为一个封闭的曲线。

因而\ ``<plate-name>_plate``\ 文件中包含了最丰富的信息。

PS：数据文件中似乎是多段数据，以\ ``:``\ 作为每段分割标识，似乎在绘图时应该使用\ ``-m:``\ 选项，但实际上不使用也可以正常绘制（GMT 4.5.12），不确定其它版本是否需要\ ``-m:``\ 选项。

绘制全部边界
------------

.. code-block:: bash

    #!/bin/bash
    R=g
    J=W20c
    B=60/30
    PS=plate.ps

    psxy -R$R -J$J -T -K > $PS
    pscoast -R$R -J$J -B$B -Glightblue -K -O >> $PS
    psxy nuvel_1_plates -R$R -J$J -W1p,red -m: -K -O >> $PS
    psxy -R$R -J$J -T -O >> $PS


.. figure:: /images/2014051801.jpg
   :width: 700 px
   :alt: nuvel-plate-boundary

绘制单个板块轮廓
----------------

以绘制太平洋板块为例，将上面的脚本中\ ``nuvel_1_plates``\ 修改为\ ``Pacific.txt``\ 即可。

.. figure:: /images/2014051802.jpg
   :width: 700 px
   :alt: Pacific-plate-boundary

PB2003板块数据集
================

该数据集在NUVEL数据的基础上加入了38个更小的板块。

主页：http://peterbird.name/publications/2003_PB2002/2003_PB2002.htm

下载地址：http://peterbird.name/oldFTP/PB2002/

其包含如下数据：

- PB2002_boundaries.dig：给出了每两个相邻板块的交界数据；
- PB2002_plates.dig：给出每个板块的边界数据；
- PB2002_orogens.dig：造山带边界数据；
- PB2002_steps.dat：两个相邻板块交界处任一点的信息，包括边界类型，运动速度等信息。数据较复杂，需要仔细研究才能知道每列的含义。
- PB2002_poles.dat：每个板块的Poles。

PS：前三个数据都是多段数据，而且其数据格式相对来说也很复杂。直观上看似乎需要对数据先做一些格式上的转换才能使用GMT进行绘图，但实际操作中（GMT4.5.12），使用上面的脚本即可绘图，无法保证在其它版本也可行。

绘图
----

板块边界图（使用PB2002_boundaries.dig或PB2002_plates.dig均可）

.. figure:: /images/2014051803.jpg
   :width: 700 px
   :alt: pb2002-boundary

造山带边界

.. figure:: /images/2014051804.jpg
   :width: 700 px
   :alt: PB2002_orogens


板块边界与洋壳年龄
==================

将边界数据与洋壳年龄放在一起：

.. code-block:: bash

    #!/bin/bash
    R=d
    J=W20c
    B=60/30
    PS=age.ps
    psxy -R$R -J$J -T -K > $PS
    grdimage -R$R -J$J -B$B -Cage.cpt age.3.6.nc2 -K -O >> $PS
    pscoast -R$R -J$J -B$B -Glightblue -K -O >> $PS
    psxy PB2002_boundaries.dig.txt -R$R -J$J -W1p,black -K -O >> $PS
    psscale -Ba20 -Cage.cpt -D10.5c/-1c/15c/.35ch -K -O >> $PS
    psxy -R$R -J$J -T -O >> $PS

.. figure:: /images/2014051805.jpg
   :width: 700 px
   :alt: plate-boundary-and-ocean-age

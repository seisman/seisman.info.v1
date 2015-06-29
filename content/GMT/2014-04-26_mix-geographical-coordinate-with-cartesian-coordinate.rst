GMT技巧之地理坐标与笛卡尔坐标混合体
###################################

:author: SeisMan
:date: 2014-04-26 09:00
:modified: 2015-06-29
:category: GMT
:tags: GMT技巧, GMT5
:slug: mix-geographical-coordinate-with-cartesian-coordinate

.. contents::

提出问题
========

需要画一个沿着某个经线或纬线的深度剖面图，即X轴表示经度或纬度，Y轴表示深度，如下图：

.. figure:: /images/2014042601.png
   :alt: mix-geographical-coordinate-with-cartesian-coordinate
   :width: 700px

分析问题
========

这张图比较特殊的地方在于，X轴是地理坐标，Y轴是笛卡尔坐标。最简单的办法是直接用线性投影\ ``-JX``\ 来绘制整张图，比如::

    gmt psbasemap -R40/50/0/600 -JX15c/-10c -Bx2 -By100 > mix.ps

效果如下图：

.. figure:: /images/2014042602.png
   :alt: mix-geographical-coordinate-with-cartesian-coordinate
   :width: 700px
   :align: center

显然，这张图还差了一点，X轴的坐标都没有“度”符号以及WSEN后缀，无法体现出其地理坐标的特征。

解决问题
========

解决办法如下::

    gmt set FORMAT_GEO_MAP +ddd:mmF
    gmt psbasemap -R40/50/0/600 -JX15cd/-10c -Bx2 -By100 > mix.ps

几点说明：

- ``FORMAT_GEO_MAP``\ 用于设置地理坐标的显示方式。这里的\ ``+ddd:mmF``\ 表示以“度:分”的形式显示，并加上EWSN后缀；
- ``-JX15cd/-10c``\ 设定了线性投影方式。X轴多了一个\ ``d``\ ，用于显式指定X轴为地理坐标；Y轴没有\ ``d``\ ，为正常的笛卡尔坐标；这里Y轴的长度是负值，表示Y值从上到下递增，以符合常见的深度的定义；
- GMT4同理，但GMT 4.5.13似乎存在bug，当使用\ ``-JX15cd/-10c``\ 时，X轴的标注的位置会出现偏差；尚未发布的GMT 4.5.14中该bug已被修复；

其它解决方法
============

下面列出最初对于这个问题的分析以及两种稍复杂的解决方案。虽说下面的两种方案更复杂了，但其思路与想法还是很有意思的，或许在其它问题上可以借鉴，因而将其列出。

分析问题
--------

#. 因为Y轴是线性坐标，所以必然只能选择线性投影，即\ ``-JX``\
#. 线性投影的情况下，图的主体很简单，关键在于X轴坐标的“度”符号以及后缀E上
#. 尝试将X轴和Y轴都当作线性坐标，然后对于X轴设置其\ **单位**\ 为特殊的“度”符号。此法看似可行，但实际上GMT内部设置了单位与标注之间的距离，通过单位设置的“度”符号明显离标注的距离较远，不太美观。
#. 为了使X轴有一个“度”符号，X轴必须当作地理坐标处理；而Y轴的范围已经超过了地理坐标的范围，所以必须当作线性坐标处理；
#. 综上，必须使用两个命令来绘制边框，分别绘制地理坐标的X轴（-BxxxSN）和线性坐标的Y轴（-BxxxEW）；
#. 关于如何绘制地理坐标的X轴，有两种解决办法。

解决问题
--------

法1
~~~

.. code-block:: bash

   #/bin/bash
   Rx=40/50    # X轴范围
   Ry=0/600    # Y轴范围
   R=$Rx/$Ry
   B=2/100     # 间隔
   J=X15c/10c
   PS=map.ps

   psxy -R$R -J$J -T -K > $PS   # 写入PS文件头

   psbasemap -R$R -J$J -B${B}SN -K -O --D_FORMAT='%g\260E' >> $PS    # 绘制X轴
   psbasemap -R$R -J$J -B${B}EW -K -O >> $PS     # 绘制Y轴

   # 这里放置其它绘图命令，不再使用B选项

   psxy -R$R -J$J -T -O >> $PS  # 写入PS文件尾
   rm .gmt*

这里绘制X轴时直接使用\ ``--D_FORMAT=%g\260E``\ ，使得在该命令中D_FORMAT的值为\ ``%g\260E``\ ，即设置显示浮点数时在其后加上“度”符号以及后缀“E”。

此法的优点在于简单，缺点在于后缀“E”是固定值，无法处理东西经同时存在的情况。

法2
~~~

.. code-block:: bash

   #/bin/bash
   Rx=40/50    # X轴范围
   Ry=0/600    # Y轴范围
   Rfake=0/1   # 假轴范围
   R=$Rx/$Ry
   B=2/100     # 间隔
   J=X20c/15c
   PS=map.ps

   psxy -R$R -J$J -T -K > $PS   # 写入PS文件头

   psbasemap -Rg$Rx/$Rfake -J$J -B${B}SN -K -O --BASEMAP_TYPE=plain >> $PS    # 绘制X轴
   psbasemap -R$R -J$J -B${B}EW -K -O >> $PS     # 绘制Y轴

   # 这里放置其它绘图命令，不再使用B选项

   psxy -R$R -J$J -T -O >> $PS  # 写入PS文件尾
   rm .gmt*

其它的说明
----------

#. GMT的B选项提供了这样一个功能，可以使用形如\ ``-Bgxmin/xmax/ymin/ymax``\ 的语法，其中\ ``g``\ 告诉命令即便使用\ ``-JX``\ 投影，也认为其是地理坐标。由于是地理坐标，“度”符号以及后缀“E”就很容易出来了
#. 使用\ ``-Bgxmin/xmax/ymin/ymax``\ 存在两个问题

   #. 虽然是线性投影，但是由于使用了地理坐标，GMT会默认将底图类型设置为fancy。这一点可以设置\ ``BASEMAP_TYPE``\ 等于\ ``plain``\ 来解决。
   #. Y轴被当作地理坐标，所以ymin和ymax的范围被限制在[-90,90]之内

#. 在此例中在绘制X轴时引入了一个假的Y轴\ ``0/1``\，以满足\ ``-Rgxmin/xmax/ymin/ymax``\ 形式中对ymin和ymax范围的限制。

这样，X轴和Y轴就都设计好了，接下来要做的就只是保证其它命令都不使用B选项即可。

修订历史
========

- 2014-04-26：初稿；
- 2014-04-26：修改脚本，解决了对Y轴范围的限制；Thanks to Chen Zhaohui；
- 2014-06-09：通过修改\ ``D_FORMAT``\ 以解决地理坐标的度符号；该方法由刘珠妹提供；
- 2014-07-09：找到了一种非常简单的方法来解决该问题；
- 2014-11-24：修正了\ ``--PLOT_DEGREE_FORMAT``\ 中的小问题；
- 2015-06-29：GMT4.5.13在解决该问题时有其他bug，这里使用GMT5；

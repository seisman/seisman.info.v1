不同比例尺曲线的画法
####################

:date: 2015-02-01
:author: SeisMan
:category: GMT
:tags: GMT技巧, GMT5
:slug: plot-multiple-lines-in-different-scales

本文由Joe Wang（cjmuqiao@163.com）投稿。

.. contents::

目标效果图
==========

.. figure:: /images/2015020101.png
   :width: 600px
   :align: center
   :alt: final figure

问题的提出
==========

在地磁场中X、Y、Z三分量幅值两两之间通常相差一两个数量级。如果直接将其画到相同比例尺的一个坐标系下，幅值小的通常就成了一条直线。此时需要将大幅值适当缩小，或者小幅值适当放大，即在一张图中绘制不同比例尺的曲线。在丁鉴海、卢振业、余素荣编著的《地震地磁学概论》中经常会看到不同比例尺的图。

使用GMT的-Jx选项，绘图时X坐标或Ｙ坐标就会根据数据的范围进行缩放，但这种放大或缩小的显示方式，会带来一个刻度值显示的问题。即：

#. 若将数据点用线连起来，由于数据点连线的时候不支持-N选项，则-R的范围必须包括整个Y轴的取值范围，Y轴的刻度会完全显示，这样有点啰嗦；
#. 若使用-S选项，将数据点用某种符号显示，此时再加上-N选项，则可以只显示部分比例尺，同时又可以把数据完整地表示出来，但是这样的散点图看起来断断续续的，无法连接起来；

解决思路
========

#. 使用psxy将数据点用线连起来，此时不绘制刻度；
#. 选择要绘制的刻度的范围，并使用psbasemap绘制部分数据的Y轴刻度，在此之前需要仔细计算坐标原点在Y轴的偏移量。

脚本
====

- 软件环境：GMT5 windows版，gawk
- 使用命令：psxy, psbasemap, gmtmath, gawk等

.. code-block:: batch

    set sta=CHL
    set day=20120101
    set ps=%sta%%day%.ps
    set Rhour=0/24/0/5
    set Rsec=0/86400/0/5
    set Jhour=x0.72/0.1
    set Jsec=x0.0002/0.1

    REM preparing the input data
    REM 1. calculate mean value
    REM 2. subtract mean value from original data
    REM 3. output line number and data
    gmt gmtmath CHL2_20120101Hx.dat CHL2_20120101Hx.dat MEAN SUB = | gawk "{print NR, $1}" > x.dat
    gmt gmtmath CHL2_20120101Hy.dat CHL2_20120101Hy.dat MEAN SUB = | gawk "{print NR, $1}" > y.dat
    gmt gmtmath CHL2_20120101Z.dat CHL2_20120101Z.dat MEAN SUB = | gawk "{print NR, $1}" > z.dat

    gmt psxy -R%Rhour% -J%Jhour% -T -K -P >%ps%

    REM plot x-axis
    gmt psbasemap -R%Rhour% -J%Jhour% -Bxa2f1+lTime/hour -Bya5 -BS -K -O >>%ps%
    gmt psbasemap -R%Rsec% -J%Jsec% -Bxa7200f3600+lTime/s -Bya5 -BS -Y2c -O -K >>%ps%

    REM plot Z
    gmt psxy z.dat -R0/86400/-20/15 -Jx0.0002/0.1 -O -K>>%ps%
    REM plot scale of z data
    gmt psbasemap -R0/86400/0/5 -J -Y2c -Bya5 -BW+t"@%%12%%\104@%%6%%Z" -K -O >>%ps%

    REM plot Hy
    gmt psxy y.dat -R0/86400/-400/400 -Jx0.0002/0.005 -Wblue -O -K >>%ps%
    gmt psbasemap -R0/86400/100/200 -J -Y2.5c -Bya100+l"nT" -BW+t"@;blue;@%%12%%\104@%%6%%Y" --FONT=blue --MAP_DEFAULT_PEN=+blue --MAP_TITLE_OFFSET=0p -O -K >>%ps%

    REM plot Hx
    gmt psxy x.dat -R0/86400/-55/30 -Jx0.0002/0.05 -Wred -O -K >>%ps%
    gmt psbasemap -R0/86400/10/20 -J -Y3.25c -Bya10 -BW+t"@;red;@%%12%%\104@%%6%%X" --MAP_TITLE_OFFSET=0p --FONT=red --MAP_DEFAULT_PEN=+blue -O -K >>%ps%

    gmt psxy -R%Rhour% -J%Jhour% -T -O >>%ps%

    del x.dat y.dat z.dat
    del gmt.history

一些说明：

- ``gmtmath``\ 命令实现是一个逆波兰式的计算器，此处其作用在于先计算数据的均值，然后从原始数据中减去，并将计算得到的结果通过管道传送给gawk；
- 绘制每个数据时，分别使用了两个命令，其中psxy用于绘制数据，而psbasemap用于绘制比例尺；
- 脚本中的参数的选择是有技巧，也是有规律的，下面会说明；
- 脚本中大部分数值都是可以从数据中自动计算得到的，因而将脚本改一改就可以实现完全的自动化；本文的脚本中没有对此进一步实现，如数据范围，移动距离等都是硬编码在脚本中；
- 命令中使用了一些额外的选项，来达到更好的绘图效果；

该脚本中某些参数的选取是很有技巧的，以Z分量数据为例：

- psxy命令中\ ``-R0/86400/-20/15``\ 是Z数据的范围，其值可以通过\ ``gmtinfo``\ 命令自动获得；
- psxy命令中\ ``-Jx0.0002/0.1``\ ，即对于Y轴而言，数据的1，在图上是0.1厘米，则Z数据的35的范围，对应于图上3.5厘米；
- 为了在Y轴的0到5处绘制一个比例尺，需要使用psbasemap命令，该命令有两个需要注意的地方：

  - ``-R0/86400/0/5``\ 设定了Y轴范围为0到5；
  - 为了在真正的0处绘制比例尺，需要移动坐标系原点，此处的移动距离为\ :math:`(0-(-20))*0.1=2cm`\ ，即\ ``-Y2c``\ 选项；

修订历史
========

- 2015-02-01：Joe Wang投稿；
- 2015-02-01：SeisMan整理语句、优化脚本；
- 2015-02-02：使用FONT和MAP_DEFAULT_PEN代替其他参数；

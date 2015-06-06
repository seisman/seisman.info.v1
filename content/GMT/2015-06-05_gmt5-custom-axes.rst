GMT5自定义坐标轴
################

:date: 2015-06-05
:author: Joe Wang
:category: GMT
:tags: GMT5, GMT技巧
:slug: gmt5-custom-axes

问题的提出
==========

GMT绘图时可以使用-B选项指定每个坐标轴的刻度、标注以及网格线。默认情况下的设置有时可能无法满足需求，比如想要在特定位置设置刻度，比如任意格式的日期、非log10的刻度等，就需要自己设置了。

解决方案
========

GMT5的-B选项，使用\ ``-B[p|s]x|ycYourTickFileName``\ 语法可以自定义轴的标注及刻度。

示例
====

想要画一张中国西南地区2008~2013年地震活动性的XY图，要求：

#. X坐标的Primary标注是yyyymmdd日期格式；
#. Secondary刻度位于每个季度的最后一天，比如，2008年第一季度20080331，第二季度20080630，第三季度20080930。

代码如下：

.. code-block:: bash

   input=chuandian_eq.txt
   title="Southwest China Seismicity"
   PS=chuandian_seismicity.ps
   J=X6i/2i
   R=1/2192/3/9

   gmt psbasemap -J$J -R$R -BWSen+t"$title"  -Bya1f0.5+lMagnitude -BpxcDateTick_px.txt -P -K > $PS
   gmt psbasemap -J$J -R$R -BsxcDateTick_sx.txt -K -O >> $PS
   awk '{print $1, $3}' $input | gmt psxy -JX6i/2i -R1/2192/3/9 -Sc0.1c -W1p,black -O >> $PS
   rm gmt.*


成图效果：

.. figure:: /images/2015060601.png
   :width: 600 px
   :alt: custom axes
   :align: center


代码说明：

#. ``chuandian_eq.txt``\ 中包含了中国西南2008~2013年大于等于4级地震事件，文件有三列，第一列是从20080101为第一天起算的日期序号，第二列是日期，第三列是震级，格式如下::

        32 20080201 4.800000
        47 20080216 4.400000
        58 20080227 5.000000
        95 20080404 4.100000
        ...

#. ``DateTick_px.txt``\ 用于控制Primary标注。其内容有三列，第一列是标注的X坐标，第二列可以是a或f或g，这里使用的是a，表示当前文件控制的是标注(annotations)，第三列是用户自定义的要显示的标注，如::

        1 a 20080101
        367 a 20090101
        732 a 20100101
        1097 a 20110101
        1462 a 20120101
        1828 a 20130101
        2192 a 20131231

#. ``DateTick_sx.txt``\ 用于控制Secondary刻度(frame)，其内容如下::

        91  f 20080331
        182 f 20080630
        274 f 20080930
        456 f 20090331
        547 f 20090630
        639 f 20090930
        821 f 20100331
        912 f 20100630
        1004 f 20100930
        1186 f 20110331
        1277 f 20110630
        1369 f 20110930
        1552 f 20120331
        1643 f 20120630
        1735 f 20120930
        1917 f 20130331
        2008 f 20130630
        2100 f 20130930

#. 似乎一个命令中只能使用一次自定义轴语法，故而这里使用了两次psbasemap，分别完成Primary标注和Secondary刻度的绘制，然后再调用psxy绘制具体数据。

修订历史
========

#. 初稿By Joe Wang(cjmuqiao@163.com)；

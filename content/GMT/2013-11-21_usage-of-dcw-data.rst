GMT5进阶之DCW数据的使用
#######################

:date: 2013-11-21 00:17
:author: SeisMan
:category: GMT
:tags: GMT技巧, GMT脚本, 数据, GMT5
:slug: usage-of-dcw-data

.. contents::

问题描述：想要绘制一个中国地图，区域范围为\ ``-R70/140/15/55``\ 。

代码1
=====

GMT4中可以使用pscoast命令的-N选项绘制国界，代码如下::

    pscoast -R70/140/15/55 -JM15c -B10 -N1/0.25p,blue -U > china.ps

效果图如下：

.. figure:: /images/2013112101.jpg
   :width: 600px
   :alt: Figure

这里的国界其实指的是陆地部分国家与国家之间的界限。显然这样的图不能用。

代码2
=====

还是用GMT4，加上海岸线，代码如下::

    pscoast -R70/140/15/55 -JM15c -B10 -N1/0.25p,blue -W1/0.3p,black -U > china.ps

效果如下：

.. figure:: /images/2013112102.jpg
   :width: 600px
   :alt: Figure

为了凸显海岸线与国界的区别，这里分别用了两种颜色。如果把二者调成一种颜色，粗细也相同，这样看上去也比较符合要求了，但是显得有点不伦不类了，当然有时候就是要这个效果。

下面用GMT5的DCW数据来画图。

pscoast
=======

关于pscoast在GMT4中的用法，可以参考《\ `GMT命令之用pscoast绘图海岸线 <{filename}/GMT/2013-10-28_gmt-pscoast.rst>`_\ 》。

GMT5的语法相对于GMT4有了不少变化，这里只说与DCW有关的-F选项，有关DCW数据的信息看上一篇博文。

::

    -Fcode1,code2,...[+l|L][+gfill][+ppen][+r|R[incs]]

-  想要绘制某个或某些国家的边界，可以使用\ ``code1,code2,...``\ 来选定，其中每个code代表不同的国家2位代码，用逗号分隔。
-  如果想要选择某个国家的某个省的边界，则code应该为\ ``country.state``\ 的格式，比如\ ``US.TX``\ 代表美国的Texas州。
-  如果想要选定整个大洲，则需要在洲代码\ **前**\ 加上等于号，比如code为"=AF"则表示选择整个非洲的数据；
-  追加\ **+l**\ 会列出国家名以及国家代码，不提取数据或绘图。（没试出效果）
-  追加\ **+L**\ 会列出州/省名，以及代码；
-  追加\ **+r**\ 会计算当前选择的边界数据的范围，并返回该范围；还可以加入xinc/yinc或者winc/einc/sinc/ninc来指定-B选项；（没理解）
-  追加\ **+R**\ 会计算当前选择的边界数据的范围，并向外扩展incs的范围；（没理解）
-  追加\ **+p**\ *pen*\ 指定边界的线条属性；
-  追加\ **+g**\ *fill*\ 指定填充属性；
-  一条命令中只能出现一次-F选项，如有特殊需求，需多次调用pscoast；
-  还有一些更复杂的规则，有些乱。。

例1
===

绘制-R70/150/10/60范围内的全部亚洲国家的边界::

    gmt pscoast -R70/150/10/60 -JM20c -B10 -F=AS -U > asia.ps

.. figure:: /images/2013112103.jpg
   :width: 600px
   :alt: Figure

例2
===

绘制中国边界（不含台湾、香港、澳门）::

    gmt pscoast -B10 -R70/150/10/60 -JM20c -FCN -U > china.ps

.. figure:: /images/2013112104.jpg
   :width: 600px
   :alt: Figure

例3
===

绘制内蒙古，并修改边界和填充颜色::

    gmt pscoast -B10 -R70/150/10/60 -JM20c -FCN.15+p1p,blue+gred -U > state.ps

.. figure:: /images/2013112105.jpg
   :width: 600px
   :alt: Figure

例4
===

导出中国内蒙古的边界数据::

    gmt pscoast -FCN.15 -M -V > neimenggu.dat

这里只需要使用-M选项即可。

例5
===

这个例子算是一个相对比较完整的中国地图，包含了必要的省界信息。距离出版可能还需要九段线数据，具体不讨论。

.. code-block:: bash
 #!/bin/bash
 R=70/150/15/55
 J=M20c
 B=10
 PS=china.ps
 gmt psxy -J$J -R$R -T -K -U > $PS

 for code in 11 12 13 14 15 21 22 23 31 32 33 34 35 36 37 41 42 43 44 45 46 50 51 52 53 54 61 62 63 64 65 71 91 92;
 do
     gmt pscoast -B10 -R$R -J$J -FCN.$code -K -O >> $PS
 done
 gmt psxy -R$R -J$J -T -O >> $PS

.. figure:: /images/2013112106.jpg
   :align: center
   :alt: fig
   :width: 600 px

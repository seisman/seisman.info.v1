中国行政区划数据下载
####################

:date: 2013-11-23 00:35
:author: SeisMan
:category: 地球物理相关资源
:tags: 数据, 格式转换, 网站, GMT4, GMT5
:slug: china-administrative-areas-data

.. contents::

GADM数据库
==========

GADM，是一个全球行政区划数据库。包括了几乎全部国家和地区的国界、省界以及更小的行政区划。

主页： http://www.gadm.org/

下载： http://www.gadm.org/country

数据格式包括：shapefile、ESRI geodatabase、RData、Google Earth kmz format。

在GADM中，country的定义为“any entity with an ISO country code”。关于ISO country code，可以参考维基百科相关\ `词条 <http://zh.wikipedia.org/wiki/ISO_3166-1>`_

因而想要下载完整的中国数据，实际上需要下载四个文件：China、Hong Kong、Macao、Taiwan。

数据格式选择shapefile。

可以在 http://www.gadm.org/version2 下载全球的行政区划数据，但非常不推荐。一方面是数据量偏大，另一方面是全球区划数据保存到一个文件中，难以整理。不如麻烦一点，需要哪个国家下哪个国家。

ogr2ogr
=======

GMT目前还不能识别shapefile格式的数据，因而就需要将shapefile格式转换为GMT可识别的格式。转换工具为ogr2ogr，这是GDAL自带的一个命令，因而如果正确安装了GMT5的话应该是很容易找到这个命令。

以中国数据为例：

解压数据
--------

::

    unzip CHN_adm.zip -d CHN_adm

解压后得到一堆文件，其中CHN_adm0.shp、CHN_adm1.shp、CHN_adm2.shp、CHN_adm3.shp为实际需要的shapefile数据，0、1、2、3为第零、一、二、三级行政区划，基本相当于国界、省界、市界、区界。（是这么个说法吧。。）

格式转换
--------

要将shp格式转换成GMT可识别的格式，可以使用gdal提供的ogr2ogr命令。Linux用户可以直接安装gdal，Windows用户则需要到gdal官网下载安装。另外，Windows用户也可以用ArcGIS等软件实现格式的转换。


具体的转换命令是从网上找到的，CHN_adm0为要生成的数据的文件名前缀，但是为什么要出现两次，表示很不解。

::

    ogr2ogr -f GMT -nln CHN_adm0 CHN_adm0 CHN_adm0.shp
    ogr2ogr -f GMT -nln CHN_adm1 CHN_adm1 CHN_adm1.shp
    ogr2ogr -f GMT -nln CHN_adm2 CHN_adm2 CHN_adm2.shp
    ogr2ogr -f GMT -nln CHN_adm3 CHN_adm3 CHN_adm3.shp

对于Hong Kong、Macao、Taiwan的数据做类似操作，最终生成了一堆以gmt结尾的文件。共计10个，如下：

::

    CHN_adm0.gmt  CHN_adm2.gmt  HKG_adm0.gmt  MAC_adm0.gmt  TWN_adm1.gmt
    CHN_adm1.gmt  CHN_adm3.gmt  HKG_adm1.gmt  TWN_adm0.gmt  TWN_adm2.gmt

绘图测试
========

国界
----

绘制国界需要全部0级数据。

PS1：数据为多段数据，在GMT4中需要使用\ ``-m``\ 选项，而GMT5已经可以自动处理多段数据，所以不需要使用\ ``-m``\ 选项。

PS2：中国的国界在有些地方是有争议的，因而使用该国界数据绘制的地图是不能在正规期刊上发表的。

.. code-block:: bash

   #!/bin/bash
   R=72/136/15/54
   J=M15c
   PS=china.ps

   gmt psxy -J$J -R$R -T -K -U > $PS
   gmt psxy -R$R -J$J CHN_adm0.gmt -K -O >> $PS
   gmt psxy -R$R -J$J HKG_adm0.gmt -K -O >> $PS
   gmt psxy -R$R -J$J MAC_adm0.gmt -K -O >> $PS
   gmt psxy -R$R -J$J TWN_adm0.gmt -K -O >> $PS
   gmt psxy -R$R -J$J -T -O >> $PS

代码运行过程中GMT会出现如下的警告(或错误？)

::

    psxy: Bad OGR/GMT: @D record has more items than declared by @N

猜测是ogr2ogr转换的问题。在我的系统环境该警告不影响绘图效果，但评论中@vv指出在他的系统环境下会导致图形无法绘制。

效果图（缺了南海的九段线数据）：

.. figure:: /images/2013112301.jpg
   :align: center
   :alt: fig
   :width: 600 px

省级行政区划
------------

与上面的代码几乎一样，1级数据中0级数据，所以直接绘制1级数据即可，Macao没有1级数据，直接用0级数据。

.. code-block:: bash

   R=72/136/15/54
   J=M15c
   PS=china.ps

   gmt psxy -J$J -R$R -T -K -U > $PS
   gmt psxy -R$R -J$J CHN_adm1.gmt -K -O >> $PS
   gmt psxy -R$R -J$J HKG_adm1.gmt -K -O >> $PS
   gmt psxy -R$R -J$J MAC_adm0.gmt -K -O >> $PS
   gmt psxy -R$R -J$J TWN_adm1.gmt -K -O >> $PS
   gmt psxy -R$R -J$J -T -O >> $PS

效果图：

.. figure:: /images/2013112302.jpg
   :align: center
   :alt: fig
   :width: 600 px


在上一篇博文《\ `GMT5进阶之DCW数据的使用 <{filename}/GMT/2013-11-21_usage-of-dcw-data.rst>`_\ 》中利用GMT自带的DCW数据也生成了类似的图，如下图。查看全图，对比一下会发现，两张图的细节方面还是有些区别的，本文的数据绘制的似乎包含了更多的细节（主要是小的岛屿）。这个就得根据需求去选择了，当然也有可能两个都是有问题的。

.. figure:: /images/2013112303.jpg
   :align: center
   :alt: fig
   :width: 600 px

市级行政区划
------------

转换出来的2级数据中包含了全国所有的市级边界，用编辑器打开查看内容就会发现，每条线段都有完整的注释，很容易从众多线段中提取出自己想要的部分。以安徽省为例，将与安徽有关的线段数据保存到文件Anhui_adm2.gmt中：

.. code-block:: bash

   R=114/120/29/35
   J=M10c
   PS=anhui.ps

   gmt psxy -J$J -R$R -T -K -U > $PS
   gmt psxy -R$R -J$J Anhui_adm2.gmt -K -O >> $PS
   gmt psxy -R$R -J$J -T -O >> $PS

上面的脚本有一个很不方便的地方：想要画一个省的2级数据，每次都要从CHN_adm2.gmt中手动提取该省的数据信息。下面的例子可以避免这种手动提取的过程，主要通过DCW数据和psclip命令，使用全国2级数据（CHN_adm2.gmt），但是只绘制安徽省的2级数据。

.. code-block:: bash

   R=114/120/29/35
   J=M10c
   PS=anhui.ps

   gmt psxy -J$J -R$R -T -K -U > $PS
   gmt pscoast -FCN.34 -M > Anhui_bnd.gmt
   gmt psclip -J$J -R$R Anhui_bnd.gmt -K -O >> $PS
   gmt psxy -R$R -J$J CHN_adm2.gmt -K -O >> $PS
   gmt psclip -C -K -O >> $PS
   gmt psxy -R$R -J$J -T -O >> $PS

脚本利用pscoast命令，将安徽省（代码为34）的省界数据导出到文件Anhui_bnd.gmt中，然后利用该文件进行clip，psxy绘图时虽然使用的是全国的2级数据CHN_adm2.gmt，但是只有安徽省内的部分会被绘制出来，最后还需要再次调用psclip以结束clip。

上面的这个脚本生成了一个中间文件Anhui_bnd.gmt，有强迫症的人是无法忍受这个的，因而上面的代码利用管道可以进一步简化为：

.. code-block:: bash

   R=114/120/29/35
   J=M10c
   PS=anhui.ps

   gmt psxy -J$J -R$R -T -K -U > $PS
   gmt pscoast -FCN.34 -M | gmt psclip -J$J -R$R -K -O >> $PS
   gmt psxy -R$R -J$J CHN_adm2.gmt -K -O >> $PS
   gmt psclip -C -K -O >> $PS
   gmt psxy -R$R -J$J -T -O >> $PS

上面三个脚本的最终结果基本是一致的，效果图如下：

注：三个脚本的成图效果是有差的，但是目前没有体现出来，在下一段“区级行政区划”中，可以更明显地看出区别。

.. figure:: /images/2013112304.jpg
   :align: center
   :alt: fig
   :width: 600 px

区级行政区划
------------

这里还是以安徽省为例，实际上只用3级数据即可，这里同时用了2级数据和3级数据，并且用不同的粗细和颜色来区分。需要注意，由于3级数据中包含了2级数据，所以下面的例子先画了3级数据，再用2级数据覆盖。如果画的顺序反了，效果就会差很多。

.. code-block:: bash

   R=114.8/120/29.3/36
   J=M14c
   PS=anhui.ps

   gmt psxy -J$J -R$R -T -K -U > $PS
   gmt psxy -R$R -J$J CHN_adm3.gmt -W0.5p,gray -K -O >> $PS
   gmt psxy -R$R -J$J CHN_adm2.gmt -W1p -K -O >> $PS
   gmt psxy -R$R -J$J -T -O >> $PS

效果图如下：

.. figure:: /images/2013112305.jpg
   :align: center
   :alt: fig
   :width: 600 px


下面的脚本利用了前面提到的psclip的方法：

.. code-block:: bash

   R=114.8/120/29.3/36
   J=M14c
   PS=anhui.ps

   gmt psxy -J$J -R$R -T -K -U > $PS
   gmt pscoast -FCN.34 -M | gmt psclip -J$J -R$R -K -O >> $PS
   gmt psxy -R$R -J$J CHN_adm3.gmt -W0.5p,gray -K -O >> $PS
   gmt psxy -R$R -J$J CHN_adm2.gmt -W1p -K -O >> $PS
   gmt psclip -C -K -O >> $PS
   gmt psxy -R$R -J$J -T -O >> $PS

效果图如下：

.. figure:: /images/2013112306.jpg
   :align: center
   :alt: fig
   :width: 600 px

将这两张图对比一下，容易发现，省界的部分线段明显变细了，这算是clip的一个缺点，使用省界数据进行clip，同时又要绘制省界数据，如何判断省界数据点是否在clip区域内部是个问题。

修订历史
========

- 2013-11-23：初稿；
- 2013-11-28：绘制2级和3级边界时，利用clip的方法以减少人工操作。Thanks to @yangtze。
- 2013-12-05：删除了数据包中的冗余隐藏文件，重新打包，提供多种格式下载。
- 2014-01-19：不推荐下载全球行政区划数据；
- 2015-04-11：存在个别IP恶意下载数据，导致我流量异常高，因而删除其他格式的数据压缩包，仅留下7z格式的，若仍出现流量异常，则删除该数据；
- 2015-05-01：流量依然异常，猜测是搜索引擎会对齐定时抓取导致的；虽然已经在七牛限制了文件的非本站访问，但似乎对压缩文件无效。故删除该数据，有需要的可以自己去转换格式；

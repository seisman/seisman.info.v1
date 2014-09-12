全球地壳模型crust 1.0
######################

:date: 2013-10-03 00:28
:author: SeisMan
:category: 地球物理相关资源
:tags: 数据, 网格, 参考模型, GMT4, GMT5
:slug: global-crustal-model-crust1

.. contents::

crust 1.0是一个常用的全球地壳模型，其从老版本的crust 5.1和crust 2.0升级得到。

基本信息
========

-  模型精度为1x1度；网格点定义在单元的中心，即纬度5-6度、经度150-151度的单元的值位于网格点(5.5,150.5)处；
-  模型中的海水深度和地形数据来自于NOAA的etopo1数据：etopo1是精度1弧分的全球起伏数据，crust 1.0从中提取了地形、海水深度和冰层厚度；对这些数据做处理得到1度精度的数据；
-  模型中包含了地壳的类型信息；
-  模型分为8层（也可以说是9层）；对于每个1x1度的单元，给出每层的Vp、Vs、$\\rho$；

模型分层
========

模型分为8层，分别为

#. 水层；
#. 冰层；
#. 上沉积层；
#. 中沉积层；
#. 下沉积层；
#. 上地壳；
#. 中地壳；
#. 下地壳；

同时还给出了Moho之下地幔的参数，地幔的速度模型来自于LLNL-G3Dv3；

下载
====

官方网址
--------

http://igppweb.ucsd.edu/~gabi/crust1.html

本站下载
--------

对官方版本（20130715）重新打包，修改如下：

-  删除了官方包中的若干垃圾文件；
-  加入了Makefile文件实现快速编译；

- `crust1.0.tar.gz <http://pan.baidu.com/s/1sYQ8j>`_
- `crust1.0-addon.tar.gz <http://pan.baidu.com/s/1oVgDX>`_

内容
====

内含说明文档readme一份；

内含模型文件四个：

-  crust1.bnds：各层上边界的深度；
-  crust1.vp：各层P波速度；
-  crust1.vs：各层S波速度；
-  crust1.rho：各层密度；

将全球划分1度x1度的单元，共计360\*180个单元；该单元的值保存在单元的中心格点上。整个网格按照经度优先的准则保存，第一个点的坐标为(89.5N,179.5W)。

文件中共360\*180=64800行，每行9列，给出每层的值；

内含Fortran代码三个，用于读取模型；

如何使用
========

getCN1point
-----------

获取任意一点的速度、密度剖面，具体用法如下例：

::

    $ ./getCN1point 
      .... reading all maps ... 
     enter center lat, long of desired tile (q to quit)
    50 100
    ilat,ilon,crustal type:   41 281
     topography:    1.6400000    
      layers: vp,vs,rho,bottom
       1.50   0.00   1.02   1.64
       3.81   1.94   0.92   1.64
       2.50   1.07   2.11   1.54
       0.00   0.00   0.00   1.54
       0.00   0.00   0.00   1.54
       6.10   3.55   2.74 -19.54
       6.30   3.65   2.78 -38.22
       7.00   3.99   2.95 -46.36
     pn,sn,rho-mantle:    7.99   4.44   3.30
     enter center lat, long of desired tile (q to quit)

getCN1maps
----------

-  生成各层的Vp、Vs、$\\rho$、层边界深度，计4\*9=36个文件，文件名map-vp[n]代表第n层的Vp，其他类似；
-  生成各层的厚度，计1\*8个文件，文件名类似map-th[n]；
-  生成沉积层厚度sedthk和地壳厚度crsthk。

所有文件均为ASCII格式；只有z值，没有x、y坐标，即z文件；

将z文件转换为GMT可识别的网格文件需要使用xyz2grd命令。下面的命令给出具体的转换方法：

使用-Rd或者-R-180/180/-90/90均可，但不可使用-Rg；注意-ZTLA选项的含义；

GMT语法::

    xyz2grd crsthk -Rd -I1/1 -Gout.grd -ZTLA -F -V

GMT5语法::

   gmt xyz2grd crsthk -Rd -I1/1 -Gout.grd -ZTLA -r -V

注意：GMT5.1.1的xyz2grd存在Bug，因而该命令仅在GMT5.1.2及其之后版本中可用。

getCN1xyz
---------

与getCN1maps生成类似的文件，只是此时的文件为xyz文件，每行三列。文件名以xyz开头或结尾。

将xyz文件转换为GMT可识别的网格文件，使用xyz2grd。注意与上面命令的区别。


GMT4语法::

    xyz2grd crsthk.xyz -Rg -I1/1 -Gout.grd -F -V

GMT5语法::

    gmt xyz2grd crsthk.xyz -Rg -I1/1 -Gout.grd -r -V

绘图示例
========

.. code-block:: bash

 #!/bin/bash
 grd2cpt out.grd -Cpolar > out.cpt
 grdimage out.grd -Rd -JN6i -B60/30 -Cout.cpt -V -K > a.ps
 pscoast -R -J -W0.1p -O >> a.ps

没有认真选择cpt文件，看上去效果不好，从细节上看，数据的转换是没有问题的。

.. figure:: /images/2013100301.jpg
   :width: 600 px
   :alt: crust1.0 model

修订历史
========

- 2013-10-03：初稿；
- 2014-06-10：加入了GMT5的命令；

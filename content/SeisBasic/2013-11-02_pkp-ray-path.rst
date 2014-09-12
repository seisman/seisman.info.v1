PKP射线路径
###########

:date: 2013-11-02 00:09
:author: SeisMan
:category: 地震学基础
:tags: GMT脚本, TauP, 射线, 震相
:slug: pkp-ray-path

.. figure:: /images/2013110201.jpg
   :align: center
   :alt: pkp
   :width: 600 px

利用TauP直接生成GMT脚本::

    taup_path -ph PKP,PKIKP -mod prem -h 100 -deg 150 --gmt --mapwidth 6

修改GMT脚本

注：脚本太长，故删除部分数据贴在这里，完整脚本在\ `这里`_\ 下载。

.. code-block:: bash

 #!/bin/sh
 gmtset HEADER_FONT_SIZE 30p

 # draw surface and label distances.
 psbasemap -K -P -R0/360/0/6371.0 -JP6.0i -B:."Ray Path of PKP": > taup_path.ps
 # draw circles for branches, note these are scaled for a
 # map using -JP6.0i
 psxy -K -O -P -R -JP -Sc -A >> taup_path.ps <<ENDLAYERS
 0.0 0.0 6.0i
 0.0 0.0 6.0i
 0.0 0.0 3.2773504i
 0.0 0.0 1.1503688i
 ENDLAYERS

 pstext -K -O -R -JP >> taup_path.ps << END
 0.0 0.0 12 0 0 CM Inner Core
 180.0 1500.0 12 0 0 RM Outer Core
 180.0 5000.0 12 0 0 CM Mantle
 70.0 2500.0 12 -15 0 CM PKPab
 70.0 1600.0 12 -15 0 CM PKPbc
 70.0 800.0 12 -15 0 CM PKPdf
 END

 # draw paths
 psxy -P -R -K -O -JP -m -A >> taup_path.ps <<END
 > PKP at 1177.26 seconds at 150.00 degrees for a 100.0 km deep source in the prem model with rayParam 2.359 s/deg.
 0.00 6271.0
 0.01 6264.0
 *****************省略了一堆数据******************
 150.04 6370.1
 150.04 6371.0
 > PKP at 1183.17 seconds at 150.00 degrees for a 100.0 km deep source in the prem model with rayParam 4.083 s/deg.
 0.00 6271.0
 0.02 6264.0
 ******************省略一堆数据****************
 150.00 6370.1
 150.00 6371.0
 > PKIKP at 1172.10 seconds at 150.00 degrees for a 100.0 km deep source in the prem model with rayParam 1.577 s/deg.
 0.00 6271.0
 0.01 6264.0
 **************省略一堆数据*************
 150.00 6370.1
 150.00 6371.0
 END
 psxy -P -R -O -JP -m -A >> taup_path.ps <<END
 END
 rm .gmt*

.. _这里: http://pan.baidu.com/s/1y1pvm

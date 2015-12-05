全球地形起伏模型ETOPO2
######################

:date: 2013-08-11 15:50
:author: SeisMan
:category: 地球物理相关资源
:tags: GMT4, GMT5, 地形, 数据, 网格, 高程
:slug: global-relief-model-etopo2
:summary: 全球地形数据etopo2。

ETOPO2与ETOPO5类似，也是陆地高程+海底地形数据，其采样间隔为2弧分。

官方地址： http://www.ngdc.noaa.gov/mgg/global/etopo2.html

官方提供了提供了很多版本， **ETOPO2v2c** 和 **ETOPO2v2g** 分别代表pixel registration和gridline registartion两种不同的网格表示方式。其中 **ETOPO2v2c** 是权威版本，建议选择 **ETOPO2v2c** 。

**ETOPO2v2c** 下又有许多格式可以选择，如下所示

::

 ETOPO2v2c
  ├── GRD98：ETOPO2v2c_i2_LSB_GRD98.zip
  ├── HDF：ETOPO2v2c_HDF.zip
  ├── netCDF：ETOPO2v2c_f4_netCDF.zip
  └── raw_binary：ETOPO2v2c_f4_LSB.zip和ETOPO2v2c_i2_LSB.zip

其中 ``netCDF`` ， ``grd98`` 和 ``raw_binary`` 格式的网格文件都可以直接在GMT中使用。由于 ``grdraster`` 命令只能使用 ``raw_binary`` 格式的数据，所以下面仅使用 ``raw_binary`` 格式网格数据。

#. 下载Little-endian，16位整型的二进制网格文件 `ETOPO2v2c_i2_LSB.zip <http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO2/ETOPO2v2-2006/ETOPO2v2c/raw_binary/ETOPO2v2c_i2_LSB.zip>`_

#. 解压::

    7za e ETOPO2v2c_i2_LSB.zip

   解压之后的 ``.bin`` 文件为二进制网格文件， ``.hdr`` 文件为头段文件

#. 拷贝::

    sudo cp ETOPO2v2c_i2_LSB.bin ${GMTHOME}/share/dbase

#. 修改 ``grdraster.info`` ::

    8 "ETOPO2 global topography"    "m"     -R-180/180/-90/90       -I2m            PG i 1          0       -32768  ETOPO2v2c_i2_LSB.bin    L

   其中的很多细节参考了 ``.hdr`` 文件中关于格式的说明，不细说。

#. 画图测试

   .. code-block:: bash

      #!/bin/bash

      grdraster 8 -Rg -I2m -Gout.grd
      makecpt -Cglobe -T-10500/8000/1000 -Z > colors.cpt
      grdimage out.grd -Ba60g30 -Rg -Yc -Xc -JN0/25c -Ccolors.cpt -K > etopo5.ps
      psscale -Ba2500f500::/:"m": -Ccolors.cpt -D12.5c/-2c/15c/.35ch -O >> etopo5.ps

      rm out.grd colors.cpt

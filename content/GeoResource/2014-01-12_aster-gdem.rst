全球数字高程数据：ASTER GDEM
#############################

:date: 2014-01-12 00:57
:author: SeisMan
:category: 地球物理相关资源
:tags: 地形, 数据, 格式转换, GMT5, GMT4, 高程
:slug: aster-gdem

.. contents::

简介
====

ASTER GDEM，即先进星载热发射和反射辐射仪全球数字高程模型，与SRTM一样为数字高程DEM，其全球空间分辨率为30米。该数据是根据NASA的新一代对地观测卫星Terra的详尽观测结果制作完成的。其数据覆盖范围为北纬83°到南纬83°之间的所有陆地区域，达到了地球陆地表面的99%。（摘自百度百科）。号称是“迄今最完整的全球地形数据”。

网站： http://gdem.ersdac.jspacesystems.or.jp

基本信息
========

空间分辨率：1弧度秒 （约30 米）

精度：垂直精度20米，水平精度30米

更多信息： http://www.gscloud.cn/userfiles/file/gdem3.pdf

其他信息
========

-  网站需要注册，即可免费下载数据；
-  点击“Search”即可进入数据选择界面；
-  数据被划分为1度\*1度的区块，每个区块文件名以区块左下角的经纬度值来命名；
-  数据选择界面有四种方式用来选择区块，界面的设计不太习惯，注意看英文；
-  数据可以单独下载，也可以批量下载；批量下载貌似需要处理一段时间；
-  下载的文件为zip压缩文件，包含了两个文件：dem和num，二者均为GeoTiff格式；
-  dem数据即为数字高程数据；
-  num数据也称为QA文件，即质量评估文件，其包含了每一点的高程数据的来源等信息，一般用不到；

格式转换
========

使用GDAL提供的工具将其转换为GMT可识别的netCDF格式：

::

    gdal_translate -of GMT ASTGTM2_N36E111_dem.tif ASTGTM2_N36E111_dem.nc

与SRTM的区别
============

-  SRTM数据的纬度覆盖范围是[-60,60]，ASTER GDEM数据的纬度覆盖范围为[-83,83]；
-  SRTM的空间分辨率一般为90m，只有美国境内存在空间分辨率为30m的数据；ASTER GDEM的空间分辨率为30m；

数据合并
========

可以使用GMT自带的grdpaster命令将两个相邻的网格文件合并起来。

- GMT 4.5.13的grdpaste有问题，会出现“Grids do not share command edge.”的错误；
- GMT 5.1.2的grdpaste没有问题；

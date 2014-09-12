GMT5的DCW数据简介
#################

:date: 2013-11-20 00:05
:author: SeisMan
:category: GMT
:tags: 数据, GMT5
:slug: introduction-to-dcw-gmt5

.. contents::

DCW
===

DCW，全称Digital Chart of the World，是一个内容广泛的数字地图，2006年免费公开，但是其数据实际上从1992年起就没有再更新过。

DCW数据被分为2094个区块，基本上一个区块代表5度×5度的区域。DCW数据中包含了国界、公路、铁路等等。

详细信息参考维基百科词条：\ `Digital Chart of the World`_

DCW-GMT
=======

DCW-GMT算是DCW的升级版，其特点在于：

-  包含全球各国国界；
-  包含部分国家的省界（目前只有8个比较大的国家，包括中国）；
-  数据格式为netCDF-4，可以直接在GMT中使用，也容易从中提取所需的边界数据；
-  数据应该是比较新的，且有人维护，因而发现问题可以报告Bug；

主页： http://www.soest.hawaii.edu/wessel/dcw/

为什么又是国界？
================

在GMT4中，可以用\ ``pscoast``\ 的\ ``-N1``\ 选项来绘制国界，\ ``-N2``\ 选项来绘制省界（仅美国、加拿大等国）。

这样绘制的国界有什么问题呢？比如，设定绘图区域为中国，然后使用\ ``pscoast -N1``\ 加入国界，得到的结果里将不仅仅是中国的国界，还有俄罗斯、日本、印度等的国界。即GSHHG的国界数据是完全的，但是并不能区分每段数据属于哪个国家。所以网上有一堆文章在研究GMT中怎么只绘制中国的边界。

DCW-GMT是为了解决这个问题而存在的，当你想绘制中国国界时，得到的就是干干净净的中国国界，而没有其他国家的国界的干扰。

DCW-GMT详情
===========

下载安装什么的在博文《\ `GMT5.1.0在Linux下的安装 <{filename}/GMT/2013-11-06_install-gmt5-under-linux.rst>`_\ 》中已经说过了，不再多说。

DCW-GMT包含了如下文件：

::

    .
    ├── COPYING.LESSERv3
    ├── COPYINGv3
    ├── dcw-countries.txt
    ├── dcw-gmt.nc
    ├── dcw-states.txt
    ├── LICENSE.TXT
    └── README.TXT

真正有用的文件包括dcw-countries.txt、dcw-gmt.nc、dcw-states.txt。其中dcw-gmt.nc是netCDF格式的数据，其他两个txt文件为辅助文档。

dcw-contries
------------

文件格式为\ ``大洲代码 国家代码 国家名``\ ，代码均为两位字符。

大洲代码包括AF(非洲)、AN(南极洲)、AS(亚洲)、EU(欧洲)、OC(大洋洲)、NA(北美洲)和SA(南美洲)。

国家代码就更多了，比如中国是CN。准确来说，不是国家代码，而是国家和/或地区代码，比如China、Hong
Kong、Macao和Taiwan分别有不同的国家代码。

这个文件是GMT绘制国界时需要查找的文件，同时也是用户绘图边界时需要参考的文件。该文件共计250个国家或地区。文件内容大致如下：

::

    AS BH Bahrain
    AS BN Brunei
    AS BT Bhutan
    AS CN China
    AS CX Christmas Island
    AS GE Georgia
    AS HK Hong Kong
    AS HM Heard Island and McDonald Islands
    AS ID Indonesia
    AS IL Israel
    AS IN India

dcw-states
----------

文件格式为\ ``国家代码 省代码 省名``\ 。国家代码为两位，与dcw-contries.txt中对应，省代码则比较乱了，用的时候再查。中国的省代码居然是数字，不知道为什么这么安排。

目前有AR(阿根廷)、AU(澳大利亚)、BR(巴西)、CA(加拿大)、US(美国)、CN(中国)、IN(印度)、RU(俄罗斯)共计八个国家的省/州界数据。

只关心中国的数据，包括全部34个省级行政区域，包括23个省，5个自治区，4个直辖市，以及香港，澳门2个特别行政区。（台湾在里面，不然又该引起争端了）。

::

    CN 11 Beijing
    CN 50 Chongqing
    CN 31 Shanghai
    CN 12 Tianjin
    CN 34 Anhui
    CN 35 Fujian
    CN 62 Gansu
    CN 44 Guangdong
    CN 52 Guizhou
    CN 46 Hainan
    CN 13 Hebei
    CN 23 Heilongjiang
    CN 41 Henan
    CN 42 Hubei
    CN 43 Hunan
    CN 32 Jiangsu
    CN 36 Jiangxi
    CN 22 Jilin
    CN 21 Liaoning
    CN 63 Qinghai
    CN 61 Shaanxi
    CN 37 Shandong
    CN 14 Shanxi
    CN 51 Sichuan
    CN 71 Taiwan
    CN 53 Yunnan
    CN 33 Zhejiang
    CN 45 Guangxi
    CN 15 Nei Mongol
    CN 64 Ningxia
    CN 65 Xinjiang
    CN 54 Xizang
    CN 91 Xianggang (Hong Kong)
    CN 92 Aomen (Macao)

如何使用DCW数据？
===================

GMT5中，可以通过pscoast命令的-F选项调用DCW数据来绘制国界和省界，具体的下一篇再说。

.. _Digital Chart of the World: http://en.wikipedia.org/wiki/Digital_Chart_of_the_World

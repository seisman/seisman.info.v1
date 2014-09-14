Global CMT信息整理
##################

:date: 2013-07-01 00:15
:author: SeisMan
:category: 地球物理相关资源
:tags: 地震目录, 震源机制解, 震级
:slug: global-cmt
:summary: 整理了Global CMT网站的相关信息。

.. contents::

简介
====

Global CMT全称Global Centroid-Moment-Tensor Project，前身是Harvard CMT，是地震学常用的地震目录和震源机制之一。其给出了自1976年以来上万个地震的地震目录以及震源机制。

主页
====

http://www.globalcmt.org/

Catalog在线查询
===============

http://www.globalcmt.org/CMTsearch.html

可以指定时间段、震级范围、震中范围、深度范围，也可以对震源时间函数以及T轴和N轴进行限制。并支持多种输出格式，其中的\ ``GMT psmeca input``\ 格式可以直接用于GMT绘图。

Catalog直接下载
===============

http://www.globalcmt.org/CMTfiles.html

很多时候我们需要根据其他条件对catalog进行筛选，得到符合自定义条件的地震事件，所以ASCII格式的目录文件就很重要了。GCMT提供了1976年到现在的地震目录，其中1976-2004年的地震目录为dek格式，包含在一个文件中。2005年以后的地震目录为ndk格式，每月一个文件。对于2005年以后的地震目录可以将一年的目录合并到一个文件中，方便管理且不会导致文件过大。

- 1976-2004目录下载： http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/jan76_dec04.dek
- 2005以后目录下载： http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/NEW_MONTHLY/
- ndk格式说明： http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/allorder.ndk_explained
- dek格式说明： http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/allorder.dek_explained

关于GCMT的文章
==============

- 1981： http://www.agu.org/pubs/crossref/1981/JB086iB04p02825.shtml
- 1983： http://www.agu.org/pubs/crossref/1983/JB088iB04p03247.shtml
- 2012： http://www.sciencedirect.com/science/article/pii/S0031920112000696

备注
====

- GCMT目录的ASCII文件中震级采用mb和/或MS，为什么不用矩震级？使用面波和体波震级的最大问题是震级饱和，导致震级基本不会超过8级。

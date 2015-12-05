震中距、方位角和反方位角的计算
##############################

:date: 2013-07-03 01:00
:modified: 2014-10-28 10:55
:author: SeisMan
:category: 地震学软件
:tags: C, Fortran, Java, Python, Matlab, 名词解释
:slug: calculate-dist-az-baz

.. contents::

给定震中经纬度以及球面上任意一点（一般是台站）的经纬度，计算震中距、方位角以及反方位角。这是地震学的一个基本问题。

名词解释
========

- 震中距：\ **地面**\ 上任意一点到\ **震中**\ 的球面距离；
- 方位角：震中到台站的连线与地理北向的夹角；
- 反方位角：台站到震中的连线与地理北向的夹角；

一张图可以说明一切:

.. figure:: /images/2013070301.jpg
   :alt: 震中距、方位角(az)、反方位角(baz)示意图
   :width: 600 px

   图1：震中距、方位角(az)、反方位角(baz)示意图

数学推导
========

公式的推导需要简单的球面三角函数的知识。具体的推导可以参考Robert B. Herrmann的作业题。

网址如下： http://www.eas.slu.edu/People/RBHerrmann/Courses/EASA462

作业题中的Ass06、Ass07、Ass08给出了计算震中距和方位角的原理。

相关代码
========

广为流传的一个程序是 ``distaz`` 。在GMT、SAC等的源码里都可以找到。\ ``distaz``\ 代码很短，简单易懂，其采用的地球模型为椭球模型，精度上可以满足需求。

- C、Fortran、Java、Python以及CGI版本： `由The lithospheric seismology program at USC整理 <http://www.seis.sc.edu/software/distaz/>`_

Matlab版本： `由specfem3d_globe提供 <https://github.com/geodynamics/specfem3d_globe/blob/master/utils/Visualization/VTK_ParaView/matlab/distaz.m>`_


使用方法
========

仅以C语言版本的 ``distaz`` 为例，用如下命令即可编译::

    cc distaz.c -o cdistaz -lm

其输入为 ``sta_lat sta_lon evt_lat evt_lon`` ，输出为\ ``Delta Baz Az``\ 。

::

    $ distaz 10 14 40 50
    43.731 40.781 236.882

修订历史
========

- 2013-07-03：初稿；
- 2014-07-06：加入了对 ``distaz`` 的用法的说明；删除了CPS330的部分；
- 2014-10-28：新增matlab版本；

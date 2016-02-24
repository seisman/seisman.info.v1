走时计算软件TauP
################

:date: 2013-07-10 00:53
:modified: 2016-02-24
:author: SeisMan
:category: 地震学软件
:tags: 走时, TauP
:slug: taup-toolkit

.. contents::

TauP是一个用于计算震相走时等相关信息的软件包。

基本信息
========

#. 开发者： `University of South Carolina <http://sc.edu/>`_
#. 语言：Java
#. 平台：跨平台，Windows、Linux、Mac等
#. 与ttimes一样，其原理基于Buland和Chapman于1983年提出的方法

功能与特色
==========

相对于ttimes而言，TauP具有更多的功能和特色：

#. 可以计算震相走时、射线参数、反射点、穿透点、射线路径、走时曲线等
#. 支持自定义速度模型
#. 内置震相解析器，支持不常见的震相名
#. 自带多个预定义地球模型：iasp91、prem、ak135、jb、1066a、1066b、pwdk、sp6、herrin
#. 部分兼容ttimes，比如用ttp表示常见P波震相，除此之外，还有tts、ttp+、tts+、ttbasic、ttall
#. 采用线性插值，可能带来0.01秒的误差
#. 直接在球坐标系下求解方程，不必做展平变换；与部分震相的解析解相比，最大误差为0.01秒，而ttimes的最大误差为0.05秒

目前来看的缺点是：

#. 不支持Pg、Pn、PKPab、PKPbc等震相名
#. 输出的格式不够灵活，有时需要自己写脚本从输出中提取信息

工具
====

TauP提供了多个工具，包括有图形界面的 ``taup`` ，交互式的 ``taup_console`` ，以及命令行工具 ``taup_time`` 、 ``taup_pierce`` 、 ``taup_setsac`` 、 ``taup_path`` 、 ``taup_curve`` 、 ``taup_create`` 、 ``taup_table`` 、 ``taup_wavefront`` 。

TauP系列博文
============

#. `安装TauP <{filename}/SeisWare/2014-10-08_install-taup.rst>`_
#. `用taup_time计算震相走时及射线信息 <{filename}/SeisWare/2015-01-24_calculate-travel-time-using-taup.rst>`_
#. `用taup_pierce计算射线的界面的穿透点 <{filename}/SeisWare/2014-11-07_calculate-pierce-points-using-taup.rst>`_
#. `用taup_setsac将走时信息写入SAC文件 <{filename}/SeisWare/2014-11-10_mark-travel-time-using-taup.rst>`_

SEIZMO：天然地震学Matlab工具箱
##############################

:date: 2014-03-30
:author: SeisMan
:category: 地震学软件
:tags: Matlab
:slug: passive-seismology-toolbox-for-matlab-and-gnu-octave

.. contents::

SEIZMO是什么？
==============

SEIZMO是一个基于Matlab和GNU Octave的地震学数据处理工具箱，其包含了700多个函数，可以用于地震数据的预处理、质量控制以及处理。

其在某种程度上包含了SAC、TauP、GMT的功能，同时包含多种地球一维、三维模型，GCMT地震目录以及IRIS的仪器响应数据库。

- 官方主页：http://epsc.wustl.edu/~ggeuler/codes/m/seizmo/
- 项目主页：https://github.com/g2e/seizmo

基本要求
========

- Matlab7.1+或最新版的GNU Octave
- Signal Processing Toolbox  (for filtering and resampling)
- Statistics Toolbox (for clustering)

优缺点
======

优点
----

- 完全基于Matlab的m脚本，无需编译
- 与开源的GNU Octave完全兼容
- 读写多种地震数据格式（SAC、NDK等）
- help很详细
- 可以满足自动分析和交互的需求

缺点
----

- 基于Matlab脚本，相比于Fortran/C来说速度要慢
- 仅由一个研究生开发，开发速度缓慢
- 没有大量的PDF/HTML文档

功能
====

- 将地震波转换为声音
- 震源机制相关转换、计算和绘制
- 卷积、反卷积、谱白化和去谱白化
- 读取各个机构的震源机制
- 滤波
- 频率-波数域分析
- 绘制GMT风格的地图
- 计算走时
- 波形叠加
- 拾取震相
- 重采样
- 去仪器响应
- 读写数据
- 走时校正
- 等等



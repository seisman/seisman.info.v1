走时计算软件TauP
################

:date: 2013-07-10 00:53
:modified: 2014-11-23
:author: SeisMan
:category: 地震学软件
:tags: 走时, TauP
:slug: taup-toolkit

.. contents::

TauP由\ `University of South Carolina <http://sc.edu/>`_\ 开发的，用于计算震相相关信息的一个软件包。该软件包由Java写成，可以在多个平台上运行。

TauP和ttimes一样都是基于Buland和Chapman于1983年提出的方法，但TauP拥有更多的功能，不仅可以计算走时，还可以计算反射点、穿透点点等等。同时，TauP还支持自定义速度模块，且支持更多不常见的震相。

TauP直接在球坐标系下求解方程，避免了展平变换带来的复杂性和误差。

TauP提供了多个工具，包括有图形界面的taup，交互式的taup_console，以及命令行工具taup_time、taup_pierce、taup_setsac、taup_path、taup_curve、taup_create、taup_table、taup_wavefront。

TauP系列博文：

#. `安装TauP <{filename}/SeisWare/2014-10-08_install-taup.rst>`_
#. `用taup_time计算震相走时及射线信息 <{filename}/SeisWare/2015-01-24_calculate-travel-time-using-taup.rst>`_\
#. `用taup_pierce计算射线的界面的穿透点 <{filename}/SeisWare/2014-11-07_calculate-pierce-points-using-taup.rst>`_\
#. `用taup_setsac将走时信息写入SAC文件 <{filename}/SeisWare/2014-11-10_mark-travel-time-using-taup.rst>`_\

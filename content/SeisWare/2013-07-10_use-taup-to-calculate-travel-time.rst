走时计算软件TauP
################

:date: 2013-07-10 00:53
:modified: 2014-11-23
:author: SeisMan
:category: 地震学软件
:tags: 走时, TauP
:slug: use-taup-to-calculate-travel-time

.. contents::

TauP由\ `University of South Carolina <http://sc.edu/>`_\ 开发的，用于计算震相相关信息的一个软件包。该软件包由Java写成，可以在多个平台上运行。

TauP和ttimes一样都是基于Buland和Chapman于1983年提出的方法，但TauP拥有更多的功能，不仅可以计算走时，还可以计算反射点、穿透点点等等。同时，TauP还支持自定义速度模块，且支持更多不常见的震相。

#. `安装TauP <{filename}/SeisWare/2014-10-08_install-taup.rst>`_
#. taup
#. taup_console
#. `taup_time <{filename}/SeisWare/2015-01-24_calculate-travel-time-using-taup.rst>`_\ ：用于计算震相走时及射线参数
#. `taup_pierce <{filename}/SeisWare/2014-11-07_calculate-pierce-points-using-taup.rst>`_\ ：用于计算射线在各个速度分界面的穿透点
#. `taup_setsac <{filename}/SeisWare/2014-11-10_mark-travel-time-using-taup.rst>`_\ ：用于将震相到时、射线参数等信息写入头段中。
#. taup_path
#. taup_curve
#. taup_create
#. taup_table
#. taup_wavefront

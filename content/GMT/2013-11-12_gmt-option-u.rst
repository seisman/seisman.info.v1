GMT选项之时间戳-U
##################

:date: 2013-11-12 00:11
:author: SeisMan
:category: GMT
:tags: GMT选项, GMT4, GMT5
:slug: gmt-option-u

.. contents::

本文适用于GMT4和GMT5。

语法
====

-U选项会在绘图上加上GMT的小logo以及时间戳。

几种常见用法：

-  ``-U``\ ：采用默认参数，时间戳位于绘图的左下角；
-  ``-Ujust/dx/dy``\ ：just指定时间戳的对齐方式，dx和dy指定时间戳与绘图原点的偏移量；缺省情况下-U等效于-UBL/-2c/-2c；
-  ``-Uc``\ ：\ **c**\ 代表command，这种方式会将当前命令打印在时间戳之后；
-  ``-Ulabel``\ ：label可以是任意的字符串；常用来做一些小注释；
-  ``-Ujust/dx/dy/c|label``\ ：最完整的用法；

默认参数
========

该选项的默认参数为\ ``-UBL/0/0``\ ，即时间戳的左下角与绘图原点对齐。

GMT提供了一些参数可以修改这些默认行为：

GMT4
----

-  UNIX\_TIME：控制默认情况下是否要绘制时间戳；缺省值为FALSE，即不绘制；
-  UNIX\_TIME\_POS：默认情况下时间戳的位置：BL/-2c/-2c；
-  UNIX\_TIME\_FORMAT：时间格式，默认值为\ ``%Y %b %d %H:%M:%S``\ ，具体格式可以参考C语言strftime函数；

GMT5
----

-  MAP\_LOGO：即GMT4中的UNIX\_TIME；
-  MAP\_LOGO\_POS：即GMT4中的UNIX\_TIME\_POS，默认值为BL/-54p/-54p；
-  FORMAT\_TIME\_STAMP：即GMT4中的UNIX\_TIME\_FORMAT；

自定义Logo
==========

其实这篇博文的目的是为了引入下一篇博文---自定义GMT的Logo。

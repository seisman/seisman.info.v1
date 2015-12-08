SOFI2D笔记
##########

:date: 2015-12-08
:author: SeisMan
:category: 地震学软件
:tags: 理论地震图
:slug: sofi2d-notes
:depends: mathjax

SOFI2D是一个二维PSV交错网格有限差分代码。要使用该程序，至少需要阅读如下几篇参考文献：

- Virieux, J. 1986. P-SV wave propagation in heterogeneous media: velocity-stress finite- difference method. Geophysics, 51(4), 889–901.
- Levander, A.R. 1988. Fourth-order finite-difference P-SV seismograms. Geophysics, 53(11), 1425–1436.
- SOFI2D User Guide

具体的用法及每个参数的意义在官方文档已经介绍的很详细，本文是我使用SOFI2D过程中的经验总结。

运行SOFI2D所需的文件都在 ``par`` 目录下，其中需要修改的文件包括：

- ``in_and_out/sofi2D.json``
- ``model/test``
- ``source/source.dat``
- ``receiver/receiver.dat``

``in_and_out/sofi2d.json`` 是程序的输入配置文件，配置文件是用json语法写的，并且将众多的变量分成了若干类。在设计不同的速度模型时，某些变量基本不需要改动，某些变量则可能需要经常改动。

在设计模型时，可以按照如下顺序逐一修改或检查如下参数：

#. 生成速度模型：2D速度模型需要自己写程序生成，参考 ``src/hh_elastic.c`` 和 ``genmod/2layer.c`` ，并将生成的模型保存到 ``model`` 目录下
#. ``source/source.dat`` 中指定震源时间函数的中心频率（也可从文件中读入震源时间函数）、振幅和时间延迟
#. 估算震源时间函数的最大频率。如果是使用内置震源时间函数，可以近似认为最大频率是中心频率的两倍，如果是从文件中读入自定义的震源时间函数，可以对其做FFT，将振幅谱中的拐点作为最大频率
#. 频散条件要求一个波长内要至少有n个网格点，因而要根据最大频率和最小速度计算出最大的网格间隔。在满足公式

   .. math::

      dh \le \frac{V_{min}}{n f_{max}}

   的前提下选择 :math:`dh` ，其中n由 ``FDORDER`` 决定

#. 为了满足稳定性条件，要根据网格间隔和模型中的最大速度选择合适的时间步长。在满足公式

   .. math::

      dt \le \frac{dh}{h \sqrt{2} V_{max}}

   的前提下选择 :math:`dt` 值，其中h由 ``FDORDER`` 决定

#. 修改 ``in_and_out/sofi2d.json`` 中的 ``DH`` 和 ``DT``
#. ``source/source.dat`` 中指定震源位置
#. ``receiver/receiver.dat`` 中指定台站位置
#. 修改配置文件中的2-D Grid部分，指定 ``NX`` 和 ``NY``
#. 根据计算机的核数以及 ``NX`` 和 ``NY`` 的值，修改Domain Decomposition部分
#. ``startSOFI2D.sh`` 中 ``-np`` 后面的进程数应与 ``NPROCX*NPROCY`` 相等
#. 修改配置文件中的Time Stepping部分
#. 如果要生成波场快照的话，则修改Snapshots部分

然后就可以开始计算了，每次修改模型之后，都需要按照上面的顺序检查各个参数。

使用过程中需要注意的一些地方：

#. 运行SOFI2D时目录名必须为 ``par`` ，该目录下各个子目录的名字不可变

   理论上运行目录是不是 ``par`` 都可以，各个子目录的名字在 ``json`` 文件中也是可以任意设定的。但实际运行的过程中如果运行目录不是 ``par`` 或者各个子目录的名字与默认的子目录名不一样都会直接报错退出。这实际上是代码 ``src/check_fs.c`` 的bug导致的，该代码的目的在于检查文件系统，即目录是否存在，以及文件是否可读、可写。由于该代码将所有目录名硬编码在源码中，所以导致各个目录名不可修改。解决办法有两个：

   #. 把主程序中对 ``check_fs`` 的调用注释掉
   #. 保留原par目录，每次自己新建目录，这样 ``check_fs`` 每次都会检查 ``par`` 目录，而不会检查新建的目录

#. 默认四个边界都是吸收边界， ``FREE_SURF`` 控制上表面是否为自由边界， ``BOUNDARY``  控制左右是否为周期性边界条件

#. 交错网格结构的定义如下::

        Txx,Tzz   Ux


        Uz        Txz

   因而同一个网格点内的垂直分量要比水平分量深半个网格点。

#. 源码中 ``src/update_v_interior.c`` 是时间二阶，空间二阶有限差分格式，对应于Virieux 1986，是最简单的一个
#. 计算出的理论地震图，到时应以onset为准，而不是以peak为准。
#. sofi2d与fk，即便用完全相同的震源时间函数，其波形也是无法直接做对比的，因为fk计算的是点源三维波场，sofi2d计算的是线源二维波场，因而sofi2d计算的结果需要做线源到点源的转换

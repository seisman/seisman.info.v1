震相走时的计算
##############

:author: SeisMan
:date: 2015-05-02
:category: 地震学基础
:tags: 走时, 理论
:slug: travel-time-calculation
:depends: mathjax

.. contents::

震相走时的计算是地震学的基本问题之一。

目前，计算一维分层模型下的震相走时，主要使用两个程序包：ttimes和TauP。ttimes相对来说有些古老，所以多数情况下更推荐使用TauP。但TauP不支持PKPab、PKPbc这种震相名，所以偶尔可能还是需要使用ttimes。

ttimes和TauP都是根据Buland and Chapman（BSSA, 1983）提出的理论框架来实现的，本文是对这篇文章的核心内容的简单总结。

提出问题
========

给定一维水平分层模型，若震源位于地表，要求计算某一震相（如P波）在特定震中距（如50度）处的震相走时。

说明：

#. 球状分层模型和水平分层模型下的理论公式基本相同，只是个别变量需要做简单替换，这里用更简单的水平分层模型；
#. 震源位于地表或地下，只会影响到积分的上下限，这里为了简化，将震源放在地表；
#. 这里以简单的P波为例，理论上是可以算各种复杂路径的震相的；

基本公式
========

对于一个速度仅是深度的函数的一维分层速度模型\ :math:`v(z)`\ ，其慢度为

.. math::

    u(z) = \frac{1}{v(z)}

定义射线参数（即水平慢度）为

.. math::

    p = \frac{\sin(i(z))}{v(z)}

其中\ :math:`i(z)`\ 是射线与垂直方向的夹角。垂直慢度为

.. math::

    \eta(p, z) = (u^2(z)-p^2)^{\frac{1}{2}}

在做了如上定义后，对于从地表发出的任意一条射线参数为\ :math:`p`\ 的射线，即可计算出该射线所对应的走时和震中距(Introduction to Seismology, Peter Shearer, 公式4.31-4.32及之间的推导)：

.. math::

    T(p) = 2\int_0^{z_p} \frac{u^2(z)}{\eta} dz

.. math::

    X(p) = 2p\int_0^{z_p}\frac{dz}{\eta}

其中\ :math:`z_p`\ 是射线的反转点（turning point）的深度。

另一个重要的公式是：

.. math::

    p = \frac{dT}{dX}

基本解法
========

有了上面的几个公式，基本就可以有一个直观暴力的解法了。

对于任一射线参数\ :math:`p`\ ，都可以找到射线的\ :math:`z_p`\ ，然后即可积分计算该射线所对应的震中距\ :math:`X(p)`\ 和走时\ :math:`T(p)`\ 。

但是问题中要计算的是特定震中距X0的走时，那么就可以对射线参数进行遍历，每给一个射线参数，就计算一个震中距X(p)，若X(p)>X0，则把射线参数改大一些，若X(p)<X(0)，则把射线参数改小一些。最终，总可以找到一个射线参数，使得X(p)和X0几乎相等。

这基本就是一个二分查找，实现起来也很简单。但此方法的问题在于，假定了X(p)是p的单调递减函数，而真实地球模型中有低速层和高速不连续面，会出现三叉波和影区，不符合单调递减函数的假设。在同一个震中距处可以有多个射线参数。

因而这里的思路仅适用于某些简单的震相，比如P、PcP、PKiKP之类。

tau(p)
======

定义delay-time函数\ :math:`\tau(p)`\ ：

.. math::

    \tau(p) = T(p) - pX(p)

简单推导可知，tau函数可以用如下公式计算：

.. math::

    \tau(p) = 2\int_0^{z_p} \eta dz

且其具有如下性质：

.. math::

    \frac{d\tau}{dp} = \frac{dT}{dp} - X(p) - p \frac{dX}{dp}
                     = \frac{dT}{dX}\frac{dX}{dp} - X(p) - p \frac{dX}{dp}
                     = -X(p)

由于X(p)是震中距，为非负值，因而，\ :math:`d\tau/dp`\ 是个非正值。即函数\ :math:`\tau(p)`\ 的斜率是非正值，因而tau函数是一个单调递减函数，即对任意一个射线参数p，都有唯一的tau。

theta(p,x)函数
==============

进一步定义theta函数：

.. math::

    \theta(p,x) = \tau(p) + px

再看看前面tau函数的定义：

.. math::

    T(p) = \tau(p) + pX(p)

theta(p,x)和T(p)看上去很相似，但需要特别注意的是，T(p)是p的函数，而theta是p和x的函数。即在T(p)的定义中，X(p)是射线p所对应的震中距，具有唯一或唯N个值；而theta函数中，x是一个任意的变量，理解这一点很重要。

theta函数对p求偏导，可得：

.. math::

    \frac{\partial \theta}{\partial p} = \frac{d\tau}{dp} + x = x - X(p)

因而，若在某个p0处，有theta函数对p的偏导为零，则有x=X(p0)，进而有：

.. math::

    T(p_0) = \tau(p_0) + p_0 X(p_0) = \theta(p_0, X(p_0))

上面的公式表明：若某个p0处，theta函数对p的偏导为零，则该射线参数p0所对应的theta值就是射线的走时T(p0)。

下图是一个比较直观的例子（Chapman, 1978, GJI, Figure 12）。对于存在高速区的情况，走时曲线中会出现三叉波，如左上图T(X)曲线所示。左下图中给出了tau(p)曲线，是一个单调递减曲线。对于震中距A、B、C、D，分别计算了其对应的theta曲线，如右边四张图所示。

.. figure:: /images/2015050201.png
   :width: 300px
   :align: center
   :alt: 2015050201.png

- 对于震中距A，从theta曲线中可以看出，该曲线有三个局部极值，因而在震中距A处，有三条射线参数不同的射线，在不同的时间抵达震中距A；
- 对于震中距B，左边有一个明显的局部极值，右边有一小段，theta曲线近似为平的，这意味着，存在某段射线参数，其到震中距B的走时基本是一样的。这一点一般称为caustic，在射线理论中，这里的振幅是无穷大的。
- 对于震中距C，有一个局部极值点；
- 对于震中距D，无局部极值点；

总之，对于特定震中距，计算出theta曲线后，从曲线中很容易看出在该震中距处有哪些射线在何时到达，这也是WKBJ理论地震图计算方法的基本原理的一部分。

高级解法
========

有了上面的theta函数及其性质作为理论基础，就可以顺畅的解决上面的问题了。

基本步骤如下：

#. 读取速度模型，计算得到慢度模型
#. 对p做遍历，计算得到离散的tau(p)函数
#. 计算特定震中距X0处的theta(p,x)，即theta(p,X0)，或表示为theta(p)
#. 寻找theta(p)对p的偏导为零的点，即theta(p)的局部极值点
#. 每个极值点处射线参数p0即为符合要求的射线参数，而theta(p0)则为要计算的走时

其他细节
========

上面总结了计算走时的理论框架，实际数值计算时还甚至到更多的细节，具体参考1983那篇文章的后面部分。

#. tau(p) 积分的计算
#. 震源深度的处理
#. 极值的寻找
#. 震相名的解析
#. ...

参考文献
========

#. Chapman, C. H. (1978). A new method for computing synthetic seismograms. Geophysical Journal International, 54(3), 481-518.
#. Shearer, P. M. (2009). Introduction to seismology. Cambridge University Press.
#. Buland, R., and Chapman, C. H. (1983). The computation of seismic travel times. Bulletin of the Seismological Society of America, 73(5), 1271-1302.

球状模型下的Tau积分
###################

:date: 2015-05-15
:author: SeisMan
:category: 地震学基础
:tags: 走时
:slug: tau-integral-in-spherical-earth
:depends: mathjax

.. contents::

在计算震相走时的过程中，对\ :math:`tau(p)`\ 函数的积分是其中比较重要的一步，具体\ :math:`tau(p)`\ 函数如何使用，在地震学教材里都有介绍。

基本公式
========

在球状分层模型下，任意一层内的\ :math:`tau(p)`\ 函数的积分可以写成：

.. math::

   \tau(p) = \int_{r_1}^{r_2} \frac{\eta}{r} dr

其中\ :math:`r_1`\ 和\ :math:`r_2`\ 分别是这一层的上下边界的地球半径。\ :math:`p`\ 是射线参数（水平慢度），\ :math:`\eta`\ 是垂直慢度，\ :math:`r`\ 是地球半径。

对于常见的地球模型，比如PREM，都是给出了地球内部各个深度的速度值。因而对于每一个球层来说，速度都是半径的函数，进而导致垂直慢度是半径的函数，因而积分会变得复杂起来。

下面会介绍几种\ :math:`tau(p)`\ 积分的思路。为了更直观起见，现在假设有这一一个球层，上下边界的半径分别为3480 km和3380km，速度分别为8.06 km/s和8.20 km/s。

匀速层积分法
============

最简单的方法是将球层内的速度近似为一个常数。比如这里，可以把这个100km厚的球层当做是一个匀速层。但是这个速度怎么取就是一个问题了。取8.06的话积分结果偏大，取8.20的话积分结果偏小。取均值8.13吧，好像又没有什么道理，毕竟垂直慢度跟速度之间又不是线性关系。所以把整个球层当做匀速有点不靠谱，而且误差会很大。

线性速度积分法
==============

一个比较合理的假设是，在球层内速度线性变化，即

.. math::

   v = a + b r

其中a和b的值由上下边界的半径和速度决定。

在速度线性变化的假定下，\ :math:`tau(p)`\ 函数的积分是没有解析表达式的，只能进行数值积分。

数值积分的话，一般可以调用库函数，自己写的话也挺简单。比如可以考虑把100km的球层，再细分为1km的子球层，然后用矩形积分公式或梯形积分公式做数值积分。

理论上，子球层的厚度越小，计算结果越精确，同时也导致计算量越大。而如果子球层的厚度取得不够小，则计算的误差可能稍大。

指数慢度模型
============

假设每一层的\ **慢度**\ 模型的形式为\ :math:`u=a r^b`\ ，这种模型一般称为Bullen Type模型，这也是TauP中使用的慢度模型。

将上下边界的半径和慢度带入：

.. math::

   u_1 = a r_1^b

   u_2 = a r_2^b

计算得到：

.. math::

   b = \frac{\log(u_1/u_2)}{\log(r_1/r_2)}

在这样的近似下，\ :math:`tau(p)`\ 函数的积分可以进一步简化。

将慢度的公式代入射线参数的定义中：

.. math::

   p = u \sin \theta = a r^b \sin \theta

将上式对半径求导数：

.. math::

   0 = ab r^{b-1} dr \sin \theta + a r^b \cos \theta d\theta

整理得到：

.. math::

   \frac{dr}{r} = - \frac{\cos\theta}{b \sin\theta} d\theta

代入tau函数的积分公式：

.. math::

   \tau(p) = \int_{r_1}^{r_2} \eta \frac{dr}{r}

           = \int_{r_1}^{r_2} p \frac{\cos \theta}{\sin\theta} \frac{dr}{r}

           = -\frac{p}{b} \int_{\theta_1}^{\theta_2} \frac{\cos^2\theta}{\sin^2\theta} d\theta

           = -\frac{p}{b} \int_{\theta_1}^{\theta_2} (\frac{1}{\sin^2\theta}-1) d\theta

           = -\frac{p}{b} \int_{\theta_1}^{\theta_2} d(\frac{\cos\theta}{\sin\theta}-\theta)

           = - \frac{p}{b}(\theta_2-\theta_1) - \frac{1}{b}(\eta_2-\eta_1)

根据tau函数的定义\ :math:`\tau(p)=T(p)-pX(p)`\ ，对比上式有：

.. math::

   T(p) = \frac{1}{b}(\eta_1-\eta_2)

   X(p) = \frac{1}{b}(\theta_2-\theta_1)

其中：

.. math::

   \eta_1 = \sqrt{u_1^2-p^2}

   \eta_2 = \sqrt{u_2^2-p^2}

   \theta_1 = \arctan \frac{p}{\eta_1}

   \theta_2 = \arctan \frac{p}{\eta_2}

整个球层的积分就被大大简化了。

特殊处理
========

p<u1且p<u2
----------

此时该射线可以正常穿过该层，直接用公式计算即可。

p<u1且p>u2
----------

此时射线会进入该层，并在该层内入射角达到90度，最终反转，从下行波变成上行波。

射线反转时有\ :math:`p=u`\ ，即垂直慢度为零，根据慢度模型可以直接计算出反转深度\ :math:`r_p`\ ，此时\ :math:`\tau(p)`\ 的积分上限\ :math:`r_2`\ 应该改成反转深度\ :math:`r_p`\ 。

实际计算时，并不需要计算反转深度，因而射线在反转深度处有\ :math:`\eta_2=0`\ 且\ :math:`\eta_2=\frac{\pi}{2}`\ ，可以直接代入公式即可。

p>u2
----

此时，射线无法进入该层，直接返回零距离和零走时。

速度间断面
----------

在模型中，速度间断面是通过在同一深度给出两个不同的速度来表示的。在程序中，直接判断这一层的厚度是否等于零即可。若厚度为零，则表示该深度有速度间断，不可用上面的公式计算，直接返回零距离和零走时即可。

参考
====

#. An Introduction to Seismology, Earthquake, and Earth Structure, Seth Stein & Michael Wysession, 2003, P159
#. TauP软件包，SlownessLayer.java的TimeDist函数；
#. Introduction to Seismology, Peter Shearer, 2009, P367

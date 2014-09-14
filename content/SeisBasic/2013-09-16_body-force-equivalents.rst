体力与等效体力
##############

:date: 2013-09-16 00:07
:author: SeisMan
:category: 地震学基础
:tags: 震源
:slug: body-force-equivalents
:depends: mathjax

地震学里最基本的运动方程是

.. math::

   \rho \ddot{u_i} = \sigma_{ij,j} + f_i

其中\ :math:`f_i`\ 是体力项，最常见的体力是重力。

除非是研究地球的自由震荡，在一般的地震波传播问题中，重力都是可忽略的，因而运动方程简化为：

.. math::

   \rho \ddot{u_i} = \sigma_{ij,j}

断层的破裂过程（即震源的激发过程）可以认为其在源区导致局部的本构关系发生变化。其中\ :math:`\sigma_{ij}`\ 是真实的应力场，而\ :math:`s_{ij}`\ 是根据原本构关系计算得到的应力场。

定义

.. math::

   f_i \equiv (\sigma_{ij}-s_{ij})_{,j}

此时运动方程重新变成

.. math::

   \rho \ddot{u_i} = \sigma_{ij,j} + f_i

:math:`s_{ij}`\ 是根据原本构关系计算得到的应力场，因而其在整个空间内是连续的。注意这里的\ :math:`f_i`\ 已经不再是体力了，而是从被修改的本构关系中分解出的体力项，因而\ :math:`f_i`\ 仅仅存在于震源区的一个点或者断层面上。

根据Aki & Richards (1980)中的表示定理：

.. math::

   u_n(x,t) = \int_{-\infty}^{\infty} d \tau \iiint_V f_p(\bm{\eta}, \bm{\tau}) G_{np}(\bm{x}, t-\tau, \bm{\eta},0) d V(\bm{\eta})\\

.. math::

   + \int_{-\infty}^{\infty} d \tau \iint_{\Sigma} \left[ u_i(\bm{\xi}, \bm{\tau}) \right] c_{ijpq} \nu_j G_{np,q}(\bm{x}, t-\tau; \bm{\xi},0) d \Sigma(\bm{\xi})

.. math::

   - \int_{-\infty}^{\infty} d \tau \iint_{\Sigma} \left[ T_p(\bm{u}(\bm{\xi}, \tau), \bm{\nu}) G_{np}(\bm{x}, t-\tau; \bm{\xi},0) \right] d \Sigma(\bm{\xi})

位移分为三项，第一项为体力引起的位移，这一项在波传播中可忽略；

第二项是位移不连续引起的位移，其等效体力为

.. math::

   f_p^{[\bm{u}]}(\bm{\eta}, \tau) = - \iint_{\Sigma}[u_i(\bm{\xi}, \tau)]c_{ijpq} \nu_j \frac{\partial}{\partial \eta_q} \delta(\bm{\eta}-\bm{\xi}) d \Sigma

第三项是应力不连续引起的位移，其等效体力为

.. math::

   \bm{f}^{[\bm{T}]}(\bm{\eta}, \tau) = - \iint_{\Sigma}[\bm{T}(\bm{u}(\bm{\xi},\tau),\bm{\nu})] \delta(\bm{\eta}-\bm{\xi}) d \Sigma(\bm{\xi})

地震学研究中常用的源是位错源，即第二项。

因而很多文献中的波动方程，\ :math:`f_i`\ 都不是体力项，而是等效体力项。

参考文献：

1. Julian, B. R., Miller, A. D., & Foulger, G. R. (1998). Non‐double‐couple earthquakes 1. Theory. Reviews of Geophysics, 36(4), 525-549.

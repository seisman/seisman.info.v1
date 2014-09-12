仪器响应实例分析
################

:date: 2013-06-30 00:01
:modified: 2014-06-10
:author: SeisMan
:category: 地震学基础
:tags: 仪器响应
:slug: deep-analysis-of-response
:depends: mathjax

.. contents::

仪器响应水很深，用起来容易，弄明白每一个参数却不简单，幸好SEED的manual提供了一个例子，可以帮助理解，不过其写得太复杂、毫无重点且有些地方打印有错误，故而这里整理并改写一下。

这个仪器响应依然是标准的三个阶段：地震仪（运动信号转电压信号）、离散器（模电转换器）、FIR滤波器。

Stage 1
=======

假定仪器的自然频率为\ :math:`f_0=1Hz`\ ，阻尼常数为\ :math:`\lambda=0.7`\ ，该仪器的加速度传递函数为

.. math::

   H(s) = \frac{s}{s^2+2\lambda \omega_0 s + \omega_0^2}

对于这样一个传递函数，需要注意如下几点：

#. 该传递函数仅表示某一类地震仪的传递函数，现代地震仪的传递函数可能比这个更复杂；
#. 根据该传递函数，很容易计算出它的一个零点和两个极点；
#. 该仪器在\ :math:`f_s=1 Hz`\ 时的Sensitivity为\ :math:`S_d=150V/m\cdot s^{-2}`\ 。即地震仪接收到的地面运动加速度，如果1 Hz时加速度为\ :math:`1 m/s^2`\ ，则地震仪的输出电压为150V。
#. 仪器真实的传递函数应该是\ :math:`G(f)=R(f)*S_d=A_0*H(s)*S_d`\ 。其中\ :math:`A_0`\ 为归一化因子，即保证在频率\ :math:`f=f_s`\ 时有\ :math:`|R(f_s)|=1.0`\ 。

Stage 2
=======

使用的模数转换器ADC为24bit的，即输出最大值可以为\ :math:`\pm 2^{23}`\ ，如果ADC所能转换的电压范围为\ :math:`\pm 20V`\ ，则ADC的放大系数为\ :math:`S_d=\frac{2^{23}}{20}=4.1943*10^{5} counts/V`\ 。这样一个ADC在输入电压为1V的情况下，其输出为\ :math:`4.1943*10^{5}`\ counts。结合地震仪的放大系数，\ :math:`1 m/s^2`\ 的地面运动加速度将导致输出为

.. math::

   1 m/s^2 * 150 \frac{V}{m/s^2} * 4.1943\times 10^5 \frac{counts}{V} = 6.29145*10^7 counts

另一方面，ADC的输入电压上限为20V，这似乎也限制了该仪器所能记录到的最大加速度为\ :math:`20/150=0.13 m/s^2`\ 。

Stage 3
=======

这个阶段的FIR滤波器通过给定多项式系数来实现。给定系数之后即可计算其响应函数，并计算该响应函数在1 Hz处的振幅，然后得到归一化因子即为该阶段的放大系数为1.9938。

Stage 0
=======

最终得到的放大系数为

.. math::

   Sd= 150 \frac{V}{m/s^2} \cdot 4.1943\times 10^5 \frac{counts}{V} \cdot 1.9938 \frac{counts}{counts}=1.25439\times 10^8 \frac{counts}{m/s^2}

最后不要忘了第一阶段的无单位的归一化因子\ :math:`A_0`\ 。

参考
====

- `SEED Reference Manual <http://www.fdsn.org/seed_manual/SEEDManual_V2.4.pdf>`_, Version 2.4, August 2012, P162-169

修订历史
========

- 2013-06-30：初稿；
- 2014-06-10：修订关于自然频率和归一化频率的问题；Thanks to 张申健；

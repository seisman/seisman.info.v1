Hi-net的仪器响应
################

:date: 2014-09-06
:author: SeisMan
:category: 地震学基础
:tags: Hinet, 仪器响应
:slug: hinet-instrumental-response
:depends: mathjax

.. contents::

前文介绍了channel table文件的格式以及每一列的含义，其中7-13列记录了channel的仪器信息。由于Hi-net并没有像IRIS那样提供RESP或SAC_PZ文件，因而需要用户根据7-13列的信息手动推导仪器响应。

警告
====

本文是在Hi-net官方网站内容、Hi-net官方回复邮件内容以及个人对于仪器响应的理解的基础上完成的。

本人无法保证本文的内容是完全正确的，望读者带着批判的眼光阅读本文！

若因阅读本文内容而造成数据处理的任何偏差以及由此带来的任何后果，由用户自己承担。

回顾
====

先回顾一下7-13列的含义：

- [7]：Quantization bit rate of A/D conversion
- [8]：Sensor sensitivity (in V/unit_of_input)
- [9]：Unit of input
- [10]：Nature period of the sensor
- [11]：Damping constant of the sensor
- [12]：Amplification factor applied to sensor output prior to A/D conversion (in dB)
- [13]：LSB value of A/D conversion

流程
====

根据\ `《仪器响应的物理细节》 <{filename}/SeisBasic/2013-06-26_physical-details-of-instrumental-response.rst>`_\ 一文的分析，将7-13列按照仪器响应的过程再细分一下：

- 输入：波场振幅（[9]）
- 输入增强：对输入波场进行放大（[12]）
- Analog Stage：将连续的波场振幅转换为连续电压信号（[10]、[11]、[8]）
- Analog-Digital Conversion：将连续电压信号转换为离散电压信号（[7]、[13]）
- Digital Stage：对离散数据进行处理

输入
----

[9]给出了输入波场振幅\ :math:`A_0`\ 的单位，一般来说，其值为\ ``m/s``\ ，即Hi-net是速度地震仪。

输入增强
--------

这一步对输入的波场振幅进行放大，[12]给出了放大系数\ :math:`L_{dB}`\ ，单位为dB。

根据维基百科中对\ `场量分贝 <http://en.wikipedia.org/wiki/Decibel#Field_quantities>`_\ 的定义可知：

.. math::

   L_{dB} = 20 \log_{10}\left(\frac{A_1}{A_0}\right)

因而，本步骤的输出波场振幅\ :math:`A_1`\ 为

.. math::

   A_1 = A_0 10^{\frac{L_{dB}}{20}}

Analog Stage
------------

在Hi-net的官方回复邮件中提到，Hi-net统一使用的是”moving coil velocity type seismometer“，此种地震仪的transfer函数在Laplace域表示为：

.. math::

   G \frac{s^2}{s^2+2 h \omega s + \omega^2}

其中

- \ :math:`G`\ ：Sensor sensitivity，即\ :math:`G`\ = [8]
- \ :math:`h`\ ：damping constant， 即\ :math:`h`\ = [11]
- \ :math:`\omega`\ ： natural angular frequency，即\ :math:`\omega=\frac{2\pi}{[10]}`

从channel table即可计算出这三个量，代入transfer函数，根据\ `仪器响应实例分析 <{filename}/SeisBasic/2013-06-30_deep-analysis-of-response.rst>`_\ 中的类似步骤，即可计算出零点和极点，以及归一化因子\ :math:`A_0`\ 。

PS：对于速度场而言，可以推导得到\ :math:`A_0 = 2*[11]`

Analog-Digital Conversion
-------------------------

首先需要理解两个概念，bit rate和LSB value。

模数转换器（ADC）的作用是将连续的模拟信号（电压，单位V）转换为离散的数字信号（单位为counts）。如果一个ADC的bit rate为8，则该ADC可以将模拟信号编码为\ :math:`2^8=256`\ 个不同的离散值，从0至255或从-128到127。

若该ADC的电压测量范围为\ :math:`\pm 20 V`\ ，则该ADC可以将40V的电压测量范围转换为256种离散值，因而该ADC的电压分辨率为40/256 V/counts。这一电压分辨率也称为最低有效位（LSB）电压，即“使得输出离散信号产生一个变化所需的最小输入电压的差值”。

bit rate与LSB value之间的关系如下：

.. math::

   \frac{V_{high}-V_{low}}{2^{bitrate}}

其中\ :math:`V_{high}`\ 和\ :math:`V_{low}`\ 分别为ADC的测量电压上下限。

LSB value的倒数\ :math:`\frac{1}{[13]}`\ ，其单位为\ :math:`counts/V`\ ，即单位电压所对应的离散值得变化量，也就是这一阶段的增益\ :math:`S_d=\frac{1}{[13]}`\ 。

Digital Stage
-------------

这一阶段，对离散信号进行处理，需要考虑这个过程中的增益。

在Hi-net官方的\ `Response of Observation Equipment <http://www.hinet.bosai.go.jp/REGS/seed/?LANG=en>`_\ 说明中，给出了三种仪器响应RESP文件，并指出

    In all response files for Hi-net data, sensor sensitivity is set to the case of 200 V/(cm/s).
    Actual sensitivity of each channel is shown at the 8th column of the channel table file.
    This means that the values at 37th line from the top and 4th line from the bottom
    should be modified from the response file in this web page, considering this point.

即\ `Response of Observation Equipment <http://www.hinet.bosai.go.jp/REGS/seed/?LANG=en>`_\ 中给出的三种仪器响应RESP文件，仅仅只是示例，每个RESP文件的前37行和后4行（PS：此处行号并不包括注释行）必须根据channel table中的值进行修改，而其余行则不需要修改。看看RESP文件的内容可知，不需要修改的行恰好对应Digital Stage（stage number为3或4），这暗示着\ **Hi-net的所有channel的Digital Stage部分是完全相同的**\ 。

从RESP文件中可以看出，stage 3和stage 4虽然看上去很复杂，但实际上其振幅增益\ :math:`S_d=1.0`\ 。换句话说，也就是不必过多考虑这一阶段。

总结
=====

- 检查[9]确认输入波场为速度场
- 由[12]计算波场放大系数
- 由[10]、[11]构造增益为1的transfer函数，计算其零点和极点，并计算transfer函数在自然频率处的振幅，以得到归一化因子\ :math:`A_0`
- [8]为增益，可直接使用
- 对[13]列取倒数得到增益（[7]没有用）

由此，可根据channel table完整构建每个channel的仪器响应文件，RESP格式或SAC_PZ格式均可，一般用SAC_PZ格式即可。


附录
====

官方回复邮件
------------

Question1: Apr 24, 2014 09:32 (UT) +0900(JST)  

::

    Hi,

    I am using Hi-net data and am confused with the instrumental response
    even after I have looked through all pages of Hi-net website.

    In the page of 'For Registered Users' -> 'Response of Observation Equipment',
    only three RESP files are given. It seems that I have to rewrite a new RESP
    or SAC_PZ file for each channel.

    So I have to confirm that I understand details of response, which are very
    important for correct data processing.

    1. Do all channels have the same zeroes and poles?
    2. At line 19, do all channels have the same A0 Normalization factor (0.999953)?
    3. In the FAQ Q08, one equation is given to convert the A/D value from an WIN32
       file to the corresponding physical quantity. It is

            v = I * [13] / ( [8] * 10 ^ ( [12] / 20 ) )

       If I want to generate a SAC PZ file, the CONSTANT will be

        CONSTANT = [8]*10^([12]/20) / [13] * A0 ?

    I am looking forward to your reply.

    Best Regards.

Answer1:  May 07, 2014 08:30 (UT) +0900(JST)  

::

    Thank you for accessing our website.
    This is the NIED Hi-net/F-net/V-net administrator.

    In the "Response of Observation Equipment" page, sample RESP files are
    provided and you need to modify them according to your purposes, as you
    wrote. The explanation in this page assumes that the parameters of the
    seismometer other than the gain factor do not change. Strictly speaking,
    the zeros, the poles, and the A0 normalization factor can change
    depending on the parameters of the seismometer. The moving coil velocity
    type seismometer is used in Hi-net and its transfer function in the
    Laplace domain is given as:

        Gs^2/(s^2 + 2hws + w^2)

    where G, h and w are the gain factor, the damping constant, and the
    natural angular frequency, respectively. Roots of the numerator and the
    denominator correspond to the zeros and the poles, respectively, and the
    A0 normalization factor is the inverse of the absolute value of the
    above equation except G at the normalization frequency. Detailed
    explanation about this type of seismometer is available in many
    literature, such as,

    Scherbaum, F., Of Poles and Zeros: Fundamentals of Digital Seismology,
    Kluwer Academic Publishers, 1996.
    #see chapter 4

    The gain factor, the damping constant, and the natural period are
    provided in the channels table file as explained in the Q&A08.
    Note that the gain factor is measured at its natural frequency.
    http://www.hinet.bosai.go.jp/faq/?LANG=en#Q08

    Please read the SEED manual about further details and SAC manual about
    SAC PZ file.

    - SEED: http://www.fdsn.org/publications.htm
    - SAC: http://www.iris.edu/files/sac-manual/

    Sincerely,

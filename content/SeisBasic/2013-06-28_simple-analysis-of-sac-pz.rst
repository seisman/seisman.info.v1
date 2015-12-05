仪器响应文件SAC PZ
###################

:date: 2013-06-28 00:13
:author: SeisMan
:category: 地震学基础
:tags: 仪器响应
:slug: simple-analysis-of-sac-pz
:summary: 介绍SAC PZ文件的格式。
:depends: mathjax

RESP文件是SEED格式默认的仪器响应文件，在上一篇博文《\ `仪器响应文件RESP <{filename}/SeisBasic/2013-06-27_simple-analysis-of-resp.rst>`_\ 》中已经分析了一个例子。RESP响应文件完整地描述了仪器响应的全部信息，与此同时也包含了不少冗余信息。

SAC对RESP文件进行了简化，仅包含了一些必要信息，这个新的文件格式叫做SAC_PZ。下面给出一个PZ文件的例子，其与上一篇博文中的RESP文件对应同一个台站，因而利用上一篇的RESP文件可以完整推导出本文的PZ文件。

::

    * **********************************
    * NETWORK   (KNETWK): IU
    * STATION    (KSTNM): COLA
    * LOCATION   (KHOLE): 00
    * CHANNEL   (KCMPNM): BHZ
    * CREATED           : 2013-06-22T14:12:09
    * START             : 2012-09-14T04:00:00
    * END               : 2599-12-31T23:59:59
    * DESCRIPTION       : College Outpost, Alaska, USA
    * LATITUDE          : 64.873599
    * LONGITUDE         : -147.861600
    * ELEVATION         : 84.0
    * DEPTH             : 116.0
    * DIP               : 0.0
    * AZIMUTH           : 0.0
    * SAMPLE RATE       : 20.0
    * INPUT UNIT        : M
    * OUTPUT UNIT       : COUNTS
    * INSTTYPE          : Geotech KS-54000 Borehole Seismometer
    * INSTGAIN          : 2.013040e+03 (M/S)
    * COMMENT           : N/A
    * SENSITIVITY       : 3.377320e+09 (M/S)
    * A0                : 8.627050e+04
    * **********************************
    ZEROS   3
            +0.000000e+00   +0.000000e+00
            +0.000000e+00   +0.000000e+00
            +0.000000e+00   +0.000000e+00
    POLES   5
            -5.943130e+01   +0.000000e+00
            -2.271210e+01   +2.710650e+01
            -2.271210e+01   -2.710650e+01
            -4.800400e-03   +0.000000e+00
            -7.384400e-02   +0.000000e+00
    CONSTANT        +2.913631e+14

星号部分是注释，其包含了台站的一些信息，这些信息比RESP文件中的内容要更丰富，比如台站名、台网名、location、channel、台站经纬度、高程、输入、输出、放大系数、归一化因子等。

然后给出了零点和极点的信息，跟RESP比较一下，发现极点信息是对的。零点个数比RESP文件多了一个。

这是为什么呢？

Laplace变换有一个很重要的性质：如果\ :math:`f(t)`\ 的Laplace变换为\ :math:`F(s)`\ ，那么\ :math:`f(t)`\ 的一阶时间偏导\ :math:`f'(t)`\ 的Laplace变换为\ :math:`sF(s)`\ ，也就是多了一个零点(0.0,0.0)。RESP文件认为仪器的输入是速度，因而其单位是m/s，而PZ文件认为输入为位移，单位为m，因而PZ文件的仪器响应首先要将位移经过一次偏导得到速度，再根据RESP的零极点信息转换为电压信息。一切都是可以合理解释的。

前面已经说过，整个仪器响应可以简化为

.. math::

   G(f)=S_{d1} A_0 H_p(s) S_{d2} S_{d3}=S_{d0} A_0 H_p(s)

所以PZ文件中将所有的放大系数以及归一化因子合并成为一个常数，也就是最后的 ``CONSTANT`` 。

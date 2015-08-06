地震数据的命名规则
##################

:author: SeisMan
:date: 2014-03-05 21:48
:category: 地震学基础
:tag: 数据
:slug: seismic-file-name-convections

.. contents::

利用rdseed程序可以很容易地从SEED格式数据中解压得到SAC格式的地震记录，下面就是一个SAC数据的文件名::

    2013.166.17.34.00.0195.IU.HRV.10.BHZ.M.SAC

这篇博文说一说文件的命名规则。

文件名格式
==========

根据rdseed的Manual，SAC数据的文件名形式如下::

    yyyy.ddd.hh.mm.ss.ffff.NN.SSSSS.LL.CCC.Q.SAC

其中

- yyyy.ddd.hh.mm.ss.ffff是SAC文件中第一个数据点对应的时间

  + yyyy为年；
  + ddd为一年的第多少天；
  + hh.mm.ss为时, 分, 秒；
  + ffff为毫秒；需要注意的是1s=1000ms, 这里毫秒却用了4位来表示，这里很容易出错。

- NN为台网名，2字符；
- SSSSS为台站名，一般是3个字符，偶尔见到4字符的；
- LL为location id；为空或两字符；
- CCC为通道名；
- Q为质量控制标识；
- SAC为文件后缀；

Location ID: LL
===============

什么是Location ID呢？我也没有找到比较权威的解释。

常见的Location ID为空，偶尔会见到\ ``00``\ , \ ``01``\ , \ ``10``\ 这样的，也有遇到\ ``60``\ 这样的。

Location ID其实是台站下的subcode，即一个台站处，有多套仪器，这些仪器可能是相同的型号，但是位于不同的深度或者指向不同的方位；也有可能是两个仪器是不同的型号。

经常见到的情况是，同一个台站，不同location ID的两个地震数据具有极为相似但有略有不同的波形，这个就自己慢慢领悟吧。

质量控制: Q
===========

质量控制标识有四种:

- D: Data of undetermined state
- M: Merged Data
- R: Raw waveform Data
- Q: QC'd data

一般见到的都是M。

通道名: CCC
===========

通道名用三个字符来表示，这三个字符分别代表了Band Code、Instrument Code和Orientation Code。

Band Code
---------

Band Code是通道名的第一个字符，表示了仪器的采样率以及响应频带等信息。

.. figure:: /images/2014030501.jpg
   :align: center
   :width: 700px
   :height: 400px
   :alt: Band Code from SEED Reference Manual

   Band Code

常见的仪器一般是宽频带(B)或长周期(L)。

Instrument Code
---------------

Instrument Code是通道名的第二个字符，代表了不同的仪器传感器。

=============== =========================
Instrument Code         说明
=============== =========================
H               High Gain Seismometer
L               Low Gain Seismometer
G               Gravimeter
M               Mass position Seismometer
N               Accelerometer
=============== =========================

常见的是高增益(H)仪器，记录地面运动速度。

Orientation Code
----------------

Orientation Code表示了传感器记录的地面运动的方向。

===== =============================
Code            说明
===== =============================
N E Z  南北向、东西向、垂向
1 2 3  3为垂向；1、2为水平方向，
       正交但与东西南北向有偏离
T R    切向、径向，主要用于射线束中
A B C  三轴向(正交)
U V W  可选分量
===== =============================

常见的是N、E、Z以及1、2、3。

需要注意的是：当仪器的方向与东西方向的夹角小于5度时，此Orientation Code 取为E；当与东西方向夹角大于5度时，Orientation Code取为1(或2).对于南北方向同理。

因而，即便Orientation Code为N，也并不意味着台站是南北方向的，真实的方向还是需要看SAC头段中的\ ``cmpaz``\ 和\ ``cpminc``\ 。

参考
====

#. rdseed 5.3.1 Manual
#. SEED Reference Manual v2.4, Appendix A, P136-P140

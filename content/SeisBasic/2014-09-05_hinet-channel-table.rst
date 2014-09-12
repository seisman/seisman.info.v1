Hi-net Channel Table文件
########################

:date: 2014-09-05 00:01
:modified: 2014-09-09
:author: SeisMan
:category: 地震学基础
:tags: Hinet, 仪器响应
:slug: hinet-channel-table

.. contents::

从Hi-net下载连续波形数据会得到ZIP压缩文件，其中包含了两个后缀为\ ``ch``\ 的文件，即Channel Table文件。两个文件内容是相同的，区别在于一个是\ ``euc``\ 编码，一个是\ ``sjis``\ 编码。只需要用其中一个即可，这里选择\ ``euc``\ 编码的文件。

Channel Table文件描述了每个channel的仪器信息。

规律分析
========

看一看Channelt Table文件的内容，很容易总结出如下规律：

- 每个台站的信息需要四行；
- 第一行以“#”开头，描述了台站名称及其他信息，可以认为是注释行；
- 第二至四行，分别为U、N、E三个分量的仪器信息；

但细细看看文件内容会发现，存在很多不符合上述规律的特例，比如：

- 有些台站只有一个或两个分量，而不是三个；
- 有些台站不包含N、E分量，而包含X、Y分量；

因而，若按照上面总结出的规律去做文本处理，会出现很多问题。更严谨的处理方式应该是：将所有以“#”开头的行当作注释行，其余行平等对待，即最小单位是channel或分量，而不是台站。

格式
====

一个channel包含了如下以\ **空格**\ 分隔的19列信息::

    2903 1 0 N.AGWH U 6 27 154.30 m/s 0.96 0.70 0 1.023e-07 43.0842 140.8199 -77 0 0 Akaigawa

每列的具体含义如下（后加问号则表示不那么确定）：

#. Channle ID：16-bit，用四位的16进制数表示，用于唯一标识一个channel；
#. Recording flag：若为1则表示该channel正常记录数据，值一般为1（？）
#. Delay time on a circuit：电路中的时间延迟，值一般为0
#. Station code：台站代码，Hi-net的台站代码格式为\ ``N.xxxH``\ ；
#. Motion component code：分量名，可以取值包括U、N、E、X、Y；
#. Reduction ratio of monitor waveform amplitude：显示器上的显示振幅与实际振幅之间的比例，其值为2的指数（？）
#. Quantization bit rate in A/D conversion：模数转换器的量化分辨率，一般值为27，个别值为20或24；
#. Sensor sensitivity：每单位输入所产生的输出为多少V；
#. Unit of input：输入的单位，一般为\ ``m/s``\ ，即输入为速度；
#. Natural period of the seismometer：传感器的自然周期；
#. Damping constant of the seismometer：传感器的衰减常数；
#. Amplification factor applied to sensor output prior to A/D conversion：在对连续波形使用ADC之前，传感器的放大因子；单位dB
#. LSB value：模数转换器的LSB值；
#. Latitude：台站纬度
#. Longitude：台站经度
#. Altitude：台站高程（单位为m）
#. P波台站校正：一般为0
#. S波台站校正：一般为0
#. 台站名称

补充说明
========

Channel ID
----------

常见的Channel ID为四位16进制数，实际上有另一类ID称为宽Channel ID，其用八位16进制表示。一般用不到，所以在本文以及后面都不会再提到。

Motion component code
---------------------

Channel Table中仅给出了分量代码，可以取值为U、N、E、X、Y。其中U表示分量为垂直方向。N、E表示分量指向北向和东向。X、Y的含义未知。

由于传感器安装在borehole的底部，所以很难精确知道传感器的真实方位。以分量代码为N的传感器为例，该传感器并不一定严格指向正北方向。一般而言，其与正北方向的夹角在5度以内，个别传感器的方向甚至与北向相差几十度。每个传感器的方位信息位于该\ `页面 <http://www.hinet.bosai.go.jp/REGS/direc/?subject=kekka>`_\ 。

在Channel Table中，只给出了分量代码而没有给出具体的方位信息。因而只能根据分量代码做一些可靠的假设。对于U向分量\ ``cmpaz=0``\ 、\ ``cmpinc=0``\ ；对于N向分量\ ``cmpaz=0``\ 、\ ``cmpinc=90``\ ；对于E向分量\ ``cmpaz=90``\ 、\ ``cmpinc=90``\ 。

Units of input
--------------

Hi-net使用的是短周期速度地震仪，输入为速度场，单位为\ ``m/s``\ ，而部分channel的输入单位为\ ``m/s/s``\ ，即输入为加速度场。

输入单位为\ ``m/s/s``\ 的channel，与输入单位为\ ``m/s``\ 的channel相比，在后期的数据处理上差别很多，因而不建议提取输入单位为\ ``m/s/s``\ 的通道数据。

Natural period of the seismometer
---------------------------------

截至2014年09月08日，对于这一列的含义有两种说法：

- ``readme.txt``\ 中对该列解释为\ **Eigen frequency of the sensor**
- `Hi-net FAQ 08 <http://www.hinet.bosai.go.jp/faq/?LANG=en#Q08>`_\ 中该列解释为\ **Natural period of the seismometer**

Hi-net官方回复指出，FAQ08中的解释是正确的，即第10列为“Natural period of the seismometer”。

总结
====

19列信息：

- Channel标识为：1
- 含义很明显，可以直接使用的有：4、5、14、15、16、19；
- 基本没用途，可以不必关心的有一：2、3、6、17、18；
- 与仪器有关的为7、8、9、10、11、12、13；

接下来会有专门的博文介绍如何根据7-13列确定该channel的仪器响应。

参考
====

#. 从Hi-net下载连续波形数据得到的ZIP文件中的\ ``readme.txt``\ ；
#. \ `Hi-net FAQ 08 <http://www.hinet.bosai.go.jp/faq/?LANG=en#Q08>`_\
#. \ `Azimuth information of the Hi-net borehole sensors <http://www.hinet.bosai.go.jp/REGS/direc/?LANG=en>`_\

修订历史
========

- 2014-09-05：初稿；
- 2014-09-09：Hi-net官方确定了第10列的含义；

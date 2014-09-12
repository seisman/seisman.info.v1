SAC中与台站有关的头段
#######################
:date: 2013-09-03 23:40
:author: SeisMan
:category: SAC
:slug: headers-of-station-in-sac

SAC头段中与台站有关的变量有：

-  KNETWK：台网名；
-  KSTNM：台站名；
-  ISTREG：台站地理区域（未使用）；
-  STLA：台站纬度（北为正）；
-  STLO：台站经度（东为正）；
-  STEL：台站高程（m，未使用）；
-  STDP：台站相对地表深度（m，未使用）；
-  CMPAZ：分量方位角；（从北开始顺时针度数）
-  CMPINC：分量入射角；（从垂直开始的角度）
-  KCMPNM：分量名称，比如BHE
-  LPSPOL：如果台站分量为正极性则为真（左手规则）；

其中与台站分量有关的头段变量有四个，即CMPAZ、CMPINC、KCMPNM、LPSPOL。

CMPAZ和CMPINC在进行波形旋转的时候很重要。根据CMPAZ和CMPINC的定义可知，对于标准三分量台站有：

-  N向：CMPAZ=0；CMPINC=90；
-  E向：CMPAZ=90；CMPINC=90；
-  Z向：CMPAZ=0；CMPINC=0；

KCMPNM标记了分量的名称，SEED格式中一般使用三个字符表示，比如BHE，第一个字符表示宽频带，第二个字符表示高增益，第三个字符表示E向分量。有兴趣的可以参考SEED中关于Channel命名的说明：\ `http://www.iris.edu/manuals/SEED\_appA.htm`_

变量LPSPOL是个很有意思的头段变量，若三分量的正极性方向符合左手规则则该变量为真。

关于左手定则，可以参考维基百科的\ `右手定则`_\ 条目。

下图简单给出了左手定则和右手定则的示意图，图中左图符合左手定则，右图符合右手定则。

.. figure:: /images/2013090301.jpg
   :width: 400px
   :alt: left-and-right

在地震学中，一般取北向为x轴，东向为y轴，向上为z轴，即符合上图的左手定则，也就是常说的NEU坐标系。但是，在有些情况下，取向下为z轴正向，此时符合右手定则（倒过来看），也就是更常见的NED坐标系。

目前已经搞清楚的一些事实是，Aki &
Richards(1980)中的坐标主要以NED坐标系为主，而常用的计算理论地震图的程序fk采用的则是NEU坐标系。除此之外，还有其他坐标系，以后整理清楚再说。

.. _`http://www.iris.edu/manuals/SEED\_appA.htm`: http://www.iris.edu/manuals/SEED_appA.htm
.. _右手定则: http://zh.wikipedia.org/wiki/%E5%8F%B3%E6%89%8B%E5%AE%9A%E5%89%87

pssac绘图之reduce velocity对齐
##############################

:date: 2013-08-07 00:18
:author: SeisMan
:category: 地震学软件
:tags: pssac
:slug: reduce-velocity-alignment-with-pssac
:summary: 介绍reduce velocity。

不晓得Reduce Velocity翻译成中文该怎么翻，Peter Shearer的Introduction to Seismology 中的一张图很好的解释了reduce velocity的概念：

.. figure:: /images/2013080701.jpg
   :alt: Reduce Velocity
   :width: 700 px

左图是标准的时距曲线X-T（也有人称走时图），左图的效果不甚理想，几条曲线斜率相近，密密麻麻放在一起看不清，由此得到了右图Reduced的时距曲线X-（T-X/8），其中8就是这里的reduce velocity，在这种图下，走时曲线更容易看了。

还是利用上一篇中生成的那些地震数据做实验。

先看看一个正常的不做任何时间对齐的剖面图（其实按照文件起始时间对齐了）：

::

 ./pssac -JX5i -R0/1420/10/40 -B200/5 -Edt-5 -M0.5/-1 \*.z > a.ps

.. figure:: /images/2013080702.jpg
   :alt: Figure
   :width: 700 px

再来看看reduce velocity的效果：

:: 

 ./pssac -JX5i -R0/1420/10/40 -B200/5 -Ed12 -M0.5/-1 \*.z > a.ps

.. figure:: /images/2013080703.jpg
   :alt: Figure
   :width: 700 px

这里reduce取了12，然后就大概把初至波给对齐了。reduce velocity的实质是将所有trace的起始时间都减去“X/V”，其中X是震中距，V是reduce 速度。

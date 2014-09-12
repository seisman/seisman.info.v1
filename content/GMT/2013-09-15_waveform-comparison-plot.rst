绘制波形对比图
##############

:date: 2013-09-15 00:29
:author: SeisMan
:category: GMT
:tags: GMT技巧, pssac, GMT4
:slug: waveform-comparison-plot

波形对比图，经常出现在如下场合：

#. 发展新的计算理论地震图的方法，与前人的结果做Benchmark；
#. 理论地震图与实际数据做对比，比如反演；
#. 展示多个波形的相关性；如doublet；

如下图所示，红色的三个trace是某差分程序计算出的地震图，黑色的三个trace是fk计算出的地震图，也就是上面的第一种情况：

.. figure:: /images/2013091501.jpg
   :align: center
   :alt: pssac figure

画地震波形肯定是要用pssac的，当初的做法是先用psbasemap绘制整体的边框，然后用六个pssac命令分别绘制每个trace，并使用-Y选项分别微调每个trace的垂直位置，这显然是一种非常笨的方法，尤其是在有很多个trace的情况下。

更好的绘图脚本如下：

.. code-block:: bash

 #!/bin/bash
 J="X6i/4i"
 B="0.2/1WeSn"
 R="0.4/2.0/0/4"
 PS="traces.ps"

 pssac -J$J -R$R -B$B -W1p/red -M1 -Ent-3 syn.* -K > $PS
 pssac -J$J -R$R -W1p/black -M1 -Ent-3 homo.* -O -Y0.1i >> $PS

这个脚本调用了两次pssac命令，第一个pssac绘制了三条红色的trace，同时绘制了底图和边框；第二个pssac命令绘制了三条黑色的trace，使用-Y选项实现垂直方位偏离。

第二个pssac命令中另一个特殊的地方在于没有使用-B选项。若有-B选项，则会出现两个边框，看上去是两张图的重叠与交错；而没有-B选项，两张图重叠在一起，看上去却是一张图，实现了波形对比的效果。这里充分利用了-B选项功能，详情参见\ `GMT进阶之被滥用的-B选项 <{filename}/GMT/2013-08-23_abused-b-option.rst>`_

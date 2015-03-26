pssac绘图之地震剖面图
#####################

:date: 2013-08-06 00:08
:author: SeisMan
:category: 地震学软件
:tags: pssac
:slug: plot-profile-with-pssac
:summary: 利用pssac绘制地震剖面图。

绘制剖面图首先需要一堆数据，这里使用SAC自带的一些数据作为例子（v101.4里面没有这些地震数据）：

::

    SAC> datagen sub tele ntkm.z nykm.z onkm.z sdkm.z
    SAC> w ntkm.z nykm.z onkm.z sdkm.z

用saclst命令看看这些数据的头段：

::

    $ saclst gcarc b e f *.z
    ntkm.z      23.4372    199.8647   1600.1013
    nykm.z      38.4145    199.8622   1600.1178
    onkm.z      25.3798    199.7684   1600.0247
    sdkm.z      17.4213    199.9976   1600.0104

从上面的显示可以看出来，这四个数据的震中距位于15-40度，文件起始时间约为200s，文件结束时间约为1600s。

下图给出了这几张地震图在SAC中画出来的效果：

::

    SAC> r *.z
    ntkm.z nykm.z onkm.z sdkm.z
    SAC> sort gcarc
    SAC> p1
    SAC> saveimg a.pdf
    save file a.pdf [PDF]

.. figure:: /images/2013080601.png
   :alt: Figure 1
   :width: 700 px

SAC画出来的图质量会比较差，效果不太好。

按照上篇博文中绘制单个地震图的方法同时画这几个地震图（注意-R的范围）：

::

     $ ./pssac -JX6i -R200/1600/-10/10 -B100/5 *.z > a.ps

.. figure:: /images/2013080602.jpg
   :alt: Figure 2
   :width: 700 px

可以看出来，四个trace在y=0处重叠在一起，完全不是想要的效果，下面画一个真正的剖面图（注意-R的范围）：

::

     $ ./pssac -JX6i -R0/1420/10/40 -B100/5 -Edt-5 -M1 *.z > a.ps

.. figure:: /images/2013080603.jpg
   :alt: Figure 3
   :width: 700 px

此处多了两个选项-E和-M，其中-Edt-5，d表示剖面类型为震中距，即y轴为震中距，所以-R中给出的y轴范围为（10，40），t-5代表所有的数据以文件起始时间对齐，上一篇博文中已经说过，这意味着所有trace的文件起始时间都是0，那么-R中的x轴范围就应该是（0，1400）。关于为什么为-5代表b，用-3代表o，这个是程序中的一些技巧决定的，习惯就好。如前所说，仅仅使用-E是无法实现真正的剖面图的，这就需要-M选项了。

如pssac的使用说明所说，-M选项有两种使用方式，一种是-Msize，另一种是-Msize/alpha。当使用-Msize时，在算法中的实现是所有数据点都乘以yscale，其中yscale=size\*fabs((north-south)/(h.depmax-h.depmin)/project\_info.pars[1])，其中north和south就是-R中给出的y方向的范围，h.depmax和h.depmin就是这个trace的最大和最小值，project\_info.pars[1]就是-J中指定的尺寸了，在这个例子中就是6。这样做使得所有的trace的最大值和最小值的差相等，且都等于y方向的一个单位长度，这里就是size英寸。比如上图大小为6英寸，y方向为40-10=30，即图上的每英寸代表y方向的5度（这里y轴是震中距，所以是度），那么size=1的时候，所有trace的最值之差也应该是1英寸，也就是5度的单位，上图证明了一切。这样的做法使得trace失去了绝对振幅和相对振幅。当使用-Msize/alpha时，若alpha<0，则根据第一个trace计算出yscale，以后所有的trace都会乘以相同的yscale，这样做使得各个trace失去了绝对振幅，但是却保持了相对振幅；若alpha>0，那么yscale=pow(fabs(h.dist),alpha)\*size。对于一个正常的地震来说，震中距越大，由于几何扩散和衰减的原因，振幅越小，这个选项就是为了将“丢失”的振幅找回来用的。

其他的选项与绘制单个地震图没有什么区别，下面就以一个比较完整的例子结束这篇博文吧：

::

     $ ./pssac -JX5i -R0/1420/10/40 -B200/5 -Edt1 -M0.5/-1 -G0/0/0/0 -r -S150 *.z > a.ps

.. figure:: /images/2013080604.jpg
   :alt: Figure 4
   :width: 700 px

这个例子中，我首先用sac大概将初至波到时标记了一下，并保存在头段变量T1中，-Edt1选项使得trace按照T1对齐，所以所有trace的初至对应的时刻是0，这样其实会很难看，所以又利用了-S选项将整个数据平移了150s，现在所有的初至大概都在150s那里了，当然你也可以选择不用-S选项而采用-R-150/1300/10/40这样的方法应该也是可以的。

关于pssac差不多就是这些了，还有两个小细节没有研究，一个是reduce\_velocity，一个是在命令行不指定文件名，而在stdin中给出\ ``sacfile [x [y [pen]]``\ 。这两个会放在下面两篇博文中说。

修订历史
=========

- 2013-08-06：初稿；
- 2014-01-11：修正\ ``-Edt-1``\ 为\ ``-Edt1``\ ；
- 2015-03-26：SAC新版本中\ ``saveimg``\ 默认只支持PS和PDF格式，此处将PNG改成PDF；

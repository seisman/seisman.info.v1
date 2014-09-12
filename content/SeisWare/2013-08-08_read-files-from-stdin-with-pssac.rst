pssac绘图之读stdin读入文件
##########################

:date: 2013-08-08 00:28
:author: SeisMan
:category: 地震学软件
:tags: pssac
:slug: read-files-from-stdin-with-pssac
:summary: pssac从标准输入中读取文件。

前几篇中提到，pssac有一个-W选项，其实际上是GMT的选项，可以控制trace的粗细颜色等特性。其相当于是一个全局的控制，所有的trace都会遵从-W给出的选项。如果你想要对每个trace有更灵活的控制，可以通过下面的方式来实现。

当在pssac的命令行中不指定文件名时，可以通过在stdin输入\ ``sac_file [x [y [pen]]]``\ 的方式获取对trace的更多控制。其中x指trace的水平位置，y指trace的垂直位置，pen与-W选项的作用相同。依然使用前面的几个数据。命令或脚本如下::

 ./pssac -JX6i -R0/2000/-10/10 -B200/2 -M1 > a.ps <<EOF
 ntkm.z 100 -8 0.25p,red,-
 nykm.z 200 -3 0.5p,blue,..-
 onkm.z 0 0 0.1p,black
 sdkm.z 300 5 0.5p,green,.
 EOF

.. figure:: /images/2013080801.jpg
   :alt: Figure
   :width: 700 px

这里分别指定了不同trace的水平和垂直位置，并分别指定了每条trace的粗细、颜色及线条。

到了这里，你可能会想用这样的方法来绘制下面这种图：

.. figure:: /images/2013080802.jpg
   :alt: Figure
   :width: 700 px

先用pscoast绘制一下后面的背景，然后再利用pssac并对每个trace指定其位置以及pen属性。想法是好的，实际上是不行的。原因在于pscoats使用了-J指定投影类型，-R指定了经纬度范围，而pssac也需要指定-J和-R，且pssac的-R横轴必须是时间，这两者是无法统一的（至少目前程序中无法统一）。因而你不可能通过指定经纬度的方式将某个trace放在你想要的经纬度上，因为pssac会使用自己的-R。总之就是此路不通，一个可行的方式是直接绘制单个地震图，然后利用-X和-Y选项进行位置的偏移，如果trace很多觉得很麻烦的话，或许可以根据台站的经纬度以及地图的-R的范围来计算每个trace的偏移量。这个工作量有点大，就不说啦。

至此，pssac应该就没啥问题了，接下来也许会看看pssac2。

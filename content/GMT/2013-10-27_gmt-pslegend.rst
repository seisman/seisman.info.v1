GMT命令之用pslegend绘制图例
###########################

:date: 2013-10-27 00:24
:author: SeisMan
:category: GMT
:tags: GMT命令, GMT脚本, GMT4
:slug: gmt-pslegend

.. contents::

GMT的psxy命令是很强大的，可以绘制各种颜色、各种类型的线段以及各种不同的符号。对于稍稍复杂的图来说，图例是必不可少的。图例的作用在于指明某种样式的线段代表什么样的数据，或者符号的大小如何与数据的具体数值相联系。

理论上来说，用psxy以及pstext就可以做出一个完整的图例了，只是这样的方法稍稍有些复杂。每个元素如何定位？每个元素之间间隔如何协调？这些都是个问题。pslegend算是解决了这个问题，从本质上来说，pslegend命令只是调用了psxy和pstext的相关功能。因而想要理解pslegend的用法，就得首先对psxy和\ `pstext <{filename}/GMT/2013-10-20_gmt-pstext.rst>`_\ 的用法有足够的了解。

语法
====

::

    usage: pslegend [<infofile>] -D[x]<x0>/<y0>/w/h/just -J<params> 
        -R<west>/<east>/<south>/<north>[r] [-B<params>] [-C<dx>/<dy>] [-F] [-G<fill>] 
        [-K] [-L<spacing>] [-O] [-P] [-S[<script>]] [-U[<just>/<dx>/<dy>/][c language="|<label>"][/c]] 
        [-V] [-X[a|c|r]<x_shift>[u]] [-Y[a|c|r]<x_shift>[u]] [-c<ncopies>]

选项
====

标准选项有-J、-R、-B、-K、-O、-P、-U、-V、-X、-Y、-c，不再说。

图例的位置-D
------------

::

    -D[x]lon/lat/width/height/just

首先可以指定整个图例的大小，也就是width和height，注意这里的width和height都用长度。

lon和lat则给定了图例的位置，just为两个字符，代表整个图例的对齐方式（这个可以参考pstext）。注意这里的lon和lat不是长度单位，而是对应地图上的某个坐标点。

如果想要指定图例离原点的距离，可以加个x，这样lon和lat代表的是长度而不是一个坐标点了。

两种指定位置的方式各有利弊，得按照实际需求选择。如果能够很好地与对齐方式just配合，则会更加方便。

下面的例子展示了常见的四种情形：

我个人更喜欢-Dx这种用法，只要知道了-JX的值8c，就可以很容易的得出图例的合适位置（0.2,0.2）,（7.8,0.2）,（0.2,7.8）,（7.8,7.8）；

.. code-block:: bash

 J=X8c
 R=0/5/0/5
 B=1g1/1g1WS
 PS=just.ps

 gmtset HEADER_FONT_SIZE 20
 gmtset HEADER_OFFSET 0.2c
 gmtset PAGE_ORIENTATION portrait

 psbasemap -J$J -R$R -B$B:."Bottom Left": -K > $PS
 pslegend -Dx0.2/0.2/2.5c/0.8c/BL -J$J -R$R -F -K -O << EOF >>$PS
 S 0.4c c 0.5 - 1p/black 0.8c Circle
 EOF

 psbasemap -J$J -R$R -B$B:."Bottom Right": -K -O -X10c >> $PS
 pslegend -Dx7.8/0.2/2.5c/0.8c/BR -J$J -R$R -F -K -O << EOF >>$PS
 S 0.4c c 0.5 - 1p/black 0.8c Circle
 EOF

 psbasemap -J$J -R$R -B$B:."Top Left": -K -O -X-10c -Y11c >> $PS
 pslegend -Dx0.2/7.8/2.5c/0.8c/TL -J$J -R$R -F -K -O << EOF >>$PS
 S 0.4c c 0.5 - 1p/black 0.8c Circle
 EOF

 psbasemap -J$J -R$R -B$B:."Top Right": -K -O -X10c >> $PS
 pslegend -Dx7.8/7.8/2.5c/0.8c/TR -J$J -R$R -F -O << EOF >>$PS
 S 0.4c c 0.5 - 1p/black 0.8c Circle
 EOF

 rm .gmt*

结果图：

.. figure:: /images/2013102701.jpg
   :align: center
   :alt: legend
   :width: 600 px

给图例加个框
------------

-F选项可以给图例加个框，框的线条由参数FRAME_PEN来控制。不管最终成图的时候，图例是否需要个框，在调试的时候有个框还是很有必要的，可以对整个图例的布局有更好的把握。

给图例区填色
------------

-G选项。默认是无填充的，加个背景色使得图例与地图本身有所区分也不错。

选项-C
------

-C选项可以控制图例框与内部图例之间的距离。

选项-L
------

设置图例里的行距比例。默认值为1.1，即行距为1.1倍的注释字体大小。

选项-S
------

前面已经说到pslegend本质上是调用了psxy和pstext。默认pslegend命令会生成相应的PS代码，可以用-K、-O加到PS绘图文件中。-S选项使得该命令不产生PS代码，而是产生由psxy和pstext构成的bash脚本。这样的话更加方便用户手动调节图例。毕竟pslegend没法完全发挥psxy和pstext的全部功能。但是需要注意的是改bash脚本本身是很危险的，牵一发而动全身。还是不太建议这样做。

输入文件格式
============

由于pslegend本质上是调用psxy和pstext，所以其输入文件的格式在很大程序上与psxy和pstext的文件格式有相似之处。

这个文件指定了图例中每个元素的细节，以及各个元素之间的相对顺序。输入文件中每一行称为一个记录，每个记录的首字符定义了该记录的具体含义，就像psxy中-Sc的c代表了circle一样。

根据首字符的不同，将所有的记录分为如下几类：

#
-

以“#”开头的记录代表注释行，后面可以加任意注释。该记录以及空白行都会被跳过。

B
-

以“B”开头的记录绘制一个水平color bar。其格式如下

::

    B cptname offset height [ optional arguments ]

cptname为color bar对应的cpt文件，offset定义了color bar与图例左边界的距离。该水平color bar的高度为height。另外可以直接将psscale的选项-A、-B、-E、-I、-L、-M、-N、-S、-Z加在记录的最后。

C
-

以“C”开头的记录定义了接下来所有文字的颜色。可以在不同的记录处使用C选项来不断改变文本颜色。

::

    C textcolor

D
-

格式如下：

::

    D offset pen

以“D”开头的记录会在图例中绘制一条水平线，其中pen定义了水平线的属性。除了画一条线之外，还会在线的上下各留出1/4行间距的空白。同时该水平线的离图例框左右各留出offset单位的距离。

G
-

::

    G gap

以“G”开头的记录会在垂直方向上产生一个gap，实际就是一个长度为gap的空白区。gap除了可以用i、c、p做单位外，还可以使用l（代表行）。

H
-

::

    H fontsize font header

以“H”开头的记录代表一个居中对齐的文本，fontsize和font指定了具体字体参数，若fontsize或font为“-”，则使用HEADER_FONT_SIZE和HEADER_FONT的值。header为要写的文本。这个主要用来写图例的标题。

I
-

::

    I imagefile width justification

将EPS文件或Sun光栅文件放在图例中的“当前位置”，有点psimage的意思。width为图像尺寸，justification为对齐方式。

L
-

::

    L fontsize font justification label

与“H”类似，这里的justification可以选择L、R、C，即左对齐、右对齐、居中对齐。label为具体文本。

M
-

::

    M slon slat length f|p [ −Rw/e/s/n −Jparam ]

该选项可以在图例中绘制比例尺（psscale）。地图在进行投影之后，不同的位置其比例尺不同，slon、slat指定了要绘制哪一点的比例尺（不是比例尺绘制在哪一点！）。slon仅对特定的倾斜投影有效，对于其他投影，可以设置slon为“-”。

lenth指定了比例尺的长度，默认单位为km（后加m代表英里，加n代表海里。），也可以加f或者p以使用fancy或者plain的比例尺。如果pslegend的-J和-R选项与绘制比例尺所需的-J、-R不同，则可以在记录中加入-J和-R参数。还有一堆看不懂的说明，等以后看了psscale再理解吧。

N
-

::

    N ncolumns

以“N”开头的记录，将图例等分为ncolumns列，该记录仅对图例中的符号（S）和标签（L）有影响。

S
-

::

    S dx1 symbol size fill pen [ dx2 text ]

最常用的记录类型，symbol指定了要绘制的符号的类型，具体参见psxy的-S选项，dx1为符号距图例当前列左边界的距离，如果只有一列，dx1就是距图例左边界的距离。size为符号尺寸，fill为符号填充，pen为符号轮廓。

可以给符号加上文本说明text，dx2指定了text距离左边界的距离。

对于两个特殊的符号front（f）和vector（v），在symbole后应加入该符号所需要的其他信息，具体参见示例。

T
-

::

    T paragraph-text

该记录会输入成段的文本，其字体由ANNOT_FONT_SIZE_PRIMARY和ANNOT_FONT_PRIMARY控制。如果想要控制更多特性，可以使用下面的“>”记录。

V
-

::

    V offset pen

与“D”记录类似，该记录在每两列之间绘制垂直线段（前提是图例被分为多列），offset是垂直线段离上下边界的空白距离。

>
-

::

    > paragraph-mode-header-for-pstext

这个记录调用pstext的段落模式，具体参见《\ `GMT命令之用pstext在图上写入文本 <{filename}/GMT/2013-10-20_gmt-pstext.rst>`_\ 》

例子
====

这个例子来自于GMT pslegend的官方例子，略有修改。

.. code-block:: bash

  pslegend -R-10/10/-10/10 -JM6i -Gazure1 -Dx0.5i/0.5i/5i/3.3i/BL -C0.1i/0.1i -L1.2 -F -B5f1 -P << EOF > map.ps
  G -0.1i
  # 设置标题
  H 24 Times-Roman My Map Legend
  # 水平线
  D 0.2i 1p
  # 分栏
  N 2
  # 垂直线起点
  V 0 1p
  # 7种符号
  S 0.1i c 0.15i p300/12 0.25p 0.3i This circle is hachured
  S 0.1i e 0.15i 255/255/0 0.25p 0.3i This ellipse is yellow
  S 0.1i w 0.15i 0/255/0 0.25p 0.3i This wedge is green
  S 0.1i f 0.25i/-1/0.075ilb 0/0/255 0.25p 0.3i This is a fault
  S 0.1i - 0.15i - 0.25tap 0.3i A contour
  S 0.1i v 0.25i/0.02i/0.06i/0.05i 255/0/255 0.25p 0.3i This is a vector
  S 0.1i i 0.15i 0/255/255 0.25p 0.3i This triangle is boring
  # 垂直线终点
  V 0 1p
  # 水平线
  D 0.2i 1p
  # 回到单栏模式
  N 1
  M 5 5 600+u f
  G 0.05i
  # I GMT_coverlogo.eps 3i CT
  G 0.05i
  # B colors.cpt 0.2i 0.2i
  G 0.05i
  L 9 4 R Smith et al., @%5%J. Geophys. Res., 99@%%, 2000
  G 0.1i
  T Let us just try some simple text that can go on a few lines.
  T There is no easy way to predetermine how many lines will be required,
  T so we may have to adjust the box height to get the right size box.
  EOF

.. figure:: /images/2013102702.jpg
   :align: center
   :alt: fig
   :width: 700 px

对于这个例子，如果在pslegend命令里加上-S选项，将会得到一个脚本，其内容为

.. code-block:: bash

 psbasemap -R0/5/0/3.3 -JX5i/-3.3i -Xr1.48425i -Yr1.48425i -K  -P -B0 -Gazure1
 echo '2.5 0.312167 24 0 Times-Roman BC My Map Legend ' | pstext -R -JX -O -K 
 echo 0.2 0.458333 > pslegend_26300.txt
 echo 4.8 0.458333 >> pslegend_26300.txt
 psxy -R -JX -O -K  -W1p pslegend_26300.txt
 rm -f pslegend_26300.txt
 echo 0.2 0.633333 | psxy -R -JX -O -K  -Sc0.15i -Gp300/12 -W0.25p
 echo '0.4 0.701389 14 0 0 BL This circle is hachured ' | pstext -R -JX -O -K 
 echo 2.7 0.633333 0 0.381 0.24765 | psxy -R -JX -O -K  -Se0.15i -G255/255/0 -W0.25p
 echo '2.9 0.701389 14 0 0 BL This ellipse is yellow ' | pstext -R -JX -O -K 
 echo 0.125 0.904167 20 60 | psxy -R -JX -O -K  -Sw0.15i -G0/255/0 -W0.25p
 echo '0.4 0.934722 14 0 0 BL This wedge is green ' | pstext -R -JX -O -K 
 echo 2.575 0.866667 > pslegend_26300.txt
 echo 2.825 0.866667 >> pslegend_26300.txt
 psxy -R -JX -O -K  -Sf-1/0.075ilb pslegend_26300.txt -G0/0/255 -W0.25p
 rm -f pslegend_26300.txt
 echo '2.9 0.934722 14 0 0 BL This is a fault ' | pstext -R -JX -O -K 
 echo 0.2 1.1 | psxy -R -JX -O -K  -S-0.15i -W0.25tap
 echo '0.4 1.16806 14 0 0 BL A contour ' | pstext -R -JX -O -K 
 echo 2.7 1.1 0 0.635 | psxy -R -JX -O -K  -Svb0.02i/0.06i/0.05i -G255/0/255 -W0.25p
 echo '2.9 1.16806 14 0 0 BL This is a vector ' | pstext -R -JX -O -K 
 echo 0.2 1.33333 | psxy -R -JX -O -K  -Si0.15i -G0/255/255 -W0.25p
 echo '0.4 1.40139 14 0 0 BL This triangle is boring ' | pstext -R -JX -O -K 
 echo # vertical lines > pslegend_26300.txt
 echo \> bar 1 >> pslegend_26300.txt
 echo 2.5 0.458333 >> pslegend_26300.txt
 echo 2.5 1.50833 >> pslegend_26300.txt
 psxy -R -JX -O -K  -W1p -H -m pslegend_26300.txt
 rm -f pslegend_26300.txt
 echo 0.2 1.50833 > pslegend_26300.txt
 echo 4.8 1.50833 >> pslegend_26300.txt
 psxy -R -JX -O -K  -W1p pslegend_26300.txt
 rm -f pslegend_26300.txt
 psbasemap -R-10/10/-10/10 -JM6i -O -K -Lfx2.5i/1.73333i/5/5/600+u
 psxy -R0/5/0/3.3 -JX5i/-3.3i -O -K -T
 echo '4.9 2.12732 9 0 4 BR Smith et al., @%5%J. Geophys. Res., 99@%%, 2000 ' | pstext -R -JX -O -K 
 echo \> 0.1 2.30887 14 0 0 TL 0.233333i 4.8i j > pslegend_26300.txt
 echo 'Let us just try some simple text that can go on a few lines. ' >> pslegend_26300.txt
 echo 'There is no easy way to predetermine how many lines will be required, ' >> pslegend_26300.txt
 echo 'so we may have to adjust the box height to get the right size box. ' >> pslegend_26300.txt
 pstext -R -JX -O -K  -m pslegend_26300.txt
 rm -f pslegend_26300.txt
 psxy -R-10/10/-10/10 -JM6i -T -Xr-0.5i -Yr-0.5i -O  -B5f1

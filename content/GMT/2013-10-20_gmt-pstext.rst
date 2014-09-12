GMT命令之用pstext在图上写入文本
################################

:date: 2013-10-20 09:42
:author: SeisMan
:category: GMT
:tags: GMT命令, GMT4
:slug: gmt-pstext

.. contents::

一张好图不仅仅是花花绿绿的颜色和各种样式的线条，还需要有必要的文字。GMT的-B选项可以设置坐标轴名、标签名、标题等，当需要在任意地方写任意字符串的时候则需要使用pstext命令。

语法
====

::

    usage: pstext <txtfile> -J<params> -R<west>/<east>/<south>/<north>[/<zmin/zmax>][r]
        [-A] [-B<params>] [-C<dx>/<dy>] [-D[j]<dx>[/<dy>][v[<pen>]]
        [-E<azim>/<elev>[+w<lon>/<lat>[<z>][+v<x0>/<y0>]] [-G<color>]
        [-H[<nrec>]] [-K] [-L] [-N] [-O] [-P] [-S<pen>] [-U[<just>/<dx>/<dy>/][c language="|<label>"][/c]]
        [-V] [-W[<fill>,][o|O|c|C[<pen>]]] [-X[a|c|r]<x_shift>[u]] 
        [-Y[a|c|r]<x_shift>[u]] [-Z[<zlevel>|+]] [-:[i|o]] [-c<ncopies>] 
        [-f[i|o]<colinfo>] [-m[<flag>]]

文件格式
========

输入文件包含一个或多个记录，每个记录的格式如下：

::

    x y size angle fontno justify text

其中

-  x、y：字符串在地图上的坐标位置；
-  size：文本字体大小，单位为points；
-  angle：文本相对于水平方向逆时针旋转的角度；
-  fontno：字体号，系统默认字体号为0-34，可以通过\ ``pstext -L``\ 命令获取GMT可用的所有字体；也可以直接用字体名来指定字体；
-  justify：文本对齐方式，即确定文本的哪个点对应（x，y）坐标；对齐方式由两个字符构成，第一个字符是L、C、R中的一个，分别代表左、中、右；第二个字符为T、M、B中的一个，分别代表上、中、下；比如BL代表文本的左下角位于(x,y)处；
-  text：要显示在地图上的字符串；除了最基本的英语字母、阿拉伯数字一些键盘上可见的符号之外，GMT还支持一些特殊字符及特殊效果，后面再说。

基本选项
========

pstext的必须选项有-J和-R，对于三维图来还需要-Jz；

其他一些标准选项包括：-B、-H、-K、-O、-P、-U、-V、-X、-Y、-：、-c、-f，不再多说。

-Z是三维绘图中常用的一个选项，不说。

最简单的例子如下：

.. code-block:: bash

 #!/bin/bash
 pstext -R0/10/0/10 -JX5i -B1g1f1/1f1g1 > a.ps <<EOF
 5 5 25 45 0 CM TEST
 EOF
 rm .gmt*

效果图：

.. figure:: /images/2013102001.jpg
   :width: 600px
   :alt: fig 1

由于justify选择了CM，所以字符串“TEST”的中心位于(5,5)处，然后整个字符串逆时针旋转了45度。

专有选项
========

选项-A
------

输入文件中angle指定了“文本方向与水平方向逆时针旋转的角度”，加上-A选项后，angle的定义变成了“方位角”，也就是相对于北向顺时针旋转的角度。

.. code-block::bash

 #!/bin/bash
 pstext -R0/360/-80/80 -JM5i -B30/30 -A > a.ps <<EOF
 180 30 25 0 0 CM TEXT1
 180 -30 25 90 0 CM TEXT2
 EOF
 rm .gmt*

.. figure:: /images/2013102002.jpg
   :width: 600px
   :alt: fig 1

从图中可以看到，加上-A选项之后，angle=0时，文本为垂直向的，angle=90时，文本为水平向的。

选项-W和-C
----------

-W可以在文本的周围加上一个矩形框，并可以设置矩形的填充色，使用o、O、c、C设置矩形轮廓细节，并可以设置矩形边框的画笔属性。-C选项设置了边框与文本之间的距离，默认为当前字体大小的15%，也可以使用具体的长度比如1c作为间距。

.. code-block:: bash

 #!/bin/bash
 pstext -R0/2/0/2 -JX2i -B1f1g1/1f1g1 -P -W -K > a.ps <<EOF
 1 1 25 0 0 CM TEXT1
 EOF

 pstext -R0/2/0/2 -JX2i -B1f1g1/1f1g1 -P -Wyellow,o3p,black,solid -K -O -X3i >> a.ps <<EOF
 1 1 25 0 0 CM TEXT2
 EOF

 pstext -R0/2/0/2 -JX2i -B1f1g1/1f1g1 -P -WO2p,blue -K -O -X-3i -Y3i >> a.ps <<EOF
 1 1 25 0 0 CM TEXT2
 EOF

 pstext -R0/2/0/2 -JX2i -B1f1g1/1f1g1 -P -W0/255/0,O2p,blue -C1c -K -O -X3i >> a.ps <<EOF
 1 1 25 0 0 CM TEXT3
 EOF

 rm .gmt*

.. figure:: /images/2013102003.jpg
   :width: 600px
   :alt: fig 1

-  左下角的图是没有使用-W和-C的参考图；
-  右下角的图设置填充颜色为yellow，o代表标准矩形轮廓，然后设置画笔属性为3p,black,solid；
-  左上角的图没有设置填充颜色，此时矩形框内无填充颜色，O表示圆角矩形轮廓，画笔属性为2p,blue；
-  右上角的图设置填充颜色为0/255/0；
-  矩形轮廓还可以用c和C，其仅可以在段落模式中使用，后面再说；

选项-D
------

-D选项可以使得文本的实际位置相对(x,y)有一定的偏移，格式为-Ddx/dy，其中dx和dy分别为相对与(x,y)点的偏移量，在最后追加v可以在(x,y)和文本真实位置之间加上一条直线。还有一种使用方式是-Djdx/dy，没看懂其原理。

.. code-block:: bash

 #!/bin/bash
 pstext -R0/4/0/4 -JX8c -B1f1g1/1f1g1 -D1c/1cv > a.ps <<EOF
 2 2 25 0 0 BL TEXT1
 1 1 25 0 0 CM TEXT2
 EOF

 rm .gmt*

.. figure:: /images/2013102004.jpg
   :width: 600px
   :alt: fig 1

选项-E
------

设置视角，可以指定Azimuth和Elevation。该选项不仅仅对文本有效果，对整个绘图都会产生影响。从不同的方向看一张图，看到的图像是不同的。默认azimuth=180,elevation=90，即视线与纸张垂直。elevation=0即视线与纸张完全平行，此时什么也看不到，所以elevation=0是被禁止的。azimuth=180为正常的看图方式，azimuth=0相当于将图倒过来看。

选项-G
------

设置文本颜色。

选项-L
------

该选项会列出GMT支持的字体名及对应的字体号。

选项-N
------

-R设定了地图的区域，当文本位置(x,y)或者偏移之后的文本位置(x+dx,y+dy)超过了-R的范围，默认文本不会被显示。-N选项使得超过-R范围的文本依然显示。

.. code-block:: bash

 #!/bin/bash
 pstext -R0/4/0/4 -JX4c -B1f1g1/1f1g1 -Gred -K > a.ps <<EOF
 3 0 25 0 0 CM TEXT
 EOF

 pstext -R0/4/0/4 -JX4c -B1f1g1/1f1g1 -Gred -N -O -X6c >> a.ps <<EOF
 3 0 25 0 0 CM TEXT
 EOF

 rm .gmt*

.. figure:: /images/2013102005.jpg
   :width: 600px
   :alt: fig 1

选项-S
------

绘制文本的轮廓，注意这里是文本的轮廓，而不是矩形框的轮廓。

.. code-block:: bash

 #!/bin/bash
 pstext -R0/4/0/4 -JX4c -B1f1g1/1f1g1 -S3p,red > a.ps <<EOF
 3 0 25 0 0 CM TEXT
 EOF

.. figure:: /images/2013102006.jpg
   :width: 600px
   :alt: fig 1

段落模式-m
==========

在其他命令中，-m一般表示输入文件是多段数据。在pstext命令中，其表示文本为段落模式。此时输入文件必须是多段文件，每段之间用特定记录隔开。该特定记录的格式如下：

::

    > x y size angle fontno justify linespace parwidth parjust

首字符为">"，第二个字符为空格，x、y、size、angle、fontno、justify与前面所说的相同。linespace为行间距，parwidth为段落的宽度，parjust为段落对齐方式，可以是l（左对齐）、c（居中对齐）、r（右对齐）、j（分散对齐）。
 
.. code-block:: bash

 #!/bin/bash
 pstext -R0/3/0/5 -JX3i -B1f1g1/1f1g1 -H -m -N -Y3i > a.ps <<EOF
 # x y size angle fontno justify linespace parwidth parjust
 > 0 -0.5 12 0 4 LT 13p 3i j
 @%5%Figure 1.@%% This illustration shows nothing useful, but it still needs
 a figure caption. Highlighted in @;255/0/0;red@;; you can see the locations
 of cities where it is @\_impossible@\_ to get any good Thai food; these are to be avoided.
 EOF

 rm .gmt*

.. figure:: /images/2013102007.jpg
   :width: 600px
   :alt: fig 1

GMT技巧之GMT与LaTeX的合作
##########################

:date: 2013-10-24 00:16
:author: SeisMan
:category: GMT
:tags: GMT技巧, 图像, 格式转换, LaTeX
:slug: use-latex-in-gmt

.. contents::

GMT的pstext命令支持一些简单的文本特效以及特殊字符，但是如果想在GMT中显示一些更复杂的公式或者其他，GMT则无能为力了。

这个时候自然而然就会想到功能强大的LaTeX了，写公式、画图都算是强项。显然GMT自身是无法直接支持LaTeX的语法的（若要支持LaTeX的语法，在绘图时必须调用LaTeX引擎，这样GMT对其他软件的依赖性过大，而且从技术上来说对于GMT的开发者来说也有些难度）。

虽然说用GMT绘图时在图上显示公式算是一个很小众的需求，从折腾的角度来看，还是很值得的。

用LaTeX写公式
=====================

下面的LaTeX代码包含了地震学里最基础的波动方程：

.. code-block:: latex

 \documentclass{book}
 \begin{document}

 \thispagestyle{empty}

 % 波动方程
 \begin{displaymath}
 \rho \frac{\partial^2 u_i}{\partial t^2} = f_i +\tau_{ij,j}
 \end{displaymath}

 \end{document}

需要说明的两点：

-  默认生成的结果中是有页码的，页码的存在会影响PS文件的Bounding Box，\thispagestyle{empty}设置当前页面不显示页码。
-  displaymath环境得到的是无编号的公式。而equation环境得到的是有编号的公式，也会影响PS文件的Bounding Box，所以不要使用。
-  公式环境还有其他表示方法，具体参见LaTeX语法；

编译LaTeX源码，并处理输出文件
====================================

上面的LaTeX代码保存在文件equation.tex中。

.. code-block:: bash

 $ latex equation.tex
 $ dvips equation.dvi
 $ ps2eps equation.ps -f -l

简单解释一下：

-  latex将tex文件编译成dvi文件；
-  dvips将dvi文件转换为ps文件；
-  ps2eps将ps文件转换为eps文件；

关于ps2eps的一些介绍：

-  -f表示若已存在同名eps文件，则强制覆盖；
-  在将ps文件转换为eps文件时，会根据ps文件中的Bounding Box信息对PS文件进行切边，但是默认的切边方式切得有点过了， ``-l`` 会在四个方向上各扩展1个点的距离，切边效果更好。
-  ``--resolution=dpi`` 可以设置PS文件的精度；默认效果应该足够了；
-  如果有其他需求，可以参考ps2eps的官方说明： http://www.tm.uka.de/~bless/ps2eps

也可以不使用ps2eps，而直接使用convert命令，convert默认的切边效果非常好，但是默认精度比较低，需要自己调高。

GMT与LaTeX的合并
========================

代码如下：

.. code-block:: bash

 #!/bin/bash
 pstext -JX15c -R0/10/0/10 -B2/2:."Equation of motion": -K > a.ps <<EOF
 5 6 15 0 0 CM Equation Start.
 EOF

 psimage equation.eps -W5c -C8/7/CM -K -O >> a.ps
 psimage equation.eps -W8c -C8/5/CM -K -O >> a.ps

 pstext -J -R -O >> a.ps <<EOF
 5 2 15 0 0 CM Equation End
 EOF

其实本质上就是利用psimage命令将EPS文件嵌入到当前PS文件中。这里写了两个psimage命令，以展示psimage对图形的自由伸缩。需要注意的是-C后面给定的是长度单位，与pstext中的坐标点的意义是不同的。

GMT和LaTeX虽然都使用PS代码（EPS算是特殊的PS），但是二者的一些结构和定义不同（最明显的区别是一个是PS-Adobe-2.0，一个是PS-Adobe-3.0），因而上面生成的ps文件不能用ps2raster来转换（撒了个小谎，实际上可以转换为eps文件，其他格式都会报错）。

这是个小问题，毕竟还有万能的convert命令（点\ `这里 <{filename}/GMT/2013-09-27_convert-and-ps2raster.rst>`_\ ），转换命令如下::

 $ convert -trim -density 300 -rotate 90 a.ps a.jpg

效果如下：

.. figure:: /images/2013102401.jpg
   :align: center
   :alt: latex-in-gmt
   :width: 600 px

其他一些需要说明的地方
======================

#. 从本质上来说，这个技巧利用了psimage命令，直接将EPS文件的代码嵌入到新的PS文件中，因而基本上只要是EPS文件都可以这么做。利用这一点可以做很多事情，比如GMT的箭头比较难看，可以用LaTeX的TikZ包来生成好看的箭头，然后再导入进去。
#. 用latex将tex编译成dvi，再转换为ps文件是一种比较老的latex编译方式；也是这里推荐的编译方式。

#. 现在更流行的是编译方式是直接用pdflatex或者xelatex生成pdf文件。但是这里需要eps文件，所以需要调用pdf2ps转换为ps再转换为eps，pdflatex生成的pdf效果很好，但是再生成ps文件清晰度会降低很多。因而最好还是用比较古老的编译方式吧。

#. 这个方法或许也可以用来在GMT上写中文。目前对中文支持最好的应该是xelatex了，其好像只能生成pdf，转换为ps后精度必然不够。一个解决办法是写足够大的字，转换之后用psimage缩小到需要的尺寸，这样或许精度上看上去效果更好。另一个办法是查一查pdf到ps转换有没有高精度的实现方法。不过GMT的中文问题还是用\ `Linux下的GMT中文显示 <{filename}/GMT/2013-08-13_gmt-chinese-under-linux.rst>`_\ 的方法更好。

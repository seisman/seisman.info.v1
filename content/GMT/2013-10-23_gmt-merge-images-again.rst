GMT技巧之图像合并2
###################

:date: 2013-10-23 09:12
:author: SeisMan
:category: GMT
:tags: GMT技巧, 图像
:slug: gmt-merge-images-again

在之前的博文《\ `GMT技巧之图像合并 <{filename}/GMT/2013-09-14_gmt-merge-images.rst>`_\ 》中说到了为什么需要图像合并以及图像合并的几种实现方法。

先说说前面的两个半方法的缺点：

-  解决办法1：为了将每个子图缩小到合适的尺寸，需要调节-J的尺寸以及其他很多细节参数（比如字体大小以及一些位置）。
-  解决办法2：通过修改纸张大小，然后将每个子图放在纸张合适的位置。这个方法的前提是每个子图的相对尺寸是合适的。
-  解决办法2升级版：同解决方法2，要求子图的相对大小合适。

先看看脚本fig1.sh：

.. code-block:: bash

 psxy -JX10c -R0/10/0/10 -B2/2 -Sc -K > a.ps << EOF
 5 5 5
 EOF
 pstext -J -R -O >> a.ps << EOF
 5 2 20 0 0 CM Outside
 5 3 20 0 0 CM Inside
 EOF

再看看脚本fig2.sh

.. code-block:: bash

 psxy -JX5c -R0/10/0/10 -B2/2 -St -K > b.ps << EOF
 5 5 5
 EOF
 pstext -J -R -O >> b.ps << EOF
 5 2 20 0 0 CM Outside
 5 3 20 0 0 CM Inside
 EOF

两个代码都很简单，一个画圆一个画三角形，然后写了"Outside"和"Inside"两个字符串。注意两张图的尺寸是不同的（-JX10c和-JX5c）。

现在要求把两张图合并到一张图中。

根据原来博文的思想，先将上面两个脚本fig1.sh和fig2.sh合并成一个脚本fig3.sh，合并过程中需要注意修改PS文件名，注意-K、-O，注意>和>>的区别，内容如下：

.. code-block:: bash

 psxy -JX10c -R0/10/0/10 -B2/2 -Sc -K > c.ps << EOF
 5 5 5
 EOF
 pstext -J -R -K -O >> c.ps << EOF
 5 2 20 0 0 CM Outside
 5 3 20 0 0 CM Inside
 EOF

 psxy -JX5c -R0/10/0/10 -B2/2 -St -K -O -X12c >> c.ps << EOF
 5 5 5
 EOF
 pstext -J -R -O >> c.ps << EOF
 5 2 20 0 0 CM Outside
 5 3 20 0 0 CM Inside
 EOF

绘图结果如下：

.. figure:: /images/2013102301.jpg
   :width: 600px
   :alt: fig

左图和右图大小不一样，这图交给老板，肯定要被老板训一顿了。

试着将左边的图修改小一点，修改之后fig4.sh，内容如下：

.. code-block:: bash

 psxy -JX5c -R0/10/0/10 -B2/2 -Sc -K > c.ps << EOF
 5 5 5
 EOF
 pstext -J -R -K -O >> c.ps << EOF
 5 2 20 0 0 CM Outside
 5 3 20 0 0 CM Inside
 EOF

 psxy -JX5c -R0/10/0/10 -B2/2 -St -K -O -X12c >> c.ps << EOF
 5 5 5
 EOF
 pstext -J -R -O >> c.ps << EOF
 5 2 20 0 0 CM Outside
 5 3 20 0 0 CM Inside
 EOF

绘图如下：

.. figure:: /images/2013102302.jpg
   :width: 600px
   :alt: fig

这下左图和右图大小一致了，但是左图已经完全变形了，又是被老板训的节奏。

根据解法1的思路，下面就是要重新调节左图的一些细节，这与重新画图基本没啥区别了。

这个时候就想，GMT要是能够实现图形的整体缩放就好了。恰好psimage可以实现这个功能。

这里直接利用最初的两个代码fig1.sh和fig2.sh:

.. code-block:: bash

 # 执行前两个脚本
 sh fig1.sh
 sh fig2.sh

 # 将生成的a.ps和b.ps转换成EPS文件
 ps2raster -A -P -Te a.ps
 ps2raster -A -P -Te b.ps

 # 利用psimage进行缩放
 psimage a.eps -W5c -K > fig.ps
 psimage b.eps -W5.3c -C6/0/BL -O >> fig.ps

效果图：

.. figure:: /images/2013102303.jpg
   :width: 600px
   :alt: fig

这个脚本在没有对原脚本进行修改的前提下，实现了图形的缩放，虽然最终效果上还是有些不足，主要表现在注释等字体的大小上。因而还需要进行一些微调。

**备注**

前段时间了解了一下TikZ的绘图功能，其自由的可缩放性让我觉得得心应手，当时就想，GMT为什么不支持缩放呢？

其实是支持的，只是一直被我忽略了。GMT的.gmtdefaults4文件中有两个参数，GLOBAL\_X\_SCALE和GLOBAL\_Y\_SCALE，可以用来控制图形的缩放。但是这两个参数与-P选项类似，在执行第一个绘图命令时就将PS代码写入了PS文件中了。之后无论怎样修改这两个参数都是没有用的。即GLOBAL\_X\_SCALE和GLOBAL\_Y\_SCALE只能修改整个图形相对纸张的比例，而不能修改图形的某个部分相对于整个图形的比例。这应该算是GMT将不同功能分布在多个命令中的弊端之一吧。

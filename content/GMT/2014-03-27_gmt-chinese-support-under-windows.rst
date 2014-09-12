GMT在Windows下的中文支持
########################

:author: SeisMan
:date: 2014-03-27 16:45
:modified: 2014-04-03
:category: GMT
:tags: GMT技巧, 中文, Windows
:slug: gmt-chinese-support-under-windows
:summary: GMT在Windows下中文支持需要注意的问题。

.. contents::

GMT在Windows下如何支持中文的问题在这个\ `博客`_\ 里已经说的差不多了，这里只是做一个归纳和补充。

中文支持
========

归纳如下，具体看上面的博文：

#. 安装Windows版GMT；
#. 安装ghostscript，需要注意的是在安装的最后步骤，会有生成cidmap的选项，默认该选项是被选中的，一定不要将该选项取消；
#. 在\ ``C:\Program Files\gs\gs9.14\examples\cjk``\ 下找到gscjk_ag.ps，用\ ``C:Program Files\gs\gs9.14\bin\gswin32c``\ 打开，若可正常显示中文则表示ghostscript已经支持中文；
#. 用编辑器打开gscjk_ag.ps，如博文中所说找到相应中文字体，例如\ ``STSong-Light--GB-EUC-H``\ ，其中H表示水平字体，V表示垂直向字体；
#. 将找到的字体添加到GMT字体列表中，GMT4的话该文件是\ ``GMT4\share\pslib\PS_font_info.d``\ ，GMT5下建议将自定义字体放在文件\ ``GMT5\share\pslib\CUSTOM_font_info.d``\ 中。 
#. \ ``pstext -L``\ 检查GMT字体；
#. 绘图查看中文字体是否正常。

需要注意的是，gsview与ghostscript没有太多的关系，GMT利用ghostscript进行ps文件的转换和查看，而gsview则只是另一个可选的查看工具而已。

理论上，完成上面的步骤之后，用ghostscript就可以正常显示GMT的中文PS了，若使用gsview查看，则会乱码，此时需要在gsview的“选项”->“高级配置”中将路径\ ``C:\Windows\Fonts``\ 加入到gsview的路径中，此时方可使用gsview正常查看。

测试脚本
========
本代码为GMT5语法！

GMT4语法的测试脚本位于 http://seisman.info/gmt-chinese-under-linux.html

.. code-block:: bash

 gmt gmtset FONT_TITLE 40p,39,black

 echo 3.5 5 0 LM 45p,39,red  GMT宋体 > tmp
 echo 3.5 4 0 LM 45p,40,blue GMT楷体 >> tmp

 gmt pstext tmp -R0/7/0/7 -JX6i/6i -Bafg -B+t"GMT中文" -F+a+c+f -P > cn.ps

图片格式转换
============

使用GMT自带的ps2raster命令可以将PS文件转换为其它图片格式。

在Windows下，对于含中文的PS文件，需要在ps2raster上加上字体路径，如下:

.. code-block:: bash

   ps2raster -C-sFONTPATH=C:\Windows\Fonts test.ps

即可正常使用。

另，GMT 5.1.1存在bug，上面的命令无法与-A选项一起使用，GMT 4可以。

.. _博客: http://xxqhome.blog.163.com/blog/static/1967330202011112810120598/

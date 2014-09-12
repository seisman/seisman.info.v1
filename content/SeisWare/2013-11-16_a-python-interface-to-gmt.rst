GMT的Python接口：GmtPy
#######################

:date: 2013-11-16 01:23
:author: SeisMan
:category: GMT
:tags: 模块, Python
:slug: a-python-interface-to-gmt

GmtPy是GitHub上的一个开源项目，其将GMT绘图功能无缝集成到Python语言中。除了GMT的功能之外，其还支持自动缩放、自动决定tick增量、整体布局管理等。

项目主页： http://emolch.github.io/gmtpy/

版本：V0.1

依赖：Python（猜测是2）、GMT（4.5以上？）、NumPy、pycdf

Manual: http://emolch.github.io/gmtpy/documentation.html#module-gmtpy

一些例子
========

看看下面一些例子，看看GmtPy的优点在哪里。

基本用法
--------

Bash：

.. code-block:: bash

 #!/bin/bash
 gmtset BASEMAP_TYPE = fancy \
        PAPER_MEDIA = a4+ \
        PAGE_ORIENTATION = portrait
 
 pscoast -R5/15/52/58 \
         -JB10/55/55/60/10c \
         -B4g4 \
         -Df \
         -S114/159/207 \
         -G233/185/110 \
         -Wthinnest > example1.eps
 
 epstopdf --outfile=example1.pdf example1.eps

GmtPy:

.. code-block:: python

 from gmtpy import GMT
 
 gmt = GMT( config={'BASEMAP_TYPE':'fancy'} )
 
 gmt.pscoast( R='5/15/52/58',
              J='B10/55/55/60/10c',
              B='4g4',
              D='f',
              S=(114,159,207),
              G=(233,185,110),
              W='thinnest' )
 
 gmt.save('example1.pdf')
 gmt.save('example1.eps')

|image0|

最大的特色在于不用像GMT那样每个绘图命令里都要将输出重定向到PS文件中。GmtPy直接使用save控制输出的文件类型，不知道是否支持其他图片格式。

GmtPy的可能机制的猜测：

GmtPy中没有-K、-O，完全无法预测哪一个命令是最后一个绘图命令，因而只能创建临时文件夹，将所有的输出重定向到临时PS文件。上面的脚本中使用GMT()创建了一个名为gmt的对象，每个对象对应一个临时文件，当遇到gmt.save命令时，即认为绘图结束，save命令向临时PS文件中加入Trailer信息，并重命名。save也许会进行格式转换工作。

从Python向GMT传递数据
---------------------

.. code-block:: python 

 from gmtpy import GMT
  
 gmt = GMT( config={'PAGE_COLOR':'247/247/240'} )
 gmt.psbasemap( R=(0,5,0,5),
                J='X%gi/%gi' % (5,3),
                B='%g:Time:/%g:Amplitude:SWne' % (1,1) )
  
  
 # Make four different datasets
  
 # (1) a nested list, with the first dim corresponding to columns
 data_as_columns = [ [ 0,1,2,3,4,5 ], [0,1,0.5,1,0.5,1] ]
  
 # (2) a nested list, with the first dim corresponding to rows
 data_as_rows = [ [0,1], [1,2], [2,3], [3,3.5], [4,3], [5,2] ]
  
 # (3) a string containing an ascii table
 data_as_string = '''0 5
 1 4
 2 3.5
 3 4
 4 4.5
 5 5'''
  
  
 # (4) write ascii table in a temporary file...
  
 # Get a filename in the private tempdir of the GMT instance.
 # Files in that directory get deleted automatically.
 filename = gmt.tempfilename('table.txt')
  
 f = open(filename,'w')
 f.write('0 3\n1 3\n5 1.2\n')
 f.close()
  
  
 # Plot the four datasets
 #
 # The kind of input is selected with the keyword arguments beginning
 # with 'in_'.
 #
 # Specifying R=True and J=True results '-R' and '-J' being passed
 # to the GMT program without any arguments. (Doing so causes GMT to
 # repeat the previous values.)
  
 gmt.psxy( R=True, J=True, W='1p,black', in_columns=data_as_columns )
 gmt.psxy( R=True, J=True, W='1p,red',   in_rows=data_as_rows )
 gmt.psxy( R=True, J=True, W='1p,blue',  in_string=data_as_string )
 gmt.psxy( R=True, J=True, W='1p,purple,a', in_filename=filename )
  
 gmt.save('example2.pdf')

|image1|

这个例子展示了Python向GMT传递数据的四种方式：in\_columns、in\_rows、in\_string、in\_filename。

默认布局
--------

.. code-block:: python

 from gmtpy import GMT, cm
 import numpy as np
 
 x = np.linspace(0,5,101)
 y = np.sin(x) + 2.5
 
 gmt = GMT( config={'PAGE_COLOR':'247/247/240'} )
 
 layout = gmt.default_layout()
 plot_widget = layout.get_widget('center')
 plot_widget.set_horizontal( 8*cm )
 layout.get_widget('top').set_vertical( 1*cm )
 
 gmt.psbasemap( R=(0,5,0,5),
                B='%g:Time [ s ]:/%g:Amplitude [ m ]:SWne' % (1,1),
                *plot_widget.XYJ())
 
 gmt.psxy( R=True,
           W='2p,blue,o',
           in_columns=(x,y),
           *plot_widget.XYJ() )
 
 gmt.save('example3.pdf', bbox=layout.bbox())


|image2|

自动计算图相对纸张的位置。

自定义布局
----------

.. code-block:: python

 from gmtpy import GMT, cm, GridLayout, FrameLayout, golden_ratio
 import numpy as np
  
 # some data to plot...
 x = np.linspace(0,5,101)
 ys = (np.sin(x) + 2.5,  np.cos(x) + 2.5)
  
 gmt = GMT( config={'PAGE_COLOR':'247/247/240'} )
  
 layout = GridLayout(1,2)
  
 widgets = []
 for iwidget in range(2):
     inner_layout = FrameLayout()
     layout.set_widget(0, iwidget, inner_layout)
     widget = inner_layout.get_widget('center')
     widget.set_horizontal( 7*cm )
     widget.set_vertical( 7*cm/golden_ratio )
     widgets.append( widget )
  
 # gmt.draw_layout( layout )
 # print layout
  
 for widget, y in zip(widgets, ys):
     gmt.psbasemap( R=(0,5,0,5),
                 B='%g:Time [ s ]:/%g:Amplitude [ m ]:SWne' % (1,1),
                 *widget.XYJ())
  
     gmt.psxy( R=True,
             W='2p,blue,o',
             in_columns=(x,y),
             *widget.XYJ() )
  
 gmt.save('example4.pdf', bbox=layout.bbox())

|image3|

.. |image0| image:: http://emolch.github.io/gmtpy/_images/example1.png
.. |image1| image:: http://emolch.github.io/gmtpy/_images/example2.png
.. |image2| image:: http://emolch.github.io/gmtpy/_images/example3.png
.. |image3| image:: http://emolch.github.io/gmtpy/_images/example4.png

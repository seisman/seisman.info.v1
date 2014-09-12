sphinx生成PDF的中文支持问题 
###########################

:author: SeisMan
:date: 2014-03-01 10:50
:category: 编程
:tags: sphinx, 中文, Python
:slug: chinese-support-for-sphinx

.. contents::

sphinx可以利用LaTeX将rST源文件转换成PDF文件，官方的模板是无法支持中文的，因而必须要对其进行修改。

修改Makefile
============

当执行\ ``make latexpdf``\ 时，会首先执行\ ``sphinx-build``\ 生成tex源文件，然后调用\ ``_build/latex``\ 目录下的makefile文件，利用pdflatex引擎将tex文件转换为PDF。

``build/latex``\ 下的Makefile文件是\ ``sphinx/texinputs/Makefile``\ 的直接拷贝。因而需要修改\ ``sphinx/texinputs/Makefile``\ ，将其中的pdflatex修改成xelatex。


修改conf.py
===========

修改完Makefile之后，直接make latexpdf之后不会报错，但是中文部分完全没有显示，这是因为缺乏中文所需要的字体设置。

修改conf.py中的latex_elements参数，如下:

.. code-block:: python

   latex_elements = { 
   # The paper size ('letterpaper' or 'a4paper').
   #'papersize': 'letterpaper',
   
   # The font size ('10pt', '11pt' or '12pt').
   #'pointsize': '10pt',
   # Additional stuff for the LaTeX preamble.
   'preamble': r'''
        \usepackage{xeCJK}
        \setCJKmainfont{SimSun}
        \XeTeXlinebreaklocale "zh"
        \XeTeXlinebreakskip = 0pt plus 1pt
   ''',
   }

修改latex.py
============

加入了xeCJK相关设置之后编译还是会出现问题::

    ! Undefined control sequence.
    \GenericError  ...            
                #4  \errhelp \@err@     ...
    l.2856   }

这是由于xeCJK包与inputenc包发生冲突导致的，因而也需要修改。

首先在\ ``conf.py``\ 中设置\ ``language=zh_CN``\ ,然后修改\ ``sphinx/writers/latex.py``\ ，在231行左右加入语句对中文做特殊处理：

.. code-block:: python

    if builder.config.language == 'zh_CN':
        self.elements['babel'] = ''
        self.elements['inputenc'] = ''
        self.elements['utf8extra'] = ''

第一个语句禁用了babel包，因而其尚不支持中文；第一个语句禁用了inputenc包，其与xeCJK冲突；第三个语句禁用了一个语句，该语句调用了inputenc包中的命令。

理论上完全可以通过修改conf.py中的latex_elements来禁用各种宏包的。但是实际上sphinx并没有提供禁用utf8extra的参数，即便禁用了inputenc依然是有问题的。

修改了这些之后，中文应该就没有问题了。在make latexpdf之前注意先make clean就好。

与TeX相关的一些名词
###################

:date: 2013-08-15 17:29
:author: SeisMan
:category: 编程
:tags: 名词解释, LaTeX
:slug: terms-about-tex

.. contents::

前言
====

在接触TeX两年之后，依然对于TeX的一些术语之间的关系表示不解。比如LaTeX、pdfLaTeX、XeLaTeX、TeX Live、CTeX等等。这些术语究竟代表什么？它们之间是怎样的关系？

TeX
===

TeX首先是一种宏语言，同时其也是一种排版引擎。基本的TeX系统只有300多个元命令 (primitive) ，十分精悍，但是很难读懂。

引擎
====

引擎是真正干活的程序。引擎的基本功能就是解释TeX语法，把字排成行，把行排成页，涉及到断字、断行、分页等算法。最原始的引擎是TeX。

-  TeX：1978年由Donald Erwin Knuth开发。是后来大部分TeX相关的基础。其生成dvi文件，然后经由其他程序转换为pdf文件。
-  pdfTeX：Tex语言的又一个实现，将TeX代码直接编译成PDF文件。
-  XeTeX：TeX 语言的新的实现，支持 Unicode 编码和直接访问操作系统字体。
-  LuaTeX：TeX 语言的一个完整的有扩展的实现。LuaTeX支持Unicode、系统字体和内嵌语言扩展，能直接输出PDF格式文件，也可以仍然输出 DVI 格式。

格式
====

TeX语言本身只有300个命令，晦涩难懂，只适合非正常的人类。一个简单的符号可能就需要多个命令来实现，可以将这些最基本的命令封装起来做个简写（宏）以实现特殊的目的。一堆简写的合集就构成了格式。格式可以与不同的引擎相结合。

-  Plain TeX：由Don Knuth提供的最小的宏集合。
-  LaTeX：更易于使用的宏集，最常见的一种格式。
-  ConTeXt：另一种常见的格式。

宏包
====

一些辅助文件，在LaTeX中叫做packages，在ConTeXt中叫做modules。在LaTeX格式中，导言区的\\usepackage的作用就是引入各种宏包。宏包其实也是一堆基本的TeX命令的集合，只是其不够全，所以称之为宏包而不是格式。

发行版
======

一个完整的TeX需要最基本的TeX引擎、格式支持、各种辅助宏包、一些转换程序、GUI、编辑器、文档查看器等等。通过选择不同的组合就构成了不同的发行版。

-  TeX Live：支持Linux，Windows，Mac OS
-  MiKTeX：只支持Windows
-  CTeX：CTeX基于MiKTeX，并加入了中文的支持，只支持Windows。同时CTEX是一个网站，ctex是可以很好支持中文的宏包。

其他相关
========

-  METAFONT：TeX中用来生成字体的程序。
-  MetaPost：用于生成图像。
-  BibTeX：用于生成参考文献。
-  dvipdf：dvi转换成pdf。

相关命令
========

在介绍了引擎以及格式之后，二者不同的搭配方式需要调用不同的命令：

.. figure:: /images/2013081501.jpg
   :width: 600px
   :alt: latex things

小结
====

目前最常用的引擎是pdfTeX和XeTeX，其中XeTeX可以很好的支持中文，因而受到国人的青睐。格式方面LaTeX当仁不让。所以目前比较流行的编译命令是xelatex，同时在中文支持方面，几年前是CJK宏包，现在是ctex宏包。

参考文章
========

-  http://blog.163.com/goldman2000@126/blog/static/1672968952012112645041621/
-  https://github.com/alt/tex-overview

附录
====

附上该表的代码：

.. code-block:: latex

 \documentclass[UTF8]{ctexart}
 \usepackage{booktabs}
 \usepackage{xltxtra}
 \begin{document}
 
 \begin{table}[h]
 \caption{\TeX相关命令比较}
 \centering
 \begin{tabular}{llll}
 \toprule
 命令 & 引擎 & 格式 & 输出 \\
 \midrule
 tex & \TeX & plain\TeX & DVI \\
 dviluatex & Lua\TeX & plain\TeX & DVI \\
 etex & PDF\TeX & plain\TeX & DVI \\
 luatex & Lua\TeX & plain\TeX & PDF \\
 pdftex & PDF\TeX & plain\TeX & PDF \\
 xetex & \XeTeX & plain\TeX & DVI \\
 \midrule
 latex & PDF\TeX & \LaTeX2e & DVI \\
 dvilualatex & Lua\TeX & \LaTeX2e & DVI \\
 lualatex & Lua\TeX & \LaTeX2e & PDF \\
 pdflatex & PDF\TeX & \LaTeX2e & PDF \\
 xelatex & \XeTeX & \LaTeX2e & PDF \\
 \bottomrule
 \end{tabular}
 \end{table}
 
 \end{document}

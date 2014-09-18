Linux下合并多个PDF
##################

:author: SeisMan
:date: 2014-09-18
:category: Linux
:tags: PDF, Linux
:slug: merge-multiple-pdfs

.. contents::

经常需要将多个PDF合并为一个文件，这里收集了网上给出的一些方案，并总结一下。

pdfunite
========

``pdfunite``\ 是\ `Poppler <http://poppler.freedesktop.org>`_\ 提供的一个工具，一般系统都已经安装了Poppler，所以这个工具在Linux下是很常见的。

::

    pdfunite input1.pdf input2.pdf input3.pdf output.pdf

该命令用法简单，没有多余的选项，需要注意的是该命令的最后一个PDF文件为输出文件名。

pdfjam
======

如果你安装了TeXLive，并且安装了\ `pdfpage <http://www.ctan.org/tex-archive/macros/latex/contrib/pdfpages/>`_\ 包，则其中包含了\ ``pdfjam``\ 工具。

::

    pdfjam input1.pdf input2.pdf input3.pdf -o output.pdf

该命令的选项很多，可以通过\ ``pdfjam --help``\ 查看。

``pdfjoin``\ 是\ ``pdfjam``\ 的一个封装，也可以直接使用::

    pdfjoin a.pdf b.pdf

pdftk
=====

`pdftk <https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/>`_\ 是专门用于处理PDF文档的一套工具。在大多数发行版中都可以直接安装使用。

::

    pdftk input1.pdf input2.pdf input3.pdf cat output output.pdf

pdftk的选项很多，用法复杂，可以参考\ `PDF合并和分割工具—PDFtk <{filename}/Linux/2013-10-31_introduction-to-pdftk.rst>`_ 。

gs
==

`GhostScript <http://www.ghostscript.com>`_\ 不仅可以用于处理PS，也可以用于处理PDF文档。

::

    gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=out.pdf in1.pdf in2.pdf

::

    gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -sOutputFile=out.pdf in1.pdf in2.pdf


参考
====

- https://blog.dbrgn.ch/2013/8/14/merge-multiple-pdfs/
- http://stackoverflow.com/questions/2507766/merge-convert-multiple-pdf-files-into-one-pdf

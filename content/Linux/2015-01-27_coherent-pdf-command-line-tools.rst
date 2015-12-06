强大的跨平台PDF处理工具：cpdf
#############################

:author: SeisMan
:date: 2015-01-27
:category: Linux
:tags: PDF, Linux, Windows
:slug: coherent-pdf-command-line-tools

日常生活中对PDF的最基本的操作大概就是合并和切割了。之前一直在用强大的PDFtk，但是由于一些底层依赖的问题，PDFtk在短时间内是不可能出现在CentOS7下了，只能寻找新的PDF替代工具了。

简介
====

Coherent PDF，简称cpdf，是个用于处理PDF的命令行工具。该软件支持Windows、Linux和Mac，且对于非商业用途是免费的。

主页：http://community.coherentpdf.com/

Linux的安装
===========

下载地址：https://github.com/coherentgraphics/cpdf-binaries/archive/master.zip

cpdf有预编译的二进制文件，直接下载解压，然后把自己的平台对应的二进制文件复制到PATH中即可使用。

常见用法
========

PDF合并::

    cpdf input1.pdf input2.pdf -o output.pdf

切割PDF中的1至3页以及12页至最后页::

    cpdf input.pdf 1-3,12-end -o output.pdf

将PDF分割成单页PDF，编号为 ``page001.pdf`` 、 ``page002.pdf`` ::

    cpdf -split in.pdf -o page%%%.pdf

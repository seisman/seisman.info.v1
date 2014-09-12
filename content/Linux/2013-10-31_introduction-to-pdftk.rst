PDF合并和分割工具--PDFtk
#########################

:date: 2013-10-31 00:24
:author: SeisMan
:category: Linux
:tags: 用法, PDF
:slug: introduction-to-pdftk

.. contents::

简介
====

PDFtk是什么？我觉得官网的一句话解释得很好。

    If PDF is electronic paper, then PDFtk is an electronic
    staple-remover, hole-punch, binder, secret-decoder-ring, and
    X-Ray-glasses. PDFtk is a simple tool for doing everyday things with
    PDF documents.

其官方网站为： http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit

PDFtk目前分为三个版本：

-  PDFtk Server：命令行工具。支持windows、Linux、Mac。
-  PDFtk Free：图形界面基础免费版；仅限windows用户；功能仅限于PDF合并和分割；
-  PDFtk Pro：图形界面专业收费版；仅限windows用户，可以对PDF文档进行合并、分割、旋转、加水印、加邮戳、加密。

对于Linux用户，唯一的选择是免费的PDFtk Server，其功能与收费PDFtk Pro完全相同，只是没有GUI而已。作者还是很厚道的。

Linux的各个发行版的官方源中基本都有该软件，直接apt-get或者yum安装即可。

功能
====

-  合并PDF；
-  分割PDF页面；
-  旋转PDF文档或页面；
-  PDF解密；（不是破解）
-  PDF加密；
-  用X/FDF填写PDF表格；
-  从PDF表格中生成PDF Data Stencils；
-  加背景水印或前景印章；
-  报告PDF Metrics，书签和元数据；
-  增加/更新PDF书签或元数据；
-  给PDF页面或文档加附件；
-  解压PDF附件；
-  分解PDF文档为多个单页；
-  解压缩和重压缩页面流；
-  修复受损的PDF文档；

这功能完全可以与Adobe Acrobat相媲美了，更重要的是PDFtk支持Linux且完全免费。（个人用户免费，若用于商业用途需付费）。

用法示例
========

具体选项看这里： http://www.pdflabs.com/docs/pdftk-man-page/

下面给出一些常见的例子。例子原文在： http://www.pdflabs.com/docs/pdftk-cli-examples/

扫描一本书，odd.pdf为书的全部奇数页，even.pdf为书的全部偶数页，下面的命令可以将两个pdf合并成页码正常的书::

    pdftk A=odd.pdf B=even.pdf shuffle A B output collated.pdf

如果odd.pdf是逆序的::

    pdftk A=odd.pdf B=even.pdf shuffle Aend-1 B output collated.pdf

加密PDF::

    pdftk secured.pdf input_pw foopass output unsecured.pdf

PDF 128位加密，保留全部权限::

    pdftk 1.pdf output 1.128.pdf owner_pw foopass

PDF 128位加密，保留全部权限，打开文档需输入密码"baz"::

    pdftk 1.pdf output 1.128.pdf owner_pw foo user_pw baz

PDF 128位加密，打开文档需输入密码"baz"，保留打印之外的其他权限::

    pdftk 1.pdf output 1.128.pdf owner_pw foo user_pw baz allow printing

合并in1.pdf和in2.pdf到新PDF中::

    pdftk in1.pdf in2.pdf cat output out1.pdf

或（使用句柄）::

    pdftk A=in1.pdf B=in2.pdf cat A B output out1.pdf

或（使用通配符）::

    pdftk *.pdf cat output combined.pdf

去除in1.pdf中的第13页，并创建out1.pdf::

    pdftk in.pdf cat 1-12 14-end output out1.pdf

或

::

    pdftk A=in1.pdf cat A1-12 A14-end output out1.pdf

对输出进行40位加密，撤销所有权限，设置owner密码为foopass::

    pdftk 1.pdf 2.pdf cat output 3.pdf encrypt_40bit owner_pw foopass

合并两个文件，其中一个需要被加密。对输出不加密::

    pdftk A=secured.pdf 2.pdf input\_pw A=foopass cat output 3.pdf

解压PDF页面流，然后就可以在文本编辑器中编辑PDF文件::

    pdftk doc.pdf output doc.unc.pdf uncompress

压缩PDF::

    pdftk mydoc.pdf output mydoc.clear.pdf compress

修复破损的PDF::

    pdftk broken.pdf output fixed.pdf

将一个PDF文档分割成一页一个文档::

    pdftk in.pdf burst

将一个PDF文档分割成一页一个文档，并加密，允许低质量的打印::

    pdftk in.pdf burst owner_pw foopass allow DegradedPrinting

获取PDF问的元数据和书签信息::

    pdftk in.pdf dump_data output report.txt

将PDF第一页顺时针旋转90度::

    pdftk in.pdf cat 1east 2-end output out.pdf

将整个PDF文档旋转180度::

    pdftk in.pdf cat 1-endsouth output out.pdf

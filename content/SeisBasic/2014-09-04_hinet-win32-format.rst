Hi-net WIN32 格式
#################

:date: 2014-09-04 00:01
:author: SeisMan
:category: 地震学基础
:tags: Hinet, 格式, 数据
:slug: hinet-win32-format

对于连续波形数据而言，从Hi-net下载的文件为zip压缩文件，其中包含了多个后缀为\ ``cnt``\ 的文件。每个cnt文件中包含了多台站多分量的一分钟的波形数据。

这些cnt文件即为WIN32格式。WIN32格式是在WIN格式上修改得到的，而WIN格式是日本某机构自行设计的一种数据格式，主要用于一套称为”WIN System“的软件中。

WIN32格式官方文档: http://www.hinet.bosai.go.jp/REGS/manual/dlDialogue.php?r=win32format&LANG=en

WIN32格式是很线性的，如果需要的话很容易自己写程序实现win32格式数据的合并、转换的。Hi-net提供了win32tools，可以实现一些基本的功能。

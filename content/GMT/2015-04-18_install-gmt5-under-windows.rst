GMT 5.1.2在Windows下的安装
##########################

:date: 2015-04-18
:modified: 2015-06-02
:author: SeisMan
:category: GMT
:tags: GMT5, Windows, 安装
:slug: install-gmt5-under-windows

.. contents::

本文介绍如何在Windows 7下安装GMT5.1.2。

下载
====

Windows下安装GMT5.1.2需要下载三个文件：

#. `GMT 64位安装包 <http://gmt.soest.hawaii.edu/files/download?name=gmt-5.1.2-win64.exe>`_ 或 `GMT 32位安装包 <http://gmt.soest.hawaii.edu/files/download?name=gmt-5.1.2-win32.exe>`_

#. `ghostscript 64位安装包 <http://downloads.ghostscript.com/public/gs916w64.exe>`_ 或 `ghostscript 32位安装包 <http://downloads.ghostscript.com/public/gs916w32.exe>`_

#. `GSView 64位安装包 <http://pages.cs.wisc.edu/~ghost/gsview/download/gsv50w64.exe>`_ 或 `GSView 32位安装包 <http://pages.cs.wisc.edu/~ghost/gsview/download/gsv50w32.exe>`_


安装
====

安装GMT
-------

跟大多数Windows的程序一样，双击exe就好。几个需要注意的地方如下图：

GMT5安装文件会自动添加环境变量，如下图所示，三个可选项中选第一个或第二个就好。不要选第三个，除非你知道自己在做什么。

.. figure:: /images/2015041801.png
   :width: 600 px
   :align: center
   :alt: 添加环境变量

GMT5默认的安装目录是 ``c:\programs\gmt5`` ，使用此默认值就好，不建议修改此安装目录。

尝试安装在 ``c:\Program Files\gmt5`` 下，执行命令好像也没问题，但不确定目录名中的空格是否会在什么地方挖个坑。

.. figure:: /images/2015041802.png
   :width: 600 px
   :align: center
   :alt: 安装目录

选择组件那里，Runtime files是必须的，DCW是国界、省界数据，Documentation是官方文件以及官方示例，GSHHG是海岸线数据。所以四个都安装就好。

.. figure:: /images/2015041803.png
   :width: 600 px
   :align: center
   :alt: 选择组件

安装完成之后，启动cmd：“开始”->“所有程序”->“附件”->“命令提示符”，也可以直接在开始那里搜索“cmd”。在cmd窗口中键入 ``gmt`` ，效果如下则表明GMT安装成功。

.. figure:: /images/2015041804.png
   :width: 600 px
   :align: center
   :alt: 启动cmd

安装ghostscript
---------------

ghostscrip的安装没什么好说的，在安装的最后，第一个复选框一定要选上，这关系到GMT能否支持中文的问题。

.. figure:: /images/2015041805.png
   :width: 600 px
   :align: center
   :alt: ghostscript CJK

安装GSView
----------

GSView的安装没什么好说的，一直点下去用默认的选项就好。

测试
====

GMT自带了一些例子，可以把 ``C:\programs\gmt5\share\doc\examples`` 目录下的例子复制一份到自己的目录下。每个例子里包含了bat脚本，以及执行脚本所需的数据文件。

双击即可直接执行bat脚本，右键编辑即可查看bat脚本的内容。

双击生成的PS文件即可用GSView打开。

其他
====

安装完成后，你可以对如下几篇博文感兴趣：

#. `GMT4脚本风格指南 <{filename}/GMT/2014-05-13_gmt4-style-guide.rst>`_ ：虽然是针对GMT4的，但是对GMT5也有一定的指导意义
#. `Windows下使用GMT的正确姿势 <{filename}/GMT/2014-12-10_how-to-use-gmt-under-windows.rst>`_ ：教你如何在Windows下更愉快地使用GMT
#. `GMT在Windows下的中文支持 <{filename}/GMT/2014-03-27_gmt-chinese-support-under-windows.rst>`_ ：如何在GMT中添加中文

修订历史
========

- 2015-04-18：初稿；
- 2015-06-02：更新至5.1.2；

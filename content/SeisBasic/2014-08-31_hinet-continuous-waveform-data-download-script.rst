Hi-net连续波形数据下载脚本
##########################

:date: 2014-08-31 19:10
:author: SeisMan
:category: 地震学基础
:tags: Hinet, 数据, 下载, Python
:slug: hinet-continuous-waveform-data-download-script

用前文的脚本实现了数据申请之后，还需要及时地把数据下载下来。

下载地址：http://www.hinet.bosai.go.jp/REGS/download/cont/cont_status.php

最简单的办法是人工点击下载链接，但是这种方法相对来说太低效，因而还是考虑用脚本实现。

查看源码或查看网页请求，或者直接查看数据下载链接，可以知道，下载数据的实质是向Hi-net服务器发送如下请求::

  http://www.hinet.bosai.go.jp/REGS/download/cont/cont_download.php?id=0005134055&LANG=en

其中id为Status/Download页面第一列给出的10位整数。

因而，数据的下载分为如下几步：

#. 从Status/Download页面获取所有数据的ID列表；
#. 从ID列表中筛选出需要下载的数据的ID列表；
#. 依次向Hi-net服务器发送请求；

HinetContDownload.py
====================

Python版的数据下载脚本位于\ `HinetContDownload.py <https://github.com/seisman/HinetScripts/blob/master/HinetContDownload.py>`_\ 。

依赖
----

- Python 3.4 （未测试Python 2.7是否可行）
- docopt模块
- requests模块
- BeautifulSoup4模块

特性
----

该脚本用于下载连续波形数据，具有如下特性：

- 支持三种筛选方式：

  #. 全部可下载的数据
  #. 全部未下载的数据
  #. idfile中指定的数据

- 支持并行下载
- 不支持断点续传
- 不支持进度条

用法
----

.. code-block:: bash

	$ python HinetContDownload.py -h
	Download coutinuous waveform datas from Hi-net.

	Usage:
	    HinetContDownload.py (--all | --new | --ids=IDFILE) [--procs=N]
	    HinetContDownload.py -h

	Options:
	    -h --help     Show this help.
	    --all         Fetch ID list of all avaiable datas from Hinet Status page.
	    --new         Fecth ID list of undownloaded datas from Hinet Status page.
	    --ids=IDFILE  Read ID list from file (ONE ID PER LINE).
	    --procs=N     Maximum processes in parallel. [default: 10]

示例
----

下载全部可下载的数据::

    HinetContDownload.py --all

用6个进程并行下载全部未下载的数据::

    HinetContDownload.py --new --procs=6

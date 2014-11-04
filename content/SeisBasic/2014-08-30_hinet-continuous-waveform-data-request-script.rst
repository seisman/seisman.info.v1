Hinet连续波形数据申请及下载的脚本实现
#####################################

:date: 2014-08-30 22:22
:modified: 2014-11-04
:author: SeisMan
:category: 地震学基础
:tags: Hinet, 数据, 申请, Python
:slug: hinet-continuous-waveform-data-request-script

.. contents::

前文已经说到，Hi-net连续波形数据申请的本质可以简化为如下几步：

#. 指定参数，构建query string
#. 向Hi-net发送数据请求
#. 等待数据准备
#. 下载数据

这篇博文介绍了如何用Python实现以上步骤。为什么用Python呢？

    Life is short, you need Python.

Python实现数据申请示例
======================

下面\ **用尽可能少且简单**\ 的Python代码实现了Hi-net数据的申请。需要注意，此版本仅仅只是为了展示数据申请方法的原理，实际用起来并不方便也不智能！

该脚本需要安装Python的requests模块。

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import requests

    # 账户密码
    user = "xxxxxxx"
    passwd = "xxxxxxxxxxx"

    # 数据申请信息
    org = "01"
    net = "01"
    year = "2014"
    month = "08"
    day = "14"
    hour = "02"
    min = "25"
    span = "5"

    url = "http://www.hinet.bosai.go.jp/REGS/download/cont/cont_request.php"
    # 构建query string
    payload = {
        'org1':  org,
        'org2':  net,
        'year':  year,
        'month': month,
        'day':   day,
        'hour':  hour,
        'min':   min,
        'span':  span,
        'arc':   'ZIP',      # compressed format of the data
        'size':  '93680',    # estimated size of the data, it is not important
        'LANG':  'en',       # english version of web
        'rn':    '12345677'  # random value
    }

    # 向Hi-net发送请求
    requests.post(url, params=payload, auth=(user, passwd), timeout=5)

就是这么简单。

上面的版本用尽可能少的代码完成了数据的申请。一个优秀的脚本，还应该做更多的细节：

- 支持更多的机构和台站，并对机构和台站代码进行判断
- 判断日期是否合法
- 判断日期是否在允许的范围区间内
- 月、日、时、分、秒的格式为\ ``%02d``\ ，即month=02而不是month=2
- 数据长度的格式为\ ``%d``\ ，即span=5而不是span=05

数据下载
========

申请完数据之后，还需要及时将数据下载下来。最简单的办法是人工点击下载链接，但是这种方法相对来说太低效，因而还是考虑用脚本实现。

查看下载页面的源码或直接查看数据的下载链接，可以知道，下载数据的实质是向Hi-net服务器发送如下请求::

  http://www.hinet.bosai.go.jp/REGS/download/cont/cont_download.php?id=0005134055&LANG=en

其中id为Status/Download页面第一列给出的10位整数。

因而写脚本自动下载的关键步骤如下：

#. 获取Status/Download的网页源码；
#. 对源码进行解析，得出要下载的数据所对应的ID；
#. 构建query-string，向服务器发送数据下载请求；

用Python实现的话，可以使用模块\ ``requests``\ 和\ ``BeautifulSoup4``\ 。这里就不再多说了。

HinetContRequest.py
===================

`HinetContRequest.py <https://github.com/seisman/HinetScripts/blob/master/HinetContRequest.py>`_\ 是用Python实现的用于申请与下载Hi-net连续波形数据的脚本。

配置文件
--------

要执行HinetContRequest.py，需要先修改配置文件\ `Hinet.cfg <https://github.com/seisman/HinetScripts/blob/master/Hinet.cfg>`_\ ，其内容如下::

    [Account]
    User = xxxxxx
    Password = xxxxxxxx

    [Cont]
    Net = 0101
    MaxSpan = 5

    [Tools]
    catwin32 = catwin32

其中：

- ``User``\ 和\ ``Password``\ 为Hi-net网站的用户名和密码；
- 由于不同台网的数据不能一起申请，因而需要指定要申请的台网的台网代码；\ ``Net``\ 为默认的台站代码；比如\ ``0101``\ 即代码Hi-net台网；
- Hi-net对于数据申请存在诸多限制，比如若申请Hi-net所有台站的数据，则单次申请的数据最大长度不得超过5分钟；若仅申请50个台站的数据，则单次申请的数据最大长度可以取为60分钟；由于具体的台站数目是保存中Hi-net账户中的，难以获取，只能通过\ ``MaxSpan``\ 人为指定；
- ``catwin32``\ 是Hi-net提供的用于合并WIN32数据的工具，这里需要指定该二进制文件的文件名\ ``catwin32``\ 或是其绝对路径\ ``/home/seisman/bin/catwin32``\ ；

用法
----

::

	$ python HinetContRequest.py -h
	Request continuous waveform data from NIED Hi-net.

	Usage:
	    HinetContRequest.py <year> <month> <day> <hour> <min> <span> [options]
	    HinetContRequest.py -h

	Options:
	    -h, --help              Show this help.
	    -c CODE --code=CODE     Select code for organization and network.
	    -d DIR --directory=DIR  Output directory. Default: current directory.
	    -o FILE --output=FILE   Output filename.
	                            Default: CODE_YYYYMMDDHHMM_SPAN.cnt
	    -t FILE --ctable=FILE   Channel table filename. Default: CODE_YYYYMMDD.ch

该脚本的参数及选项比较简单：

- year、month、day、hour、min为要申请的连续波形的起始时间；
- span为要申请的连续波形的持续时间；
- ``-c``\ 用于指定台网代码；
- ``-d``\ 用于指定输出目录，默认为当前目录；
- ``-o``\ 用于指定输出文件名，默认文件名为\ ``CODE_YYYYMMDDHHMM_SPAN.cnt``\ ；
- ``-t``\ 用于指定channel table的文件名，默认文件名为\ ``CODE_YYYYMMDD.ch``\ ；

申请流程
--------

#. 从配置文件中读取配置信息
#. 从参数列表中读入要申请的连续波形数据的起始时间和持续时间
#. 确定要申请的台网代码，并检测该时间段内是否有可用数据
#. 若要申请的数据持续时间\ ``span``\ 大于\ ``MaxSpan``\ ，则将整个申请分为几次子申请；每次子申请会检测申请状态，待上次子申请完成后再进行下次子申请；
#. 待所有子申请完成后，并行下载全部数据；
#. 解压全部ZIP文件，并调用\ ``catwin32``\ 合并所有解压出的cnt文件；
#. 对cnt和ch文件重命名；
#. 清理不必要的文件；

示例
----

最简单的例子::

    python HinetContRequest.py 2012 01 01 10 30 20

申请其他台网的数据::

    python HinetContRequest.py 2012 01 01 10 30 20 -c 0103

自定义输出信息::

    python HinetContRequest.py 2012 01 01 10 30 20 -d abc -o xxx.cnt -t xxx.ch

建议的用法是::

    python HinetContRequest.py 2012 01 01 10 30 20 -d 201201010130

即指定输出目录，输出文件名使用默认设置。

修订历史
========

- 2014-08-30：初稿；
- 2014-09-12：账号及密码位于配置文件中；
- 2014-11-04：将数据申请与数据下载合并在一起；

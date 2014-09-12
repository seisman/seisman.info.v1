Hinet连续波形数据申请脚本
#########################

:date: 2014-08-30 22:22
:author: SeisMan
:category: 地震学基础
:tags: Hinet, 数据, 申请, Python
:slug: hinet-continuous-waveform-data-request-script

.. contents::

前文已经说到，Hi-net连续波形数据申请的本质可以简化为如下几步：

#. 指定参数，构建query string
#. 向Hi-net发送数据请求
#. 等待数据准备

这篇博文介绍了如何用Python实现以上步骤。为什么用Python呢？

    Life is short, you need Python.

Python实现示例
==============

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

HinetContRequest.py
===================

**功能更完整的脚本**\ 为\ `HinetContRequest.py <https://github.com/seisman/HinetScripts/blob/master/HinetContRequest.py>`_\ 。

依赖
----

- Python 3.4（未测试Python 2.7是否可行）
- requests模块
- docopt模块

注意事项
--------

- 使用该脚本时首先要修改\ ``user``\ 和\ ``passwd``\
- 该脚本仅实现了单次数据申请，多次调用该脚本即实现了多次申请，具体实现需要自己根据实际情况实现。

用法
----

.. code-block:: bash

	$ python HinetContRequest.py -h
	Request continuous waveform data from Hi-net.

	Usage:
	    HinetContRequest.py <year> <month> <day> <hour> <min> <span> [options]
	    HinetContRequest.py -h

	Options:
	    -h --help    Show this help.
	    --code=CODE  Select code for organization and network. [default: 0101]
	    --arc=ARC    Compressed format: Z, GZIP, ZIP, LZH. [default: ZIP]

	Codes of org & net:
	    '0101' : 'NIED:NIED Hi-net',
	    '0103' : 'NIED:NIED F-net (broadband)',
	    '0103A': 'NIED:NIED F-net (strong motion)',
	    '0201' : 'UNIV:Hokkaido University',
	    '0202' : 'UNIV:Tohoku University',
	    '0203' : 'UNIV:Tokyo University',
	    '0204' : 'UNIV:Kyoto University',
	    '0205' : 'UNIV:Kyushu University',
	    '0206' : 'UNIV:Hirosaki University',
	    '0207' : 'UNIV:Nagoya University',
	    '0208' : 'UNIV:Kochi University',
	    '0209' : 'UNIV:Kagoshima University',
	    '0301' : 'JMA:JMA',
	    '0401' : 'OTHER:JAMSTEC',
	    '0501' : 'OTHER:AIST',
	    '0601' : 'OTHER:GSI',
	    '0701' : 'LOCAL:Tokyo Metropolitan Government',
	    '0702' : 'LOCAL:Hot Spring Research Institute of Kanagawa Prefecture',
	    '0703' : 'LOCAL:Aomori Prefectural Government',
	    '0705' : 'LOCAL:Shizuoka Prefectural Government',

示例
----

#. \ ``python HinetContRequest.py 2013 01 02 10 20 5``\
#. \ ``python HinetContRequest.py 2013 01 02 10 20 5 --code=0103 --arc=GZIP``\

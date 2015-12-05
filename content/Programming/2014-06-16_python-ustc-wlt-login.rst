USTC网络通登录脚本Python版
##########################

:author: SeisMan
:date: 2014-06-15 21:00
:category: 编程
:tag: web, Python, USTC
:slug: python-ustc-wlt-login

最近几日在学Python以及相关的网页请求模块，练习着重写了USTC网络通的登录脚本，比之前的Perl版要简短了很多，其中使用了 ``Requests`` 模块。

最新版本位于：https://gist.github.com/seisman/2d04d52c6415d283dac8

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    # Python Script to login wlt @ USTC
    #
    # Author: Dongdong Tian @ USTC
    # Date  : 2014/06/15
    #
    import requests

    name = 'xxxxxxx'
    passwd = "xxxxxxxxx"
    url = "http://wlt.ustc.edu.cn/cgi-bin/ip"

    print("""\
    请选择出口：
            1: 教育网出口(国际,仅用教育网访问,适合看文献)
            2: 电信网出口(国际,到教育网走教育网)
            3: 联通网出口(国际,到教育网走教育网)
            4: 电信网出口2(国际,到教育网免费地址走教育网)
            5: 联通网出口2(国际,到教育网免费地址走教育网)
            6: 电信网出口3(国际,到教育网走教育网,到联通走联通)
            7: 联通网出口3(国际,到教育网走教育网,到电信走电信)
            8: 教育网国际出口(国际,国内使用电信和联通,国际使用教育网)
            9: 移动测试国际出口(国际,无P2P或带宽限制)
    注：选择出口2、3无法使用的某些电子资源，使用出口4、5、6可能可以正常使用""")
    while True:
        port = int(input("[1-9] "))
        if port >= 1 and port <= 9:
            port -= 1
            break

    print("""
    使用时限：
            1: 0s, 永久
            2: 3600s, 1小时
            3: 14400s, 4小时
            4: 39600s, 11小时
            5: 50400s, 14小时""")
    expire = {
        '1' :     0,
        '2' :  3600,
        '3' : 14400,
        '4' : 39600,
        '5' : 50400,
    }
    while True:
        exp = int(input("[1-6] "))
        if exp >= 1 and exp <= 5:
            exp = expire[str(exp)]
            break

    payload = {
        'cmd'      : 'set'  ,
        'name'     : name   ,
        'password' : passwd ,
        'type'     : port   ,
        'exp'      : exp    ,
    }
    r = requests.get(url, data=payload)

    if r.status_code != requests.codes.ok:
        print("request error with status code: %s", r.status_code)


代码就60行左右，其中真正必要的代码才10行。

修订历史
========

- 2014-06-16：初稿；
- 2014-06-24：修改已兼容Python 2.7和Python 3.4。

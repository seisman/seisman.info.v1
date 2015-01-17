Hinet连续波形数据申请及下载的脚本实现
#####################################

:date: 2014-08-30 22:22
:modified: 2015-01-17
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
- 2014-12-03：由于Hinet网址的更新，原Python脚本失效，现已修正；
- 2015-01-17：Hinet网址改动比较大，脚本实现需要更多的技巧，因而把原来的示例脚本删除；

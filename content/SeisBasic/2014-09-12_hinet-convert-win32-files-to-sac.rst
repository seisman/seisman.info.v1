Hi-net WIN32转SAC脚本
#####################

:date: 2014-09-12
:author: SeisMan
:category: 地震学基础
:tags: Hinet, Python, 数据
:slug: hinet-convert-win32-files-to-sac

.. contents::

该脚本用于实现Hinet WIN32格式到SAC格式的转换，脚本位于\ `rdhinet.py <https://github.com/seisman/HinetScripts/blob/master/rdhinet.py>`_\ 。

用法
====

::

    $ python rdhinet.py -h
    Extract SAC data files from Hi-net WIN32 files

    Usage:
        rdhinet.py DIRNAME [-C <comps>] [-D <outdir>] [-S <suffix>] [-P <procs>]
        rdhinet.py -h

    Options:
        -h          Show this help.
        -C <comps>  Selection of components to extract.
                    Avaiable components are U, N, E, X, Y. [default: UNE]
        -D <outdir> Output directory for SAC files.
        -S <suffix> Suffix of output SAC files.
        -P <procs>  Parallel using multiple processes. Set number of cpus to <procs>
                    if <procs> equals 0.    [default: 0]

参数说明
========

#. ``DIRNAME``\ 为必须参数，即要处理的文件夹。文件夹中包含了从Hi-net下载得到的ZIP格式的连续波形数据；
#. ``-C <comps>``\ 为可选参数，表示要提取哪些分量的波形，可选的值为U、E、N、X、Y，默认为\ ``UNE``\ ；
#. ``-D <outdir>``\ 为可选参数，表示SAC文件的输出目录。可以是绝对路径，也可以是相对于\ ``DIRNAME``\ 的相对路径。默认值为\ ``.``\ ，即解压到文件夹\ ``DIRNAME``\ 下；
#. ``-S <suffix>``\ ，输出SAC文件的扩展名，默认无扩展名
#. ``-P <procs>``\ 为可选参数，表示用多个进程并行提取数据；默认值为0，即设置进程数与CPU数目相同；

脚本说明
========

脚本的数据处理流程如下：

#. 进入目录\ ``DIRNAME``\ ；
#. 解压全部ZIP格式的文件；
#. 将解压得到的WIN32格式的\ ``cnt``\ 文件合并为一个文件；
#. 生成参数文件\ ``win.prm``\ ；
#. 从channel table文件中获取channle列表；
#. 根据channel列表，提取不同channel的数据；
#. 修改所有SAC文件的扩展名；

示例
====

处理目录201201010101下的WIN32文件，其他参数使用默认值::

    python rdhinet.py 201201010101

仅提取\ ``U``\ 分量::

    python rdhinet.py 201201010101 -C U

输出SAC文件到的\ ``DIRNAME``\ 下的\ ``RAW``\ 目录中::

    python rdhinet.py 201201010101 -D RAW

输出到\ ``RAW``\ 目录下，并指定文件扩展名为\ ``SAC``\ ::

    python rdhinet.py 201201010101 -D RAW -S SAC

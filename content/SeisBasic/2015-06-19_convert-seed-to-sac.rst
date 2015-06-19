SEED格式转SAC格式
#################

:date: 2015-06-19
:author: SeisMan
:category: 地震学基础
:tags: SEED, SAC, 格式
:slug: convert-seed-to-sac

本文会介绍将SEED、miniSEED等格式转换为SAC格式所使用的工具和用法。需要注意，本文并不会详细介绍工具的具体语法，只介绍常用的功能，其他功能及选项，读者应自行阅读相关文档。

.. contents::

SEED格式简介
============

SEED，即Standard for the Exchange of Earthquake Data，是地震学波形数据的标准格式之一。每个SEED文件中可以包含多台站多分量多时间段的连续波形数据。

SEED格式又可以细分为三种格式：

#. Full SEED格式：也就是一般说的SEED格式，包含波形数据以及仪器相关信息；
#. miniSEED格式：仅包含波形数据；
#. dateless SEED格式：仅包含仪器相关信息；

rdseed: SEED => SAC
===================

rdseed可以直接提取波形数据::

    rdseed -df infile.seed

可以同时提取波形数据以及RESP仪器响应文件::

    rdseed -Rdf infile.seed

还可以同时提取波形数据以及SAC PZ仪器响应文件::

    rdseed -pdf infile.seed

rdseed: SEED => RESP/PZ
========================

只提取RESP文件::

    rdseed -Rf infile.seed

只提取PZ文件::

    rdseed -pf infile.seed

rdseed: Dataless SEED => RESP/PZ
================================

从Dataless SEED中提取RESP::

    rdseed -Rf infile.dataless

从Dataless SEED中提取PZ::

    rdseed -pf infile.dataless

rdseed: miniSEED => SAC
=======================

利用rdseed将miniSEED数据转换为SAC格式时，需要使用\ **对应**\ 的dataless SEED数据。

从miniSEED中提取波形数据::

    rdseed -df infile.miniseed -g infile.dataless

从miniSEED中提取波形数据，同时从dataless SEED中提取RESP::

    rdseed -Rdf infile.miniseed -g infile.dataless

从miniSEED中提取波形数据，同时从dataless SEED中提取PZ::

    rdseed -pdf infile.miniseed -g infile.dataless

mseed2sac: miniSEED => SAC
===========================

mseed2sac可以直接将miniSEED文件转换为SAC格式，而不需要dataless SEED文件::

    mseed2sac infile.miniseed

但解压出来的SAC文件中只有台站名和台网名，与用miniSEED解压出来的SAC数据相比，少了cmpaz、cmpinc、stla、stlo、stel、stdp、kcmpnm信息，因而需要手动添加台站信息。

在使用mseed2sac时，还可以加上额外的metafile和selectfile文件，以及地震事件信息。比如::

    mseed2sac -m metafile -I selectfile -E 2006,123,15:27:08.7/-20.33/-174.03/65.5/Tonga

其中metafile提供了台站的基本信息，selectfile中列出了要提取哪些台站的数据。具体文件格式参考官方文档。

metafile可以自己根据格式生成，也可以直接使用IRIS提供的\ `FetchMetadata <https://seiscode.iris.washington.edu/projects/ws-fetch-scripts/files>`_\ 脚本获取。

obspy: miniSEED => SAC
======================

obspy可以读取miniSEED，并输出为多种格式，输出时文件名的格式需要自己指定。

.. code-block:: python

   from obspy.core import read

   st = read("20150612.miniseed")
   for tr in st:
       fname = "%s.%s.%s.%s.SAC" % (tr.stats.network, tr.stats.station, tr.stats.location, tr.stats.channel)
       tr.write(fname, format="SAC")

参考
====

#. `IRIS Data Format <https://ds.iris.edu/ds/nodes/dmc/data/formats/>`_
#. `IRIS Dataless SEED <http://ds.iris.edu/ds/nodes/dmc/data/formats/dataless-seed/>`_
#. `mseed2sac <https://seiscode.iris.washington.edu/projects/mseed2sac/wiki>`_
#. `Working with SEED data <http://portal.resif.fr/?Working-with-SEED-data&lang=en>`_

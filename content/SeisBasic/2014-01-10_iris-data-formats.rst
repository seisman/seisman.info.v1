地震波形数据格式
################

:date: 2014-01-10 00:49
:author: SeisMan
:category: 地震学基础
:tags: 数据, 格式
:slug: iris-data-formats

.. contents::

地震数据的格式，大概分为两种：一种是以归档和交换为目的的格式，比如SEED，这种格式要求一个文件中包含足够多的数据信息，如果可能的话，进行数据压缩，以减少数据传输量和数据存储空间；另一种是以数据处理为目的的格式，比如SAC，这种格式一般只包含单个台站单个分量或多分量的数据。这里简介一下IRIS提供的以归档和交换为目的的数据格式。

SEED
====

全称是The Standard for the Exchange of Earthquake Data，其设计的目的是为了数据交换和归档，因而不适宜直接数据处理，一般使用rdseed将seed格式转换为其他数据格式。

一个完整的SEED数据包含了时间序列以及台站的相关信息。完整的SEED数据又可以分解为两个部分：只包含时间序列的miniSEED格式和只包含台站信息的Dataless SEED格式。完整的SEED格式的说可以参考SEED Reference Manual。

miniSEED
========

miniSEED格式是SEED格式的一个子集，其只包含时间序列和极少量的其他信息。

一个连续的时间序列在SEED格式中被分为若干等长的数据段，这样做的目的还不清楚，也许是出于数据实时传递的考虑。对于实时数据流，段长度为512-byte，对于归档数据段长度为4096-byte。

`libmseed`_\ 是一个比较友好的函数库，可以用于读写miniSEED文件。

miniSEED数据可以通过BREQ_FAST获取，其邮箱地址为：miniseed@iris.washington.edu。

Dataless SEED
=============

dataless SEED中只包含台站的坐标以及仪器响应信息，而不包含任何时间序列。

为什么要将台站信息保存到单独的文件中？因为台站位置以及仪器响应等信息，在相当长一段时间内（1年的量级）是保持不变的，当大量申请SEED数据时，数据中的台站信息部分大量重复。由于dataless SEED中记录了台站信息的变化历史，因而在大量数据的情况下，将台站信息单独存放更加经济。 

获取dataless SEED数据的几种方法：

-  在线申请： http://www.iris.edu/data/DatalessRequest.htm
-  根据BREQ\_FAST格式发送邮件到dataless@iris.washington.edu
-  从\ `BUD`_\ 申请
-  直接从IRIS的\ `FTP`_\ 下载

StationXML
==========

与dataless SEED类似，保存台站信息。详细信息在\ `这里 <http://www.fdsn.org/xml/station/>`_\ 。

Simple ASCII
============

ASCII格式，占用硬盘空间，不常用。\ `格式说明 <http://www.iris.edu/dms/nodes/dmc/data/formats/simple-ascii/>`_\ 。

.. _libmseed: https://seiscode.iris.washington.edu/projects/libmseed
.. _BUD: http://www.iris.edu/bud_stuff/bud/bud_start.pl?BUDDIR=/budnas/virtualnets/ALL
.. _FTP: http://www.iris.edu/pub/RESPONSES/DATALESS_SEEDS/

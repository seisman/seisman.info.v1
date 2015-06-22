IRIS数据申请之BREQ_FAST
#######################

:date: 2013-07-23 01:40
:author: SeisMan
:category: 地震学软件
:tags: breq_fast, IRIS, 数据申请
:slug: iris-breq-fast

.. contents::

IRIS提供了很多申请地震数据的软件或方法，比如Wilber III、SOD、JWeed等等。

BREQ_FAST是众多方法中的一个，喜欢它的人爱得死去活来，不喜欢它的人对它不屑一顾。其实每种方法都有自己的优点和缺点，每种方法都有自己擅长和不擅长的领域。

简介
====

BREQ_FAST是Batch REQuests FAST的简称。简单来说，就是通过发送一封邮件到指定的邮箱来申请数据，邮件的内容要按照规定的格式来写。这种数据申请的方法不同于常见的交互式方法，因而特别适合写脚本自动生成邮件内容、自动发送邮件、自动下载数据。

优点
====

- 简单易用，写一次脚本基本就一劳永逸了
- 速度快，不受网速限制
- 从申请到下载可以完全脚本化，适合数据批量申请

缺点
====

- 需要自己准备事件信息（即地震目录）以及台站列表；
- 非交互式，不像其他方法那样可以在线获得事件信息，根据事件选择符合一定条件的台站；

邮件内容格式
============

BREQ_FAST只对邮件内容有严格要求，不要求邮件主题。

::

    .NAME
    .INST
    .MAIL
    .EMAIL
    .PHONE
    .FAX
    .MEDIA:
    .ALTERNATE MEDIA:
    .ALTERNATE MEDIA:
    .LABEL
    .SOURCE     ---
    .HYPO         | optional
    .MAGNITUDE  ---
    .QUALITY
    .END
     request line-1
     request line-2
     ...
     ...
     ...
     request line-n

要保证所有以“.”开头的标记行左对齐！！！

- .Name：用户姓名，IRIS会根据此标记在ftp上建立相关文件夹；
- .INST：单位或者机构信息（应该没啥用）；
- .MAIL：邮寄地址；（不会寄东西的）
- .EMAIL：邮箱。IRIS会向这个邮箱发送有关数据状态的邮件，可以与发送该邮件的邮箱地址不同；
- .PHONE：电话；（没用）
- .FAX：传真；（没用）
- .MEDIA：数据获取介质。有如下几种方式可以选择（按照倾向性排序），现在常用的方式是FTP，要求指定第一、第二、第三介质；

  + Electronic (FTP)
  + EXABYTE – 2 gigabyte
  + EXABYTE – 5 gigabyte
  + DAT (digital audio tape)
  + DLT
  + DVD-R

- .LABEL：申请的SEED数据将会以该LABEL命名，SEED文件内部也会包含这个LABEL的信息，应该选择合适的LABEL以保证文件名的唯一性和可区分性；（以发震时刻命名是个不错的选择）
- .SOURCE、.HYPO和.MAGNITUDE是可选的，其指定了震源的一些信息，这些信息最终会被写入SEED文件中；若未指定这三个标记，SEED解压出的SAC文件时没有震源信息的；若指定了这三个标记，解压出来的SAC文件时有震源信息的（只是猜测，没试过）。这几行写起来有些复杂，不要也罢，震源信息可以后期再写入。这三个标记的详细信息可以参考最后给出的链接。
- .QUALITY：数据质量；一般默认B；

  - B：最好的数据（首选Q，没有Q则选择D，没有D则选择R）
  - E：所有数据（Q & D & R）
  - Q：标记了QC的数据（即进行了质量控制）
  - D：中等质量数据；
  - R：最原始数据；

- request line是真正的数据申请信息，前面的那些都只是辅助信息；

Request Line格式
================

::

    STA NN YYYY MM DD HH MM SS.TTTT YYYY MM DD HH MM SS.TTTT #_CH CH1 CH2 CHn LI

- ``STA``\ ：台站名
- ``NN``\ ：台网或虚拟台网名
- YYYY、MM、DD、HH、MM：年份（四位）、月、日、时、分
- ``SS.TTTT``\ ：秒；小数点后为毫秒，可以省略；
- 日期和时间出现了两次，分别代表要申请的数据的开始时间和结束时间；
- ``#_CH``\ ：接下来出现的通道标识的数目；
- ``CHn``\ ：通道标识符，可以包含通配符；
- ``LI``\ ：LOCATION ID，可选

每行最多包含100个字符。

通配符
======

通道标识符支持通配符，目前仅支持通配符"?"，代表任意单个字符，比如"BH?"代表所有宽频带（Broadband）高增益（High gain）的通道，可能包含BHE、BHN、BHZ、BH1、BH2等等；通道列表可以包含多个字段，比如\ ``3 LHZ BH? S??``\ 。

一般通道名长度为三个字符，第一个字符为Band Code，第二个字符为Source Code，第三个字符为Orientation Code。

台网和台站也可使用通配符，但是不建议台网和台站同时使用通配符；单个"?"可以匹配该台网的所有台站。

如果不指定位置号，则获取该台站的全部location的数据。

对于每个台站可以分别指定数据窗范围，因而可以根据到时信息确定需要的数据窗，最大程度减少数据量。不过长一点也无所谓。

例子
====

给出了SOURCE、HYPO、MAGNITUDE的例子，request line给出了尽可能多的写法：

::

    .NAME Joe Seismologist
    .INST Podunk University
    .MAIL 101 Fast Lane, Middletown, KS  89432
    .EMAIL joe@podunk.edu
    .PHONE 555 555-1212
    .FAX   555 555-1213
    .MEDIA FTP
    .ALTERNATE MEDIA 1/2" tape - 6250
    .ALTERNATE MEDIA EXABYTE
    .LABEL Joe's FIRST Request
    .SOURCE =NEIC PDE=Jan 1990 PDE=National Earthquake Information Center - USGS DOI=
    .HYPO =1999 01 02 20 21 32.62= 13.408= 144.439=135.0=18=216=Mariana Islands=
    .MAGNITUDE =5.7=mb=
    .QUALITY B
    .END
    GRFO IU 1999 01 02 00 18 10.4 1999 01 02 00 20 10.4  1 SHZ
    ANTO IU 1999 01 02 02 10 36.6 1999 01 02 02 12 36.6  1 SH?
    AFI  IU 1999 01 02 02 10 37.1 1999 01 02 02 12 37.1  1 BH? 00
    SEE  CD 1999 01 02 14 45 08.9 1999 01 02 14 47 08.9  1 SHZ
    CASY IU 1999 01 04 02 42 13.4 1999 01 04 02 44 13.4  1 BHZ 10
    NNA  II 1999 01 04 02 41 57.5 1999 01 04 02 43 57.5  1 BHZ
    PFO  TS 1999 01 04 02 41 57.5 1999 01 04 02 43 57.5  1 BHZ
    PFO  II 1999 01 04 02 41 57.5 1999 01 04 02 43 57.5  1 BHZ
    KMI  CD 1999 01 04 02 41 57.5 1999 01 04 02 43 57.5  1 BHZ
    SSE  CD 1999 01 04 02 18 25.4 1999 01 04 02 20 25.4  2 B?? SHZ
    PAS  TS 1999  1  4  2 10 49   1999  1  4  2 12 49    3 BH? SHZ L??

发送邮件到这里
==============

根据上面的规则生成了邮件内容，直接将内容作为邮件正文（不是附件）发送到指定邮箱，不同的邮箱功能不同；

- breq_fast@iris.washington.edu：申请完整的SEED文件，最常用的方式；
- DATALESS@iris.washington.edu：无数据的SEED文件，包含仪器响应、仪器坐标等台站信息，一般与miniSEED数据联合使用；
- miniseed@iris.washington.edu：miniSEED数据，只有数据没有台站信息；
- sync@iris.washington.edu：合成数据

申请回应
========

发送数据请求之后，会收到两封回复邮件。第一封邮件告诉你IRIS已经收到邮件，且邮件格式正确。第二封邮件告诉你数据已经准备完毕，并给出下载地址。

注意：有多人反映，发送申请邮件之后很久没有收到第一封邮件。似乎直接通过网页版的邮箱界面发送邮件会出现这个问题，而通过命令行发送则没有问题。如果出现未收到回复邮件的情况，可以考虑用Perl或Python发送邮件。

Bug和限制
=========

- 无法识别超过正常范围的时间，比如分钟数大于59，这要求用户自己认真处理时间问题；
- 每行必须左对齐；
- 通配符只支持"?"

参考
====

- BREQ_FAST Manaul：http://www.iris.edu/dms/nodes/dmc/manuals/breq_fast/
- SEED通道命名规则：http://www.iris.edu/manuals/SEED_appA.htm
- Location ID命名规则：http://www.iris.edu/dms/newsletter/vol1/no1/specification-of-seismograms-the-location-identifier/

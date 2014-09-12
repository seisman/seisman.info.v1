Hi-net连续波形数据
##################

:date: 2014-08-27 11:08
:author: SeisMan
:category: 地震学基础
:tags: Hinet, 数据, 申请, 下载
:slug: hinet-continuous-waveform-data

.. contents::

本文将介绍如何从Hi-net申请并下载连续波形数据，并介绍Hi-net数据的一些细节。

连续波形数据申请地址：http://www.hinet.bosai.go.jp/REGS/download/cont/?LANG=en

第一印象
========

下图是数据申请页面的具体样子，看上去还是相当直观的。

.. figure:: /images/2014082701.png
   :width: 800px
   :alt: download-continous-waveform-data

申请流程
========

#. 台站选择

   点击“Hi-net/F-net Station selection is here”会打开台站选择页面，可以通过“点击”或“拖曳”的方式选取台站。

   该页面的台站选择功能比较鸡肋，实际用起来很不方便。因而除非特殊情况下，建议选择Hi-net全部台站（即默认情况），将全部台站的数据下载下来再自己写脚本对台站进行筛选。下文也默认使用全部台站。

   点击“Check the current configure for user”可以看到用户的台站选择情况，默认情况下选择的台站数为0，即下载全部台站的波形数据。

#. 选择机构和台网

   Hi-net网站提供了多个机构和台网的波形数据的下载，可选的机构名和台网名可以在相应的下拉列表中看到。对于Hi-net数据而言，Organization处选择NIED，Network处选择NIED Hi-net，即默认选项。

#. 连续波形数据的时间范围

   确定要申请的波形数据的起始时刻（精确到分）以及数据长度（1-60分钟），然后点击“Search”。比如选择开始时间为“Year:2014”、“Month:08”、“Day:29”、“00:”、“00”，数据长度为“5min”。

一大堆说明
==========

点击“Search”之后显示如下，可以看到，连续波形数据被分割成一分钟的小段，每段数据都有一个“Download”链接，所有数据还有一个“Package Download”链接：

.. figure:: /images/2014082702.png
   :width: 800px
   :alt: hinet-search-result

之所有要介绍Hi-net数据申请流程，就是因为这其中涉及到太多规则和例外，下面一一说明：

- 连续波形数据范围：\ **2004年4月1日**\ ~ \ **今日此刻前一小时**\
- 所有时间均为\ **JST**\ 时间，即东九区。在数据申请以及数据处理时都必须将这点考虑进去
- Hi-net将连续波形数据切割成一分钟长度的数据段，即\ **每个文件仅包含一分钟的波形**

由于Hi-net将连续波形数据切割成一分钟长度的数据段，因而：

- 若申请时数据长度为30分钟，则会生成30段数据，每段数据提供一个“Download”链接，30段数据意味着需要点击30次链接，需要下载30个文件；
- 若Number of Channels * Record Length (min) <= 12000 min，且Record Length < 60min，则可以将多段数据打包下载，即“Package Download”
- Hi-net共计约800个台站（实为785个），每个台站三个channel（并非所有台站都有完整的三个channel），即800*3=24000个channel，因而若想要将多段数据打包下载，Record Length不得超过5 min。

下面简单算个账，对于一个地震事件，假设需要申请Hi-net所有台站30分钟的连续波形数据，有两种做法：

#. 数据长度设置为30min，然后点击30次“Download”链接，下载30个文件；
#. 数据长度设置成5min，分为6次申请，每次均可使用“Package Download”，点击6次链接，下载6个文件；

无论是点击“Download”还是“Package Download”，每次点击均称为一个“申请”。每次申请之后，Hi-net服务器需要一定的时间来准备数据，在此期间不可申请新数据，否则会出现错误。数据准备所需的时间由该次申请的数据大小来决定，若申请所有台站5分钟的连续波形，\ **准备时间大概为30-60s**\ 。

单次申请数据准备完成后，即可下载数据或继续下一次申请。需要注意，\ **Hi-net最多只保留150次申请的数据**\ ，因而要及时下载。

了解了上面的规则，可知，第二种申请方法要更实用一些，申请的次数更少，下载的文件也更少，唯一的不方便是需要将数据手动分成几次申请。后面将只使用第二种方法申请数据。

数据下载
========

在申请数据之后，会自动打开”Status/Download“页面。如下图所示：

.. figure:: /images/2014082703.png
   :width: 800px
   :alt: status and donwload page

图中的每行代表一次申请，具有唯一的ID。黄色背景的行表示该数据尚未被下载过，白色背景的行表示该数据已经下载过，还可以再次下载。超过一定天数的数据则无法下载，另外申请时若出现错误会显示为灰色行。

另外，下载数据时似乎同时只能下载5个数据，点击其他数据的下载链接没有反应。目前不确定是浏览器的限制、带宽的限制还是Hi-net服务器的限制。

对数据的说明
=============

- 下载得到的为压缩文件，默认压缩格式为ZIP格式（推荐使用ZIP格式），文件名格式为::

  [Organization ID]_[Network ID]_[Start time yyyymmddHHMM (in JST)]_[Record length (min)].zip

- 每个ZIP文件中包含了若干个cnt文件、两个ch文件以及一个readme文件；
- cnt文件中包含了一分钟的地震波形数据，为win32格式。win32格式是日本某机构自定义的一种地震数据格式，可以通过Hi-net提供的win32tools转换成SAC格式；
- ch文件即channels table，其包含了每个台站的经纬度以及每个channel的仪器响应信息，两个channel table文件内容相同，只是一个使用euc编码，一个使用sjis编码；

关于数据格式、数据转换以及channel table文件的具体使用，放在后面的篇章再细说。

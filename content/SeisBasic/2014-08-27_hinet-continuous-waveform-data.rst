Hi-net连续波形数据
##################

:date: 2014-08-27 11:08
:modified: 2014-12-03
:author: SeisMan
:category: 地震学基础
:tags: Hinet, 数据, 申请, 下载
:slug: hinet-continuous-waveform-data

.. contents::

本文将介绍如何从Hi-net申请并下载连续波形数据，并介绍Hi-net数据的一些细节。

连续波形数据申请地址：https://hinetwww11.bosai.go.jp/auth/download/cont/?LANG=en

第一印象
========

下图是数据申请页面的具体样子，看上去还是相当直观的。

.. figure:: /images/2014082701.jpg
   :width: 800px
   :alt: download-continous-waveform-data

申请流程
========

#. 选择机构和台网

   Hi-net网站提供了多个机构和台网的波形数据的下载，可选的机构名和台网名可以在相应的下拉列表中看到。对于Hi-net数据而言，Organization处选择NIED，Network处选择NIED Hi-net。

#. 台站选择

   目前仅支持对Hi-net和F-net这两个台网进行台站筛选。其他台网，必须下载全部台站的数据才能筛选。

   点击“Hi-net/F-net Station selection is here”会打开台站选择页面，可以通过“点击”或“拖曳”的方式选取台站。该页面的台站选择功能使用起来不太方便，一般情况下，选择全部台站，将所有数据下载下来再写脚本对台站进行筛选。

   点击“Check the current configure for user”可以看到用户的台站选择情况，默认情况下选择的台站数为0，即下载全部台站的波形数据。

#. 连续波形数据的时间范围

   确定要申请的波形数据的起始时刻（精确到分）以及数据长度（1-60分钟），然后点击“Search”。比如选择开始时间为“Year:2014”、“Month:08”、“Day:29”、“00:”、“00”，数据长度为“5min”。

一大堆说明
==========

点击“Search”之后显示如下，可以看到，连续波形数据被分割成一分钟的小段，每段数据都有一个“Download”链接，所有数据还有一个“Package Download”链接：

.. figure:: /images/2014082702.png
   :width: 800px
   :alt: hinet-search-result

之所有要介绍Hi-net数据申请流程，就是因为这其中涉及到太多规则和例外，下面一一说明：

- 连续波形数据范围：

  不同台网提供的波形数据的起始日期不同，具体如下：

  - NIED Hi-net : 2004/04/01 00:00
  - NIED F-net : 2004/04/01 00:00
  - NIED V-net : 2010/04/01 00:00
  - JMA Seismometer Network : 2004/04/01 00:00
  - JMA Volcanic Seismometer Network : 2010/12/01 00:00
  - Universities : 2004/04/01 00:00
  - Tokyo Metropolitan Government : 2004/04/01 00:00
  - Hot Spring Research Institute of Kanagawa Prefecture : 2004/04/01 00:00
  - Aomori Prefectural Government : 2004/04/01 00:00
  - Shizuoka Prefectural Government : 2004/06/15 00:00
  - JAMSTEC Realtime Data from the Deep Sea Floor Observatory : 2004/04/01 00:00
  - JAMSTEC DONET1 : 2014/10/01 00:00
  - AIST : 2004/04/01 00:00
  - GSI : 2004/04/01 00:00

  所有台网的波形数据的结束时间均相同，即\ **此刻前两小时**\ 。

- 该网站中的所有时间均为\ **JST**\ 时间，即东九区时间。比如，假设中国现在是22点，则GMT时间为22-8=14点，而日本时间为14+9=23点。在数据申请以及数据处理时都必须将这点考虑进去。
- Hi-net将连续波形数据切割成一分钟长度的数据段，即\ **每个文件仅包含一分钟的波形数据**

由于Hi-net将连续波形数据切割成一分钟长度的数据段，因而：

- 若申请时数据长度为30分钟，则会生成30段数据，每段数据提供一个“Download”链接，30段数据意味着需要点击30次链接，需要下载30个文件；
- Hi-net提供了打包下载的功能，但对数据量有所限制。若Number of Channels * Record Length (min) <= 12000 min，且Record Length < 60min，则可以将多段数据打包下载，即“Package Download”

以Hi-net为例，Hi-net共计约800个台站（经统计为785个），每个台站三个channel（个别台站有两个或四个），即约800*3=2400个channel。因而在选择全部Hi-net台站的前提下，若想要使用打包下载功能，则数据的Record Length不得超过12000/2400=5 min。若只选择了其中50个台站，则12000/150=80 min>60 min，则Record length最大可以取为60 min。

下面简单算个账，对于一个地震事件，假设需要申请Hi-net所有台站30分钟的连续波形数据，有两种做法：

#. 数据长度设置为30min，会生成30段数据，然后点击30次“Download”链接，并下载30个文件；
#. 数据长度设置成5min，将30分钟连续波形分为6次申请，每次均可使用打包下载“Package Download”，点击6次链接，并下载6个文件；

无论是点击“Download”还是“Package Download”，每次点击均称为一次“申请”。每次申请过程的耗时大概如下：

#. 发送申请：主要由当前网络状况以及Hi-net服务器繁忙程度决定，根据经验需要3-5s；
#. 数据准备：由Hi-net服务器的繁忙程度、处理速度以及该次申请的数据大小决定。若申请所有台站一分钟的连续波形，约需要10s；若申请所有台站5分钟的连续波形，约需要20-40s；
#. 获取数据状态：在Hi-net服务器准备数据时，是不能再次申请新数据的，否则会出现错误。因而必须等待Hi-net网站更新数据申请的状态，待确认无误之后方可再次申请。因而获取数据状态大概需要3-10s。

在确认单次申请的数据准备完成后，即可下载此次申请的数据或继续下一次申请。需要注意，\ **Hi-net只保留最近150次申请的数据**\ ，并且会在数据申请之后一段时间（可能是几天）\ **删除数据**\ ，因而应及时下载。

了解了Hi-net的游戏规则之后，可知，第二种申请方法要更实用一些，申请的次数更少，耗时更短，下载的文件也更少。唯一的不方便是需要将数据手动分成几次申请，但很容易用脚本实现。后面将只使用第二种方法申请数据。

数据下载
========

在申请数据之后，会自动打开”Status/Download“页面。如下图所示：

.. figure:: /images/2014082703.png
   :width: 800px
   :alt: status and donwload page

图中的每行代表一次申请，具有唯一的ID。黄色背景的行表示该数据尚未被下载过，白色背景的行表示该数据已经下载过，还可以再次下载（数据超过一定天数后会无法下载），申请时若出现错误会显示为灰色行。

PS：下载数据时似乎同时只能下载5个数据，再点击其他数据的下载链接没有反应。目前不确定是浏览器的限制、带宽的限制还是Hi-net服务器的限制。

对数据的说明
=============

- 下载得到的为压缩文件，默认压缩格式为ZIP格式（推荐使用ZIP格式）。文件名格式为：

  - 一般台网： \ ``[OrgID]_[NetID]_[Start time yyyymmddHHMM (in JST)]_[Record length (min)].zip``\
  - 火山台网： \ ``[OrgID]_[NetID]_[VolcID]_[Start time yyyymmddHHMM (in JST)]_[Record length (min)].zip``\

- 每个ZIP文件中包含了若干个cnt文件、两个ch文件以及一个readme文件；
- cnt文件中包含了一分钟的地震波形数据，为win32格式。win32格式是日本某机构自定义的一种地震数据格式，可以通过Hi-net提供的win32tools转换成SAC格式；
- cnt文件的文件名中包含了波形的时间信息以及台网信息，但对于一般台网和火山台网，文件名的长度是不同的；
- ch文件即channels table，其包含了每个台站的经纬度以及每个channel的仪器响应信息，两个channel table文件内容相同，只是一个使用euc编码，一个使用sjis编码；

关于数据格式、数据转换以及channel table文件的具体使用，放在后面的篇章再细说。

修订历史
========

- 2014-08-27：初稿；
- 2014-11-02：修订了部分内容，并加入了对火山台网的说明；
- 2014-12-03：连续波形的申请网址发生变化；

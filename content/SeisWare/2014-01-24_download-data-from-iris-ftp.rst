IRIS FTP数据下载的几个方法
###########################

:date: 2014-01-24 00:48
:author: SeisMan
:category: 地震学基础
:tags: breq_fast, IRIS, 数据
:slug: download-data-from-iris-ftp

.. contents::

从IRIS申请地震数据，有些工具会将准备好的数据放在ftp中，供用户下载。

FTP地址格式如下： ftp://ftp.iris.washington.edu/pub/userdata/USERNAME\ ，其中USERNAME因人而异。

下载方式
========

官方提供了三种数据下载方式：

登录FTP下载
-----------

::

 $ ftp ftp.iris.washington.edu
 Name (iris:joe): anonymous # 匿名登录
 Password: JoeSeismologist@email.net # 密码随意，建议填写邮件地址
 ftp> cd pub/userdata
 ftp> ls -f
 ftp> cd Joe_Seismologist # 进入自己的目录
 ftp> ls -l
 ftp> binary # 二进制传输
 ftp> mget * # 下载所有文件
 ftp> quit

wget下载全部文件
----------------

::

    wget -P Directory -m -nd -np -r -c ftp://ftp.iris.washington.edu/pub/userdata/USERNAME/

其中

-  Directory为要保存的文件路径，默认为当前目录；
-  -m等效于-r -N -l inf --no-remove-listing，其中-r表示对文件夹进行递归，-N表示只下载比本地文件新的文件；-l指定递归深度，inf表示无穷递归；
-  -nd表示不在本地重建目录结构，这意味着无论FTP中的目录结构有多复杂，所有文件都保存到本地的一个目录中；
-  -np表示不遍历父目录；
-  -r表示递归下载；
-  -c表示支持断点续传；

wget下载单个或多个文件
----------------------

::

    wget -P Directory -m -nd -np -r -c -A "FileName" ftp://ftp.iris.washington.edu/pub/userdata/USERNAME/


其中-A表示只下载"FileName"指定的文件。FileName可以表示后缀也可以表示模式，当FileName中只包含英文字母时，则表示后缀，比如FileName为seed，则表示下载所有以seed为后缀的文件。

当FileName中包含通配符"*","?","[","]"时，FileName表示模式，只下载文件名符合该模式的文件，比如FileName为"2010*.seed"，则表示只下载所有文件名匹配“2010*.seed”的文件。

缺点
====

在大批量数据的情况下，上面三种方法都有一些缺点。

#. FTP方法，使用ftp自带的mget命令进行下载，不支持断点续传，难以指定要下载哪些文件。

#. wget下载全部数据，若FTP中的数据已存在于当前目录，则不会再次下载。这要求下载好的数据不能从当前目录中移除。一般来说数据下载和数据处理是同步进行的，这样就要求在下载目录中和数据处理目录中存有两份相同的数据。更严重的是，IRIS的FTP数据可以保留7天，今天申请的数据与3天前申请将会下载到同一目录中，不利用用户对SEED文件进行整理。

#. wget下载指定数据，如果每次申请的数据是有规律的，比如先申请2004年数据，申请->等待->下载，再申请2005年数据，这样可以使用通配符来指定下载数据。若数据申请没有类似规律，则会非常麻烦。理论上，使用BREQ\_FAST申请数据时，可以为数据指定LABEL，则SEED文件名为LABEL.xxxx.seed，其中xxxx为"随机数"，因而用户在申请时是无法完全知道seed文件的全名的，又因为wget不支持\ ``wget http://example.com/20100101.*.seed``\ 这样的语法，因而对于数据申请不规律的情况，第三种方法也是很有问题的。

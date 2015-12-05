如何彻底卸载Intel Parallel Studio
#################################

:author: SeisMan
:date: 2014-07-16 10:00
:category: Linux
:tags: CentOS, Intel
:slug: uninstall-intel-parallel-studio-completely

Intel的开发工具默认安装在 ``/opt/intel`` 目录下，由于一时手贱，用\ ``sudo rm -rf /opt/intel``\ 把整个intel文件夹给删除了。

在重新安装Intel Parallel Studio的时候一直提示“已安装该产品”，进而导致无法再次安装。实际上是因为在上一次安装的时候，安装了一大堆rpm文件，并将文件的信息写入了rpm数据库中，而在删除的时候数据库没有被更新。再次安装的时候，会在数据库中检测到，继而出现“已安装该产品”的提示。

解决办法很简单，找到所有已安装的intel相关的包，然后删除。

::

  rpm -qa | grep intel | awk '{print "yum remove -y",$1}' > uninstall.sh

查看 ``uninstall.sh`` 文件，删除其中不以intel开头的包。然后用root权限执行该脚本即可。

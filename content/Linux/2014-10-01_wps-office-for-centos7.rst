CentOS 7下安装WPS Office
########################

:date: 2014-10-01
:modified: 2014-10-23
:author: SeisMan
:category: Linux
:tags: CentOS
:slug: wps-office-for-centos7

在Microsoft Office盛行的今日，Linux下一直没有一个能与之完美兼容的Office套件。大多数发行版默认安装的OpenOffice或LibreOffice，也只是刚刚达到能用的地步，界面以及功能的差异还是很明显的。

或许WPS Office for Linux是个不错的选择。

- 中文官网： http://linux.wps.cn/
- 英文官网： http://www.wps.com/linux/

目前WPS Office for Linux尚处在测试阶段。根据惯例，alpha版为内测版本，beta版为公测版本。这里选择alpha版，版本为20141021发布的Alpha 16。

- 安装包： `wps-office-9.1.0.4885-1.a16.i686.rpm <http://kdl.cc.ksosoft.com/wps-community/download/a16/wps-office-9.1.0.4885-1.a16.i686.rpm>`_
- 字体包： `wps-office-fonts-1.0-1.noarch.rpm <http://kdl.cc.ksosoft.com/wps-community/download/a15/wps-office-fonts-1.0-1.noarch.rpm>`_

WPS Office提供的rpm包为32位版本，对于64位系统需要安装相应的32位依赖包方可使用，幸好\ ``yum``\ 可以自动判断并解决包的依赖关系，所以安装很简单。

首先\ ``cd``\ 到下载的RPM包所在的文件夹下，然后执行如下\ ``yum``\ 命令。注意，这里用的是\ ``yum``\ 而不是\ ``rpm -i``\ ，因为\ ``rpm``\ 似乎无法自动解决32位库的依赖问题。

.. code-block:: bash

   $ sudo yum install wps-office-9.1.0.4885-1.a16.i686.rpm
   $ sudo yum install wps-office-fonts-1.0-1.noarch.rpm

安装完成后，即可在“Application”中找到相关项。

参考
====

1. `WPS下载地址 <http://community.wps.cn/download/>`_
2. `WPS社区Wiki <http://community.wps.cn/wiki/%E9%A6%96%E9%A1%B5>`_
3. `原生对话框问题 <http://bbs.wps.cn/thread-22371203-1-1.html>`_
4. `部分数学公式显示支持 <http://community.wps.cn/wiki/%E9%83%A8%E5%88%86%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F%E6%98%BE%E7%A4%BA%E6%94%AF%E6%8C%81>`_

修订历史
========

- 2014-10-01：初稿；
- 2014-10-23：更新至Alpha 16；此版本中不再有\ ``mui``\ 语言包；

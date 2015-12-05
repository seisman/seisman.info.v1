CentOS 7安装fcitx中文输入法
###########################

:author: SeisMan
:date: 2014-09-20
:modified: 2015-03-09
:category: Linux
:tags: CentOS, 中文
:slug:  fcitx-for-centos-7

.. contents::

**本文不再更新**

目前不确定是否可行，具体参考：https://github.com/1dot75cm/myrepo

前面\ `CentOS 7.0下安装小小输入法 <{filename}/Linux/2014-07-10_install-yong-chinese-input-method-under-centos-7.rst>`_\ 一文中已经介绍了如何在CentOS 7下安装小小输入法来输入中文，实际用起来还是有不少不如意的地方。

今天恰好发现了CentOS 7下安装fcitx输入法的简单方法，如下。

加入EPEL源
==========

EPEL7几乎是CentOS必备的源::

    $ sudo yum install epel-release

添加mosquito-myrepo源
=====================

mosquito-myrepo是一个私人制作的第三方源，其中包含了fcitx输入法。

- 项目地址： https://github.com/1dot75cm/myrepo
- 支持的发行版： Fedora 19/20/21/rawhide 以及RHEL/CentOS 7

::

    $ sudo yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo/repo/epel-7/mosquito-myrepo-epel-7.repo

安装输入法
==========

可以选择下面的各种输入法中的某一个或多个::

    $ yum install fcitx-googlepinyin fcitx-cloudpinyin # 谷歌拼音输入法
    $ yum install fcitx-rime fcitx-cloudpinyin # 中州韵输入法
    $ yum install fcitx-libpinyin fcitx-cloudpinyin # libpinyin输入法
    $ yum install fcitx-sunpinyin sunpinyin-data fcitx-cloudpinyin # sunpinyin输入法

清理工作
========

mosquito-myrepo在不断地支持更多的软件，这也进一步造成该repo中的软件与base、EPEL中的软件存在版本冲突，在该repo的项目主页中建议安装yum的优先级插件 ``yum-plugin-priorities`` ，这在一定程度上会缓解版本冲突问题，但无法从根本上避免。

鉴于多个repo的版本冲突会造成一些麻烦，最好的办法还是在安装完需要的软件之后就禁用该repo，需要的时候再启用。

编辑 ``/etc/yum.repos.d/mosquito-myrepo-epel-7.repo`` ，将其中的\ ``enable=1``\ 改成\ ``enable=0``\ 即可。

参考
====

- https://copr.fedoraproject.org/coprs/mosquito/myrepo/

修订历史
========

- 2014-09-20：初稿；
- 2014-09-29：安装完成之后建议禁用该repo以避免任何可能的版本冲突；
- 2014-12-27：更新sogou的配置；
- 2015-03-09：由于搜狗输入法是私有软件，违反了copr的相关规定，因而目前该源中已不再包含搜狗输入法。故删除本文中搜狗输入法相关部分；

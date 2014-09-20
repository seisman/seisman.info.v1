CentOS 7安装fcitx中文输入法
###########################

:author: SeisMan
:date: 2014-09-20
:category: Linux
:tags: CentOS, 中文
:slug:  fcitx-for-centos-7

.. contents::

前面\ `CentOS 7.0下安装小小输入法 <{filename}/Linux/2014-07-10_install-yong-chinese-input-method-under-centos-7.rst>`_\ 一文中已经介绍了如何在CentOS 7下安装小小输入法来输入中文，实际用起来还是有不少不如意的地方。

今天恰好发现了CentOS 7下安装fcitx输入法的简单方法，如下。

加入EPEL源
==========

EPEL7几乎是CentOS必备的源::

    $ wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-1.noarch.rpm
    $ sudo rpm -ivh epel-release-7-1.noarch.rpm
    $ sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

添加mosquito-myrepo源
=====================

mosquito-myrepo是一个私人制作的第三方源，其中包含了fcitx输入法以及基于fcitx的搜狗输入法。

- 项目地址： https://copr.fedoraproject.org/coprs/mosquito/myrepo/
- 支持的发行版： Fedora 19/20/21/rawhide 以及RHEL/CentOS 7

::

    $ yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo/repo/epel-7/mosquito-myrepo-epel-7.repo

安装搜狗输入法
==============

安装
----

::

    $ yum install sogou-pinyin sogou-pinyin-skins

配置
----

首先关闭gnome-shell 对键盘的监听，然后切换输入法为fcitx::

    $ gsettings set org.gnome.settings-daemon.plugins.keyboard active false
    $ imsettings-switch fcitx

似乎需要重启，或者退出用户重新登陆。

安装其他输入法
==============

搜狗输入法基本够用了，也可以安装其他中文输入法::

    $ yum install fcitx-googlepinyin fcitx-cloudpinyin # 谷歌拼音输入法
    $ yum install fcitx-rime fcitx-cloudpinyin # 中州韵输入法
    $ yum install fcitx-libpinyin fcitx-cloudpinyin # libpinyin输入法
    $ yum install fcitx-sunpinyin sunpinyin-data fcitx-cloudpinyin # sunpinyin输入法


参考
====

- https://copr.fedoraproject.org/coprs/mosquito/myrepo/

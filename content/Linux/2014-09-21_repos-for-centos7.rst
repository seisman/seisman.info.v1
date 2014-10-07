CentOS7下的第三方源
###################

:author: SeisMan
:date: 2014-09-21
:modified: 2014-10-07
:category: Linux
:tags: CentOS
:slug: repos-for-centos7

.. contents::

CentOS是Red Hat Enterprise Linux的衍生版本，以稳定著称，其官方源（base、updates）中软件种类相对较少，版本相对较老。有些时候想要安装官方源中未提供的一些软件，则需要使用第三方源。这里列出我正在使用的第三方源。

EPEL7
=====

EPEL全称Extra Packages for Enterprise Linux，是一个由Fedora特别兴趣小组创建、维护并管理的，针对红帽企业版Linux（RHEL）及其衍生发行版（比如CentOS、Scientific Linux、Oracle Enterprise Linux）的一个高质量附加软件包项目。EPEL的软件包通常不会与官方源中的软件包发生冲突，因而可以放心使用。

项目主页： https://fedoraproject.org/wiki/EPEL

添加方法::

    wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm
    sudo rpm -ivh epel-release-7-2.noarch.rpm
    sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

Google Chrome
=============

Google repo包含了三个软件，即\ ``google-chrome-stable``\ 、\ ``google-chrome-beta``\ 和\ ``google-chrome-unstable``\ ，因而不会与其他源产生冲突。

在\ ``/etc/yum.repo.d/``\ 目录下新建repo文件\ ``google-chrome.repo``\ ，向其中添加如下内容即可::

    [google-chrome]
    name=google-chrome
    baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
    enabled=1
    gpgcheck=1
    gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub

RepoForge
=========

原名为rpmforge，包含了一些EPEL中没有的软件包，当然也有部分软件包与EPEL存在冲突::

    wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm
    sudo rpm -ivh rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm

在安装该源中的软件包时应格外注意软件包的依赖包，以尽可能避免版本冲突。另外，平常建议禁用该源。

mosquito-myrepo-epel-7
======================

私人第三方repo，该repo依赖于EPEL。

- 项目主页： https://copr.fedoraproject.org/coprs/mosquito/myrepo/
- 软件列表

  - pidgin-lwqq：使用WebQQ协议编写的pidgin-QQ插件
  - pidgin-openfetion：使用fetion v4协议编写的pidgin飞信插件
  - pidgin-sendscreenshot：pidgin截图插件
  - wiz-note：为知笔记
  - sogou-pinyin：搜狗拼音输入法，基于fcitx框架开发
  - sogou-pinyin-skins：搜狗拼音输入法皮肤
  - fcitx-googlepinyin：基于fcitx框架的谷歌拼音输入模块
  - fcitx-rime：中州韵输入法
  - fcitx-libpinyin：基于fcitx框架的libpinyin 输入法
  - fcitx-sunpinyin：基于fcitx框架的sunpinyin 输入法
  - fcitx-configtool, kcm-fcitx：GTK和KDE下的fcitx 配置工具
  - openyoudao：一个python编写的有道词典linux客户端

添加方法::

    yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo/repo/epel-7/mosquito-myrepo-epel-7.repo



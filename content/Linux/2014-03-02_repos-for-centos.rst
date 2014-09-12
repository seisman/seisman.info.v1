CentOS下的非官方源
##################

:author: SeisMan
:date: 2014-03-02
:category: Linux
:tags: CentOS
:slug: repos-for-centos

CentOS以稳定著称，其官方源中软件种类相对较少，版本相对较老。因而需要其他一些非官方源的支持。

具体CentOS下可以使用哪些源，可以在\ http://pkgs.org/\ 查看，其中比较常用的源是EPEL源和Repoforge(RPMforge)源。

EPEL
====

对于CentOS 6 x86_64::

    $ wget -c http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
    $ rpm -Uvh epel-release-6-8.noarch.rpm

RPMforge
========

对于CentOS 6 x86_64::
    
    $ wget -c http://apt.sw.be/redhat/el6/en/x86_64/rpmforge/RPMS/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
    $ rpm -Uvh rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm

不同的源之间可能有相同或相似的软件，因而可能存在冲突，所以需要解决冲突问题，这需要使用到yum的priorities插件，具体参考 http://www.ha97.com/2626.html

鉴于在安装netcdf时两个源中的netcdf版本会导致众多问题，因而建议只使用EPEL源。若使用rpmforge源，最好在安装完需要的软件包之后将其禁用。

Hinet配置检查脚本
#################

:date: 2016-03-07
:author: SeisMan
:category: 地震学基础
:tags: Hinet, Python
:slug: hinetdoctor

``HinetDoctor.py`` 是 `HinetScripts <https://github.com/seisman/HinetScripts>`_ 项目中的一个Python脚本。

该脚本主要有如下功能：

#. 检查Python版本是否大于3.3
#. 检查是否已安装所有依赖
#. 检查配置文件是否可正常读取
#. 检查账号密码是否正确，或是否可以正常登陆
#. 检查Hinet网站是否有更新，若网站有更新，而脚本未更新，则脚本可能失效
#. 检查win32tools中的 ``catwin32`` 和 ``win2sac_32`` 是否可以被正常调用
#. 检查已选中的Hinet和Fnet的台站数目
#. 检查配置文件中 ``MaxSpan`` 是否符合要求

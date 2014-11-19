个人偏好列表
############

:date: 2014-08-05 20:00
:author: SeisMan
:category: 胡言乱语
:tags: Linux, Perl, Python
:slug: personal-preferences

.. contents::

本文记录我个人目前在使用的一些软件、工具、App，以及一些偏好。

- 操作系统：Linux > iOS > Android > Windows
- Linux发行版：CentOS 7.0
- 浏览器： Google Chrome
- 科学上网： `huhamhire-hosts`_ > `USTC LUG OpenVPN`_
- 输入法： 搜狗（Linux）
- 密码管理：LastPass（Linux版+Chrome插件+iOS客户端）
- 文件/目录比较工具： `meld`_ > `smartsynchronize`_ > vimdiff > diff
- 文献管理： `Mendeley`_
- 配色方案： `Solarized`_ （vim, terminal, PyCharm, Gedit）
- Windows下的SSH客户端: `Xshell Home/School`_

阅读与笔记
==========

- RSS阅读器： `feedly`_
- 稍后阅读： `Pocket`_ + Chrome书签
- 笔记类工具： `印象笔记`_ + `马克飞象`_
- 清单管理： `Wunderlist`_

编程语言
========

- 高级编程语言： C > Fortran
- 脚本语言： Python3 > Perl > Bash
- 其他：LaTeX, reStructureText, Markdown

Shell
=====

大多数Linux自带的shell都是bash，我也用了好几年，直到遇到了zsh，才知道原来shell也可以玩出花样来。

zsh基本是兼容bash的，但是相对于bash而言提供了更多更方便的功能，具有很强的可配置性。一般用户折腾zsh的配置就没有必要了，直接用\ `oh my zsh <https://github.com/robbyrussell/oh-my-zsh>`_\ 就好。

阅读器
======

- PDF阅读器： evince > `zathura`_
- PS阅读器： `zathura`_ > gs > gv > evince

网盘
====

同步类网盘
----------

在CentOS下有客户端的同步类网盘应该只有两个，\ `坚果云`_\ 和\ `Dropbox`\ 。Dropbox算是最优秀的同步网盘，可惜在国内被墙了，同步起来很纠结。坚果云是不错的替代品，同步速度也不错。

目前的策略是在CentOS下同时使用坚果云和Dropbox。将需要同步的文件放在\ ``~/Nutstore``\ 目录下，然后在\ ``~/Dropbox``\ 目录下做指向\ ``Nutstore``\ 的软链接。（反过来是不可以的，因为Dropbox支持软链接，而Nutstore不支持软链接）。

备份类网盘
----------

坚果云也是不错的备份类网盘，每个月1G的上传流量，只适合备份小文件。

资源类网盘
----------

以电影资源为主，主要有百度云、360云盘和115网盘。

编辑器与IDE
===========

文本编辑器
----------

Vim > Gedit > Sublime Text 3

Python IDE
----------

`PyCharm Communitu Edition`_


版本控制
========

使用Git作为版本控制工具，svn之类的未接触过，也不打算接触。

源码分类托管在三个地方：

- `GitHub`_ ：博客源码以及可公开的代码
- `USTC GitLab`_ ：托管私有项目
- `GitCafe`_ ：仅用于托管博客，用于国内用户的访问

编程字体
========

#. `Source Code Pro`_

   试用中。各字符之间很容易区分，字体稍扁，正在适应中。

#. `Droid Sans Mono`_

   Droid Sans Mono是很好看的等宽字体，用了很长一段时间后发现了几个比较严重的问题。

   #. 难以数字0（zero）和大写字母O（oh）
   #. 中文的左引号（“）和右引号（”）无法区分

   虽然有修改版，将零修改为dotted版和dashed版，但使用过程中明显看到数字0的尺寸与其他数字尺寸有差，影响美观，故放弃该字体。


.. _Droid Sans Mono: https://www.google.com/fonts/specimen/Droid+Sans+Mono
.. _Dropbox: https://www.dropbox.com
.. _feedly: http://feedly.com/
.. _Git: http://git-scm.com/
.. _GitCafe: https://gitcafe.com
.. _GitHub: https://github.com/
.. _huhamhire-hosts: https://hosts.huhamhire.com
.. _LastPass: https://lastpass.com
.. _meld: http://meldmerge.org/
.. _Mendeley: http://www.mendeley.com/
.. _Pocket: http://getpocket.com/
.. _PyCharm Communitu Edition: http://www.jetbrains.com/pycharm/
.. _Raysnote: https://raysnote.com/
.. _smartsynchronize: http://www.syntevo.com/smartsynchronize
.. _Solarized: http://ethanschoonover.com/solarized
.. _Source Code Pro: https://github.com/adobe-fonts/source-code-pro
.. _USTC LUG OpenVPN: https://vpn.lug.ustc.edu.cn/
.. _USTC GitLab: https://gitlab.lug.ustc.edu.cn/
.. _Wunderlist: https://www.wunderlist.com/zh/
.. _Xshell Home/School: http://www.netsarang.com/products/xsh_overview.html
.. _zathura: http://pwmt.org/projects/zathura
.. _百度云: http://yun.baidu.com
.. _马克飞象: http://maxiang.info
.. _坚果云: https://jianguoyun.com
.. _印象笔记: https://www.yinxiang.com/

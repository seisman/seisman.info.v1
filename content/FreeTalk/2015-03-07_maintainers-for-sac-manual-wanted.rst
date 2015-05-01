征集《SAC参考手册》维护者
#########################

:date: 2015-03-07
:modified: 2015-03-14
:author: SeisMan
:category: 胡言乱语
:tags: SAC, 文档
:slug: maintainers-for-sac-manual-wanted

.. contents::

如题，希望能够征集到至少一人参与《SAC参考手册》的维护。

手册简介
========

SAC（Seismic Analysis Code）是地震学专业常用的数据处理软件之一，《SAC参考手册》是一本详细介绍SAC用法的中文电子书。2011年暑假，我尝试翻译了官方的英文文档，2012年初将其整理为PDF，并放在网络上免费下载，2012年至2015年的三年间，该手册不断更新，目前文档的最新版本为v3.1。

- 文档发布页：http://seisman.info/sac-manual.html
- 项目主页：https://github.com/seisman/SAC_Docs_zh

我为何不再维护
==============

自3.0版发布之后，我就已经有不再维护该手册的想法：

- 我对于SAC已经足够熟悉，日常使用过程中，没有阅读手册的需求，也就没有更新的动力；
- 进入博士阶段，科研的压力日益繁重，没有足够的时间和精力继续维护；

为何要征集维护者
================

#. SAC在接下来的几年之内都不会被淘汰，依然是地震学专业常用的数据处理软件之一；
#. 当SAC软件更新时，手册也需要及时更新；用着新版的软件却读着旧版的文档，谁也不知道什么时候会遇到一个坑；
#. 整个文档的主体部分我已经基本做完，维护者的负担不会太大；

需要维护的内容
==============

所谓的维护，主要包括如下几个方面：

#. 随着SAC软件新版本的发布，新增或更新手册中相应的内容；
#. 完善未讲清楚或易引起歧义的部分；
#. 修复错别字；
#. 增加日常数据处理过程中的一些SAC技巧；
#. 对于命令及用法，若不同版本间存在不兼容，则以最新版本的SAC为准，并在正文或脚注中适当提及版本间的差异。
#. 增加你认为值得加入的部分；
#. 文档整体布局的调整以及LaTeX源码的简化；

对维护者的最低要求
==================

#. SAC用户（SAC初学者）；
#. 操作系统以Linux为主；
#. 有时间和精力；
#. 了解LaTeX、Git的基础知识（至少愿意学习和了解）；

维护者可以得到什么
==================

维护者完全无偿工作，没有任何经济上的报酬（若是有机会，我可以请吃顿饭）。除此之外，维护者还可以得到如下一些虚无缥缈的东西：

#. 手册中会将你列为维护者，并留有邮箱；
#. 结识更多的SAC用户以及地震学同行；
#. 了解MarkDown和LaTeX的基础语法；
#. 学会使用Git，参与开源项目；

如何参与
========

若有意参与到该手册的维护，请参考如下步骤，过程中遇到问题可以在博客中留言或直接邮件联系我。

简单的说，参与该项目需要如下步骤：

#. 拥有Linux系统；
#. 拥有一个GitHub账户；
#. 安装TexLive以及中英文字体（可选）；
#. Fork手册源码，Clone至本地；
#. 修改源码，提交修改，并Push到自己的Repo里，再提交Pull Request；

维护者需要了解三个工具：Linux、Git和LaTeX。其中，对于Git的要求较高，其余两者没有太多要求。

关于如何利用LaTeX编译生成PDF，请参考项目主页里的README。

了解GitHub
----------

- `注册 <https://github.com/join>`_\ GitHub账户；
- 向GitHub账户中添加当前机器的SSH秘钥，参考“\ `GitHub官方文档 <https://help.github.com/articles/generating-ssh-keys/>`_\ ”。添加秘钥的目的是使得GitHub账户信任当前计算机，并赋予其\ **写**\ 权限；

安装和配置git
-------------

- git是版本控制工具，gitk是用于查看的图形工具::

    sudo yum install git gitk

- git全局配置::

    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"

第一次使用
----------

#. 进入该手册的\ `项目主页 <https://github.com/seisman/SAC_Docs_zh>`_\ ，点击右上角的fork；该操作会将\ ``seisman``\ 账户下的\ ``SAC_Docs_zh``\ 项目复制到你的账户下。下面均假定你的账户名叫\ ``USER``\ 。

#. 在终端执行如下操作::

       # 下载源码至本机
       git clone git@github.com:USER/SAC_Docs_zh.git

       # 添加seisman账户下的repo作为其中一个远程repo，并命名为seisman
       git remote add seisman https://github.com/seisman/SAC_Docs_zh.git

       # 用编辑器修改文档
       #   比如先修改contributor.tex文件，该文件中包括了该手册的维护者的列表
       #   参照已有的记录，添加自己的姓名/昵称、邮箱
       #   开始时间是你开始维护此手册的时间
       #   结束时间是你决定不再维护此手册的时间
       # 修改该文档后，按如下操作提交并推送修改
       git add contributor.tex           # 将修改的文件添加到缓存区
       git commit -m "add contributor"   # 提交修改，-m后接注释信息
       git push -u origin master         # 将修改推送到GitHub服务器

#. 进入 https://github.com/USER/SAC_Docs_zh\ ，点击Pull Request即可；
#. 提交完Pull Request之后，我会审核修改，并决定是否接受Pull Request；

第n次使用
---------

第一次使用的时候有些复杂，第n次使用的时候步骤就简单很多了。

命令行操作如下::

    # 从seisman的repo中拉取源码的最新版本
    git pull seisman

    # 将seisman的repo中的最新版本与本地版本合并
    git merge seisman/master

    #
    # 修改文件 xxx.0 xxx.1 xxx.2
    #

    # 添加到缓冲区
    git add xxx.0 xxx.1 xxx.2

    # 提交更改
    git commit -m 'commit messages'

    # 推送更改到服务器
    git push

Push之后，进入GitHub网站，提交Pull Request即可。

其他说明
--------

- 我对于Git也只是了解皮毛，上面的步骤也许有更简单的操作；
- 使用Git进行协作的方式有好几种，文中说的是比较常用的一种方式；
- `git简易指南 <http://www.bootcss.com/p/git-guide/>`_
- `廖雪峰的Git教程 <http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000>`_
- 可以多次\ ``add``\ 多次再\ ``commit``\ ，多次\ ``commit``\ 再\ ``push``\ ，多次\ ``push``\ 之后再pull request；

总之，希望有人能够参与进来，哪怕只是改几个错别字也是极好的。

如何维护
========

在前面提到了手册中有哪些东西需要维护，根据工作量的大小大致可以分为两类：

- 小工作量维护，比如修复简单的bug和typo、整理部分语句、微调LaTeX模板，可以直接修改并提交Pull Requests；
- 大工作量维护，比如新增章节、调整文档整体结构等，为了避免多人重复劳动，请先到\ `项目主页 <https://github.com/seisman/SAC_Docs_zh>`_\ 中提交Issues

  - 若暂时不打算解决该Issue，则设置标签为“Pull Request Welcomed”；
  - 若正在解决该Issue，则设置标签为“In Progress”；
  - Issue列表中所有标签为“Pull Request Welcomed”的Issue均可随意认领；

修订历史
========

- 2015-03-07：初稿；
- 2015-03-09：补充了参与维护的具体步骤；
- 2015-03-13：置顶本文；
- 2015-03-23：取消置顶；

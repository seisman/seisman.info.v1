SAC参考手册中文版
#################

:date: 2013-07-06 18:21
:modified: 2015-09-15
:author: SeisMan
:category: SAC
:tags: 书籍, PDF
:slug: sac-manual

.. contents::

征集《SAC参考手册》维护者，有意者点\ `这里 <{filename}/SAC/2015-03-07_maintainers-for-sac-manual-wanted.rst>`_\ ，长期有效。

3.5 dev版
=========

此文档使用Git进行版本控制，文档会不定期修复bug以及添加新内容。读者可以下载已定稿的3.4版或正在修订中的3.5-dev版。

注意：由于LaTeX本身的一些限制，3.5-dev版在新增内容的情况下，部分含图/表的页面在排版的时候可能会留出一些空白。我一般只会在某个正式版本发布之前整体检查一下排版情况，所以dev版的排版无法保证。

下载地址：\ `3.5-dev版 <http://home.ustc.edu.cn/~dongzhi/SAC_Docs.pdf>`_

2015-09-15 3.4版
================

下载地址：\ `SAC参考手册v3.4.pdf <http://7j1zxm.com1.z0.glb.clouddn.com/downloads/sac-manual-v3.4.pdf>`_

对于用户：

- 调整与修订：

  - 将命令的“错误消息”和“警告消息”集中整理到附录中
  - 将文件重命名脚本移动到“在脚本中调用SAC”一章
  - 重新整理了“震相拾取”一节的内容

- 新增内容：

  - 在Mac OS X 10.10中安装SAC
  - 在C程序中调用SAC提供的 ``distaz`` 函数
  - 数据处理中使用 ``decimate`` 和\ ``interpolate``\ 进行数据重采样
  - Python中修改发震时刻
  - 在C程序中读写SAC文件
  - 在Fortran程序中读写SAC文件
  - 在Python脚本中读写SAC文件
  - 在matlab中读写SAC文件
  - 修改SAC所能读取的文件数目的上限
  - 文档维护与更新并征集维护者

- 命令整理： ``mtw`` 、\ ``markptp``\ 、\ ``markvalue``\ 、\ ``readcss``
- 修正Bugs和Typos

对于维护者：

- 更新至TeXLive 2015
- CTeX宏包版本要求>=2.0
- listings宏包版本要求>=1.6
- 新增“文档维护与更新”一章以介绍文档维护的流程
- 使用longtable宏包处理跨页长表格
- 使用siunitx宏包处理数字与单位之间的间隙
- 小括号统一使用英文输入法下的半角括号，而不是中文输入法下的全角符号
- Tips环境改成note环境

2015-06-06 3.3版
================

下载地址: `SAC参考手册v3.3.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v3.3.pdf>`_

对于用户：

- 修正bugs和typos；
- 命令整理

    - ``hilbert``
    - ``transfer`` 与仪器响应

- 新增内容：

    - 四个文件重命名脚本
    - 读取某个目录下全部文件遇到的问题
    - 使用Tab遇到的问题
    - 数据命名规则
    - 时区校正
    - 错误与警告消息
    - 未定义变量
    - SAC debug
    - ``wh`` 与 ``w over``\ 的区别

对于维护者：

- 删除原来的所有Git提交；
- 精简Repo的尺寸；
- 删除了scons；

2015-05-02 3.2版
================

下载地址: `SAC参考手册v3.2.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v3.2.pdf>`_

对于用户：

- 修复bugs和typos；
- 命令整理：

  - `systemcommand`
  - `transfer`

- 新增内容

  - 波形排序
  - 标记震相理论走时的三种方法
  - 图像格式转换
  - SAC初始化宏文件
  - SAC命令的长度上限
  - 字节序
  - 新增附录“仪器响应”，整理了“去仪器响应”一节

- 新增示例

  - 调用SAC的Hilbert函数

对于维护者：

- 新增ChangeLog；
- 更新README，可根据说明自行编译源码生成PDF；
- 修改Makefile，对依赖的检测更加智能；
- 英文使用TeX默认字体；中文使用开源中文字体Fandol；
- 使用 ``minted`` 实现代码的语法高亮，替代\ ``listings``\ ；
- datetime宏包升级至datetime2；
- 简化了绘图脚本的Makefile；

2014-09-25 3.1版
================

下载地址: `SAC参考手册v3.1.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v3.1.pdf>`_

- 重新整理了大部分命令的语法说明；
- 对“SAC图像”一章进行了修订；
- 新增“信号迭加子程序”一章；
- 新增“谱估计子程序”一章；
- 新增“在Python中调用SAC”一节；
- Bug修订；

2014-04-18 3.0版
================

下载地址: `SAC参考手册v3.0.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v3.0.pdf>`_

- 重新设计了整个文档的结构
- 重写了教程部分的大多数内容
- 教程部分根据SAC v101.6a进行修正
- Bug修订

2014-02-22 2.3版
================

下载地址: `SAC帮助文档中文版v2.3.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v2.3.pdf>`_

- 使用Git管理源码
- 整理结构和布局的修改
- 新的小节: “SAC IO升级版”、“黑板变量的读写”、“SAC保存图像”
- Bug修订

2013-04-12 2.2版
================

下载地址： `SAC帮助文档中文版v2.2.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v2.2.pdf>`_  

命令已经整理完毕，排版上基本已经没有问题了，重新设计了封面，在接下来很长一段时间应该都不会有大的改动了。如果有时间，会加一些SAC其他方面的东西。如果有读者反馈，命令方面也可能会有更新。

2013-04-06 2.1版
================

下载地址： `SAC帮助文档中文版v2.1.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v2.1.pdf>`_  

重新细致整理了手册的第一章，基本达到了我认为可以打印的地步。命令部分还没有整，200多个，需要很长一段时间才能出来。

2013-03-29 2.0版
================

下载地址：\ `SAC帮助文档中文版v2.0.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v2.0.pdf>`_

花了两天的时间重新制作了整个文档，内容及排版部分有很多bug，草草结束是因为接下来的一段时间要好好干活了，先把v2.0的细节总结如下：

- 操作系统：CentOS 6.4 (Final)
- 编译环境：TeX Live 2012
- 编译命令：xeLaTeX
- 中文实现：CTEX宏包
- 中文字体：宋体+黑体
- 英文主字体：Liberation Sans
- 代码字体：Courier 10 Pitch

2012-09-18 1.2版
================

下载地址：\ `SAC帮助文档中文版v1.2.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v1.2.pdf>`_

- 增加了封面配图。

2012-09-03 1.1版
================

下载地址：\ `SAC帮助文档中文版v1.1.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v1.1.pdf>`_

- 重新格式化整个文档，使得其看上去更规范，也易于以后的修改；
- 文档中的所有C或Fortran代码从notepad++中直接导出，代码支持语法高亮；
- 代码及正文英文字体采用Consolas字体。
- 增加了“在脚本中调用SAC”一节；
- 新增了transfer、traveltime、saveimg、datagen命令（依赖于SAC v101.5c）；
- 公式用公式编辑器编辑

2012-01-08 1.0版
================

下载地址：\ `SAC帮助文档中文版v1.0.pdf <http://seisman.qiniudn.com/downloads/sac-manual-v1.0.pdf>`_

自学SAC是在2010年的寒假，看的是1995年出版的《数字地震波形分析》的电子版以及SAC自带的英文文档。《数字地震波形分析》大概是当时唯一一本介绍SAC的中文书，电子版很不清晰而且有些命令已经过时了。我一直希望能有一个新版本出现。

这个SAC中文手册最初翻译于2011年暑假，用了20天左右的时间，完成了大部分的翻译工作。这个版本主要参考了《数字地震波形分析》一书。包含了大部分的用户指南以及几乎全部的命令。这个版本的优点在于：

- 结合了SAC101.4版本，增加、删除和修改了一些命令；
- 更清晰；
- 增加了书签，方便定位，支持全文搜索。

这个版本的缺点在于：

- 与matlab引擎相关的几个命令未加入；
- SAC的两个子程序部分暂时还没有翻译；
- 由于没有时间和心思检查，中间可能会出现一些错误；
- 关于命令的简写还有一些细节没有做；
- 在某些linux版本下，pdf打开后看到的是完全颠倒的字（比如悲摧的CentOS...）希望这些可以在以后的版本中得到改善和加强。

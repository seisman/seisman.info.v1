SAC发展史及其版权
#################

:date: 2014-04-01 16:30
:author: SeisMan
:category: 胡言乱语
:tags: SAC
:slug: history-and-copyright-of-sac
:summary: 介绍SAC的历史以及版权问题       

.. contents::

发展史
======

Lawrence Livermore国家实验室和Los Alamos国家实验室是美国承担核武器设计工作的两个实验室。SAC 于20世纪80年代诞生于实验室的Treaty Verification Program小组里，该组由W. C. Tapley和Joe Tull共同领导。

起初，SAC是用Fortran语言实现的，并将源代码分发给感兴趣的学者，允许用户进行非商业性的地震数据处理，用户和维护者之间的合作协议要求用户提交bug修正和改进以换取SAC的使用权。到了大概1990年，SAC已经成为全球地震学家的数据处理标准软件。

从1992年开始，SAC的开发逐渐由Livermore接管，并开始通过分发协议严格限制源代码的分发。与此同时，开发者认为Fortran是一种过于局限的编程语言，其阻碍了SAC特性的进一步开发，因而开发者使用f2c转换工具将SAC的Fortran源码转换成了C源码。

接下来，Livermore以转换得到的C源码为基础，计划开发一个商业版的地震数据处理产品，命名为SAC2000。这个版本扩展了很多功能，其中一个功能是建立一个日志数据库，记录一个波形从原始数据到最终产品之间的所有处理步骤。这样的设计允许用户暂时保存数据处理步骤，随时将处理的结果提交到内存或回滚到之前的状态。

约1998年，IRIS意识到，SAC的核心用户群(主要是IRIS的成员)无法确保能够获取SAC的源码。IRIS开始和Livermore协商，希望将SAC的开发分成两条线:一个包含数据库特性，供核监测机构使用;另一个不包含数据库特性，仅供学术机构使用。商业化的努力主要集中在含数据库功能的版本上。

终于，在2005年，IRIS与Livermore签订了合同，Livermore提供给IRIS一个SAC协议，允许在IRIS社区内部分享SAC/SAC2000的源代码，并提供有限的支持以促进社区的发展。而学术圈对于商业版的SAC没有太大兴趣，因而Livermore逐渐撤出了对于SAC2000的支持。最终IRIS完全接手了SAC的开发和技术支持，并成为了一个新的版本，也就是我们现在正在使用的SAC。

版权
====

根据IRIS与Livermore的协议，只有IRIS可以分发SAC二进制包以及源码包，任何其它的分发都是不合法的。

昨日，在SAC邮件组里，有人提了一个问题，附件中附带了SAC的源码包，于是IRIS给出了如下警告。

    The distribution of SAC is done by IRIS under an agreement we have with LLNL of the US Department of Energy and the University of California.  The distribution of SAC is limited and  does not allow you to redistribute SAC at all.  In your email to the SAC-HELP list you attached the the distribution of SAC which violates the license agreement that you accepted when you requested SAC,.

    I am copying the SAC-HELP list as well to insure that all subscribers are aware of the limitation of SAC that  is in place. No one other than IRIS should ever redistribute SAC to anyone including a broadcast distribution to a email list server.

    Please take care in following the license conditions that you agreed to or we could lose the ability to distribute SAC to anyone in the future.  I will notify LLNL of this infraction.

私人分发SAC源码的最严重后果是：用户违背了申请SAC时的agreement，IRIS违反了与LLNL签订的协议，LLNL不再允许IRIS分发SAC源码，SAC软件就此没了。

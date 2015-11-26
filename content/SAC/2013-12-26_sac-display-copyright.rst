脚本中调用SAC时不显示版本信息
#############################

:date: 2013-12-26 20:52
:author: SeisMan
:category: SAC
:tags: SAC技巧
:slug: sac-display-copyright

在终端使用SAC时默认会出现版本信息，如下::

 $ sac
 SEISMIC ANALYSIS CODE [11/11/2013 (Version 101.6a)]
 Copyright 1995 Regents of the University of California

 SAC>

若在SAC宏文件或者bash、perl脚本中多次调用SAC命令的话，则会重复出现版本信息，严重干扰了宏文件或脚本的输出，对于用户来说是很糟糕的体验。

版本信息的显示由环境变量SAC_DISPLAY_COPYRIGHT来控制，其可以取值为0或1，其中1代表显示版本信息（默认值），0代表不显示版本信息。

在Bash脚本中，可以这样写::

 SAC_DISPLAY_COPYRIGHT=0

在Perl脚本中，可以这样写::

 $ENV{SAC_DISPLAY_COPYRIGHT} = 0 ;

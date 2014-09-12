SAC ERROR 1303: Overwrite flag is not on for file
#####################################################

:date: 2013-10-07 10:55
:author: SeisMan
:category: SAC
:tags: SAC技巧
:slug: sac-error-1303-overwrite-flag-is-not-on-for-file

在修改SAC头段或者对SAC数据进行处理之后，想要将头段或处理结果写入原文件，有时会出现如下错误：

    ERROR 1303: Overwrite flag is not on for file xxx

SAC头段中有这样一个变量LOVROK，若其为false则文件不可被覆盖，类似于用户没有写权限，这应该算是一种数据保护机制。

因而只要

::

    SAC> ch lovrok true

文件则可以被修改了。

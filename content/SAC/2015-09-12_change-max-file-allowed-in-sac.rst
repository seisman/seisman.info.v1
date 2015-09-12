修改SAC所允许的最大文件数目
###########################

:date: 2015-09-12
:author: SeisMan
:category: SAC
:tags: SAC技巧
:slug: change-max-file-allowed-in-sac

SAC在处理数据时，一次性最多只能读入1000个SAC文件。当读入过多的SAC文件时，会出现如下警告::

    Max files: reading first 1000  files.

并只读入文件列表中的前1000个文件。

想要突破最多只能读1000个文件的上限，就需要修改SAC的源代码。

最大文件数目由源码\ ``sac/inc/mach.h``\ 中的宏变量\ ``MDFL``\ 控制。将其中的::

    #define MDFL    1000

改成::

    #define MDFL    10000

即可将最大文件数目修改成10000。

修改之后，重新编译安装即可。

简单测试了一下，修改后的确可以读取超过1000个文件，基本的数据处理命令也没有问题，但尚不确定是否有其他副作用。

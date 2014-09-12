Hi-net生成仪器响应SAC PZ文件
#############################

:author: SeisMan
:date: 2014-09-13 01:00
:category: 地震学基础
:tags: Hinet, 仪器响应, Python
:slug: hinet-convert-channel-table-to-sac-pz-file

前文\ `Hinet仪器响应 <{filename}/SeisBasic/2014-09-06_hinet-instrumental-response.rst>`_\ 中介绍了Hi-net的仪器响应的详细信息。据此，用Python写了一个脚本，将Hi-net的Channel Table文件转换为常用的SAC PZ文件。

脚本位于：\ `ch2pz.py <https://github.com/seisman/HinetScripts/blob/master/ch2pz.py>`_\ 。

用法
=====

::

    Convert Hi-net Channel Table file to SAC PZ files

    Usage:
        ch2pz.py CHFILE [-C <comps>] [-D <outdir>] [-S <suffix>]

    Options:
        -C <comps>      Channel Components to convert. Choose from U,N,E,X,Y.
                        [default: UNE]
        -D <outdir>     Output directory of SAC PZ files. Use the directory of
                        Channel Table file as default.
        -S <suffix>     Suffix for SAC PZ files. [default: SAC_PZ]

说明
=====

参考\ `Hi-net WIN32转SAC <{filename}/SeisBasic/2014-09-12_hinet-convert-win32-files-to-sac.rst>`_\ 一文中对选项的解释。

Hi-net win32tools
#################

:date: 2014-09-07
:modified: 2014-12-01
:author: SeisMan
:category: 地震学基础
:tags: Hinet, 格式转换
:slug: hinet-win32tools

.. contents::

从Hi-net获取的波形数据为不常见/用的WIN32格式，Hi-net提供了win32tools来实现波形数据的基本处理和转换。

下载
====

下载地址：http://www.hinet.bosai.go.jp/REGS/manual/dlDialogue.php?r=win32tools

直接解压编译即可。

Tools
======

win32tools中包含了一系列用于数据处理的命令。

catwin32
--------

``catwin32``\ 可以合并两个或多个WIN32文件，一般用于将\ **多个一分钟**\ 的文件合并\ **一个多分钟**\ 的文件。

用法::

  catwin32 File_1 File_2 ... File_n [-oOutFile | -o OutFile] [-s] [-h]
        File_n        : Input WIN32 file name
                      : You may use a wild word character.
        OutFile       : Output WIN32 file name
        -s            : Sort by date
        -h            : This usage print

示例::

    catwin32 20140830000*.cnt -o 2014083001.cnt

上面的示例中，会将201408300000*.cnt文件合并成2014083001.cnt文件。若数据存在缺失，比如，缺少某些分钟的数据，或者某分钟内缺失若干秒的数据，则在使用win2sac_32将WIN32数据转换为SAC格式时，会自动对缺失的数据进行补领，因而不必担心数据缺失的问题。

关于\ ``-s``\ 选项，需要注意一下的用法：

- 无\ ``-s``\ 的情况下，\ ``catwin32``\ 会将所有的WIN32文件，按照\ **文件在参数列表中的顺序**\ 合并在一起。
- 有\ ``-s``\ 的情况下，\ ``catwin32``\ 会检查所有WIN32文件的起始时间，按照\ **文件的起始时间的顺序**\ 合并在一起。

比如::

    catwin32 201408300001.cnt 201408300002.cnt -o 2014083001_2.cnt
    catwin32 201408300002.cnt 201408300001.cnt -o 2014083001_2.cnt
    catwin32 201408300002.cnt 201408300001.cnt -o 2014083001_2.cnt -s

该例中，第一种方法是对的；第二种方法是错误的；第三种方法加上了“-s”选项是对的；

在bash下，形如\ ``20140830000*.cnt``\ 这样的通配符，会将当前目录下符合的所有文件按照文件名的顺序排序，并作为catwin32的参数，在默认的情况下，按文件名排序与按文件起始时间排序是等效的，但存在一些特殊的情况：

#. 自定义了cnt文件的文件名，此时在bash下用通配符得到的文件顺序不一定是按照时间排序的；
#. python中的\ ``glob.glob()``\ 函数，默认返回的文件顺序是乱序的，需要使用\ ``sorted()``\  函数；

因而，在确保参数列表中文件顺序正确的前提下，不需要使用“-s”选项；反之，则必须使用“-s”选项，否则在执行win2sac_32命令时会出现“The time is not sort.”的错误。但，加入了“-s”选项后，由于需要检查每个cnt文件的起始时间，并按起始时间对数据进行排序，因而会影响到数据合并的速度，尤其是在需要合并大量cnt文件的时候。

win2sac_32
-----------

``win2sac_32``\ ：主要用于将WIN32格式转换为SAC格式。除此之外，还可以对数据进行重采样，以二进制或ASCII形式输出

用法
~~~~

::

    win2sac_32 winfile ch_no sacfile [outdir] [-p(prmfile)]
        [-e] [-b[BIN]] [-a[ASC]] [-r(RATIO)] [-m(PMAX)]

对选项的说明
~~~~~~~~~~~~

- winfile：WIN32格式的数据文件
- ch_no：通道号列表，多个通道号之间以逗号分隔，也可以使一个包含一系列通道号的文件名；比如\ ``4CC4``\ 或\ ``4CC4,4F73``\ 或\ ``chno.file``\ 。
- sacfile：SAC输出文件的扩展名
- outdir：SAC文件的输出目录。若未指定或指定为“-”，则输出到当前目录
- p选项：指定参数文件名prmfile；若未使用该选项，则参数文件名默认为“win.prm”。关于参数文件的格式，在下面会介绍。
- e选项：设定输出SAC二进制文件的字节序，若不指定该选项，则输出的SAC二进制文件总是big endian；若指定该选项，则输出SAC二进制文件的字节序由当前机器的字节序决定；
- b选项：将数据以二进制形式输出，BIN为文件扩展名，在不指定的情况下，默认为“bin”
- a选项：将数据以ASCII形式输出（即单列数据），ASC为文件扩展名，在不指定的情况下，默认为“asc”
- r选项：对输出文件的数值乘以某常数RATIO，在不指定的情况下，默认值为1.0（？）
- m选项：指定最大数据点数，默认值为200万；若win32文件中包含的数据点数超过该值，则报错。比如，一个win32数据中包含了所有台站一天的数据，即每个通道分别有24*60*60*100=8640000个点，超过默认最大点数2000000，则此时需要使用\ ``-m``\ 选项增大最大数据点数。

输出文件名格式
~~~~~~~~~~~~~~

输出文件名格式为\ ``XXXX.Y.ZZZ``\ ，其中\ ``XXXX``\ 为台站代码，\ ``Y``\ 为分量代码，\ ``ZZZ``\ 为BIN或ASC或sacfile所指定的值。

输出文件的SAC的头段信息
~~~~~~~~~~~~~~~~~~~~~~~

该命令在生成SAC文件的同时会将相关信息写入SAC头段中，具体如下：

- npts, b
- leven
- ievtyp, idep
- nzyear, nzjday, nzhour, nzmin, nzsec, nzmsec
- kstnm, kcmpnm, knetwk, cmpaz, cmpinc, stla, stlo, stel
- kevnm

PS：生成的SAC文件中头段e为未定义值。

参数文件prmfile格式
~~~~~~~~~~~~~~~~~~~

在标准的prmfile中，有16个记录行。但win2sac_32程序仅使用第二行和（至？）第四行；

#. 行1：数据文件winfile所在目录
#. 行2：channel table文件
#. 行3：台站组文件名
#. 行4：pick文件所在目录
#. 行5：hypomh程序
#. 行6：hypomh所使用的速度结构
#. 行7：map data file
#. 行8：cut-out wave data输出目录
#. 行9：数据格式（B4/B2/L4/L2）
#. 行10：滤波设置文件
#. 行11：打印机...
#. 行12：upper/lower 半球投影
#. 行13：NOISE, FAR...
#. 行14：hypocenter数据所在目录
#. 行15：打印机DPI
#. 行16：临时工作目录

因而一般来说，在使用win2sac_32时需要创建文件“win.prm”，其内容为::

    .
    ./01_01_20140830.euc.ch
    .
    .

其中第二列为数据对应的channel table文件。

示例
~~~~

::

    win2sac_32 2000082404000101VM.cnt 4c55,4c65 sac ./sacdir -pwin.aaa.prm 1>ww.tmp

dewin_32
---------

``dewin_32``\ 从WIN32格式文件中取出指定通道的数据。

用法::

    usage: dewin_32 [-m] [-s samp] [-c] [-a] [-n] [-e extend] [-f filter_file] ch_no [input_file]
            -m  Win file is minutes file.
            -s  [samp] sampling number.
            -c  character output
            -a  audio format (u-law) output
            -n  not fill absent part
            -e  [extend] file extend name
            -f  [filter_file] filter paramter file
         ch_no  channel no.(in hex.) or channel no. file name
         input_file  input win file(default=stdin)

下面解释一下几个比较重要的选项：

- input_file：输入文件，为WIN32格式；
- ch_no：要提取的通道号列表，多个通道号之间以逗号分隔，也可以是一个包含一系列通道号的文件名；比如\ ``4CC4``\ 或\ ``4cc4,4f73``\ 或\ ``chno.file``\ 。
- c选项：表示将数据以字符形式输出，即单列数据；
- e选项：默认情况下，输出到标准输出；当指定多个通道时，标准输出会比较混乱，因而需要输出到文件中，该选项指定输出文件的扩展名；

几个不重要的选项：

- a选项：表示将数据以音频格式输入（参见\ `u-law <http://www.wikiwand.com/en/%CE%9C-law_algorithm>`_\ ）
- n选项：若数据存在缺失，默认情况下补零输出，该选项不对缺失部分补零。
- m、s选项：不是太理解，似乎都是用于数据缺失时，应该不重要；
- f选项：后接滤波参数文件，以对输出的数据进行滤波，一般用不到；

示例::

    dewin_32 -e dwn -c 4CC4,5B35 -m 2003070507400101VM.cnt
    dewin_32 -e dwn -c -n ch.lst < 2003070507400101VMs.cnt
    dewin_32 -c -n 5b35 < 2003070507400101VMs.cnt > ww5b35.dat


其他
----

下面的一些工具应该是很少用到的：

- ``wadd_32``\ ：合并两个WIN32数据，与catwin32有些类似，但在细节上有区别。具体不知。一般用不到。
- ``wch_32``\ ：从WIN32文件中提取指定通道号的数据并写入到新的WIN32文件中
- ``wck_32``\ ：似乎是用于检查WIN32文件的。
- ``w32tow1``\ ：WIN32格式转换为WIN格式（WIN32格式是根据WIN格式修改得到的）
- ``wed_32``\ ：用于编辑WIN32文件
- ``wchch_32``\ ：修改通道号

小结
====

在win32tools提供的9个工具中，最常用的有两个：\ ``catwin32``\ 和\ ``win2sac_32``\ ，其中前者用于合并数据，后者用于格式转换。

修订历史
========

- 2014-09-07：初稿；
- 2014-11-03：``catwin32``\ 命令要使用\ ``-s``\ 选项；
- 2014-11-14：加入了“生成的SAC文件的头段信息”一节；
- 2014-12-01：对\ ``-s``\ 选项的理解错误，该选项只会对文件按照起始时间排序，不会影响到数据的补零；

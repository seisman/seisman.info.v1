GMT修改默认参数
###############

:date: 2013-08-04 15:00
:author: SeisMan
:category: GMT
:tags: GMT4, GMT技巧
:slug: modify-default-parameters

GMT的默认参数文件为 ``.gmtdefaults4`` ，其系统默认值位于文件 ``$GMTHOME/share/conf/gmtdefaults_SI`` 中。GMT查找参数文件的顺序是

::

    ./gmtdefaults4 > ~/.gmt/.gmtdefaults4 > ~/.gmtdefaults4

GMT手册中给出了修改GMT参数的几种方法，具体总结起来如下：

#. 在单个命令行上使用“+filename”这样的语法来指定要使用的参数文件，该法仅对当前命令有效。
#. 将要使用的参数文件.gmtdefaults4拷贝到当前路径，执行相关绘图命令，然后删除该参数文件，这要求写脚本时要特别小心。
#. 通过gmtset命令显式修改参数，具体参见gmtset的manual
#. 在命令行上直接显式修改单个参数，仅对当前命令有效
#. 使用GMT的isolation模式，将所有的参数文件存储到临时目录中

可以将上面的5种方法分成三类：

-  法1和法4为一类，都是在当前命令上加参数修改，效果仅限于当前命令，不同之处仅在于一个指定文件一个指定参数
-  法2和法5都是使用临时参数文件，不同之处在于法2需要将参数文件拷贝到当前目录，法5则在指定的临时目录中直接读取参数文件
-  法3很特别，其修改了当前路径下的参数文件（或者新建），这会带来一个潜在的问题：假若在一个脚本中，你首先执行了一堆命令，这个时候使用GMT默认的参数文件，然后使用gmtset修改了参数，再继续执行另外几个命令，当整个脚本执行结束之后，当前路径下的.gmtdefaults是已经被修改后的参数文件了，因而当你再次执行这个脚本的时候，前面执行的一堆命令将会读取当前路径下的参数文件（即读取已经被修改的那个，而实际上它们需要的是GMT系统参数文件）。当你没有意识到这个问题的时候，你可能会莫名其妙的得到奇怪的结果。所以一个比较好的做法是在脚本结束时删除当前路径下的参数文件。

个人感觉，GMT参数设计的不够合理。isolation模式不错，但是总觉得用起来不是那么方便，gmtset这里也容易产生问题。比较合理的解决办法是用gmtset，然后在脚本结束的时候删除当前路径下的参数文件。

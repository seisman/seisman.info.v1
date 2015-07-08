GMT之gmtset与gmtget
####################

:date: 2013-08-15 17:16
:author: SeisMan
:category: GMT
:tags: GMT命令, GMT4
:slug: gmtset-gmtget

gmtset用于修改当前目录下的.gmtdefaults4文件中的GMT参数，如果没有该文件，则会先创建。由于gmtset会修改当前目录下的参数文件，所以这个修改对接下来的命令都是有效的。在一个脚本中，首先执行了一些命令，然后gmtset修改了参数，再执行几个命令，这些绘制出自己想要的效果。但是当你再次执行该脚本时，由于当前目录下已经存在.gmtdefaults4文件，且参数已经被修改，绘制出的图可能不是你想要的效果。可以在脚本的结尾通过gmtset将参数改回原值或者直接删除.gmtdefaults4来避免这种情况。

gmtget用于获取当前目录下的.gmtdefaults4中的参数值，其本质上是一个shell脚本，内容如下：

.. code-block:: bash

 #!/bin/sh
 #
 # gmtget - Return the current setting of the specified parameter
 #
 if [ ${#} -ne 1 ]; then
 echo "usage: gmtget PARAMETER" >&2
 exit -1
 fi
 gmtdefaults -L | grep "^${1} " | awk '{print $3}'

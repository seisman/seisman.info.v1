GMT网格数据之grdraster.info
############################

:date: 2013-08-10 00:05
:author: SeisMan
:category: GMT
:tags: GMT4, GMT5, 数据, 网格
:slug: grdraster-info-of-gmt-grid
:summary: 介绍如何修改grdraster.info

GMT可以绘制各种各样的地图，只要有网格数据，就可以在地图上叠加地形、海洋深度、重力、地磁等等彩色图像。

一般来说是从一个网格数据文件中利用grdraster命令抽取研究区域的网格数据，再用grdimage等命令绘制。一切绘制的前提是GMT可以找到各种各样的网格数据文件。

在GMT/share/dbase是储存数据文件的地方，grdraster.info包含了这些数据文件的信息。grdraster.info中的每一条分别代表一个网格数据，其格式如下：

::

    file_number "title string" "z units" -R -I GorP type scale offset NaNflag filename [L|B] [H<bytes>]

-  file\_number : 文件号，为整数，分别对应每个文件；
-  title\_string : 对数据的简单描述，需要用引号；
-  z\_unit : 数据在经过比例缩放和偏移之后的单位；
-  -R : 网格代表的区域范围，参见GMT的-R；
-  -I : 网格横向和纵向采样间隔，参见GMT的-I；
-  G或者P：代表两种Grid和Pixel两种网格方式，具体参见GMT网格的说明，其后可接G（表示地理坐标）或C（表示笛卡尔坐标）；
-  type : 可以取b（位数据，非0即1）、u（无符号字符类型）、c（有符号字符类型）、d（无符号两位整型）、i（有符号两位整型）、l（有符号四位整型）
-  scale：读取网格文件之后需要乘以scale才是真实值；
-  offset：读取网格文件，并乘以scale之后需要加上的值；
-  NaNflag：网格文件中无值的点怎样表示，若所有点都有值，则为none
-  filename：网格文件名，若以“/”开头则代表绝对路径，否则代表$(GMT\_GRIDDIR)/filename
-  L \| B ：网格文件的字节序，若你的系统和该网格数据字节序不同，则命令会自动进行转换。参见big-endian和little-endian；
-  H：如果网格文件前有头段，则给出头段的字节数。

下面给出一个例子：

::

    1 "ETOPO5 global topography"  "m"  -R0/359:55/-90/90 -I5m  GG i 1  0 none  etopo5.i2

这是全球地形网格数据，间隔为5分，单位为m，数据为有符号两位整型。

这些网格数据都需要自己寻找，下载以及格式转换。

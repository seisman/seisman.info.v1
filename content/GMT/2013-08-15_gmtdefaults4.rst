GMT之gmtdefaults
################

:date: 2013-08-15 17:14
:author: SeisMan
:category: GMT
:tags: GMT命令, GMT4
:slug: gmtdefaults4

.. contents::

前言
====

GMT中存在很多默认参数，这些参数会影响最后的绘图效果。gmtdefaults命令可以给出系统默认的参数以及用户自己的当前参数。关于GMT如何修改参数，可以看另一篇博文。

命令及选项
==========

:: 

 gmtdefaults 4.5.9 [64-bit] - List GMT default parameters to stdout

 usage: gmtdefaults [-D[s|u] | -L]

 -D prints the default settings for the GMT system.
 Append s to see the SI version of defaults.
 Append u to see the US version of defaults.
 -L prints the users current GMT default settings.

命令和选项很简单，-D和-L一个是打印系统参数，一个打印用户自定义参数。

默认参数
========

绘图介质参数：

-  PAGE\_COLOR = white  #纸张的背景色，不能透明
-  PAGE\_ORIENTATION = landscape # portrait或landscape
-  PAPER\_MEDIA = a4 #纸张大小

底图注释参数：

-  ANNOT\_MIN\_ANGLE = 20 #在倾斜投影中，若地图边界与注释的基线夹角小于该值，则无注释。在一般投影中地图边界与注释基线垂直
-  ANNOT\_MIN\_SPACING = 0  #相邻注释之间的最小距离
-  ANNOT\_FONT\_PRIMARY = Helvetica  #主注释字体，系统自带35种
-  ANNOT\_FONT\_SIZE\_PRIMARY = 14p  #主注释文字大小
-  ANNOT\_OFFSET\_PRIMARY = 0.2c  #主注释与刻度之间的距离
-  ANNOT\_FONT\_SECONDARY = Helvetica #次注释字体
-  ANNOT\_FONT\_SIZE\_SECONDARY = 16p #次注释大小
-  ANNOT\_OFFSET\_SECONDARY = 0.2c #次注释的底部与主注释顶部的距离
-  DEGREE\_SYMBOL = ring   #如何表示度这个符号
-  HEADER\_FONT = Helvetica # 标题字体
-  HEADER\_FONT\_SIZE = 36p #标题大小
-  HEADER\_OFFSET = 0.5c #标题与上边界的距离
-  LABEL\_FONT = Helvetica  #
-  LABEL\_FONT\_SIZE = 24p #
-  LABEL\_OFFSET = 0.3c #
-  OBLIQUE\_ANNOTATION = 1 #
-  PLOT\_CLOCK\_FORMAT = hh:mm:ss #绘图时间格式
-  PLOT\_DATE\_FORMAT = yyyy-mm-dd #绘图日期格式
-  PLOT\_DEGREE\_FORMAT = ddd:mm:ss #绘图度格式
-  Y\_AXIS\_TYPE = hor\_text  # y轴注释水平还是垂直

底图布局参数

-  BASEMAP\_AXES = WESN  #控制在哪条边上注释
-  BASEMAP\_FRAME\_RGB = black  #底图frame颜色
-  `BASEMAP\_TYPE <{filename}/GMT/2013-08-25_gmt-basemap-type.rst>`_ = fancy  # inside会把注释和刻度放在图内部，graph用于线性投影，在坐标轴上加箭头，plain是最一般的类型,fancy是画地图常见的黑白相间的边框
-  FRAME\_PEN = 1.25p  # plain frame的宽度
-  FRAME\_WIDTH = 0.2c #fancy frame的宽度
-  GRID\_CROSS\_SIZE\_PRIMARY = 0c #主注释经纬度交线处十字叉的尺寸，0表示连续的网格线
-  GRID\_PEN\_PRIMARY = 0.25p # 线的宽度
-  GRID\_CROSS\_SIZE\_SECONDARY = 0c  #
-  GRID\_PEN\_SECONDARY = 0.5p #
-  MAP\_SCALE\_HEIGHT = 0.2c  # 地图scale的高度
-  POLAR\_CAP = 85/90 #控制两极地区网格线
-  TICK\_LENGTH = 0.2c #tickmark的长度
-  TICK\_PEN = 0.5p  #tickmark的宽度
-  X\_AXIS\_LENGTH = 25c
-  Y\_AXIS\_LENGTH = 15c
-  X\_ORIGIN = 2.5c # 绘图相对于纸张左下角的X距离
-  Y\_ORIGIN = 2.5c #
-  UNIX\_TIME = FALSE #是否显示时间戳（-U）
-  UNIX\_TIME\_POS = BL/-2c/-2c #时间戳位置
-  UNIX\_TIME\_FORMAT = %Y %b %d %H:%M:%S #时间戳格式

颜色参数

-  COLOR\_BACKGROUND = black   # z<cpt文件最小值时的背景色
-  COLOR\_FOREGROUND = white  # z>cpt文件最大值的前景色
-  COLOR\_NAN = 128      #图像中z=NaN部分的颜色
-  COLOR\_IMAGE = adobe   #控制PS渲染
-  COLOR\_MODEL = rgb     #默认cpt文件类型
-  HSV\_MIN\_SATURATION = 1  #
-  HSV\_MAX\_SATURATION = 0.1 #
-  HSV\_MIN\_VALUE = 0.3 #
-  HSV\_MAX\_VALUE = 1 #

PostScript参数

-  CHAR\_ENCODING = ISOLatin1+   #字符编码，用于绘制特殊字符
-  DOTS\_PR\_INCH = 300   #绘图精度，每英寸的像素数
-  GLOBAL\_X\_SCALE = 1  # ？？
-  GLOBAL\_Y\_SCALE = 1  # ？？
-  N\_COPIES = 1 #每张图的copy数
-  PS\_COLOR = rgb #
-  PS\_IMAGE\_COMPRESS = lzw # 图像压缩算法
-  PS\_IMAGE\_FORMAT = ascii #生成的图像是ASCII还是二进制
-  PS\_LINE\_CAP = butt #控制线段的端点
-  PS\_LINE\_JOIN = miter #
-  PS\_MITER\_LIMIT = 35 #
-  PS\_VERBOSE = FALSE #是否在PS文件中写更多的注释
-  TRANSPARENCY = 0  #控制透明度，基本没用

输入输出格式参数

-  D\_FORMAT = %.12lg  #双精度浮点型的输出格式
-  FIELD\_DELIMITER = tab #GMT输出的每列的的分割符
-  GRIDFILE\_FORMAT = nf  # 默认网格文件格式
-  GRIDFILE\_SHORTHAND = FALSE #是否检查网格文件后缀
-  INPUT\_CLOCK\_FORMAT = hh:mm:ss # 输入的时间格式
-  INPUT\_DATE\_FORMAT = yyyy-mm-dd #输入的日期格式
-  IO\_HEADER = FALSE #输入输出文件是否有头段
-  N\_HEADER\_RECS = 1 # 如果有头段的话，默认为1个
-  NAN\_RECORDS = pass #遇到NaN该如何处理
-  OUTPUT\_CLOCK\_FORMAT = hh:mm:ss #输出时间格式
-  OUTPUT\_DATE\_FORMAT = yyyy-mm-dd #输出日期格式
-  OUTPUT\_DEGREE\_FORMAT = D #输出度的格式
-  XY\_TOGGLE = FALSE #经纬度互换

投影参数

-  ELLIPSOID = WGS-84  # 地球椭球模型
-  MAP\_SCALE\_FACTOR = default #
-  MEASURE\_UNIT = cm  # 默认单位

日期时间参数

-  TIME\_FORMAT\_PRIMARY = full #
-  TIME\_FORMAT\_SECONDARY = full #
-  TIME\_EPOCH = 2000-01-01T12:00:00 # 相对时间的参考点
-  TIME\_IS\_INTERVAL = OFF #
-  TIME\_INTERVAL\_FRACTION = 0.5 #
-  TIME\_LANGUAGE = us # 时间语言
-  TIME\_UNIT = d # 相对时间的单位
-  TIME\_WEEK\_START = Sunday # 每周起始日
-  Y2K\_OFFSET\_YEAR = 1950 #

其他参数

-  HISTORY = TRUE # 是否记录历史命令中的参数
-  INTERPOLANT = akima # 一维插值算法
-  LINE\_STEP = 0.025c #绘制直线时取点的间隔
-  VECTOR\_SHAPE = 0 #矢量头部的形状。
-  VERBOSE = FALSE #


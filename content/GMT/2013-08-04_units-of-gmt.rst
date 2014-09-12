GMT单位制
#########

:date: 2013-08-04 14:50
:author: SeisMan
:category: GMT
:tags: GMT4
:slug: units-of-gmt
:summary: GMT4的两种单位制之间的区别。

GMT提供了两种单位制，即SI和US。默认情况下GMT使用国际单位制SI。若想要使用US单位制，在安装GMT时可以在configure后在参数--enable-US即可。

若在安装之后想要修改单位制也很简单，直接修改GMT/share/conf/gmt.conf文件即可。

SI单位制和US单位制分别对应不同的默认参数文件，即share/conf下的gmtdefaults_SI和gmtdefaults_US。

下面简单看看这两个单位制默认参数文件的差异

.. code-block:: bash

 $ diff gmtdefaults_SI gmtdefaults_US

diff给出的结果为：

::

    1c1
    < # $Id: gmtdefaults_SI.in 9545 2011-07-27 19:31:54Z pwessel $
    ---
    > # $Id: gmtdefaults_US.in 9545 2011-07-27 19:31:54Z pwessel $
    4c4
    < # SI Version
    ---
    > # US Version
    9c9
    < PAPER_MEDIA = a4
    ---
    > PAPER_MEDIA = letter
    15c15
    < ANNOT_OFFSET_PRIMARY = 0.2c
    ---
    > ANNOT_OFFSET_PRIMARY = 0.075i
    18c18
    < ANNOT_OFFSET_SECONDARY = 0.2c
    ---
    > ANNOT_OFFSET_SECONDARY = 0.075i
    22c22
    < HEADER_OFFSET = 0.5c
    ---
    > HEADER_OFFSET = 0.1875i
    25c25
    < LABEL_OFFSET = 0.3c
    ---
    > LABEL_OFFSET = 0.1125i
    36,37c36,37
    < FRAME_WIDTH = 0.2c
    < GRID_CROSS_SIZE_PRIMARY = 0c
    ---
    > FRAME_WIDTH = 0.075i
    > GRID_CROSS_SIZE_PRIMARY = 0i
    39c39
    < GRID_CROSS_SIZE_SECONDARY = 0c
    ---
    > GRID_CROSS_SIZE_SECONDARY = 0i
    41c41
    < MAP_SCALE_HEIGHT = 0.2c
    ---
    > MAP_SCALE_HEIGHT = 0.075i
    43c43
    < TICK_LENGTH = 0.2c
    ---
    > TICK_LENGTH = 0.075i
    45,48c45,48
    < X_AXIS_LENGTH = 25c
    < Y_AXIS_LENGTH = 15c
    < X_ORIGIN = 2.5c
    < Y_ORIGIN = 2.5c
    ---
    > X_AXIS_LENGTH = 9i
    > Y_AXIS_LENGTH = 6i
    > X_ORIGIN = 1i
    > Y_ORIGIN = 1i
    50c50
    < UNIX_TIME_POS = BL/-2c/-2c
    ---
    > UNIX_TIME_POS = BL/-0.75i/-0.75i
    63c63
    < CHAR_ENCODING = ISOLatin1+
    ---
    > CHAR_ENCODING = Standard+
    93c93
    < MEASURE_UNIT = cm
    ---
    > MEASURE_UNIT = inch
    107c107
    < LINE_STEP = 0.025c
    ---
    > LINE_STEP = 0.01i

由上面显示的结果可以看出，两种单位制的不同主要体现在默认纸张大小(PAPER_MEDIA)的不同以及字符编码方式的不同(CHAR_ENCODING)。

由于1 inch = 2.54 cm，其他参数在两种单位制下的效果基本相同。

GMT手册中给出了两种指定单位的方法，参见GMT 4.5.9 Technical Reference and Cookbook Section 4.1 P49，即显式指定和隐式指定，GMT建议使用显式指定的方法。

默认情况下，GMT使用的是国际单位制，但是由于GMT的手册上的例子大多使用US单位制，导致大部分人在显式指定单位时都使用US单位制，比如习惯使用-JM6i而不是-JM15c。对于国人来说，由于对US单位制没有概念，所以在使用的时候是不方便的，比如想要使用-X将图整体上移一定距离时，由于A4纸张的大小是已知的，所以肉眼很容易判断是该上调2cm左右而不是5cm左右，但是如果使用US单位制的时候，却不那么容易判断究竟是1英寸还是3英寸。

所以国人在GMT中或许应该更多地使用SI国际单位制。

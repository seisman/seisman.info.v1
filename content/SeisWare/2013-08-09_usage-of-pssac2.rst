pssac2之用法
############

:date: 2013-08-09 00:05
:author: SeisMan
:category: 地震学软件
:tags: pssac2
:slug: usage-of-pssac2
:summary: pssac2的用法。

::

 pssac2: Plot seismograms
 Usage: pssac2 <infiles> -C<cut0/cut1> -J<params> -R<w/e/s/n>
       [-B<tickinfo>] [-E(k|d|a|n|b)(t(0-9,-5(b),-3(o),-2(a))|vel)] [-K] [-V]
       [-Msize/alpha] [-Gr/g/b/c/t1/t2] [-O] [-P] [-Sshift] [-U[<label>]]
       [-W<pen>] [-#<ncopies>] [-X<x_shift>] [-Y<y_shift>] [-r]
  
       sacfiles may be given on either the command line or
       if none are given they will be expected using standard in (stdin)
       Using stdin indicate (sacfile,x,y,pen)
           if x and y are given, it will override the position
                taken from the sacfile
           if pen is given the pen on the command line will be overridden
  
       All options are in the same meaning as standard GMT EXCEPT:
       -C <cut_begin/cut_end>
               windowing data
               -Ct[0-9]/t[0-9] will use the t[0-9] header values
               or -Ct[0-9]/cut_end or -Ccut_begin/t[0-9]
       -E option determines
         (1) profile type:
       a: azimuth profile
       b: back-azimuth profile
       d: distance profile with x in degrees
       k: distance profile with x in kilometers
       n: traces are numbered from 1 to N in y-axis
         (2) time alignment:
       tn: align up with time mark tn in SAC head
             n= -5(b), -3(o), -2(a), 0-9 (t0-t9)
       vel: use reduced velocity
               Examples: -Ek8.0 -Eat-2 -Ed4.4 -Ent-3
       -M vertical scaling in sacfile_unit/MEASURE_UNIT = size<required> 
           size: each trace will normalized to size (in MEASURE_UNIT)
               scale =  (1/size) * [data(max) - data(min)]
           size/alpha: plot absolute amplitude multiplied by (1/size)*r^alpha
               where r is the distance range in km across surface
               specifying alpha = 0.0 will give absolute amplitudes
               scale = (1/size) * r^alpha
           size/s: plot absolute amplitude multiplied by (1/size)*sqrt(sin(gcarc))
               where gcarc is the distance in degrees.
               scale = (1/size) * sqrt(sin(gcarc))
       -Gr/g/b/zero_line/t0/t1 positive phase painting
               paints the positive portion of the trace in color r/g/b
               from the zero_line to the top and between times t0 and t1
       -gr/g/b/zero_line/t0/t1 negative phase painting
               paints the negative portion of the trace in color r/g/b
               from the zero_line to the bottom and between times t0 and t1
       -N turn clipping off, data will be plotted outside the bounds
               clipping is on by default in X/Y plots and maps
       -S <seconds> shift the trace by seconds
               u: if next character after S is a u
                  then shift using the user variable
                  i.e. -Su9 will use 'user9' for shifting
                  positive shifts move the plot backwards in time
       -L <seconds per MEASURE_UNIT> while poltting on maps <required for maps>
               If your seismograms look choppy and pixelated
               Check the value of DOTS_PR_INCH in gmtdefaults
               and increase the value using gmtset
       -l <x/y/length/bar_length/font_size>
               plot a timescale in seconds per MEASURE_UNIT at (x,y)
               Only works while plotting on maps
       -D <dx/dy> shifts position of seismogram in MEASURE_UNIT
               Only works while plotting on maps
       -W <pen> the pen may be specified on the command line
               or it may be specified with individual files using stdin
       -n Distances and Great Circle Arcs may be negative, don't complain
       -r remove the mean value
       -s byte swap the data before plotting
       -v plot the traces vertically
       -V Verbose (use more for more information)

-  在sac文件方面与pssac相同，可以直接在命令行中指定或者在标准输入通过给出\ ``sacfile [x [y [pen]]]``\ 来指定。若给出了x、y，则x、y会覆盖sacfile文件指定的位置；若给定pen，则命令行中-W指定的pen选项会被覆盖。
-  \ ``-C<cut_begin/cut_end>``\ 截取部分数据用于绘图，与pssac相似；特殊之处在于cut_begin和cut_end在这里可以使用头段变量T0-T9，这样相对更灵活一些。
-  -E选项与pssac相同，貌似-E和-M选项在pssac2中是必须的。
-  -M选项和pssac相似，说明方面要详细很多，多了一个-Msize/s选项，这里的yscale=(1/size)*sqrt(sin(gcarc))，其实gcarc是震中距，大概也相当于几何扩散的振幅校正，原理不知。从代码中看还有一个-Msize/b选项，是根据J-B表进行振幅校正。
-  -Gr/g/b/zero_line/t0/t1将t0到t1时间段内振幅大于zero_line的部分根据rgb涂色。
-  -gr/g/b/zero_line/t0/t1将t0到t1时间段内振幅小于zero_line的部分根据rgb涂色。
-  -N当地震图振幅过大时，则将超过部分切除
-  -S时间平移，-Su9表示按照头段变量user9进行平移
-  -L在地图上绘制地震图时，指定每个MEASURE\_UNIT代表的地震图秒数，MEASURE\_UNIT可能是cm也可能是inch；如果波形看起来很“像素化”，那就要检查一下GMT参数中的DOTS\_PR\_INCH，可以适当地增大这个值。
-  \ ``-l<x/y/length/bar_length/font_size>``\ 在位置x、y处绘制一个timescale，即MEASURE\_UNIT所代表的时间秒数，仅对地图有用。
-  -D<dx/dy>对trace做整体偏移
-  -W画笔属性
-  -n 表示震中距是负的（为什么要设计这个？）
-  -r去均值
-  -s对数据进行byte swap，参见big endian 和 little endian
-  -v垂直绘制trace
-  -V GMT的verbose模式

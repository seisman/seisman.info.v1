pssac之使用
###########

:date: 2013-08-04 15:18
:author: SeisMan
:category: 地震学软件
:tags: pssac, 用法
:slug: usage-of-pssac
:summary: 介绍pssac的使用方法

直接键入pssac，会得到pssac的使用说明：

::

 Usage: pssac standardGMToptions [SACfiles] [-C[t1/t2]] [-E(k|d|a|n|b)(t[n]|vel)] [-Gr/g/b/c] [-I] [-Msize[/alpha]] [-Q] [-r] [-Sshift] [-V]
 
 pssac plots SAC traces. If no SAC file names is provided in the command line, it expects (sacfile,[x,[y [pen]]) from stdin.
       -C only plot data between t1 and t2
       -E option determines
         (1) profile type:
      a: azimuth profile
      b: back-azimuth profiel
      d: epicentral distance (in degs.) profile
      k: epicentral distance (in km.) profile
      n: traces are numbered from 1 to N in y-axis
         (2) time alignment:
      tn: align up with time mark tn in SAC head
              default is the reference time. Others are
          n= -5(b), -3(o), -2(a), 0-9 (t0-t9)
      vel: use reduced velocity
       -G paint amplitudes larger than c with color r/g/b
       -I integrate the trace before plotting
       -M multiple traces
      size: each trace will normalized to size (in y-unit)
      size/alpha: if alpha<0, use same scale for all traces
          else plot absolute amplitude multiplied by size*r^alpha
          where r is the distance range in km
       -Q square the trace
       -r remove the mean value in the trace
       -S shift traces by shift seconds
       -V plot traces vertically

想要彻底理解这个程序还要看看源代码。

pssac从GMT中继承的选项包括：

::

    J R  # 必须
    B K O U X x Y y # \0  #可选

这些选项都是GMT的常见选项，具体含义参见GMT，这里不再介绍这几个选项的用法。J和R是必须的，可选参数中不太常见的选项有四个，x、y、#、\\0，其中x、y和X、Y是一样的，这是GMT中为数不多的几个不区分大小写的选项，#和\\0的含义不明，个人猜测是代表注释行和空文件名。

pssac特有的选项包括：

::

     C E G I M Q r S V W 

其中-I表示画图之前先积分（比如数据是速度，你想要画的是位移）。-Q先平方再画图（这个处理有点诡异，不知道什么场合会用到）。-r先去均值再画图。从源代码中可以看出，当三个选项同时存在时，先积分，再平方，最后去均值。这三个选项非常简单，其他的选项会在后面详细介绍。

利用pssac绘制的图大致分为两类，一类是绘制单个地震图，另一类是绘制剖面图。所谓剖面图，又分为5种剖面图，即-E选项所指定的a、b、d、k、n。剖面图的特点在于你需要给出多个文件（当然一个也可以），一旦剖面类型给定了，地震图的相对位置也就给定了，比如当你的R选项的y轴范围给定为0-90时，选取剖面类型为d时，那么震中距为1度的地震图就会放在1那个位置，震中距为30的地震图放在30那个位置，这个时候y轴只表示震中距了，跟地震图的振幅一点关系也没有。所谓单个地震图，并不意味着一张图里就只有一个trace，可能有很多个trace，但是这些trace之间不像剖面图那样关系密切。

《\ `pssac绘图之单个地震图 <{filename}/SeisWare/2013-08-05_plot-single-trace-with-pssac.rst>`_\ 》介绍了如何使用pssac绘制单个地震图。

《\ `pssac绘图之地震剖面图 <{filename}/SeisWare/2013-08-06_plot-profile-with-pssac.rst>`_\ 》介绍了如何使用pssac绘制地震剖面图。

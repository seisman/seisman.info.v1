如何生成GMT网格数据(I)
#######################

:date: 2013-10-09 10:55
:author: SeisMan
:category: GMT
:tags: 格式转换, 网格, C, GMT4
:slug: generate-xyz-file-for-gmt-grid

.. contents::

这个系列计划有四篇博文，讲述如何自己写程序生成网格数据，以供GMT的grdimage或者grdcontour命令绘图所用。

四篇博文分别介绍四种可以用于GMT绘图的数据格式，分别为

-  ASCII的XYZ数据
-  二进制的Z数据
-  ArcInfo ASCII交换网格格式
-  NetCDF格式

这篇先说说最简单的，如何生成ASCII格式的XYZ数据，并将该数据转换为GMT可识别的网格文件并绘图。

网格描述
========

要生成一个12\*8的网格，网格间隔为0.5，每个网格点的值为1或者-1。(0,0)点位于网格区域的左下角。

这其实是在生成一个非常小的checkboard，12\*8的网格很小，但是足以说明问题，X方向和Y方向网格点数不同、网格间隔为0.5，又稍稍增加了问题的复杂度。

C Code
======

该C代码生成ASCII格式的XYZ数据：

.. code-block:: c

 /*
  * Filename: grid.c
  */
  #include <stdio.h>
  #define NX 12
  #define NY 8
  #define DELTA 0.5
 
  int main(int argc, char const *argv[])
  {
      int ix, iy;
      int a[NX][NY];
      FILE *fop;
   
  // 给每个网格点赋值
      for (ix = 0; ix < NX; ix++)
        for (iy = 0; iy < NY; iy++){
          if ((ix+iy)%2 == 0){
              a[ix][iy] = 1;
          } else {
              a[ix][iy] = -1;
          }
      }
     
  // 写入ASCII XYZ数据到文件xyz.dat
      fop = fopen("xyz.dat","w");
      for (iy = 0; iy < NY; iy++)
        for (ix = 0; ix < NX; ix++)
          fprintf(fop, "%3.1f %3.1f %d\n", ix*DELTA,iy*DELTA,a[ix][iy]);  
      fclose(fop);
 
      return 0;
 }

文件转换方式
============

生成的数据的前几列如下：

::

    0.0 0.0 1
    0.5 0.0 -1
    1.0 0.0 1
    1.5 0.0 -1
    2.0 0.0 1
    2.5 0.0 -1
    3.0 0.0 1
    3.5 0.0 -1
    4.0 0.0 1

XYZ数据生成之后，需要转换成可被GMT识别的NetCDF格式。

已知网格维度为12\*8，网格间隔为0.5，因而可知数据的范围是-R0/5.5/0/3.5，数据间隔为-I0.5/0.5。因而使用如下命令进行转换：

::

     xyz2grd xyz.dat -Gxyz.grd -I0.5/0.5 -R0/5.5/0/3.5 

完整示例
========

.. code-block:: bash

 #!/bin/bash
 R=0/5.5/0/3.5
 
 # 生成XYZ数据
 ./grid
 # xyz数据转换为NetCDF格式
 xyz2grd xyz.dat -Gxyz.grd -I0.5/0.5 -R$R
 # 生成cpt文件
 grd2cpt xyz.grd -Cgray > xyz.cpt
 # 利用生成的网格绘图
 grdimage xyz.grd -B1/1 -R$R -Cxyz.cpt -JX4i/2i > checkboard.ps

.. figure:: /images/2013100901.jpg
   :width: 600px
   :alt: checkboard

小结
====

该方法的优点在于：简单。

该方法的缺点在于：

-  数据以ASCII格式保存，对于大型网格，数据文件会比较庞大，占用大量硬盘空间(比如1200\*800的网格，文件大小大概是13M甚至更多)。
-  数据以ASCII格式写入磁盘，读写速度相对二进制格式要慢很多，降低程序速度；
-  数据生成与转换过程信息不共享，很难直观地知道网格的范围以及间隔。当网格发生变化时，转换命令也要变化。


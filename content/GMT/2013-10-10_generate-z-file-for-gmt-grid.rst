如何生成GMT网格文件(II)
########################

:date: 2013-10-10 08:36
:author: SeisMan
:category: GMT
:tags: 格式转换, 网格, GMT4
:slug: generate-z-file-for-gmt-grid

.. contents::

这篇说说如何生成二进制格式的Z数据，并将该数据转换为GMT可识别的网格文件并绘图。

网格描述
========

要生成一个12\*8的网格，网格间隔为0.5，每个网格点的值为1或者-1。(0,0)点位于网格区域的左下角。

C Code
======

该C代码生成二进制格式的Z数据：

.. code-block:: c

 #include <stdio.h>
 #define NX 12
 #define NY 8
 #define DELTA 0.5
 
 int main(int argc, char const *argv[])
 {
     int ix, iy;
     int a[NX][NY];
     FILE *fop;
 
 // 给网格点赋值
     for (ix = 0; ix < NX; ix++)
         for (iy = 0; iy < NY; iy++){
             if ((ix+iy)%2 == 0){
                 a[ix][iy] = 1;
             } else {
                 a[ix][iy] = -1;
             }
     }
 // 写二进制Z文件，起点位于(0,0)点，行优先格式写入
     fop = fopen("z.dat","wb");
     for (iy = 0; iy < NY; iy++)
       for (ix = 0; ix < NX; ix++)
         fwrite(&a[ix][iy],sizeof(int),1,fop);
      
     fclose(fop);
     return 0;
 }


文件转换方式
============

Z数据生成之后，需要转换成可被GMT识别的NetCDF格式。

数据转换需要如下信息：

-  数据范围是-R0/5.5/0/3.5，数据间隔为-I0.5/0.5；
-  数据的第一个点位于区域的左下角；
-  数据按照行优先方式写入，即先从左向右写入Y=0列，再从左向右写入Y=1列，如此类推。。。
-  数据是以int型存储的，即4字节。

::

     xyz2grd z.dat -Gz.grd -I0.5/0.5 -R0/5.5/0/3.5 -ZBLi

完整示例
========

.. code-block:: bash

 #!/bin/bash
 R=0/5.5/0/3.5

 # 生成XYZ数据
 ./grid
 # xyz数据转换为NetCDF格式
 xyz2grd z.dat -Gz.grd -I0.5/0.5 -R$R -ZBLi
 # 生成cpt文件
 grd2cpt z.grd -Cgray > z.cpt
 # 利用生成的网格绘图
 grdimage z.grd -B1/1 -R$R -Cz.cpt -JX9i/6i -X1.2i > checkboard.ps

.. figure:: /images/2013101001.jpg
   :width: 600px
   :alt: checkboard

小结
====

该方法的优点在于：

-  数据以二进制格式保存，数据文件更小；
-  数据以二进制文件写入磁盘，速度更快；

该方法的缺点在于：

-  生成的数据文件为二进制文件，无法直接打开查看其细节。
-  写数据文件时，第一个点可以选择左上、右上、左下、右下角，可以按行优先或列优先方式，因而共8种写数据的方式。
-  数据中只有每个点的值，没有任何数据范围、网格间隔的信息；这些信息只能从其他地方获取；
-  需要知道写数据时的数据类型；


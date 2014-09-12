如何生成GMT网格数据(III)
#########################

:date: 2013-10-11 09:26
:author: SeisMan
:category: GMT
:tags: 格式转换, 网格, GMT4
:slug: generate-arcinfo-file-for-gmt-grid

.. contents::

GMT支持ESRI ArcInfo ASCII格式的数据，这种数据格式是以ASCII方式写入文件的，因而速度上效率并不高；文件只写入了所有网格点的Z值以及一些头段信息，因而相对ASCII格式的XYZ数据来说，文件大小会小很多。

最关键的一点在于，这种格式的数据，头段中包含了与网格有关的全部信息，利用xyz2grd进行转换时非常方便。因而这篇说说如何生成ArcInfo ASCII格式的数据，并将该数据转换为GMT可识别的网格文件并绘图。

网格描述
========

要生成一个12\*8的网格，网格间隔为0.5，每个网格点的值为1或者-1。(0,0)点位于网格区域的左下角。

C Code
======

ArcInfo ASCII数据有两种不同的格式，分别对应于GMT中所说的gridline registration和pixel registered。

关于ArcInfo ASCII格式的具体信息，可以参考\ `ArcGIS的官方简短说明`_\ 。

该C代码同时生成两种格式的ArcInfo ASCII数据：

.. code-block:: c

 /*
  * Filename: grid.c
  */
 #include <stdio.h>
 #define NX 12
 #define NY 8
  
 int main(int argc, char const *argv[])
 {
     int ix, iy;
     int a[NX][NY];
     FILE *fop;
     float delta = 0.5;
  
 // 为每个网格点赋值
     for (ix = 0; ix < NX; ix++)
         for (iy = 0; iy < NY; iy++){
             if ((ix+iy)%2 == 0){
                 a[ix][iy] = 1;
             } else {
                 a[ix][iy] = -1;
             }
     }
  
 // 第一个文件，该网格采用gridline registration
     fop = fopen("ArcInfo1.dat","w");
     fprintf(fop,"nclos %d\n",NX);
     fprintf(fop,"nrows %d\n",NY);
     fprintf(fop,"xllcenter %d\n",0);              // !!!!!
     fprintf(fop,"yllcenter %d\n",0);              // !!!!!
     fprintf(fop,"cellsize %f\n",delta);
     fprintf(fop,"NODATA_VALUE %d\n",-9999);
      
     for (iy = NY-1; iy >= 0; iy--){               
       for (ix = 0; ix < NX; ix++){
         fprintf(fop,"%d ",a[ix][iy]);
       }
       fprintf(fop,"\n");
     }
     fclose(fop);
  
 // 第二个文件，该网格采用pixel registration
     fop = fopen("ArcInfo2.dat","w");
     fprintf(fop,"nclos %d\n",NX);
     fprintf(fop,"nrows %d\n",NY);
     fprintf(fop,"xllcorner %d\n",0);            // !!!!
     fprintf(fop,"yllcorner %d\n",0);            // !!!!
     fprintf(fop,"cellsize %f\n",delta);
     fprintf(fop,"NODATA_VALUE %d\n",-9999);
      
     for (iy = NY-1; iy >= 0; iy--){
       for (ix = 0; ix < NX; ix++){
         fprintf(fop,"%d ",a[ix][iy]);
       }
       fprintf(fop,"\n");
     }
     fclose(fop);
  
     return 0;
 }   


文件转换方式
============

由于ArcInfo
ASCII格式的头段中已经包含了足够的信息，因而该格式的转换非常简单：

::

     xyz2grd ArcInfo.dat -GArcInfo.grd -E

完整示例
========

.. code-block:: bash

 #!/bin/bash
 R=0/5.5/0/3.5

 # 生成数据
 ./grid

 # 转换并绘制第一个文件
 xyz2grd ArcInfo1.dat -GArcInfo1.grd -E
 grd2cpt ArcInfo1.grd -Cgray > ArcInfo1.cpt
 grdimage ArcInfo1.grd -B1/1 -R$R -CArcInfo1.cpt -JX9i/6i -X1.2i > checkboard1.ps

 # 转换并绘制第二个文件
 xyz2grd ArcInfo2.dat -GArcInfo2.grd -E
 grd2cpt ArcInfo2.grd -Cgray > ArcInfo2.cpt
 grdimage ArcInfo2.grd -B1/1 -R$R -CArcInfo2.cpt -JX9i/6i -X1.2i > checkboard2.ps

.. figure:: /images/2013101101.jpg
   :align: center
   :alt: fig

.. figure:: /images/2013101102.jpg
   :align: center
   :alt: fig

小结
====

该方法的优点在于：

-  数据只写入Z值和头段，相对XYZ文件来说更小；
-  所有必须的信息都位于头段中，数据转换简单。
-  数据写入方式固定；

该方法的缺点在于：

-  生成的数据文件虽然为ASCII文件，但是难以直接查看其细节。

.. _ArcGIS的官方简短说明: http://help.arcgis.com/zh-cn/arcgisdesktop/10.0/help/index.html#//009t0000000z000000

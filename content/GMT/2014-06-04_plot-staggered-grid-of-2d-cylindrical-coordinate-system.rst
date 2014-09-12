二维柱坐标系下交错网格的绘制
############################

:author: SeisMan
:date: 2014-06-04 20:00
:category: GMT
:tags: GMT4, GMT脚本
:slug: plot-staggered-grid-of-2d-cylindrical-coordinate-system
:depends: mathjax

.. contents::

说明
====

这篇博文给出了一个利用GMT绘制示意图的实例。该实例由王桥完成并投稿至本博客。总的来说，该图看上去画起来不难，实际在画的过程中还是需要经过一些设计的。这其中也涉及到一些具体的处理技巧。其实GMT并不是特别适合绘制这种示意图，但是目前没有想到更高效且精确的绘图方法。

背景介绍
========

在柱坐标系\ :math:`(r,\theta,z)`\ 中，若假定所有的物理场在z方向均保存不变，则P-SV系统的一阶速度-应力形式的波动方程可以表示如下：

.. figure:: /images/2014060401.jpg
   :alt: momentum conservation
   :width: 300 px

.. figure:: /images/2014060402.jpg
   :alt: constitutive relations
   :width: 300 px

将这样的一组方程进行离散，很容易通过有限差分方法进行波场的模拟。对于有限差分方法，一般有同位网格和交错网格两种网格布局，目前最常用的应该是交错网格布局。关于交错网格布局最早的两篇文章是Virieux于1984和1986年于Geophysics上发表，分别介绍了笛卡尔坐标系下SH系统和P-SV系统的波动方程如何使用交错网格布局。

绘图效果
========

想要绘制如下交错网格布局：

.. figure:: /images/2014060403.jpg
   :alt: staggered-grid-layout
   :width: 600 px

绘图脚本
========

脚本如下：

.. code-block:: bash

	#!/bin/sh
	R=0/360/0/1.2
	J=P6i
	S1=t0.45    # 三角
	S2=c0.4     # 圆
	S3=s0.5     # 方
	W=1p,0/0/0  # black
	W1=1p,255/0/0   # red
	G1=black
	G2=white
	fig=PSVpolar.ps
	indata=circle.dat

	gmtmath -T0/360/1 -N1 = $indata

	psxy -R$R -J$J -T -K > $fig
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	#画不同半径的圆弧
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	for r in  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
	do
  	awk -v r=$r '$1<=45 {print $1,r}' $indata | psxy -R$R -J$J  -W$W  -K -O >> $fig
  	awk -v r=$r '$1>=90 && $1<=135 {print $1,r}' $indata  | psxy -R -J -W$W -K -O >> $fig
  	awk -v r=$r '$1>=180 && $1<=225 {print $1,r}' $indata | psxy -R -J -W$W -K -O >> $fig
  	awk -v r=$r '$1>=270 && $1<=315 {print $1,r}' $indata | psxy -R -J -W$W -K -O >> $fig
	done

	#突显某个半径的弧度
	awk '$1<=45 {print $1,0.5}' $indata | psxy -R -J -W$W1 -K -O >> $fig
	awk '$1<=45 {print $1,0.6}' $indata | psxy -R -J -W$W1 -K -O >> $fig

	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	#画半径
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	for theta in 0 45 90 135 180 225 270 315; do
  	for r in 0.1 0.3 0.5 0.7 0.9; do
    	r1=`awk -v r=$r 'BEGIN{ printf("%0.1f", r+0.1);}'`
    	psxy  -R -J  -W$W -N -K -O <<EOF >> $fig
    	$theta $r
    	$theta $r1
	EOF
  	done
	done

	#突显某个半径
	for theta in 0 45; do
  	for r in 0.5; do
    	r1=`awk -v r=$r 'BEGIN{ printf("%0.1f", r+0.1);}'`
    	psxy -R -J -W$W1 -N -K -O << EOF >> $fig
    	$theta $r
    	$theta $r1
	EOF
  	done
	done

	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	# Plot shadow
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	for angle in 0 5 10 15 20 25 30 35 40; do
  	a1=`awk -v angle=$angle 'BEGIN{printf("%0.1f",angle-0.1);}'`
  	a2=`awk -v angle=$angle 'BEGIN{printf("%0.1f",angle+5);}'`
  	psxy -J -R  -Gred -K -O << EOF >> $fig
  	$a1  0.5
  	$a1  0.6
  	$a2  0.6
  	$a2  0.5
	EOF
	done

	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	# Plot Symbols
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	#白色三角形
	for r in 0.1 0.3 0.5 0.7 0.9; do
  	psxy -R -J -S$S1 -W$W -G$G2 -K -O   << EOF >> $fig
  	0 $r
  	90 $r
  	180 $r
  	270 $r
	EOF
	done

	#白色圆圈
	for r in 0.2 0.4 0.6 0.8 1; do
  	psxy -R -J -S$S2 -W$W -G$G2  -N -K -O  << EOF >> $fig
  	45 $r
  	135 $r
  	225 $r
  	315 $r
	EOF
	done
	#黑色方块
	for r in 0.2 0.4 0.6 0.8 1; do
  	psxy -R -J -S$S3 -W -G$G1  -N -K -O  << EOF >> $fig
  	0 $r
  	90 $r
  	180 $r
  	270 $r
	EOF
	done
	#黑色实心圆
	for r in 0.1 0.3 0.5 0.7 0.9; do
  	psxy -R -J -S$S2 -W -G$G1  -N -K -O  << EOF >> $fig
  	45 $r
  	135 $r
  	225 $r
  	315 $r
	EOF
	done

	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	# 添加图例
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	R=-1/1/-1/1
	J=X6i
	psxy -R$R -J$J -S$S3 -W$W -G$G1 -K -O << EOF >> $fig
  	0.4 -0.16
	EOF
	pstext -R -J -K -O << EOF >> $fig
 	0.45 -0.17 15 0  4  BL @%6%v@%12%@-q
	EOF

	psxy -R -J -S$S2 -W$W -G$G1 -K -O << EOF >> $fig
  	0.65 -0.16
	EOF
	pstext -R -J -K -O << EOF >> $fig
 	0.7 -0.17 15 0  4  BL @%6%v@%6%@-r
	EOF

	psxy -R -JX -S$S1 -W$W -G$G2 -K -O   << EOF >> $fig
  	0.4 -0.26
	EOF
	pstext -R -J -K  -O   << EOF >> $fig
 	0.45 -0.27 15 0 4 BL @%12%\163@%6%@-r@%12%q
	EOF

	psxy -R -J -S$S2 -W$W -G$G2  -N -K -O  << EOF >> $fig
  	0.65 -0.26
	EOF
	pstext -R -J -K  -O   << EOF >> $fig
 	0.7 -0.27 15 0 4 BL @%12%\163@%6%@-rr\040@-,@-\040@-@%12%\163@-qq
	EOF
	psxy -R -J -W$W -K -O <<EOF >> $fig
  	0.35 -0.12
  	0.35 -0.3
  	0.95 -0.3
  	0.95 -0.12
  	0.35 -0.12
	EOF

	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	# Plot Arrows
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	gmtset VECTOR_SHAPE 1
	psxy -R -J -W$W -G$G1 -K -O << EOF >> $fig
  	0.25 -0.05
  	0.81  -0.05
	EOF
	pstext -R -J -K  -O   << EOF >> $fig
  	0.8 -0.06 7 0 34 BL \344
	EOF
	pstext -R -J -K  -O << EOF >> $fig
  	0.5 -0.1 15 0 6 BL r@%4%(@%%j@%4%)
	EOF
	psxy -R-1/1/-1/1 -J -Sml14c -W$W -K  -O   << EOF >> $fig
 	0 0  0  40
	EOF
	pstext -R -J -N -K -O << EOF >> $fig
  	0.87 0.3 15 0 12 BL q@%4%(@%6%i@%%)
	EOF

	psxy -R$R -J$J -T -O >> $fig

	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	# Remove useless data or files
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	rm ${indata}
	rm .gmt*

代码说明
========

#. 先按照seisman建议的GMT代码风格定义变量
#. gmtmath生成1到360间隔为1的一列数据
#. 通过循环绘制不同半径的圆弧以及半径。其中涉及到在awk里面使用bash变量的问题，这里使用\ `-v`\ 选项将bash的变量传递给awk。
#. 最有意思的是绘制红色阴影部分。由于是极坐标-JP, 所以我用了9段矩形，每段5度填充了45度的一个弧形区域。如果在GMT5.1里面用透明-t60的话，可以看出有一小部分重叠的区域。GMT4里没有透明，就掩盖了重叠的部分。
#. 画图例时改用了直角坐标-JX. 特别之处在于应力分量的希腊字母不能用简体。想到的一个解决办法是将它旋转负15度，试过了，非常麻烦。
#. 画坐标弧形箭头的时候，seisman给出了解决方法：使用-Sm选项。对于直线箭头，默认的我认为不是很好看，就用了34号字体里面\344号箭头加上一个直线组合起来的。

致谢
====

画图我用MATALAB用得比较多，都是一些简单的图，还没有涉及到地图、地形图等。直到前年，要用到地图，从我一个统计地震学师弟JK那里学到了GMT作图。从那以后，都是麻烦师弟JK帮忙。我给他描述图件，他给我写一个GMT画图的开头和底板，然后我在上面修改，中间不停地问他命令，都快把他弄烦了。这张图也不例外。借此机会多谢JK师弟了。非常感谢seisman的博客内容，非常好，我几乎都看完了，给我非常在的帮助。

修订历史
========

- 2014-05-27：王桥投稿；
- 2014-06-05：SeisMan对部分代码进行简化；

由矩张量计算双力偶断层参数
##########################

:date: 2013-07-16 17:01
:author: SeisMan
:category: 地震学软件
:tags: 震源机制解, 断层
:slug: from-moment-tensor-to-double-couple

Double Couple由四个参数描述：Strike、Dip、Rake、Moment；Moment Tensor由9个量描述，由于对称性，减少到六个。

任意一个double couple都可以写成moment tensor的形式，但并非所有的moment tensor都可以写成double couple形式。double couple只是moment tensor的一个子集而已。

若干月前，有人问到如何将moment tensor转换成double couple，搜了一下，发现了一个别人写的代码。做了一下排版，试了一个例子，结果是对的，没有再看细节。

代码分为三个部分：

- ten2axe：将moment tensor转换成主轴坐标系；
- axe2dc：将主轴坐标系下的结果转换为double couple解；
- ten2dc.pl：我写的perl脚本，实现两个程序的衔接（作者给的是shell脚本）

原文链接： http://www.fcaglp.unlp.edu.ar/~esuarez/gmt/1998/0102.html

代码下载： http://pan.baidu.com/share/link?shareid=511728517&uk=19892171

PS：没看过代码，不确定原理，不确定正确性。

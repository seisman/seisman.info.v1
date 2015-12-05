GMT进阶之-B选项中的冒号
########################

:date: 2013-10-12 09:15
:author: SeisMan
:category: GMT
:tags: GMT技巧, GMT选项, GMT4, Perl
:slug: gmt-option-b-colon

.. contents::

-B选项是GMT的常用选项之一，其除了可以设置刻度之外，还可以设置标题、坐标轴名、注释前缀以及单位。在绘图的过程中遇到一个非常有趣的问题，总结如下。

问题描述
========

如下图，想要用-B选项给图加上标题，标题的格式为 ``Title : eltiT`` ，即想要在标题中加个冒号，为了增加问题的复杂度，标题中还有空格。

.. figure:: /images/2013101201.png
   :width: 400px
   :align: center
   :alt: fig

Bash实现
========

无冒号的写法
------------

.. code-block:: bash

   #!/bin/bash
   psbasemap -R0/5/0/5 -JX5i -B1/1:."Title eltiT": > a.ps

用 ``:."string":`` 这样的方式可以很容易的加上标题，由于字符串中有空格，所以需要用双引号（或单引号）将标题字符串括起来。

经典错误写法
------------

根据无冒号时候的写法，很容易想当然地直接在标题字符串中加上冒号，如下：

.. code-block:: bash

   #!/bin/bash
   psbasemap -R0/5/0/5 -JX5i -B1/1:."Title : eltiT": > a.ps


直接运行报错如下：

::

    psbasemap: ERROR: Missing terminating colon in -B string 1ltiT:\

这样的写法为什么错呢？在-B选项中，冒号被用作为分界符，一对冒号包围了一个标题或一个坐标轴名或单位。上面的例子中，直接加上一个冒号之后形成了三个冒号的尴尬局面，GMT默认将离得最近的两个冒号当成一对分界符，然后最后的一个冒号就悲剧了，然后报错。上面给出的错误信息只是常见的错误信息之一。另外，上面的写法用单引号也是错误的。理由相同。

正确写法
--------

既然-B选项把冒号当作分界符，那么字符串中就不能再出现 ``:`` 了，考虑用冒号的八进制编码来表示冒号。查查GMT官方文档的附录F可以知道冒号对应的八进制编码为 ``\072`` 。脚本如下所示：

.. code-block:: bash

   #!/bin/bash
   psbasemap -R0/5/0/5 -JX5i -B1/1:."Title \072 eltiT": > a.ps

为什么用八进制表示冒号就可以呢？GMT对-B选项进行解释时，遇到了":."，代表着接下来的字符串是标题，然后往后寻找找到下一个冒号":"，并将":."和":"之间的字符串作为标题。那么对于这种情况来说这个字符串就是"Title \072 eltiT"（引号不是字符串的一部分）。由于GMT是用C语言写的，当把字符串"Title \072 eltiT"用类似printf("Title \072 eltiT")的语法写到PS文件中时，就变成了"Title : eltiT"。即字符串以"Title \072 eltiT"的形式被GMT解释，然后以"Title : eltiT"的形式被C打印出来。

Perl实现
========

对于习惯使用Perl的人来说，不要以为仅仅知道上面一点就结束了，Perl实现起来比Bash要更复杂一些。

无冒号写法
----------

在Perl中通过system函数来调用系统命令来运行GMT。当然也可以使用倒引号调用系统命令，倒引号敲起来更简单，但是其运行效率相对system更低，不可滥用。

对于system函数来说，参数需要放在引号中，引号中的内容是要调用的系统命令及系统命令的参数。这里存在至少两对引号，system参数所需要的引号以及带空格的字符串所需要的引号。

下面两种写法使用了两种引号，因而是对的：

.. code-block:: perl

 #!/usr/bin/env perl
 system "psbasemap -R0/10/0/10 -JX6i -B1/1:.'Title eltiT': > a.ps";

.. code-block:: perl

 #!/usr/bin/env perl
 system 'psbasemap -R0/10/0/10 -JX6i -B1/1:."Title eltiT": > a.ps';

下面两种写法只用了一种引号，因而会出现无法正确分界的问题：

.. code-block:: perl

 #!/usr/bin/env perl
 system "psbasemap -R0/10/0/10 -JX6i -B1/1:."Title eltiT": > a.ps";

.. code-block:: perl

 #!/usr/bin/env perl
 system 'psbasemap -R0/10/0/10 -JX6i -B1/1:.'Title eltiT': > a.ps';

经典错误写法
------------

在吸取了bash的经验教训之后，知道可以用"\072"来表示冒号，脚本如下：

.. code-block:: perl

 #!/usr/bin/env perl
 system "psbasemap -R0/10/0/10 -JX6i -B1/1:.'Title \072 eltiT': > a.ps";

这种写法为什么是错的？因为perl首先会对system的参数（即双引号内的值）进行解释，双引号内的单引号被当作普通字符来解释（而不是任何分界符），而在双引号内反斜杠是可以转义的，因而\072被转义为":"，然后再调用psbasemap命令，即真正传给psbasemap并运行的命令其实是

::

    psbasemap -R0/10/0/10 -JX6i -B1/1:.'Title : eltiT': > a.ps

这相当于Bash的经典错误写法。

一种正确的写法
--------------

.. code-block:: perl

 #!/usr/bin/env perl
 system 'psbasemap -R0/10/0/10 -JX6i -B1/1:."Title \072 eltiT": > a.ps';

这种写法为什么是正确的呢？因为Perl首先要对参数进行内插，由于参数是由单引号括起来的，此时双引号被当作普通字符而不是分界符，而单引号内反斜杠可以转义的字符只有单引号以及反斜杠，因而在单引号内\072不会被解释。那么传送给psbasemap的命令实际上就是

::

    psbasemap -R0/10/0/10 -JX6i -B1/1:."Title \072 eltiT": > a.ps

这相当于Bash中的正确写法。

正确写法在变量内插时遇到的问题
------------------------------

使用Perl而不是Bash的一个重要理由在于，Perl在字符串处理以及数值计算方面相对Bash来说要有很大的优势。因而用Perl写脚本的时候，如果仅仅只是像上面那个例子那样单引号内只有一堆字符就没有意义了。更常见的情况是system的参数中含有一些变量，如下所示：

.. code-block:: perl

 #!/usr/bin/env perl
 $R = "0/10/0/10";
 $J = "X6i";

 system 'psbasemap -R$R -J$J -B1/1:."Title \072 eltiT": > a.ps';

这样写是错误的，因为单引号内变量$R和$J都不会被内插，所以传送给psbasemap的是无意义的参数。

错误写法修正版
--------------

单引号内的变量不会被内插是肯定的了，但是变量不可能不用，那就只能把错误写法修改一下啦：

.. code-block:: perl

 #!/usr/bin/env perl
 $R = "0/10/0/10";
 $J = "X6i";

 system "psbasemap -R$R -J$J -B1/1:.'Title \\072 eltiT': > a.ps";

这里的修改在于将"\072"改成了"\\072"，这样perl会将"\\"解释为"\"，然后进行系统调用，因而此时传给psbasemap的参数实际上是

::

    psbasemap -R0/10/0/10 -JX6i -B1/1:.'Title \072 eltiT': > a.ps

总结
====

一切罪恶的来源都来自于转义字符。由于需要使用一些特殊字符，就一定会需要转义字符，同时还需要方便的使用转义字符本身这个字符。因而什么时候会转义、什么时候不会转义，就显得额外重要了。对于多个不同语言或者不同命令相互调用的时候，转义就更加重要了。

以Bash为例，bash本身是个空壳，基本不具有任何数据处理能力，因而常常需要借助于awk、grep、sed等命令。Bash中的变量以$作为标识符，awk的变量也以$作为标识符，当在bash中用awk时，就存在一个问题：眼前的$变量到底是bash去解释还是awk去解释。awk为了凑合bash，采用了如下的设计：

::

    awk '{print $1}' infile

当在bash中调用awk时，由于单引号的存在，bash不会对$1进行解释，此时$1交给awk取解释，这也许是你想要的。但是有些时候，如果真的想要将bash的变量$par交给awk就会出现问题：

::

    awk '{print $par,$1}' infile

由于单引号的存在，awk看到的是字符"$par"，而不是变量$par的值，所以$par交给了awk取解释，而awk又不认识变量$par，就会出现问题。为了解决bash向awk传递变量的问题，awk设计了-v选项，感觉问题一下子就被复杂化了。相反，perl是一个自给自足的体系，就不会存在类似的设计缺陷了。

参考来源
========

1.Perl的单引号字符直接量： http://seisman.info/single-quoted-string-literals-in-perl.html

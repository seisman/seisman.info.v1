修改GMT生成的PS文件的标题
#########################

:date: 2015-03-14
:author: SeisMan
:category: GMT
:tags: GMT技巧
:slug: change-title-of-postscript-files-generated-by-gmt

本文整理自：http://gmt.soest.hawaii.edu/boards/1/topics/1820

需要说明的一点，本文是要修改PS文件的标题，而不是PS文件的文件名。

用编辑器打开任意一个GMT生成的PS文件，查看文件的前几行，其中一行大概如下::

    %%Title: GMT v5.1.1 (r12968) [64-bit] Document from psxy

这就是所谓的PS文件的标题。当用evince或gv打开PS文件时，该标题会在软件的某个位置显示。

从上面的例子中可以看到，GMT生成的PS文件的标题中几乎没有带有任何有意义的信息。而在看图的时候可能经常需要从几张相似的图中区分哪张图来自哪个数据，当然可以通过定义很复杂的PS文件名来区分不同的数据，但那么大的一个标题不用，似乎有些太浪费了。

GMT软件自身不能自定义PS文件的标题，只能通过外部程序实现::

    sed -i 's/^%%Title:.*/%%Title: '"$NEW_TITLE/" $FILE

其中变量 ``$FILE`` 是要修改标题的PS文件名， ``$NEW_TITLE`` 是要修改的新标题。这条命令本质上就是一个简单的字符串替换而已，比如::

    sed -i 's/^%%Title:.*/%%Title: '"This is new title/" test.ps

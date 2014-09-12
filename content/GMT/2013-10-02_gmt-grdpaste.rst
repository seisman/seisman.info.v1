GMT之grdpaste合并网格文件
#########################

:date: 2013-10-02 01:00
:author: SeisMan
:category: GMT
:tags: GMT命令, 网格, GMT4
:slug: gmt-grdpaste

该命令语法如下：

::

    grdpaste file_a.grd file_b.grd −Goutfile.grd [ −V ] [ −f[i|o]colinfo ]

该命令用于将两个grd文件合并到一个grd文件中。

需要注意的是，该命令要求两个grid文件必须有相同的横向间隔、纵向间隔且拥有共同的一条边。若网格文件不满足此需要，可以使用grdcut、grdsample等命令修改网格文件以满足该要求。

其他选项没啥好说的。

该命令一次只能合并两个网格文件，因而若有多个网格文件需要合并，需要多次执行grdpaste，且极其需要注意grdpaste的顺序，相当繁琐。对于这种情况，可以考虑使用另一个合并网格文件的命令---grdblend。

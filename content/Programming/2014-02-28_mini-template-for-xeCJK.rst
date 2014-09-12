使用xeCJK解决中文问题的最小模板
###############################

:date: 2014-02-28 21:15
:author: SeisMan
:category: 编程
:tags: LaTeX, 中文
:slug: mini-template-for-xeCJK

LaTeX的中文支持一直是个问题，11年左右刚开始学习LaTeX的时候，那时的中文解决办法是CJK宏包。到了12年或13年的时候，再接触LaTeX的时候，LaTeX中文支持的最优解决办法变成了\ ``xeLaTeX+xeCJK``\ ，只知道这是目前为止最优的中文解决方案。

后来，CTEX学会将xeCJK的功能进行打包，发布了ctex宏包，进一步简化了用LaTeX写中文文档的问题。

下面是利用\ ``xeLaTeX``\ 和 \ ``xeCJK``\ 实现中文支持的最小模板:

.. code-block:: tex

    \documentclass{article}
    \usepackage{xeCJK}
    \setCJKmainfont{SimSun}
    \begin{document}
    中文English混合示例。
    \end{document}

相对于英文的最小LaTeX模板来说多了两句::

    \usepackage{xeCJK}
    \setCJKmainfont{SimSun}

其中字体名\ ``SimSun``\ 等在Linux下可以通过\ ``fc-list :lang=zh``\ 获取。


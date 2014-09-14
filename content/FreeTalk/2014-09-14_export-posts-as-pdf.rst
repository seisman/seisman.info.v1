博客现已支持全文PDF导出
#######################

:date: 2014-09-14
:author: SeisMan
:tags: 博客, PDF, Pandoc
:category: 胡言乱语
:slug: export-posts-as-pdf

近几日对博客进行了一些调整，加入了PDF全文输出的功能。在每篇博文的右侧，都会有“\ **Export**\ ”一项，点击下面的PDF图标，即可将当前博文以PDF格式导出。

好吧，被你识破了。所谓的PDF导出，实际上是我自己将每篇博文转换为PDF并上传到服务器，供读者点击下载。

转换过程中的一些细节如下：

- 利用\ `Pandoc`_\ 实现从rST源码到PDF的转换
- 之所以采用Pandoc而不是rst2pdf是因为rst2pdf的安装一直有问题
- 转换脚本为\ `makepdf.py`_
- 转换为PDF时使用了xelatex，其中LaTeX模板为\ `seisman.latex`_
- 只转换博文，不转换其他页面
- 自动更新，保证PDF与博文内容的一致性

总的来说，生成的PDF效果还是不错的。其中还有一些不够理想的细节，会在将来不断改进。

待解决的问题：

- 无论博文本身有没有目录，PDF中都会显示“Contents”
- 目录与正文之间的分界不够明显
- 若单行代码过长，网页显示时可以使用水平滚动条，PDF显示时则会将一行代码分两行或多行显示，稍稍影响阅读效果；个别过长的行在显示时会超过纸张边界；
- 部分公式太麻烦，直接使用的截图，在PDF中效果较差
- 部分URL没有以链接的形式显示
- 图片不能为GIF格式，否则无法生成PDF

.. _Pandoc: http://johnmacfarlane.net/pandoc/
.. _makepdf.py: https://github.com/seisman/seisman.info/blob/master/makepdf.py
.. _seisman.latex: https://github.com/seisman/seisman.info/blob/master/seisman.latex

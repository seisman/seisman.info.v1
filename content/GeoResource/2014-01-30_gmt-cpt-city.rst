GMT cpt文件库
#############

:date: 2014-01-30 00:33
:author: SeisMan
:category: 地球物理相关资源
:tags: CPT, GMT4, GMT5, 网站
:slug: gmt-cpt-city

GMT4自带了24个cpt文件，GMT5自带了36个cpt文件。如何选择合适的cpt文件是个很头疼的问题，以后再研究。

cpt-city是一个网站，在很多Linux发行版中也是一个软件包，其包含了众多cpt文件（6000+个）。

网址： http://soliton.vm.bytemark.co.uk/pub/cpt-city/

该网站包含多种格式的cpt文件：

-  GMT的cpt格式；
-  CSS3的c3g格式；
-  GIMP的ggr格式；
-  Gnuplot的gpf格式；
-  Paint Shop Pro或Photoshop支持的grd格式；
-  POV-Ray的inc格式；
-  svg格式；

其提供了软件包\ `cptutils`_\ 实现了不同cpt格式之间的转换，同时也提供了一个简洁方便的\ `在线版本`_\ 。

cpt按照用途来分类：

-  Palettes for `bathymetry`_ and a selection of `blues`_
-  Palettes for `topography`_
-  Mixed palettes for `topography and bathymetry`_
-  Schemes for `temperature`_
-  Schemes for `precipitation`_
-  Various `reds`_, `greys`_, `greens`_
-  Schemes for `diverging`_ data
-  Palettes with `transparency`_
-  Gradients of `discordance`_

不得不说，有些cpt绘制出的图真心好看。

.. _cptutils: http://soliton.vm.bytemark.co.uk/pub/jjg/en/code/cptutils.html
.. _在线版本: http://soliton.vm.bytemark.co.uk/pub/cptutils-online/
.. _bathymetry: views/bath.html
.. _blues: views/blues.html
.. _topography: views/topo.html
.. _topography and bathymetry: views/topobath.html
.. _temperature: views/temp.html
.. _precipitation: views/rain.html
.. _reds: views/reds.html
.. _greys: views/greys.html
.. _greens: views/greens.html
.. _diverging: views/div.html
.. _transparency: views/transparency.html
.. _discordance: views/discord.html

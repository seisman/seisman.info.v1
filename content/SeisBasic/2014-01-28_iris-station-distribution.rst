查看IRIS台站分布
################

:date: 2014-01-28 00:21
:author: SeisMan
:category: 地震学基础
:tags: IRIS, 台站
:slug: iris-station-distribution

IRIS利用Google Map服务，提供了直观查看台站分布的方法。

主页： http://www.iris.edu/gmap/

这个服务比较特别，不包含常见的按钮或选项。用户需要根据网站介绍的格式，创建自己需要的URL，直接输入到浏览器中即可查看相关台站分布，并可以查看每个台站的具体信息。

基本格式为::

    http://www.iris.edu/gmap/[network]/[station]?key1=value1&key2=value2

其中中括号包围的项为可选项，问号后接(key,value)对。具体参见原网站。

下面是一些例子：

#.  列出II台网的全部台站::

        http://www.iris.edu/gmap/?net=II

    其等效于::

        http://www.iris.edu/gmap/II

#.  列出IU台网的COLA台站::

        http://www.iris.edu/gmap/IU/COLA

#.  列出虚拟台网_GSN::

         http://www.iris.edu/gmap/_GSN

#.  列出TA台网2004下半年的所有台站::

        http://www.iris.edu/gmap/TA?timewindow=2004/6/1-2004/12/31

#.  列出_GSN台网1988年工作的所有台站::

        http://www.iris.edu/gmap/_GSN?timewindow=1988-1988

#.  列出一定范围内的所有台站::

        http://www.iris.edu/gmap/?minlat=46&maxlat=49&minlon=-125&maxlon=-117

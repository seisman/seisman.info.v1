博客托管的一些调整
##################

:date: 2014-07-17 10:00
:author: SeisMan
:category: 胡言乱语
:tag: 博客
:slug: blog-hosts

博客托管一直是一个比较头疼的问题。作为一个中文博客，访问者必然主要来自于国内，也有少量访问者来自于美国、加拿大等国家的中国人。如果将博客托管在国内主机，可以保证国内大部分人的访问速度，但是托管在国内服务器上的网站必须进行备案，想想就觉得很麻烦；如果将博客托管在国外主机，则大部分国内读者访问网站的速度会很慢，甚至可能由于墙的问题而完全无法访问。

刚使用静态博客的时候，一直将博客托管在国外的GitHub上，我自己测试的ping值大概是300ms左右，相对来说还是有些慢的。后来发现了GitCafe，其可以用于免费托管博客，且主机位于国内所以国内读者访问速度很快，最重要的一点是虽然其主机在国内但却不要求进行备案。（一直无法理解这一点，但是现在的情况的确是这样，不知道能用多久。）将博客托管在GitCafe后，我测试的ping值大概是20ms，速度的增长还是很明显的。也遇到个别国内的读者说不能正常访问，这个我就没办法了。

今天，对博客的托管进行了一些改进，同时将博客的静态HTML文件托管在GitHub和GitCafe上，国内读者访问时使用GitCafe，国外读者访问时使用GitHub，这样一来国内和国外的大部分读者都可以有比较好的访问速度了。

目前博客的一些细节记录如下：

#. 博客源码（Pelican配置以及rst源文件）托管在 `GitHub <https://github.com/seisman/seisman.info>`_ 上；
#. 生成的HTML文件push到GitHub上项目 ``seisman.github.io`` 的 ``master`` 分支，并使用CNAME设置别名；
#. 生成的HTML文件push到GitCafe上项目seisman的 ``gitcafe-pages`` 分支，并设置别名。

因而，实际上本博客有多个访问地址：

- http://seisman.info
- http://seisman.github.io
- http://seisman.gitcafe.io

DNSPod的具体设置如下图，这样的设置使得联通、电信、移动线路的用户（即大部分国内用户）走GitCafe，其他用户走GitHub。

.. figure:: /images/2014071701.png
   :width: 600 px
   :alt: DNSPod settings

用 `17MON <http://tool.17mon.cn/>`_ 测试了修改前后全球各地的ping值。

修改前ping值汇总如下图。国内最快的仅需要1.4ms，国内平均需要50ms。国外的话亚洲其他地区ping值在150ms左右，其他洲基本都在300ms以上。

.. figure:: /images/2014071702.png
   :width: 750px
   :alt: ping0

修改后ping值汇总如下图。国内访问的是GitCafe所以依然保持着50ms左右的ping值，北美洲访问的是GitHub，均值也大概在60ms上下。港澳台以及亚洲其他国家现在走GitHub所以速度稍慢，其他洲的速度变化不明显。

.. figure:: /images/2014071703.png
   :width: 750px
   :alt: ping1

就目前的测试结果来看，国内大部分地区以及美国地区的访问者应该都可以有理想的访问速度了。

修订历史
========

- 2014-07-17：初稿；
- 2014-12-26：GitCafe的博客托管服务有所调整， ``gitcafe.com`` 改成 ``gitcafe.io`` ，需要在DNS中设置CNAME；
- 2016-03-04：GitCafe与Coding合并，博客托管到Coding；

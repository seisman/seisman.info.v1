Python科学计算发行版--Anaconda
##############################

:date: 2014-05-14 13:00
:author: SeisMan
:category: 编程
:tags: 版本, Python
:slug: anaconda-scientific-python-distribution

Python是一种强大的编程语言，其提供了很多模块，可以用于科学计算，常见的包括numpy、scipy和matplotlib。要利用Python进行科学计算，就需要一一安装所需的模块，而这些模块可能又依赖于其它的软件包或库，因而安装和使用起来相对麻烦。幸好有人专门在做这一类事情，将科学计算所需要的模块都编译好，然后打包以发行版的方式供用户使用，Anaconda就是其中一个。

主页：https://store.continuum.io/cshop/anaconda/

Anaconda的特点：

- 包含了众多流行的科学、数学、工程、数据分析的Python包 http://docs.continuum.io/anaconda/pkgs.html
- 完全开源和免费
- 额外的加速、优化是收费的，但对于学术用途可以申请免费的License
- 全平台支持：Linux、Windows、Mac
- 支持Python 2.6、2.7、3.3、3.4，可自由切换

安装
====

#. 安装pyenv

   pyenv可以方便的管理多个版本的Python，建议使用pyenv来安装anaconda。

   pyenv的安装可以参考《\ `Python多版本共存之pyenv </Python/2013-10-04_python-pyenv.rst>`_\ 》。
   
   当然，也可以不使用pyenv，而直接从其官方网站下载：http://continuum.io/downloads

   这里只说如何安装和使用Python2。

#. 安装

   .. code-block:: bash

      $ pyenv install anaconda-2.0.1
   
#. 申请免费的学术License

   申请地址：https://store.continuum.io/cshop/academicanaconda

   申请后，会得到一个license文件，将其放在\ ``~/.continuum``\ 目录下即可。

#. 安装额外的功能包

   .. code-block:: bash

      $ conda update conda    
      $ conda install accelerate    
      $ conda install iopro

Python科学计算发行版--Anaconda
##############################

:date: 2014-05-14 13:00
:author: SeisMan
:category: 编程
:tags: Python
:slug: anaconda-scientific-python-distribution

Python是一种强大的编程语言，其提供了很多用于科学计算的模块，常见的包括numpy、scipy和matplotlib。要利用Python进行科学计算，就需要一一安装所需的模块，而这些模块可能又依赖于其它的软件包或库，因而安装和使用起来相对麻烦。幸好有人专门在做这一类事情，将科学计算所需要的模块都编译好，然后打包以发行版的形式供用户使用，Anaconda就是其中一个常用的科学计算发行版。

主页： https://store.continuum.io/cshop/anaconda/

Anaconda的特点：

- 包含了众多流行的科学、数学、工程、数据分析的Python包 http://docs.continuum.io/anaconda/pkgs.html
- 完全开源和免费
- 额外的加速、优化是收费的，但对于学术用途可以申请免费的License
- 全平台支持：Linux、Windows、Mac
- 支持Python 2.6、2.7、3.3、3.4，可自由切换

安装
====

#. 安装pyenv

   安装anaconda之后，系统内就会存在两个版本的Python：anaconda以及系统自带的Python。

   为了保证两个Python版本之间不相互干扰，需要使用专门的工具来管理多个Python版本。这里选择的工具是pyenv。

   pyenv的安装可以参考《\ `Python多版本共存之pyenv </Python/2013-10-04_python-pyenv.rst>`_\ 》。

   当然，也可以不使用pyenv，而直接从其官方网站下载： http://continuum.io/downloads 。此时用户需自行承担可能的版本冲突。

#. 安装anaconda

   Anaconda支持Python 2和Python 3，但二者是分开的，用户需要自己选择使用Python 2还是Python 3。当然，借助于pyenv的版本管理功能，同时装两个版本也是没问题的。

   安装支持Python 2.7的Anaconda::

    $ pyenv install anaconda-2.0.1 -v

   安装支持Python 3.4的Anaconda::

    $ pyenv install anaconda3-2.0.1 -v

#. 申请免费的学术License

   对于学生来说，可以申请免费的学术License，以安装额外的功能包，以实现计算过程的加速。

   申请地址： https://store.continuum.io/cshop/academicanaconda

   申请后，会得到一个license文件，将其放在 ``~/.continuum`` 目录下即可。

#. 安装额外的功能包

   .. code-block:: bash

      $ conda update conda
      $ conda install accelerate
      $ conda install iopro

安装模块
========

Anaconda已经自带了大量科学计算中的常用模块，可以直接使用。有时需要安装一些其他python模块。

conda
------

anaconda自带了conda命令用于安装与更新模块，比如::

    # 安装模块
    conda install scipy
    # 更新模块
    conda update scipy
    # 更新所有模块
    conda update --all

不过conda能安装的模块很有限。

pip
---

pip是Python自带的模块安装工具，比如::

    pip install requests
    pip install requests --upgrade

升级Anaconda
------------

新版本发布之后，可以使用pyenv安装Anaconda的最新版本，也可以用Anaconda的自带更新工具升级::

    conda update conda
    conda update anaconda

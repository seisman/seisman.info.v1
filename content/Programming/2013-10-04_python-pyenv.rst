Python多版本共存之pyenv
########################

:date: 2013-10-04 00:27
:author: SeisMan
:category: 编程
:tags: 安装, Python, 版本
:slug: python-pyenv
:summary: 使用pyenv管理多个Python版本。

.. contents::

需要使用新版本Python的相关功能，但是又不想要影响到系统自带的Python，这个时候就需要实现Python的多版本共存。

`pyenv`_\ 可以很好的实现Python的多版本共存。

安装pyenv
=========

.. code-block:: bash

   $ git clone git://github.com/yyuu/pyenv.git ~/.pyenv
   $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   $ exec $SHELL -l

安装Python
==========

查看可安装的版本
----------------

.. code-block:: bash

   $ pyenv install --list

安装指定版本
------------

使用如下命令即可安装python 3.3.2.

.. code-block:: bash

    $ pyenv install 3.3.2

该命令会从github上下载python的源代码，并解压到/tmp目录下，然后在/tmp中执行编译工作。编译过程依赖一些其他的库文件，若库文件不能满足，则编译错误，需要重新下载、编译。。。(为什么每次都要重新下呢？)

已知的一些需要预先安装的库包括：

-  readline readline-devel readline-static
-  openssl openssl-devel openssl-static
-  sqlite-devel
-  bzip2-devel bzip2-libs

在所有python依赖库都安装好的情况下，python的安装很顺利。

更新数据库
----------

安装完成之后需要对数据库进行更新：

.. code-block:: bash

    $ pyenv rehash

查看当前已安装的python版本
--------------------------

.. code-block:: bash

    $ pyenv versions
    * system (set by /export/home/seisman/.pyenv/version)
    3.3.2

其中的星号表示使用的是系统自带的python。

设置全局的python版本
--------------------

.. code-block:: bash

    $ pyenv global 3.3.2
    $ pyenv versions
    system
    * 3.3.2 (set by /export/home/seisman/.pyenv/version)

当前全局的python版本已经变成了3.3.2。也可以使用\ ``pyenv local``\ 或\ ``pyenv shell``\ 临时改变python版本。

确认python版本
--------------

.. code-block:: bash

    $ python
    Python 3.3.2 (default, Sep 30 2013, 20:11:44) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

使用python
==========

-  输入\ ``python``\ 即可使用新版本的python；
-  系统命令会以/usr/bin/python的方式直接调用老版本的python；
-  使用pip安装第三方模块时会安装到~/.pyenv/versions/3.3.2下，不会和系统模块发生冲突。

.. _`https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py`: https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py)%E8%8E%B7%E5%8F%96%E4%BB%A3%E7%A0%81%EF%BC%8C%E4%BD%86%E6%98%AF%E4%B8%8D%E7%9F%A5%E4%B8%BA%E4%BD%95%E8%BF%99%E4%B8%AA%E7%BD%91%E5%9D%80%E6%97%A0%E6%B3%95%E9%93%BE%E6%8E%A5%EF%BC%8C%E6%89%80%E4%BB%A5%E5%AE%89%E8%A3%85%E4%B8%80%E7%9B%B4%E4%B8%8D%E6%88%90%E5%8A%9F%E3%80%82
.. _pyenv: https://github.com/yyuu/pyenv


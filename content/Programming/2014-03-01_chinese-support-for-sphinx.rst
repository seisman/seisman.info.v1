sphinx生成中文PDF
#################

:author: SeisMan
:date: 2014-03-01 10:50
:modified: 2015-11-07
:category: 编程
:tags: sphinx, 中文, Python, PDF, LaTeX
:slug: chinese-support-for-sphinx

.. contents::

`sphinx <http://sphinx-doc.org/>`_ 是Python提供的文档生成工具，其可以将rST源文件转换成网页、PDF等多种格式。目前，sphinx 1.3.1在生成中文PDF时有一堆问题，所以需要做一些额外的处理才能解决。

`readthedocs <https://readthedocs.org>`_ 可以直接用于托管sphinx生成的网页文档，由于sphinx不支持中文PDF，所以readthedocs也不支持。readthedocs的服务器是Ubuntu，具体版本未知，TeXLive版本未知，但是肯定早于TeXLive 2014。所以readthedocs上中文支持就更是一个问题。因而在readthedocs网站上以及在本地，有两套不同的做法。

修改conf.py
===========

对 ``conf.py`` 修改如下：

.. code-block:: python

    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

    if on_rtd:
        latex_elements = {
        # The paper size ('letterpaper' or 'a4paper').
        #'papersize': 'letterpaper',

        # The font size ('10pt', '11pt' or '12pt').
        #'pointsize': '10pt',

        # Additional stuff for the LaTeX preamble.
        'preamble': r'''
        \hypersetup{unicode=true}
        \usepackage{CJKutf8}
        \DeclareUnicodeCharacter{00A0}{\nobreakspace}
        \DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
        \DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
        \DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
        \DeclareUnicodeCharacter{2713}{x}
        \DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
        \DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
        \DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
        \DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
        \DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
        \begin{CJK}{UTF8}{gbsn}
        \AtEndDocument{\end{CJK}}
        ''',
        }
    else:
        latex_elements = {
            'papersize' : 'a4paper',
            'utf8extra' : '',
            'inputenc'  : '',
            'babel'     : r'''\usepackage[english]{babel}''',
            'preamble' : r'''
            \usepackage{ctex}
            ''',
        }

其中， ``READTHEDOCS`` 是readthedocs定义的环境变量，通过检测该环境变量来判断是在readthedocs服务器上还是在本地。

在readthedocs服务器上，只能使用 ``latexpdf`` 编译，且只能使用其自带的中文字体。在本地，如果安装了TeXLive 2015，则可以使用ctex宏包，并用 ``xelatex`` 编译。

修改Makefile
============

对Makefile修改如下，这一修改仅对本地生效，不影响readthedocs上的使用：

.. code-block:: makefile

    xelatexpdf:
        $(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
        @echo "Running LaTeX files through xelatex..."
        sed -i s/pdflatex/xelatex/ $(BUILDDIR)/latex/Makefile
        $(MAKE) -C $(BUILDDIR)/latex all-pdf
        @echo "xelatex finished; the PDF files are in $(BUILDDIR)/latex."

参考
====

#. https://github.com/rtfd/readthedocs.org/issues/621
#. https://github.com/JuliaCN/julia_zh_cn/blob/master/conf.py
#. https://github.com/sphinx-doc/sphinx/issues/894

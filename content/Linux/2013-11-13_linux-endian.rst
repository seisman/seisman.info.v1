判断字节序的多种方法
#####################

:date: 2013-11-13 00:33
:author: SeisMan
:category: Linux
:tags: endian, Bash, Python
:slug: linux-endian

本文整理自： http://serverfault.com/questions/163487/linux-how-to-tell-if-system-is-big-endian-or-little-endian

直接查看系统文件::

    lscpu | grep -i byte

Bash版::

    echo -n I | od -to2 | head -n1 | cut -f2 -d" " | cut -c6

若输出为1则为Little Endian，若输出为0则为Big Endian。

为了适应不同操作系统的需求，还有其他各种变种

::

    echo I | tr -d [:space:] | od -to2 | head -n1 | awk '{print $2}' | cut -c6

::

    echo -n I | od -to2 | awk '{ print substr($2,6,1); exit}'

::

    echo -n I | hexdump -o | awk '{ print substr($2,6,1); exit}'


Python一行命令版

.. code-block:: python

    python -c "import sys;print(0 if sys.byteorder=='big' else 1)"

Python脚本版

.. code-block:: python

 #!/usr/bin/env python
 from struct import pack
 if pack('@h', 1) == pack('<h', 1):
    print "Little Endian"
 else:
    print "Big Endian"

Jython脚本版

.. code-block:: java

 from java.lang import System
 for property, value in dict(System.getProperties()).items():
 if property.endswith('cpu.endian'):
 return value

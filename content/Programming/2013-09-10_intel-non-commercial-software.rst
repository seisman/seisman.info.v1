Intel 非商业开发工具
####################

:date: 2013-09-10 11:39
:updated: 2015-04-08
:author: SeisMan
:category: 编程
:tags: 安装, Intel, C, Fortran
:slug: intel-non-commercial-software

.. contents::

Intel的软件开发工具包括：C/C++编译器、Fortran编译器、MKL数学库、MPI并行库等。

这一套开发工具价格很贵，但是Intel为科研工作者、学生、教育者以及开源贡献者提供了免费的版本。

主页：https://software.intel.com/en-us/qualify-for-free-software/
学生申请： https://software.intel.com/en-us/qualify-for-free-software/student

对于学生，intel提供了全套开发工具一年的使用权。Linux和Windows用户可以申请Intel Parallel Studio XE的Cluster版本（包含全部工具）；对于OS X用户，则只能申请Composer版本（只包含C编译器、Fortran编译器以及MKL数学库）。

对于Linux用户，进入学生申请页，点击“Linux”即可申请。申请时需要填写edu邮箱，再填写其他一些必要的信息即可。

若学校的edu邮箱不再Intel的邮箱列表中，则无法申请，可以发邮箱给Intel，申请把学校的邮箱加入到邮箱列表中。申请完成后，Intel会向注册邮箱内发送license以及下载链接。License有效期一年，一年后需要重新申请。

依赖关系
========

安装之前需要先安装如下包::

    yum install gcc gcc-c++ gcc-gfortran pangox-compat-devel libunwind-devel

除此之外，64位系统还需要安装一些32位的库文件::

    yum install glibc.i686 libgcc.i686 libstdc++.i686

解压
====

.. code-block:: bash

   $ tar -xvf parallel_studio_xe_2015_update3.tgz
   $ cd parallel_studio_xe_2015_update3
   $ su
   # ./install_GUI.sh   # 图形化界面，也可以直接执行./install.sh


安装过程
========

#. 检测依赖性

   检测依赖的过程中，会有“Unsupported OS”的错误，除非系统非常老，否则该错误都可以忽略。如果出现其他错误，需要“detailed info about issues”逐一排查。

#. License
#. 激活

   点击“Use serial number to active and install product”，并到邮箱中找到序列号。序列号的格式为\ ``XXXX-XXXXXXXX``\ 。

#. 安装选项

   可以直接使用默认值，也可以自定义指定安装路径以及要安装哪些组件。

修改环境变量
============

对于bash用户，在\ ``~/.bashrc``\ 中加入如下语句

.. code-block:: bash

   # Intel
   source /opt/intel/vtune_amplifier_xe_2015/amplxe-vars.sh quiet
   source /opt/intel/inspector_xe_2015/inspxe-vars.sh quiet
   source /opt/intel/advisor_xe_2015/advixe-vars.sh quiet
   source /opt/intel/bin/compilervars.sh intel64

然后执行\ ``source .bashrc``\ 使环境变量生效。对于csh用户，类似。

说明：2015_update3版本，直接\ ``source``\ 会报错::

    /opt/intel/composer_xe_2015/ipp/bin/ippvars.sh:19: = not found

这似乎是一个bug，把\ ``/opt/intel/composer_xe_2015/ipp/bin/ippvars.sh``\ 第19行的\ ``==``\ 改成\ ``=``\ 即可。

修订历史
========

- 2013-09-10：初稿for CentOS 6.5；
- 2014-07-15：加入了依赖包for CentOS 7.0；
- 2015-04-08：Intel非商业软件在停止一段时间后重新接受申请；
- 2015-07-17：学生可申请完整版开发工具（含Fortran）；

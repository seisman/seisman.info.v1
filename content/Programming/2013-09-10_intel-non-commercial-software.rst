Intel 非商业开发工具安装记录
############################

:date: 2013-09-10 11:39
:updated: 2015-04-08
:author: SeisMan
:category: 编程
:tags: 安装, Intel, C, Fortran
:slug: intel-non-commercial-software

.. contents::

Intel为学生提供了非商业的License，使得学生可以免费获取Intel开发工具一年的使用权。

Linux和Windows用户可以申请Intel Parallel Studio XE的Professional版；对于OS X用户，则只能申请Composer版。

Professional版包括：C/C++编译器、Inspector、VTune、IPP、MKL、Advisor，似乎不含Fortran编译器

地址： https://software.intel.com/en-us/qualify-for-free-software/student

申请时需要填写edu邮箱，再填写其他一些必要的信息即可。然后Intel会向注册邮箱内发送license以及下载链接。License有效期一年，一年后需要重新申请。

依赖关系
========

安装之前需要先安装如下包::

  yum install gcc gcc-c++ gcc-gfortran pangox-compat-devel libunwind-devel

除此之外，64位系统还需要安装一些32位的库文件::

  yum install glibc.i686 libgcc.i686 libstdc++.i686

解压
====

.. code-block:: bash

 $ tar -zxvf parallel_studio_xe_2013_update3_intel64.tgz
 $ cd parallel_studio_xe_2013_update3_intel64
 $ su
 # ./install.sh

检测依赖性
==========

::

    Step 1 of 7 | Welcome > Missing Optional Prerequisite(s)
    --------------------------------------------------------------------------------
    There are one or more optional unresolved issues. It is highly recommended to
    resolve them all before you continue the installation. You can fix them without
    exiting from the installation and re-check. Or you can quit from the
    installation, fix them and run the installation again.
    --------------------------------------------------------------------------------
    Missing optional prerequisites
    -- Intel(R) VTune(TM) Amplifier XE 2013 Update 15: Unsupported OS
    -- Intel(R) Inspector XE 2013 Update 9: Unsupported OS
    -- Intel(R) Advisor XE 2013 Update 5: Unsupported OS
    -- Intel(R) Fortran Composer XE 2013 SP1 Update 2 for Linux*: Unsupported OS
    -- Intel(R) C++ Composer XE 2013 SP1 Update 2 for Linux*: Unsupported OS
    --------------------------------------------------------------------------------
    1. Skip missing optional prerequisites [default]
    2. Show the detailed info about issue(s)
    3. Re-check the prerequisites

    h. Help
    b. Back to the previous menu
    q. Quit
    --------------------------------------------------------------------------------
    Please type a selection or press "Enter" to accept default choice [1]: 1

检测过程中，intel给出“不支持当前操作系统”的错误，除非系统非常老，否则该错误都可以忽略。如果出现其他错误，需要“detailed info about issues”逐一排查。

激活
====

::

    Step no: 3 of 7 | Activation
    --------------------------------------------------------------------------------
    If you have purchased this product and have the serial number and a connection
    to the internet you can choose to activate the product at this time. Activation
    is a secure and anonymous one-time process that verifies your software licensing
    rights to use the product. Alternatively, you can choose to evaluate the
    product or defer activation by choosing the evaluate option. Evaluation software
    will time out in about one month. Also you can use license file, license
    manager, or remote activation if the system you are installing on does not
    have internet access activation options.
    --------------------------------------------------------------------------------
    1. I want to activate my product using a serial number [default]
    2. I want to evaluate my product or activate later
    3. I want to activate either remotely, or by using a license file, or by using a
       license manager

    h. Help
    b. Back to the previous menu
    q. Quit
    --------------------------------------------------------------------------------
    Please type a selection or press "Enter" to accept default choice [1]: 1

    Please type your serial number (the format is XXXX-XXXXXXXX): 查看邮箱找激活码
    --------------------------------------------------------------------------------
    Activation completed successfully.
    --------------------------------------------------------------------------------
    Press "Enter" key to continue:

安装完成
========

::

    Step no: 7 of 7 | Complete
    --------------------------------------------------------------------------------
    Thank you for installing and using the
    Intel(R) Parallel Studio XE 2013 Update 3 for Linux*

    Reminder: Intel(R) VTune(TM) Amplifier XE users must be members of the "vtune"
    permissions group in order to use Event-based Sampling.

    To register your product purchase, visit
    https://registrationcenter.intel.com/RegCenter/registerexpress.aspx?clientsn=N43
    3-3FHWSF85

    To get started using Intel(R) VTune(TM) Amplifier XE 2013 Update 5:
        - To set your environment variables: source
    /opt/intel/vtune_amplifier_xe_2013/amplxe-vars.sh
        - To start the graphical user interface: amplxe-gui
        - To use the command-line interface: amplxe-cl
        - For more getting started resources: /opt/intel/vtune_amplifier_xe_2013/
          documentation/en/welcomepage/get_started.html.
    To get started using Intel(R) Inspector XE 2013 Update 5:
        - To set your environment variables: source
    /opt/intel/inspector_xe_2013/inspxe-vars.sh
        - To start the graphical user interface: inspxe-gui
        - To use the command-line interface: inspxe-cl
        - For more getting started resources: /opt/intel/inspector_xe_2013/
          documentation/en/welcomepage/get_started.html.
    To get started using Intel(R) Advisor XE 2013 Update 2:
        - To set your environment variables: source
    /opt/intel/advisor_xe_2013/advixe-vars.sh
        - To start the graphical user interface: advixe-gui
        - To use the command-line interface: advixe-cl
        - For more getting started resources: /opt/intel/advisor_xe_2013/
          documentation/en/welcomepage/get_started.html.
    To get started using Intel(R) Composer XE 2013 Update 3 for Linux*:
        - Set the environment variables for a terminal window using one of the
          following (replace "intel64" with "ia32" if you are using a 32-bit
          platform).
          For csh/tcsh:
               $ source /opt/intel/bin/compilervars.csh intel64
          For bash:
               $ source /opt/intel/bin/compilervars.sh intel64
          To invoke the installed compilers:
               For C++: icpc
               For C: icc
               For Fortran: ifort

          To get help, append the -help option or precede with the man command.
        - For more getting started resources:
               /opt/intel/composer_xe_2013/Documentation/en_US/get_started_lc.htm.
               /opt/intel/composer_xe_2013/Documentation/en_US/get_started_lf.htm.


    To view movies and additional training, visit
    http://www.intel.com/software/products.

    --------------------------------------------------------------------------------
    q. Quit [default]
    --------------------------------------------------------------------------------
    Please type a selection or press "Enter" to accept default choice [q]:

修改环境变量
============

在.bashrc中加入如下语句

.. code-block:: bash

 # Intel
 source /opt/intel/vtune_amplifier_xe_2013/amplxe-vars.sh
 source /opt/intel/inspector_xe_2013/inspxe-vars.sh
 source /opt/intel/advisor_xe_2013/advixe-vars.sh
 source /opt/intel/bin/compilervars.sh intel64

使环境变量生效：

.. code-block:: bash

 $ . .bashrc
 Copyright (C) 2009-2013 Intel Corporation. All rights reserved.
 Intel(R) VTune(TM) Amplifier XE 2013 (build 274450)
 Copyright (C) 2009-2013 Intel Corporation. All rights reserved.
 Intel(R) Inspector XE 2013 (build 278112)
 Copyright (C) 2009-2013 Intel Corporation. All rights reserved.
 Intel(R) Advisor XE 2013 (build 270011)

出来一堆版权说明好烦人，再改.bashrc如下：

.. code-block:: bash

 source /opt/intel/vtune_amplifier_xe_2013/amplxe-vars.sh quiet
 source /opt/intel/inspector_xe_2013/inspxe-vars.sh quiet
 source /opt/intel/advisor_xe_2013/advixe-vars.sh quiet
 source /opt/intel/bin/compilervars.sh intel64

搞定收工！

修订历史
========

- 2013-09-10：初稿for CentOS 6.5；
- 2014-07-15：加入了依赖包for CentOS 7.0；
- 2015-04-08：Intel非商业软件在停止一段时间后重新接受申请；

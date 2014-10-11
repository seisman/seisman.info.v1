TauP的安装
##########

:date: 2014-10-08
:author: SeisMan
:category: 地震学软件
:tags: Java, 走时
:slug: install-taup

TauP是用Java写的一个用来计算震相走时的软件。

官方主页: http://www.seis.sc.edu/taup/index.html

#. 确认Java运行环境已安装

   在终端中键入\ ``java -version``\ ，若显示版本信息，则表示Java运行环境已安装::

        $ java -version
        java version "1.7.0_65"
        OpenJDK Runtime Environment (rhel-2.5.1.2.el7_0-x86_64 u65-b17)
        OpenJDK 64-Bit Server VM (build 24.65-b04, mixed mode)

   否则则需要先安装Java运行环境，在CentOS 7下用如下命令::

        $ sudo yum install java

#. 下载TauP::

      wget http://www.seis.sc.edu/downloads/TauP/TauP-2.1.2.tgz

#. 解压::

    tar -xvf TauP-2.1.2.tgz

#. 安装::

    sudo mv TauP-2.1.2 /opt

#. 修改环境变量::

    echo 'export TAUPHOME=/opt/TauP-2.1.2' >> ~/.bashrc
    echo 'export PATH=${TAUPHOME}/bin:${PATH}' >> ~/.bashrc
    source ~/.bashrc

#. 执行测试

   终端键入\ ``taup``\ 若出现TauP图形界面则表示安装成功。





安装NVIDIA显卡驱动
##################

:date: 2014-07-13 14:00
:author: SeisMan
:category: Linux
:tags: CentOS
:slug: install-nvidia-drivers-under-linux

大部分Linux发行版都使用开源的显卡驱动nouveau，对于nvidia显卡来说，还是闭源的官方驱动的效果更好。最明显的一点是，在使用SAC拾取震相的时候，使用官方显卡驱动在刷新界面的时候要快很多。

#. 查看显卡型号

   .. code-block:: bash

      $ lspci | grep VGA
      03:00.0 VGA compatible controller: NVIDIA Corporation GF100GL [Quadro 4000] (rev a1)

   从这里可以得出显卡型号为Quadro 4000。

#. 驱动下载

   下载地址为：http://www.nvidia.com/Download/index.aspx?lang=en-us

   下载对应的驱动即可。

#. 安装kernel-devel

   .. code-block:: bash
      
      $ sudo yum install kernel-devel

#. 将nouveau驱动加入黑名单，在\ ``/etc/modprobe.d/blacklist.conf``\ （CentOS 7下为\ ``/usr/lib/modprobe.d/dist-blacklist.conf``\ ）中加入\ ``blacklist nouveau``\ 

#. 备份initramfs文件  
  
   .. code-block:: bash

      $ sudo mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).img.bak

#. 重建initramfs文件

   .. code-block:: bash

      $ sudo dracut -v /boot/initramfs-$(uname -r).img $(uname -r)

#. 关机重启。由于此时nouveau驱动已经被禁用，桌面的显示效果非常差。

#. 进入文本界面

   .. code-block:: bash
      
      $ sudo init 3

   会直接进入文本界面。

#. 在文本界面登录后直接安装

   .. code-block:: bash

      $ sh NVIDIAxxx --kernel-source-path=/usr/src/kernels/x.xx.x-xxxxx

   其中\ ``NVIDIAxxx``\ 为nvidia驱动脚本文件，\ ``x.xx.x-xxxx``\ 为kernel版本号。


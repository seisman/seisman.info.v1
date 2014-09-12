使用EPEL和RPMforge源安装netcdf时的冲突
######################################

:author: SeisMan
:date: 2014-03-03 00:05
:category: Linux
:tags: CentOS, GMT5
:slug: conflict-between-epel-and-rpmforge

新版本的GMT的编译与运行要求netCDF的版本大于4，且支持netCDF4/HDF5。即如果想要手动编译netCDF4以上的版本，则同时需要编译hdf5，而hdf5又依赖于zlib和szlib等等包，所以手动编译netcdf相当不合算。

大多数发行版中应该都有netcdf4，所以不会出现太多的问题。

CentOS官方源中没有netcdf，因而需要使用第三方源，直接将别人已经编译好的文件拿过来使用。其中最常用的就是EPEL和RPMforge。而恰好二者都包含了netcdf、netcdf-devel、hdf5、hdf5-devel包。由此引发了一些冲突。

EPEL中的netcdf版本为4.1.1，其编译过程中依赖于hdf5，因而当通过

::

    sudo yum install netcdf netcdf-devel

安装netcdf时，hdf5以及hdf5-devel会由于依赖关系而被自动安装。

而RPMforge中netcdf的版本为4.1.2，其编译过程中没有加入hdf5依赖，所以当

::

    sudo yum install netcdf netcdf-devel

时，hdf5由于没有被依赖，所以不会被安装。

所以通过EPEL安装的netcdf4是可以被GMT使用的，而通过RPMforge安装的netcdf4是不能被使用的。而由于RPMforge的netcdf版本比EPEL的版本高，因而两个源共存时，RPMforge的netcdf会被优先安装。（利用优先级插件设置之后好像没有用）

因而当遇到如下报错时::

    -- Looking for nc_def_var_deflate
    -- Looking for nc_def_var_deflate - not found
    CMake Error at cmake/modules/FindNETCDF.cmake:127 (message):
    Library found but netCDF-4/HDF5 format unsupported. Do not configure
    netCDF-4 with --disable-netcdf-4.
    Call Stack (most recent call first):
    src/CMakeLists.txt:39 (find_package)

需要确认netcdf究竟来自于EPEL还是RPMforge。

用来检查的命令如下:

#. 查看当前系统中所使用的源
   ::
    
       yum repolist

#. 查看优先的netcdf-devel的版本以及来自哪个源
   ::

    yum info netcdf-devel

#. 查看netcdf-devel包依赖于哪些其他包
   ::

    yum deplist netcdf-devel

#. 查看当前系统中已安装的相关包
   ::
    
    rpm -qa | grep netcdf
    rpm -qa | grep hdf5

通过以上四个方法确认netcdf以及hdf5均来自于EPEL，则没问题。

如果确认无误，依然出现如上报错，一个可能的原因是自己曾经尝试编译过netcdf，并禁用了hdf5相关功能，而删除netcdf时没有删除干净，或者怎样。

如果真的没招了，可以查看编译GMT时的\ ``build/CMakeFiles``\ 目录下的\ ``CMakeError.log``\ 和\ ``CMakeOutput.log``\ 这两个日志文件，寻找与netcdf相关的部分。

其实质是找到netcdf的动态链接库，并通过如下C代码

.. code-block:: c

    #include <netcdf.h>

    int main(int argc, char** argv)
    {
        (void)argv;
        #ifndef nc_def_var_deflate
            return ((int*)(&nc_def_var_deflate))[argc];
        #else
            (void)argc;
            return 0;
        #endif
    }

检测动态链接库中是否定义了函数\ ``nc_def_var_deflate``\ 。

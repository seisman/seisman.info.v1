地球物理相关软件
################

:date: 2014-02-20 10:20
:author: SeisMan
:category: 地球物理相关资源
:tags: 理论地震图, SAC, GMT4, GMT5
:slug: geo-software

.. contents::

通用数据处理
============

- `SAC`_: Seismic Analysis Code，地震学数据处理的常用软件。
- `CPS330`_
- `ObsPy`_: 基于Python的地震学数据处理框架

数据格式转换
============

- `rdseed`_: SEED格式转换为SAC等地震数据格式
- `win32tools`_: Hi-net提供的工具，用于将WIN32格式的数据转换为SAC格式
- `mseed2sac`_: 将miniSEED格式转换为SAC格式
- `dataselect`_: miniSEED数据处理

数据获取工具
============

- `jweed`_: 用Java实现的IRIS数据申请客户端。
- `SOD`_: 数据自动下载命令行工具。

绘图类
======

- `GMT`_: 地球物理方向绘制地图必备神器。
- `pssac`_: 利用GMT强大的绘图库直接绘制地震图
- `JPlotResp`_: 绘制RESP仪器响应文件的振幅相位响应谱。可以直接联网查询某台网某台站某个时间的仪器响应，也可以直接处理本地的RESP文件。
- `MoPad`_: 地震矩分析和绘图软件，可以做地震矩的各种分解以及分析，绘制各种类型的震源球，可控性非常强，比GMT的psmeca命令要灵活，且可以与GMT联合使用。
- `GmtPy`_: GMT的非官方Python接口。

通用辅助类
==========

- `distaz`_: 给定震中和台站经纬度，计算震中距、方位角和反方位角的经典代码。
- `TauP`_: 强大的走时计算器，不过其功能可不仅仅只是计算走时这么简单。射线参数、射线路径、反射点、投射点都可以计算，支持自定义速度模型、支持不常见的震相。

理论地震图
==========

- `fk`_: 频率-波数法，计算水平分层各向同性介质下理论地震图位移静态解和动态解
- `SHaxi`_: 有限差分方法计算全球尺度高精度SH波场。
- `Mineos`_: Normal modes方法计算球对称非旋转地球模型下的合成地震图
- `yaseis`_: 频率-波数法，球状分层介质下的理论地震图
- `AxiSEM`_: 球层介质中的3D弹性、非弹性、各向异性、声波理论地震图
- `Instaseis`_: 用Python写的，基于AxiSEM的地震图合成工具
- `GEMINI`_:
- `DSM`_: Direct Solution Method
- `SOFI2D`_: 二维有限差分
- `SOFI3D`_: 三维有限差分
- `SPECFEM2D`_: 谱元法2D
- `SPECFEM3D`_: 谱元法3D(笛卡尔坐标系)
- `SPECFEM3D Global`_: 谱元法3D(球坐标系)

震源机制
========

- `gcap`_: 通用Cut and Paste方法反演震源机制
- `pyTDMT`_: 时间域震源机制反演的Python实现
- `WPhase`_: W Phase方法反演震源机制
- `focmec`_: 确定并绘制震源机制

特定功能类
==========

- `hk`_: 用于接收函数研究的代码。
- `CCP`_: 共转换点地震数据叠加，用于接收函数研究。
- `IRFFM`_: 带界面的接收函数软件包。
- `astack`_: 自适应迭代以实现震相对齐。
- `LASIF`_: 基于Python的大规模全波形反演框架，似乎是层析成像。

数学处理类
==========

- `SHTOOLS`_: 实现球谐相关操作，包括变换、重建、旋转、谱分析等。

.. _astack: http://rses.anu.edu.au/seismology/soft/astack/index.html
.. _SAC: http://www.iris.edu/ds/nodes/dmc/forms/sac/
.. _CPS330: http://www.eas.slu.edu/eqc/eqccps.html
.. _rdseed: http://www.iris.edu/ds/nodes/dmc/forms/rdseed/
.. _win32tools: http://www.hinet.bosai.go.jp/REGS/manual/dlDialogue.php?r=win32tools
.. _mseed2sac: https://seiscode.iris.washington.edu/projects/mseed2sac
.. _jweed: http://ds.iris.edu/ds/nodes/dmc/software/downloads/jweed/
.. _GMT: http://gmt.soest.hawaii.edu/
.. _pssac: http://www.eas.slu.edu/People/LZhu/home.html
.. _JPlotResp: http://www.isti2.com/JPlotResp/
.. _MoPad: http://www.larskrieger.de/mopad/
.. _GmtPy: http://emolch.github.io/gmtpy/
.. _distaz: http://www.seis.sc.edu/software/distaz/
.. _TauP: http://www.seis.sc.edu/taup/
.. _fk: http://www.eas.slu.edu/People/LZhu/home.html
.. _SHaxi: http://svn.geophysik.uni-muenchen.de/trac/shaxi
.. _Mineos: https://github.com/geodynamics/mineos
.. _hk: http://www.eas.slu.edu/People/LZhu/home.html
.. _IRFFM: http://rses.anu.edu.au/~hrvoje/IRFFMv1.1.html
.. _CCP: http://www.eas.slu.edu/People/LZhu/home.html
.. _gcap: http://www.eas.slu.edu/People/LZhu/home.html
.. _yaseis: https://seiscode.iris.washington.edu/projects/yaseis
.. _AxiSEM: http://seis.earth.ox.ac.uk/axisem/
.. _Instaseis: http://instaseis.net/
.. _LASIF: http://www.lasif.net/
.. _pyTDMT: https://github.com/fabriziobernardi/pydmt
.. _GEMINI: http://www.quest-itn.org/library/software/gemini-greens-function-of-the-earth-by-minor-integration
.. _DSM: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/software/software.htm
.. _SOFI2D: https://www.gpi.kit.edu/Software.php
.. _SOFI3D: https://www.gpi.kit.edu/Software.php
.. _SPECFEM2D: https://geodynamics.org/cig/software/specfem2d/
.. _SPECFEM3D: https://geodynamics.org/cig/software/specfem3d/
.. _SPECFEM3D Global: https://geodynamics.org/cig/software/specfem3d_globe/
.. _ObsPy: https://github.com/obspy/obspy/wiki
.. _dataselect: https://seiscode.iris.washington.edu/projects/dataselect
.. _SHTOOLS: https://github.com/SHTOOLS/SHTOOLS
.. _WPhase: http://eost.u-strasbg.fr/wphase/
.. _focmec: https://seiscode.iris.washington.edu/projects/focmec
.. _SOD: http://www.seis.sc.edu/sod/

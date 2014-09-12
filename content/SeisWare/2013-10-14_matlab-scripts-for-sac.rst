用Matlab处理SAC数据的一些脚本
#############################

:date: 2013-10-14 06:19
:author: SeisMan
:category: 地震学软件
:tags: SAC技巧, Matlab
:slug: matlab-scripts-for-sac

.. contents::

我是那种乖乖用SAC处理sac数据的人。身边有些老师及其学生比较喜欢用matlab处理sac数据，故而这里还是收集一下相关脚本，以造福部分人。

来源1
=====

其实SAC包中自带了一些matlab脚本。

在sac/utils目录下有四个matlab脚本，作者Xiaoning Yang，具体功能看文件名，具体用法看脚本：

::

    getsacdata.m  padcat.m  readsac.m  writesac.m

在sac/aux/mat目录有62个脚本文件，看上去功能很齐全，可能是SAC调用matlab引擎后可以执行的一些命令，不确定是否可以直接调用：

::

    arrow3d.m              GetFiles2.m          mat.m           SaveResults.m
    BAZauto.m              GetFiles.m           mkAxisSymb.m    ScrollHelp.m
    BAZ.m                  getMisFit.m          mkcircle.m      setAZIM.m
    ButtonRelease.m        getReferenceTime.m   MLest.m         setDomain.m
    CalcMLM.m              getWinPolariz.m      MLMcallback.m   setELEV.m
    closePPM.m             hclose.m             mlm.m           SetFilter.m
    crosshair.m            inspCallbacks.m      NextGroup.m     SetHighCorner.m
    deleteDuplicatePick.m  inspector.m          plotmain.m      SetLowCorner.m
    DeletePick.m           inspFigure.m         ppm3.m          SetOrder.m
    DispatchButtonPress.m  inspRealPlot.m       PrevGroup.m     SetPickType.m
    DispatchKeys.m         inspToolbar.m        printfig.m      SetUpSlider.m
    DispatchMouseMove.m    magnifyTrces.m       quitP.m         SetWaveType.m
    dispHelp.m             MainButtonPress.m    RedrawSeis.m    UpdatePPMplot.m
    DoRotations.m          MainButtonRelease.m  RotateToBAZ.m   Winpolariz.m
    drawRect.m             MainMouseMove.m      SacCheck.m
    filterTraces.m         makeFigure.m         SaveResults2.m

来源2
=====

Prof. Zhigang Peng或收集、或编写、或改写了部分matlab脚本，如下：

::

    fget_sac.m newSacHeader.m  rdSacHead.m  rdSac.m  sacfft.m  sachdr.m  sac.m wtSac.m

其下载地址位于： http://geophysics.eas.gatech.edu/people/zpeng/Teaching/MatSAC.tar.gz

具体用法可以看脚本或者点击\ `这里`_\ 。

来源3
=====

Prof. Michael Thorne写了几个matlab脚本：

::

    rsac.m - Read SAC binary
    wsac.m - Write SAC binary
    bsac.m - Be SAC - convert Matlab array to saclab format
    lh.m - List header
    ch.m - Change header
    p1.m - Plot traces (one plot per subplot) - Example screenshot
    p2.m - Plot traces (overlay traces) - Example screenshot
    marktimes.m - Calculate travel times and put in SAC header (by Sean Ford)

下载地址：http://web.utah.edu/thorne/software.html

.. _这里: http://geophysics.eas.gatech.edu/classes/SAC/

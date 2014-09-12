freqlimits的选取
################

:date: 2014-01-16 09:33
:author: SeisMan
:category: 地震学基础
:tags: 仪器响应
:slug: how-to-choose-freqlimits

真实的地面运动，其频谱范围是非常广泛的，从0 Hz到几千Hz甚至更高。

下文全部假定采样间隔为T=0.01s。

根据奈奎斯特采样定理，采样频率为f=1/T=100 Hz，相应的Nyquist采样频率为f'=f/2=50 Hz。即当采样间隔为T=0.01 s时，频率低于50 Hz的信号会被正确采样并可以重建原信号，而频率高于50 Hz的信号则会与频率对于50 Hz的信号发生混叠。因而，在模拟信号转换为数字信号之前，必须要使用一个低通模拟滤波器或其他数字滤波手段。

无论怎样，信号在经过采样之后，信号中高于50Hz的部分必须被削弱，因而仪器响应的振幅谱在接近50 Hz时迅速下降为0或者非常小的值。

去除仪器响应，实际上就是频率域的除法，直接做除法会在大于50 Hz时出现除以0或小值的情况。因而就需要使用freqlimits。

freqlimits有四个参数，f1、f2、f3、f4，满足f1其中f4必须小于或等于50Hz，对于其他参数没有过多要求。

一般而言，f2到f3之间的范围应尽量宽。

参考：

- http://www.eas.slu.edu/eqc/eqc_cps/Questions/qa0001.html
- http://www.eas.slu.edu/eqc/eqc_cps/Questions/qa0002.html

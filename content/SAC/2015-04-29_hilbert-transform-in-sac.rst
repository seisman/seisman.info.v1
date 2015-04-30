调用SAC进行Hilbert变换
######################

:author: SeisMan
:date: 2015-04-29
:category: SAC
:tags: C
:slug: hilbert-transform-in-sac

需要在C程序中对数据做Hilbert变换，自己写显然是不可能的啦，重复造轮子不说，写的还不一定对。找了一些代码，发现都写的好复杂，后来发现SAC在函数库中提供了Hilbert变换的接口，可以直接调用。

firtrn可以用于对数据进行Hilbert变换，但是官方没有给一个比较直白的例子。下面就贴一个我写的例子啦。

需要注意，SAC自带的Hilbert变换要求数据至少201个点。

.. code-block:: C

    #include <stdio.h>
    #include <stdlib.h>
    #define NPTS 1000
    float *hilbert(float *in, int npts);

    int main(){
        float data[NPTS];
        float *hdata;

        int i;
        // 准备输入数据
        for (i=0; i<NPTS; i++)  data[i] = i;

        // 进行Hilbert变换，hdata为Hilbert变换的结果
        hdata = hilbert(data, NPTS);

        for (i = 0; i < NPTS; i++)
            printf("%f\n", hdata[i]);
    }

    // 这里定义了hilbert函数，是对firtrn函数的一个封装
    float *hilbert(float *in, int npts) {
        float *buffer;
        float *out;

        buffer = (float *)malloc(sizeof(float)*50000);
        out = (float *)malloc(sizeof(float)*npts);
        firtrn("HILBERT", in, npts, buffer, out);

        return out;
    }

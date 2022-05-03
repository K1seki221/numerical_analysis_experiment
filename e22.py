'''
/**
 * date : 17:27, 2022-04-27
 * author : Ruijie Zhang@Huazhong University of Sci & Tech
 * mail : zrjhust@gmail.com
**/
'''

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

def question22():
    def question221():
        print('实验2.2.1：三次样条及其与拉格朗日插值法的比较')
        print("\n","type 1: f(x)=1/(1+25x^2)","\n","type 2: f(x)=x/(1+x^4)","\n","type 3:f(x)=arctan(x)")
        f = int(input('select taget function:'))
        n = int(input('input number n for deviding X:'))
        if f == 1:
            a,b = -1, 1
        else:
            a,b = -5, 5


        def func(f,x):
            if f == 1:
                return (1/(1+25*x**2))
            if f == 2:
                return (x/1+x**4)
            if f == 3:
                return (np.arctan(x))
            else:
                print("function选择错误")

        gap = abs(a-b)
        inc_x = gap/n
        inc_xs = 0.01
        x = np.arange(a,b + inc_x,inc_x)
        y= func(f,x)


        cs = CubicSpline(x, y)
        lg = lagrange(x, y)
        xs = np.arange(a, b + inc_xs, inc_xs)

        plt.figure('CubicSpline interpolate')
        plt.subplot(4,1,1)
        plt.plot(x,func(f,x),color='r',label='data')
        plt.scatter(np.array(x),np.array(func(f,x)),color = 'r')
        plt.legend(['primitive function'])
        plt.grid()
        plt.title('primitive function')

        plt.subplot(4,1,2)
        plt.plot(xs,cs(xs),label='CubicSpline')
        plt.legend(['CubicSpline'])
        plt.grid()
        plt.title('CubicSpline')

        plt.subplot(4,1,3)
        plt.scatter(np.array(x),np.array(func(f,x)),color = 'r')
        plt.plot(x,func(f,x),color='r',label='data')
        plt.plot(xs,cs(xs),label='S')
        plt.legend(['data','primitive function',"CubicSpline"])
        plt.title('CubicSpline fitting primitive function')
        plt.grid()

        plt.subplot(4,1,4)
        plt.scatter(np.array(x),np.array(func(f,x)),color = 'r')
        plt.plot(x,func(f,x),color='r',label='data')
        plt.plot(xs,cs(xs),label='S')
        plt.plot(xs,lg(xs),label='L')
        plt.legend(['data','primitive function',"CubicSpline",'lagrange polynomial'])
        plt.title('CubicSpline,lagrange polynomial fitting primitive function')
        plt.grid()
        plt.show()

    def question222():
        print('实验2.2.2：汽车制造商问题')
        x = np.arange(0,11,1)
        y = np.array([0.0, 0.79, 1.53, 2.19, 2.71, 3.03, 3.27, 2.89, 3.06, 3.19, 3.29])
        xs = np.arange(0, 10+0.1, 0.1)

        cs_bc = CubicSpline(x, y,bc_type=((1,0.8),(1,0.2)))
        cs = CubicSpline(x, y)

        plt.plot(x,y,color='r',label='data')
        plt.plot(xs,cs_bc(xs),color='b',label='CubicSpline with boundary conditions')
        plt.legend(['data','CubicSpline with boundary conditions'])
        plt.show()


    print('数值实验题2.2:样条差值的收敛')
    print("\n","type 1: 第一小问","\n","type 2: 第二小问","\n")
    w = int(input('选择要查看的小问：'))
    if w == 1:
        question221()
    if w == 2:
        question222()
    else:
        print('输入整型的1或2')


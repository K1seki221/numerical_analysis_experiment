'''
/**
 * date : 16:47, 2022-04-27
 * author : Ruijie Zhang@Huazhong University of Sci & Tech
 * mail : zrjhust@gmail.com
**/
'''

import numpy as np
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
def question21():
    print('实验2.1：多项式插值的震荡现象')
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


    lg = lagrange(x, y)
    xs = np.arange(a, b + inc_xs, inc_xs)

    plt.figure('lagrange interpolate')
    plt.subplot(3,1,1)
    plt.plot(x,func(f,x),color='r',label='data')
    plt.scatter(np.array(x),np.array(func(f,x)),color = 'r')
    plt.legend(['primitive function'])
    plt.grid()
    plt.title('primitive function')

    plt.subplot(3,1,2)
    plt.plot(xs,lg(xs),label='lagrange')
    plt.legend(['lagrange polynomial'])
    plt.grid()
    plt.title('lagrange polynomial')

    plt.subplot(3,1,3)
    plt.scatter(np.array(x),np.array(func(f,x)),color = 'r')
    plt.plot(x,func(f,x),color='r',label='data')
    plt.plot(xs,lg(xs),label='L')
    plt.legend(['data','primitive function',"lagrange polynomial"])
    plt.title('lagrange polynomial fitting primitive function')
    plt.grid()
    plt.show()

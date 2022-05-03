'''
/**
 * date : 10:12, 2022-04-28
 * author : Ruijie Zhang@Huazhong University of Sci & Tech
 * mail : zrjhust@gmail.com
**/
'''


import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import copy as cp

x = np.arange(-1,2+0.5,0.5)
xs = np.arange(-2,3+0.1,0.1)
y = np.array([-4.447,-0.452,0.551,0.048,-0.447,0.549,4.552])

def orth_poly():
	para = np.polyfit(x,y,3)
	phi = np.poly1d(para)
	e = y - phi(x)
	delta = 0
	for m in e:
		delta += m**2
	print("正交多项式的{a_k}为",para)
	print("正交多项式的平方误差为：",delta)


	plt.figure('polynomial fit function')
	plt.scatter(x,y,color='r')
	plt.plot(xs,phi(xs))
	plt.legend(['data','orthogonal polynomial fit function'])
	plt.show()

def poly():
	a_0 = np.ones(7)
	a_1 = cp.copy(x)
	a_2 = a_1**2
	a_3 = a_1**3
	A_t = np.vstack((a_0,a_1,a_2,a_3))
	A = A_t.T
	ATA = np.matmul(A_t,A)
	ATY = np.matmul(A_t,y)
	a_k_inv = np.matmul(np.linalg.inv(ATA),ATY)
	a_k = a_k_inv[::-1]
	phi = np.poly1d(a_k)
	
	e = y - phi(x)
	delta = 0
	for m in e:
		delta += m**2
	
	print("多项式的{a_k}为",a_k)
	print("多项式的平方误差为：",delta)
	plt.figure('polynomial fit function')
	plt.scatter(x,y,color='r')
	plt.plot(xs,phi(xs))
	plt.legend(['data','polynomial fit function'])
	plt.show()

if __name__ == '__main__':
	print('数值实验题3')
	print("\n","type 1: 第一小题","\n","type 2: 第二小题","\n")
	q = int(input('选择要查看的小题：'))
	if q == 1:
		poly()
	if q == 2:
		orth_poly()
	else:
		print('输入整型的1或2')
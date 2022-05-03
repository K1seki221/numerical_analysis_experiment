'''
/**
 * date : 15:56, 2022-04-28
 * author : Ruijie Zhang@Huazhong University of Sci & Tech
 * mail : zrjhust@gmail.com
**/
'''

import numpy as np
import time
import copy

def e42():
	def f_s(q):
		if q == 1:
			return lambda x: 0.1*(x**6) - x**2 + x,0,2,122/105
		if q == 2:
			return lambda x: x*x**(1/2),0,1,2/5
		if q == 3:
			return lambda x: 1/(x**(1/2)),5,200,2*np.sqrt(200)-2*np.sqrt(5)
	def sim_calcu_nomal(a,b,func,intervals):
		n = intervals# intervals
		h = abs(a-b)/n
		ans = func(a)+func(b)
		v1,v2 = 0,0
		for i in range(0,n):
			v1 += func(a + h*(i+1/2))
		for i in range(1,n):
			v2 += func(a + h*i)
		ans = (h/6)*(ans + 4*v1 + 2*v2)
		return n,ans

	def sim_calcu_n(a,b,func,intervals=1):
		delta = 0.5*1e-7
		n,ans = sim_calcu_nomal(a,b,func,intervals)
		temp = 0
		while abs(ans - temp) >= (4**2-1)*delta:
			temp = ans
			intervals *= 2
			n,ans = sim_calcu_nomal(a,b,func,intervals)

		return n,ans

	q=int(input('选择所查看的小问（请输入int类型）'))
	func,a,b,real = f_s(q)
	n,ans = sim_calcu_n(a,b,func)
	print("真实值：",real)
	print("simpson逐次区间分半法:","\n","所需节点数：",n,"\n","得到结果：",ans)


	delta = 0.5*1e-7
	in_sim = 1
	n_sim,re_sim = sim_calcu_nomal(a,b,func,in_sim)
	while abs(real - re_sim) >= delta:
		in_sim += 1
		n_sim , re_sim = sim_calcu_nomal(a,b,func,in_sim)
	print("复化simpson法：","\n","所需节点数：",n_sim,"\n","得到结果：",re_sim)
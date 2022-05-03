'''
/**
 * date : 11:22, 2022-04-28
 * author : Ruijie Zhang@Huazhong University of Sci & Tech
 * mail : zrjhust@gmail.com
**/
'''

import numpy as np
import time

def e41():
	def get_time(f):
		def inner(*arg,**kwarg):
			s_time = time.time()
			res = f(*arg,**kwarg)
			e_time = time.time()
			print(f.__qualname__,'耗时:{}秒'.format(e_time-s_time))
			return res
		return inner

	def f_slect(q):
		if q == 1:
			return lambda x: -2 /(x**2 - 1),np.log(2)-np.log(3),2,3
		if q == 2:
			return lambda x: 4 / (1 + x**2),np.pi,0,1
		if q == 3:
			return lambda x: 3**x,2/np.log(3),0,1
		if q == 4:
			return lambda x: x*np.exp(x),np.exp(2),1,2
		else:
			print("输入正确的题号")
	'''
	@get_time
	def ctr_calcu(a,b,func,delta):
		temp = (func(a)+func(b))*abs(b-a)/2
		n,temp0 = 1,0
		while abs(temp - temp0)>=delta*3:
			temp0 = temp
			h = abs(b-a)/2**n
			temp = temp0/2 + h * sum(func(np.arange(a + h, b - h+2*h,2*h )))
			n += 1
		return n,temp
	'''
	class integral():
		def ctr_calcu(a,b,func,intervals):
			n = intervals
			h = abs(a-b)/n
			ans = func(a) + func(b)
			v = 0
			for i in range(1,n):
				v += func(a+i*h)
			ans = (h/2)*(2*v + ans)
			return n,ans,1


		def sim_calcu(a,b,func,intervals):
			n = intervals# intervals
			h = abs(a-b)/n
			ans = func(a)+func(b)
			v1,v2 = 0,0
			for i in range(0,n):
				v1 += func(a + h*(i+1/2))
			for i in range(1,n):
				v2 += func(a + h*i)
			ans = (h/6)*(ans + 4*v1 + 2*v2)
			return n,ans,2


		def gaussI_calcu(a,b,func,intervals):
			n = intervals
			h = abs(a-b)/n
			v1,v2,ans = 0,0,0
			for i in range(0,n):
				v1 += func(a + h*(i+1/2) - h/(2*np.sqrt(3)))
				v2 += func(a + h*(i+1/2) + h/(2*np.sqrt(3)))
			ans = (h/2)*(v1+v2)
			return n,ans,3
	'''
	def inv(calcutype,delta):
		if calcutype == 1:
			n_ctr = 1
			while abs(ctr_calcu(2,3,func,n_ctr) - real) >= delta:
				n_ctr += 1
		if calcutype == 2:
			n_sim = 1
			while abs(sim_calcu(2,3,func,n_sim) - real) >= delta:
				n_sim += 1

		if calcutype == 1:
			n_gauss = 1
			while abs(gaussI_calcu(2,3,func,n_gauss) - real) >= delta:
				n_gauss += 1
		return n_ctr,n_sim,n_gauss

	'''

	q=int(input('选择所查看的小问（请输入int类型）'))
	func,real,a,b = f_slect(q)
	delta = (1/2)*1e-7
	in_ctr,in_sim,in_gauss = 1,1,1
	n_ctr , re_ctr, ctr = integral.ctr_calcu(a,b,func,in_ctr)
	n_sim,re_sim, sim = integral.sim_calcu(a,b,func,in_sim)
	n_g,re_g, gauss= integral.gaussI_calcu(a,b,func,in_gauss)

	while abs(real - re_ctr) >= delta:
		in_ctr += 1
		n_ctr , re_ctr, ctr = integral.ctr_calcu(a,b,func,in_ctr)
	while abs(real - re_sim) >= delta:
		in_sim += 1
		n_sim , re_sim, sim = integral.sim_calcu(a,b,func,in_sim)
	while abs(real - re_g) >= delta:
		in_gauss += 1
		n_g , re_g, gauss = integral.gaussI_calcu(a,b,func,in_gauss)
	ctr_time_s = time.time()
	n_ctr , re_ctr, ctr = integral.ctr_calcu(a,b,func,in_ctr)
	ctr_time_e = time.time()
	sim_time_s = time.time()
	n_sim , re_sim, sim = integral.sim_calcu(a,b,func,in_sim)
	sim_time_e = time.time()
	g_time_s = time.time()
	n_g , re_g, gauss = integral.gaussI_calcu(a,b,func,in_gauss)
	g_time_e = time.time()

	print('真实值：',real)
	print("复化梯形公式：","\n","所需要节点：",n_ctr,"\n","所得结果",re_ctr,"\n","运行时间：",ctr_time_e-ctr_time_s)
	print("复化Simpson公式：","\n","所需要节点：",n_sim,"\n","所得结果",re_sim,"\n","运行时间：",sim_time_e-sim_time_s)
	print("Gauss_I型公式:","\n","所需要节点：",n_g,"\n","所得结果",re_g,"\n","运行时间：",g_time_e-g_time_s)
'''
/**
 * date : 17:42, 2022-04-27
 * author : Ruijie Zhang@Huazhong University of Sci & Tech
 * mail : zrjhust@gmail.com
**/
'''

from e21 import * 
from e22 import *

if __name__ == '__main__':
    print('数值实验题2')
    print("\n","type 1: 第一小题","\n","type 2: 第二小题","\n")
    q = int(input('选择要查看的小题：'))
    if q == 1:
        question21()
    if q == 2:
        question22()
    else:
        print('输入整型的1或2')
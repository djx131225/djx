'''
根号计算：
1.导入math内置函数
2.
'''
import math
from calculator import calculator2

def cac(first_number,second_number):
    return first_number*second_number

def sca():
    h =calculator2.cac()
    print(type(h),h)
    return h

def genhao():
    k = eval(input("请输入一个根号内的数值："))
    print(type(math.sqrt(k)),math.sqrt(k))
    return math.sqrt(k)
# -*- coding: cp936 -*-
def fast_powmod(a,p,n):
    """采用模重复平方计算法，计算 result = a^p mod n"""
    result = a % n
    remainders = []
    while p != 1:
        remainders.append(p & 1)    #取出指数p化为二进制后的最低位
        
        p = p >> 1
        
    while remainders:           #只要remainders不空就保持循环
        rem = remainders.pop()
        result = ((a**rem) * (result**2)) % n
    return result

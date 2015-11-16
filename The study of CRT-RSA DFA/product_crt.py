# -*- coding: cp936 -*-
import os
import math
import random
import Euclid
import fast_powmod
import prime_test
e = 65537
binary_bits = 1024#大约为十进制的309位，由下式计算得出
binary_bits >>=1#相当于除以2，为p和q的位数
def produce_primes(binary_bits):
    """产生指定位数的随机数"""
    while True:
        random.seed()#改变随机数种子
        odd = random.getrandbits(binary_bits)#步长为2,产生一个随机奇数
        if len(bin(odd))-2 != binary_bits:
            continue
        if prime_test.fast_prime_test(odd) == False:#先快速判断一下是否为素数
            continue
        is_prime = prime_test.miller_rabin(odd)#miller_rabin算法素性测试
        if is_prime == True:
            return odd
        elif is_prime == False:
            continue
def produce_p_q():
    """产生两个不同的大素数p和q"""
    p = produce_primes(binary_bits)
    len
    while True:
        q = produce_primes(binary_bits)
        if q != p:
            return(p,q)
def produce_CRT():
    (p,q) = produce_p_q()
    n = p*q
    Euler = (p-1)*(q-1) #欧拉函数
    d = Euclid.extended_Euclid(e,Euler)#求出e模Euler的逆元d，e*d=1mod（Euler）
    dP = Euclid.extended_Euclid(e,p-1)
    dQ = Euclid.extended_Euclid(e,q-1)
    qInv = Euclid.extended_Euclid(q,p)
    return (p,q,n,d,dP,dQ,qInv)





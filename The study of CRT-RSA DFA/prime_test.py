# -*- coding: cp936 -*-
import fast_powmod
DEBUG = False   #判断是否要调试

def get_d_r(prime_n_1):
    """prime_n_1 = prime-1,而 prime-1 = odd_m * 2^r,返回：(odd_m,r)"""
    r = 0
    bits = prime_n_1
    while not (bits & 1):#看二进制低位有多少个0，计算r和odd_m
        r += 1
        bits >>= 1
    odd_m = prime_n_1 / (2**r)    
    if DEBUG:
        print 'r=%d,odd_m=%d' %(r,odd_m)
    return (odd_m,r)
        

def fast_prime_test(prime):
    """先用整除的办法，从3至5000，快速判断一下prime是否为素数"""
    for test in range(3,5000,2):
        if prime % test == 0:
            return False    #一定不是素数
        else:
            return True     #可能是素数
        

def miller_rabin(prime):
    """用miller_rabin算法进行素性测试，返回False表示一定是非素数，
        返回True则表示可能为素数"""
    witness = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47)
    """上述共15个基数,若prime为素数，则因为基数也选为素数，
        二者必然互素,满足了Fermat小定理的条件"""
    prime_n_1 = prime - 1
    (odd_m,r) = get_d_r(prime_n_1)#分解b^(n-1)mod(n)中的n-1，小Fermat必须满足模为1

    for rand_witness in witness:
        y = fast_powmod.fast_powmod(rand_witness,odd_m,prime)
        if DEBUG:   
            print 'y=%d' %y
        """平方根检验,模prime的情况下,prime-1相当于-1,而此处正负1均可通过"""
        if r == 0:
            if y == 1:  #小Fermat
                continue
            else:
                return False
        else:
            if y==1 or y==prime_n_1:
                continue
            else:
                for j in range(1,r+1):
                    y = fast_powmod.fast_powmod(y,2,prime)
                    if y == prime_n_1:
                        break
                    else:
                        return False
             
    return True     #如果r=0,这里就一定是True
    """只有-1能过，-1平方变为1,正负1全出现；而1之后全为1，不会再出现-1，这样没有全出现正负1,非素数"""
    """范围从1到r,小Fermat必须满足模为1，然后平方根检验不能出现其他值，前面的if已有一个不为正负1的数"""


if __name__ == '__main__':
    prime = 2**4253-1
    print '%d 是个素数么\t%s' %(prime,miller_rabin(prime))
    
    print miller_rabin(105)#False

    print miller_rabin(2047)#False

    print miller_rabin(1373653)#False

             
                        
                
    

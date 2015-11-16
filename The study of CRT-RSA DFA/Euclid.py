# -*- coding: cp936 -*-
def gcd(a,b):
    """求2个数的最大公约数"""
    if(a < b):
        (a,b) = (b,a)
    if b == 0:  #又是缩进
        return a
    else:
        return gcd(b,a%b)#递归调用


def extended_Euclid(e,z):
    """利用扩展的欧几里得算法来求密钥e模z的乘法逆元d"""
    (x1,x2,x3) = (1,0,z)
    (y1,y2,y3) = (0,1,e)
    while True:
        if y3 == 0:
            return False
        if y3 == 1:
            if y2<0:
                return (y2%z+z)%z  #负数画为正数
            else:
                return y2%z
        div = x3/y3
        (t1,t2,t3) = (x1-div*y1,x2-div*y2,x3-div*y3)
        (x1,x2,x3) = (y1,y2,y3)
        (y1,y2,y3) = (t1,t2,t3)

if __name__ == '__main__':
    print gcd(100,125)
    print extended_Euclid(7,48)
        

# -*- coding: cp936 -*-
from product_crt import *
import sha
sha1_OID="3021300906052b0e03021a05000414"
h=sha.new(raw_input("输入待加密内容:")).hexdigest()
#消息编码EM = 0x00 || 0x01 || PS || 0x00 || T,T=OID+H
EM=int("0001ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"+"00"+sha1_OID+h,16)
#快速模幂运算，相当于pow（base,exp,n）
def fast_pow(base,exp,n):
    result=1
    while(exp):
#按位与运算，若为1，则不可被2整除
        if exp&1:
            result=(result*base)%n
        exp=exp>>1
        base=(base*base)%n
    return result
#CRT-RSA签名，参考《PKCS #1 V2.1》5.2.1 RSAP1
#QInv是在模p下的乘法逆元
def sign(m,P,Q,Dp,Dq,Qinv):
    
    s1=fast_pow(m,Dp,P)
    s2=fast_pow(m,Dq,Q)
    h=((s1-s2)*Qinv)%P
    C=s2+Q*h
    return C
def main():
    (p,q,n,d,dP,dQ,qInv)=produce_CRT()
    print "产生的随机密钥："
    print "p:",hex(p)[2:-1]
    print "q:",hex(q)[2:-1]
    print "d:",hex(d)[2:-1]
    print "n",hex(n)[2:-1]
    print "CRT幂dP：",hex(dP)[2:-1]
    print "CRT幂dQ：",hex(dQ)[2:-1]
    print "CRT系数qInv：",hex(qInv)[2:-1]
    C=sign(EM,p,q,dP,dQ,qInv)
    print "签名结果c:",hex(C)[2:-1],
    m_v=pow(C,65537,n)
    print "\n验签结果m_v:",hex(m_v)[2:-1]
    
if __name__=="__main__":
    main()

    

#make by liujian,2015.07.16
# -*- coding: cp936 -*-
from product_crt import *
import sha
(p,q,N,D,dP,dQ,qInv)=produce_CRT()  #产生CRT-RSA密钥
print "***********************产生的随机密钥***********************"
print "私钥因子p:",hex(p)[2:-1]
print "私钥因子q:",hex(q)[2:-1]
print "私钥D:",hex(D)[2:-1]
print "公钥因子N",hex(N)[2:-1]
print "N长度：",len(bin(N))-2,   "\D:长度",len(bin(D))-2
print "**********************************************************"
sha1_OID="3021300906052b0e03021a05000414" #来自 PKCS#1，构建EM的参数
#快速模幂运算，相当于pow（base,exp,n）
def fast_pow(base,exp,n):
    result=1
    while(exp):
        if exp&1:
            result=(result*base)%n
        exp=exp>>1
        base=(base*base)%n
    return result
#错误的模幂运算，可选择注入错误点:例如在第4次exp未移位
def fast_pow_F(base,exp,n):
    result=1
    i=1
    while(exp):
        i=i+1
        if exp&1:
            result=(result*base)%n
        else:
            pass
        if i==4:
           # exp=exp>>1
           base=((base)*base)%n     
        else:
            exp=exp>>1
            base=((base)*base)%n        
    return result
#CRT-RSA签名，参考《PKCS #1 V2.1》5.2.1 RSAP1
def sign(m,P,Q,Dp,Dq,Qinv):    
    s1=pow(m,Dp,P)
    s2=pow(m,Dq,Q)
    h=((s1-s2)*Qinv)%P
    C=s2+Q*h
    return C
#选择注入错误运算，s1和s2都可以
def sign_F(m,P,Q,Dp,Dq,Qinv):   
    s1=fast_pow_F(m,Dp,P)
    s2=fast_pow(m,Dq,Q)
    h=((s1-s2)*Qinv)%P
    C1=s2+Q*h
    return C1
#最大公约数计算，欧几里得算法
#d=gcd(m,n)=>d|m,d|n,m=q1*n+r1
def gcd(m,n):
    while n:
        m,n=n,m%n
    return m
#M - M' = (((Mq - Mp)*K) mod q)*p - (((M'q - Mp)*K) mod q)*p = (x1-x2)*p
#由Gcd( M-M', n ) = Gcd( (x1-x2)*q, p*q ) = q,则计算
def DFA_CRT_RSA(C,C1):
    q=gcd(C-C1,N)    
    return q    
def main():
    #消息编码EM = 0x00 || 0x01 || PS || 0x00 || T,T=OID+H,《PKCS #1 V2.1》
    h=sha.new(raw_input("输入待签名内容:")).hexdigest()
    EM=int("0001ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"+"00"+sha1_OID+h,16)
    C=sign(EM,p,q,dP,dQ,qInv)
    C1=sign_F(EM,p,q,dP,dQ,qInv)
    q_F=DFA_CRT_RSA(C,C1)
    p_F=N/q_F
    q_F=hex(q_F)[2:-1]
    p_F=hex(p_F)[2:-1]
    print "正确签名结果：",hex(C)[2:-1],"\n错误签名结果:",hex(C1)[2:-1]
    print "验签计算结果：",hex(fast_pow(C,65537,N))[2:-1]
    print "经过计算的:\n",'p:',p_F,'\n','q:',q_F
    print "**********************************************************"
if __name__=="__main__":
    main()
    re=raw_input("修改签名内容按y再来一次！")
    if re =="y":
                 
                main()
                re=raw_input("修改签名内容按y再来一次！")
    else:
                pass
        

    

#!/usr/bin/python
#coding=utf-8
import math
import sys
import time
def main():
    start=time.time()
    sum=0
    for k in range(10):
        temp=2*math.sqrt(2)/9801*math.factorial(4*k)*(1103+26390*k)/\
             (pow(math.factorial(k),4)*pow(396,4*k))
        sum+=temp
    sum=1/sum
    print("sum:")
    print(sum)
    #判断sum是否与math.pi相等
    print("sum==math.pi?")
    print(sum==math.pi)
    print(time.time()-start)

if __name__=='__main__':
    main()
#!/usr/bin/python
#coding=utf-8
import time
def main():
    start=time.time()
    x=set()
    while True:
        i=input("Please add the element(0 for out):")
        if(i!='0'):
            x.add(i)
        else:
            break
    with open('fiveone.txt','r') as f:
        words=f.read().split()
    _dict=dict()
    for i in words:
        if(i in x):
            if(i not in _dict):
                _dict[i]=0
            else:
                _dict[i]+=1
    print(_dict)
    print(time.time()-start)


if __name__=='__main__':
    main()
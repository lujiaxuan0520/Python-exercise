#!/usr/bin/python
#coding=utf-8
import time
def main():
    start=time.time()
    with open('fiveone.txt','r')as f:
        words=f.read()
    wordss=words.split()
    _dict=dict()
    for i in wordss:
        if i not in _dict:
            _dict[i]=0
        elif i in _dict:
            _dict[i]+=1
    print(_dict)
    print(time.time()-start)

def main2():
    from collections import Counter
    cnt=Counter()
    with open('fiveone.txt','r') as fp:
        words=fp.read().split()
    for i in words:
        cnt[i]+=1
    print(cnt)

if __name__=='__main__':
    main2()
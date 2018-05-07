#!/usr/bin/python
#coding=utf-8
import random
def main():
    x=set()
    while len(x)<20:
        i=random.randint(1,100)
        x.add(i)
    print(x)



if __name__=='__main__':
    main()
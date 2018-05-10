#!/usr/bin
#coding=utf-8
import time
import re
def rotateword(strsrc,n):
    start=time.time()
    if(isinstance(strsrc,str) and isinstance(n,int)):
        strdes=str()
        for i in strsrc:
            if i.isupper():
                strdes+=chr((ord(i)+n-ord('A'))%26+ord('A'))
            elif i.islower():
                strdes+=chr((ord(i)+n-ord('a'))%26+ord('a'))
            else:
                strdes+=i #非字母原样添加
        print('time for rotateword:', time.time() - start)
        return strdes
    else:
        raise Exception('arguments error!')


#使用了re模块的search
#默认全部转换为小写来判断
#如果含有非字母，抛出异常
def avoids(word,Str):
    start=time.time()
    if isinstance(word,str) and isinstance(Str,str) and word.isalpha() and Str.isalpha():
        word=word.lower()
        Str=Str.lower()
        result=re.search(Str,word)
        if result:
            print('time for avoids:',time.time()-start)
            return True
        else:
            print('time for avoids:', time.time() - start)
            return False
    else:
        raise Exception('arguments error!')


#使用了re模块的search
#默认全部转换为小写来判断
#如果含有非字母，抛出异常
def useonly(word,Str):
    start=time.time()
    if isinstance(word,str) and isinstance(Str,str) and word.isalpha() and Str.isalpha():
        word=word.lower()
        Str=Str.lower()
        for i in word:
            if(not re.search(i,Str)):
                print('time for useonly:', time.time() - start)
                return False
        else:
            print('time for useonly:', time.time() - start)
            return True
    else:
        raise Exception('arguments error!')



if __name__=='__main__':
    x="ABbCcDdEeZz"
    print(rotateword(x,27))
    print(avoids(x,'ab'))
    print(useonly(x,'abcdeezwq'))


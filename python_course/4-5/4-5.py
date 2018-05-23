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
        for i in Str:
            research=re.search(i,word)
            if research:
                print('time for avoids:', time.time() - start)
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


#使用了re模块的search
#默认全部转换为小写来判断
#如果含有非字母，抛出异常
def useall(word,Str):
    if isinstance(word,str) and isinstance(Str,str) and word.isalpha() and Str.isalpha():
        word = word.lower()
        Str = Str.lower()
        for i in Str:
            if (not re.search(i, word)):
                return False
        else:
            return True
    else:
        raise Exception('arguments error!')


#输出words.txt中使用了所有元音字母aeiou的单词
def countFor4():
    start=time.time()
    s=[]
    with open('words.txt','r')as f:
        data=f.readlines()
        for words in data:
            w=words.strip()
            if useall(w,"aeiou"):
                s.append(w)
    print(s)
    print(time.time()-start)


#使用正则表达式\w*e\w*来匹配含有e/E的单词，没有返回True
def hasnoe(word):
    if isinstance(word,str):
        word=word.lower()
        result=re.search(r'\w*e\w*',word) #返回None表示不含e
        if result:
            return False
        else:
            return True
    else:
        raise Exception('arguments error!')


#输出words.txt中不含e的单词在整个字母表中的百分比
def countFor5():
    start = time.time()
    total_num,num=0,0 #total_num表示单词表中单词总数,num表示不含e的单词数
    with open('words.txt', 'r')as f:
        data = f.readlines()
        for words in data:
            w = words.strip()
            total_num+=1
            if hasnoe(words):
                num+=1
    print('Percentage:',num/total_num)
    print(time.time() - start)


def isabecedarian(word):
    if isinstance(word,str):
        word=word.lower()
        for i in range(1,len(word)):
            if word[i]<word[i-1]:
                return False
        else:
            return True
    else:
        raise Exception('arguments error!')


#输出words.txt中所有符合字母表序的单词
def countFor6():
    start = time.time()
    s=[]
    with open('words.txt', 'r')as f:
        data = f.readlines()
        for words in data:
            w = words.strip()
            if isabecedarian(w):
                s.append(w)
    print(s)
    print(time.time() - start)


if __name__=='__main__':
    x="ABbCDdEeZz"
    print(rotateword(x,4))
    print(avoids(x,'za'))
    print(useonly(x,'z'))
    print(useall(x,'abcdem'))
    countFor4()
    print(hasnoe('asdw'))
    countFor5()
    print(isabecedarian('aBc'))
    countFor6()



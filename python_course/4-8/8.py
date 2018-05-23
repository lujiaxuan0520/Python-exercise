#!/usr/bin/python
#coding=utf-8
import re
import random
def MEKF(n,m):#n阶马尔科夫,生成m个句子
    lib=dict()
    with open('whitefang.txt') as f:
        data=f.read()
        f.close()
    words=re.findall('\w+[\']*\w+[,\.]*',data)#取出所有可以包括引号、逗号和句号的纯单词
    headWord=re.findall('[\.\n]\s*[A-Z]\w*',data)#取出所有句子开头的单词，包含前面的特殊符号
    for i in range(len(headWord)):#去除特殊符号
        x=re.search('\w+',headWord[i])
        headWord[i]=(headWord[i])[x.start():]
    out=open('outputForDict.txt','w')
    for i in iterator(words,n):#遍历所有元组，将所有构成的字典输出到output.txt
        temp_dict=dict()
        temp_dict[i[:len(i)-1]]=i[-1]#让元组前面的元素作为字典的键，最后一个元素作为值
        out.write(str(temp_dict))
        out.write('\n')
    out.close()

    #开始构造字典lib，其中，键为n个单词构成的元组，值为一个列表，包括所有以该键作为前缀的后缀单词
    for item in iterator(words,n):#item为构成的每一个元组
        qianzhui=item[:len(item)-1]#前缀（元组类型）
        houzhui=item[-1]#后缀（str类型）
        if qianzhui not in lib:
            lib[qianzhui]=list()
            lib[qianzhui].append(houzhui)
        else:
            lib[qianzhui].append(houzhui)

    # 生成m个句子
    out = open('outputForSentence.txt', 'w')
    for num in range(m):
        while True:
            temp=random.choice(list(lib.keys()))
            if (temp[0])[0].isupper():
                break
        value=random.choice(lib[temp])
        s=""
        for i in temp:
            s+=' '
            s+=i
            if s[-1]=='.':
                continue
        s+=(' '+value)
        while True:
            if s[-1]=='.':
                break
            s+=' '
            allWordsInStr= re.findall('\w+[,\.]*',s)
            temp=tuple(allWordsInStr[len(allWordsInStr)-n:])#截取出当前str的最后n个单词并转换为元组
            if temp in lib:#如果最后n个单词组成的元组在lib中，就在键里随机选择一个作为后面的单词,否则随机选一个单词
                value = random.choice(lib[temp])
                s+=value
            else:
                s+=random.choice(words)
        out.write(s)
        out.write('\n')

def iterator(words,n):
    '''n阶,定义一个迭代器，返回n个前缀单词和1个后缀单词组成的元组'''
    for i in range(0,len(words)-n):
        x=[]
        for j in range(i,i+n+1):
            x.append(words[j])
        yield tuple(x)


if __name__=='__main__':
    n=input("Please input n:")
    m=input("Please input m:")
    MEKF(eval(n),eval(m))
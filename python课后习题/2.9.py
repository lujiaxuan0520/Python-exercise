#2.9
#!/usr/bin/python
#encoding=utf-8
def main():
    dic={'a':1,'b':2,'c':3}
    x=input('请输入键')
    print(dic[x] if x in dic.keys() else '您输入的键不存在！')

if __name__=='__main__':
    main()
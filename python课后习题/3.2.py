#3.2
#!/usr/bin/python
#encoding=utf-8
def main():
    x=int(input('请输入年份：'))
    if x%100==0 or (x%4==0 and x%100!=0):
        print("是闰年")
    else:
        print("不是闰年")

if __name__=='__main__':
    main()
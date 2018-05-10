#5.2
#!/usr/bin/python
#encoding=utf-8
def is_sushu(x):
    if(x==1 or x==2):
        return True
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

if __name__=='__main__':
    x=input('Please input a number:')
    x=eval(x)
    print("是素数" if is_sushu(x) else "不是素数")
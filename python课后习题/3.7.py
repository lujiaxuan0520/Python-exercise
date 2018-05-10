#3.7
#!/usr/bin/python
#encoding=utf-8
def method1():
    sum=0
    for i in range(1,100,2):
        sum+=i
    print(sum)

def method2():
    sum=0
    for i in range(100):
        if(i%2==1):
            sum+=i
    print(sum)

if __name__=='__main__':
    method1()
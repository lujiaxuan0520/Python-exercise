#3.6
#!/usr/bin/python
#encoding=utf-8
def main():
    x=input("Please input a number(less than 1000)")
    x=num=eval(x)
    elem=[]
    s=str()
    if(isinstance(x,int) and 0<x<=1000):
        for i in range(2,x+1):
            if(x==0):
                break
            elif(x%i==0):
                x=x/i
                elem.append(i)
                i-=1
        for i in range(0,len(elem)):
            s+=(str(elem[i])+'*')
        print(num,"=",s[:len(s)-1])

if __name__=='__main__':
    main()
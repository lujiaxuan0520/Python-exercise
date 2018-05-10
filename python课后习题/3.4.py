#3.4
#!/usr/bin/python
#encoding=utf-8
import random
def main():
    lst=[random.randint(0,100) for i in range(50)]
    for i in range(len(lst)-1,-1,-1):
        if(lst[i]%2==1):
            del lst[i]
            i=i-1
    print(lst)

if __name__=='__main__':
    main()
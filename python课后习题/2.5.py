#2.5
#!/usr/bin/python
#encoding=utf-8
def main():
    lst=input('Please input a list(start with [,end with ])')
    if(lst[0]=='[' and lst[-1]==']'):
        lst=eval(lst)
        print('Please input two arguments:')
        a=int(input())
        b=int(input())
        print(lst[a:b+1])
    else:
        print('Error!')

if __name__=='__main__':
    main()
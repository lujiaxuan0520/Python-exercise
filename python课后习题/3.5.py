#3.5
#!/usr/bin/python
#encoding=utf-8
import random
def main():
    lst=[random.randint(1,100) for i in range(20)]
    l=lst[::2]
    l.sort(reverse=True)
    lst[::2]=l
    print(lst)

if __name__=='__main__':
    main()
#2.10
#!/usr/bin/python
#encoding=utf-8
import random
def main():
    lst=[random.randint(0,100) for i in range(20)]
    lst_q=lst[0:10]
    lst_h=lst[10:19]
    lst_q.sort()
    lst_h.sort(reverse=True)
    lst=lst_q+lst_h
    print(lst)

if __name__=='__main__':
    main()
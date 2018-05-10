#5.9
#!/usr/bin/python
#encoding=utf-8
def f(lst):
    print('max:',max(lst))
    print('sum:',sum(lst))

if __name__=='__main__':
    lst=[]
    while True:
        x=input("Please input number(q for quit):")
        if x=="q":
            break
        elif isinstance(eval(x),int):
            lst.append(eval(x))
        else:
            break
    f(lst)


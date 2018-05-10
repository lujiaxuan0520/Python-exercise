#5.10
#!/usr/bin/python
#encoding=utf-8
def Sum(l):
    _sum=0
    for i in l:
        _sum+=i
    return _sum

if __name__=='__main__':
    print(Sum([1,2,3]))
    print(Sum((1,2,3)))
    print(Sum({1,2,3}))
    print(Sum({1:'a',2:'b',3:'c'}))
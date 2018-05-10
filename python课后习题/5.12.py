#5.12
#!/usr/bin/python
#encoding=utf-8
def Sorted(lst,reverse=False):
    _l=lst[::]
    result=[]
    if reverse==False:
        while len(_l)!=0:
            temp=min(_l)
            result.append(temp)
            _l.remove(temp)
    elif reverse==True:
        while len(_l)!=0:
            temp=max(_l)
            result.append(temp)
            _l.remove(temp)
    return result

if __name__=='__main__':
    lst=[3,4,2,3,1,5,6,2]
    print(Sorted(lst))
    print(Sorted(lst,reverse=True))

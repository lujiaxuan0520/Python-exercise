#3.8
#!/usr/bin/python
#encoding=utf-8
def is_sushu(x):
    if(x==1 or x==2):
        return True
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def main():
    result=[]
    x=[1234,1243,1324,1342,1423,1432,2134,2143,2314,2341,2413,2431,3124,3142,
       3214,3241,3412,3421,4123,4132,4213,4231,4312,4321]
    for i in x:
        if(is_sushu(i)):
            result.append(i)
    print(result)

if __name__=='__main__':
    main()
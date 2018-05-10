#5.3
#!/usr/bin/python
#encoding=utf-8
def _count(str):
    upper=lower=digit=other=0
    for c in str:
        if c.isupper():
            upper+=1
        elif c.islower():
            lower+=1
        elif c.isdigit():
            digit+=1
        else:
            other+=1
    return (upper,lower,digit,other)

if __name__=='__main__':
    s=input('Please input a string:')
    print(_count(s))

#4.2
#!/usr/bin/python
#coding=utf-8
import re
import math
def main():
    x = "I mIss you very much."
    r=re.search(r'(?:[\w])I(?:[\w])',x)
    if r:
        num=math.floor((r.start()+r.end())/2)
        y=x[:num]+'i'+x[num+1:]
        print(y)
    else:
        print(x)

if __name__=='__main__':
    main()
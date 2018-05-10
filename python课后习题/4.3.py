#4.3
#!/usr/bin/python
#coding=utf-8
import re
import math
def main():
    x="This is is a desk."
    pattern=re.compile(r'(\w+)\s+(\w+)')
    lst=re.split(r'\s+',x)
    y=x[::]
    a=0
    for i in range(len(lst)-1):
        result=pattern.search(y,a)
        if not result:
            break
        if result.group(1)==result.group(2):
            y=y[:result.start()]+y[result.start()+math.floor((result.end()-result.start())/2)+1:]
        else:
            a+=len(lst[i])
            continue
    print(y)

if __name__=='__main__':
    main()
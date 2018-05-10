#2.3
#!/usr/bin/python
#encoding=utf-8
import random
def main():
    x=[random.randint(0,100) for i in range(1000)]
    all_elem=set(x)
    _dict=dict()
    for elem in all_elem:
        _dict[elem]=x.count(elem)
    print(_dict)

if __name__=='__main__':
    main()
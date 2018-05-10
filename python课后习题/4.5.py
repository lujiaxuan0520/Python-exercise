#4.5
#!/usr/bin/python
#coding=utf-8
import re
def main():
    x=input("Please input a paragraph:")
    print(re.findall(r'\b\w{3}\b',x))

if __name__=='__main__':
    main()
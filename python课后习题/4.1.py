#4.1
#!/usr/bin/python
#coding=utf-8
import re
def main():
    x = "Can i help you? i can."
    print(re.sub('i','I',x))

if __name__=='__main__':
    main()
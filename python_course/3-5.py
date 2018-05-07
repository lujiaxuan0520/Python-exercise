#coding=utf-8
#!/usr/bin/python
import time
def Ack(m,n):
    '''input two arguments and
    return the result of Ackermann function.'''
    if(not isinstance(m,int) or not isinstance(n,int)):
        print('Arguments must be integer.')
    elif(m==0):
        return n+1
    elif(m>0 and n==0):
        return Ack(m-1,1)
    elif(m>0 and n>0):
        return Ack(m-1,Ack(m,n-1))
    else:
        print('Arguments must greater than zero.')

def main():
    print(Ack(3,6))


if __name__=='__main__':
    start=time.time()
    main()
    print('time:',time.time()-start)
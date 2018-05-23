#!/usr/bin/python
#coding=utf-8
class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        if self.isvalid:
            return str(self.hour).rjust(2)+'h'+str(self.minute).rjust(2)+'m'+str(self.second).rjust(2)+'s'
        else:
            raise Exception('Time object is invalid.')

    def __add__(self, n):
        if self.isvalid:
            new = Time(self.hour, self.minute, self.second)
            if isinstance(n, int):
                new.increment(n)
                return new
            elif isinstance(n, Time):
                new.increment(n.time2int())
                return new
            else:
                raise Exception('Arguments Error!')
        else:
            raise Exception('Time object is invalid.')

    def isvalid(self):
        if 0<=self.hour<24 and 0<=self.minute<60 and 0<=self.second<60:
            return True
        else:
            return False

    def time2int(self):
        if self.isvalid():
            return self.hour * 3600 + self.minute * 60 + self.second
        else:
            raise Exception('Time object is invalid.')

    def printtime(self):
        if self.isvalid():
            print(self.__str__())
        else:
            raise Exception('Time object is invalid.')

    def isafter(self, time2):
        if self.isvalid() and time2.isvalid():
            if self.time2int() > time2.time2int():
                return True
            else:
                return False
        else:
            raise Exception('Time object is invalid.')

    def increment(self, n):
        if self.isvalid() and n>0:
            self.second += n
            while self.second > 59:
                self.minute += 1
                self.second -= 60
            while self.minute > 59:
                self.hour += 1
                self.minute -= 60
            while self.hour > 23:
                self.hour -= 24
        else:
            raise Exception('Arguments Error!')


if __name__ == '__main__':
    t1 = Time(1, 2,30)
    t2 = Time(2, 3)
    t1.printtime()
    t2.printtime()

    if t1.isafter(t2):
        print(t1.__str__() + ' is after than ' + t2.__str__())
    else:
        print(t2.__str__() + ' is after than ' + t2.__str__())
    t2.increment(62)
    t2.printtime()

    sum=t1+t2
    sum.printtime()


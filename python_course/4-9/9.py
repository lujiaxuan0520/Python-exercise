#!/usr/bin/python
#coding=utf-8
class Lunch:
    def __init__(self):
        self.Cus=Customer()
        self.Emp=Employee()
    def order(self,foodName):
        self.Cus.placeOrder(foodName,self.Emp)
    def result(self):
        #ask the Customer what kind of food it has
        self.Cus.printFood()

class Customer:
    def __init__(self):
        self.food=None
    def placeOrder(self,foodName,employee):
        self.food=employee.takeOrder(foodName)    
    def printFood(self): #print the name of my food
        print(self.food.name)

class Employee:
    def takeOrder(self,foodName) :#return a Food,wih requested name
        return Food(foodName)   
    
class Food:
    def __init__(self,name):
        self.name=name

def menu():
    print("num\t\t\tname\t\t\tprice")
    print("1\t\t\tpotato\t\t\t7")
    print("2\t\t\tmeat\t\t\t9")
    print("3\t\t\tmilk\t\t\t3")
    selected()

def isnum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def order(s, context):
    f2 = open('orderlist.txt', 'w')
    f2.write(context)
    f3 = open('totalmoney.txt', 'r')
    if s == '1':
        f2.write("potato\t\t7" + "\n")
        money1 = f3.read()
        x = Lunch()
        x.order('potato')
        x.result()
        if isnum(money1):
            money2 = 7 + int(money1)
        else:
            money2 = 7
    elif s == '2':
        f2.write("meat\t9" + "\n")
        money1 = f3.read()
        y = Lunch()
        y.order('meat')
        y.result()
        if isnum(money1):
            money2 = 9 + int(money1)
        else:
            money2 = 9
    elif s == '3':
        f2.write("milk\t\t3" + "\n")
        money1 = f3.read()
        z = Lunch()
        z.order('milk')
        z.result()
        if isnum(money1):
            money2 = 3 + int(money1)
        else:
            money2 = 3

    f3 = open('totalmoney.txt', 'w')
    f2 = open('orderlist.txt', 'w')
    f2.write(context)
    f3.write(str(money2))
    f2.close()
    f3.close()

def selected():
    f = open("orderlist.txt", "r")
    s1 = f.read()
    f.close()
    print("\nOrdered：" + "\n" + s1)
    f3 = open('totalmoney.txt', 'r')
    totalmoney = f3.read()
    f3.close()
    # print("总计：" + totalmoney+"元")
    print(''.center(25,'-'))
    num = input("Please input your option：")
    order(num, s1)
    s = input("y for continue,q for quit.")
    if s == 'y':
        f = open("orderlist.txt", "r")
        s1 = f.read()
        f.close()
        print('\n')
        print("Ordered：" + "\n" + s1)
        f3 = open('totalmoney.txt', 'r')
        moneynum = f3.read()
        f3.close()
        print("total：" + moneynum)
        if isnum(moneynum):
            # print("此次订单需支付：" + str(moneynum))
            f3 = open('totalmoney.txt', 'w')
            f3.write("")
            f2 = open('orderlist.txt', 'w')
            f2.write("")
            f2.close()
            f3.close()
            # print("订单已提交!")
        else:
            print("No food ordered.")
    elif s == 'n':
        print("Quit Success！")
        f3 = open('totalmoney.txt', 'w')
        f3.write("")
        f2 = open('orderlist.txt', 'w')
        f2.write("")
        f2.close()
        f3.close()
    else:
        selected()


if __name__=='__main__':
    print("Order System".center(25,'='))
    print("a.menu")
    print("q.quit")
    x=input("Please input your option：")
    if x =='a':
        menu()
    elif x=='q':
        print("Quit Success!")
        exit()

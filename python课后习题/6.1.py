#6.1
#!/usr/bin/python
#coding=utf-8
import types
class Person(object):
    def __init__(self, name = '', age = 20, sex = 'man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        if not isinstance(name,str):
            print('name must be string.')
            return
        self.__name = name

    def setAge(self, age):
        if not isinstance(age,int):
            print('age must be integer.')
            return
        self.__age = age

    def setSex(self, sex):
        if sex != 'man' and sex != 'woman':
            print('sex must be "man" or "woman"')
            return
        self.__sex = sex

    def show(self):
        print(self.__name)
        print(self.__age)
        print(self.__sex)

class Student(Person):
    def __init__(self,name='',age=30,sex='man',major='Computer'):
        super(Student,self).__init__(name,age,sex)
        self.setMajor(major)

    def setMajor(self,Major):
        if not isinstance(Major,str):
            print("Major must be a string.")
            return
        self.__major=Major

    def show(self):
        super(Student,self).show()
        print('Major:',self.__major)

if __name__=='__main__':
    zhangsan=Person('Zhang San',19,'man')
    zhangsan.show()
    lisi=Student('Li Si',32,'man','Math')
    lisi.show()
    lisi.setAge(40)
    lisi.show()
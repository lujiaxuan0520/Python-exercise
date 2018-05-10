#6.2
#!/usr/bin/python
#coding=utf-8
class Vector3D:
    def __init__(self,x=0,y=0,z=0):
        self.__x=x
        self.__y=y
        self.__z=z

    def __add__(self,v):
        n=Vector3D()
        n.__x=self.__x+v.__x
        n.__y=self.__y+v.__y
        n.__z=self.__z+v.__z
        return n

    def __sub__(self,v):
        n = Vector3D()
        n.__x = self.__x - v.__x
        n.__y = self.__y - v.__y
        n.__z = self.__z - v.__z
        return n

    def __mul__(self,r):
        if not isinstance(r,int):
            print('arguments error!')
            return
        n=Vector3D()
        n.__x = self.__x *r
        n.__y = self.__y *r
        n.__z = self.__z *r
        return n

    def __truediv__(self, r):
        if not isinstance(r,int):
            print('arguments error!')
            return
        n=Vector3D()
        n.__x = self.__x /r
        n.__y = self.__y /r
        n.__z = self.__z /r
        return n

    def show(self):
        print(self.__x,self.__y,self.__z)

if __name__=='__main__':
    v1=Vector3D(1,1,1)
    v2=Vector3D(2,2,2)
    p=v1+v2
    s=v1-v2
    n=5
    m=p*5
    d=p/5
    p.show()
    s.show()
    m.show()
    d.show()

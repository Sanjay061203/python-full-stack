"""
polymorphism
------------
it means many forms, it allows same ,function or operator to perform different tasks depending on the same object...
types
-----
1.method overloading
--------------------
eg
--
class cal:
    def add(self,a,b=0):
        print(a+b)
    def add(self,a,b=4,c=6):
        print(a+b+c)
c=cal()
c.add(4,6)
c.add(3,7,8)


2.method overrididng
--------------------
the method overriding occurs when a child class provides its own implementation of a method already defined in its parent class...

eg
--
class f:
    def fun(self):
        print("hello")
class s(f):
    def fun(self):
        print("world")
a=s()
a.fun()


3.operator overloading
----------------------
this allows opeators (+,-,*) to work differently for user-defined objects.

1.__add__(+)
2.__sub__(-)
3.__mul__(*)
4.__truediv__(/)
5.__eq__() (==)
6.__it__() (<)

eg
--

class a:
    def __init__(self,marks):
        self.marks=marks
    def __mul__(self,others):
        return self.marks*others.marks
b=a(45)
c=a(7)
print(b*c)

data abstraction
----------------
it is a process of hididng implementations details and showing only the essential data to the user
eg
--
atm
car
app

eg
--
from abc import ABC,abstractmethod
class bank:

    @abstractmethod
    def intrest(self):
        raise NotImplementedError('subclass must implement intrest()')
class SBI(bank):
    def intrest(self):
        print("SBI intrest rate: 6%")
class HDFC(bank):
    def intrest(self):
        print("HDFC intrest rate: 5.5%")
class ICIC(bank):
    def intrest(self):
        print("ICIC intrest rate: 6.9%")

banks=[SBI(),HDFC(),ICIC()]
for j in banks:
    j.intrest()



"""
class cal:
    def add(self,a,b=0):
        print(a+b)
    def add(self,a,b=4,c=6):
        print(a+b+c)
c=cal()
c.add(4,6)
c.add(3,7,8)


class f:
    def fun(self):
        print("hello")
class s(f):
    def fun(self):
        print("world")
a=s()
a.fun()

        
class a:
    def __init__(self,marks):
        self.marks=marks
    def __mul__(self,others):
        return self.marks*others.marks
b=a(45)
c=a(7)
print(b*c)
        
from abc import ABC,abstractmethod
class parent:
    @abstractmethod
    def display(self):
        pass


from abc import ABC,abstractmethod
class bank:

    @abstractmethod
    def intrest(self):
        raise NotImplementedError('subclass must implement intrest()')
class SBI(bank):
    def intrest(self):
        print("SBI intrest rate: 6%")
class HDFC(bank):
    def intrest(self):
        print("HDFC intrest rate: 5.5%")
class ICIC(bank):
    def intrest(self):
        print("ICIC intrest rate: 6.9%")

banks=[SBI(),HDFC(),ICIC()]
for j in banks:
    j.intrest()



    
        

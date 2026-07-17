"""
inheritance
===========
it is an oop concept where one class (child/derived) acquired the properties and methods of another class (parent/base).

class parent:
    pass
class child(parent):
    pass

1.single inheritance
--------------------
a child class inherits from one parent is single inheritance.

class animal:
    def sound(self):
        print("animals")
class cat(animal):
    def sound1(self):
        print("meow")
        
c=cat()
c.sound()
c.sound1()

class father:
    def house(self):
        print("10 acres")
class son(father):
    def land(self):
        print("is mine")
s=son()
s.house()
s.land()

multiple inheritance
--------------------
a child inherits more than one parent is called multiple inheritance

class father:
    def action(self):
        print("driving")
class mother:
    def action1(self):
        print("cooking")
class son:
    def action2(self):
        print("coding")
class sister(father,mother,son):
    def action3(self):
        print("fighting")
s=sister()
s.action()
s.action1()
s.action2()
s.action3()

multi-level
-----------
one child class becomes the parent for another class

class father:
    def house(self):
        print("10 acres")
class son(father):
    def land(self):
        print("is mine")
class sis(son):
    def work(self):
        print("all")
s=sis()
s.house()
s.land()
s.work()

class f:
    def action(self):
        print("10")
class m(f):
    def action1(self):
        print("acres")
class s(m):
    def action2(self):
        print("is")
class d(s):
    def action3(self):
        print("mine")
e=d()
e.action()
e.action1()
e.action2()
e.action3()

hierarchial
-----------
multiple childs inherits from the same parent

class f:
    def action(self):
        print("10")
class s(f):
    def action1(self):
        print("kg")
class m(f):
    def action2(self):
        print("gold")
class da(f):
    def action3(self):
        print("is mine")
a=da()
b=m()
c=s()
a.action3()
a.action()
b.action2()
b.action()
c.action1()
c.action()

hybrid inheritance
------------------
this is the combination of two or more types of inheritance
example of multiple+multi-level

class a:
    def action(self):
        print("hi")
class b(a):
    def action1(self):
        print("welcome")
class c(a):
    def action2(self):
        print("to")
class d(b,c):
    def action3(self):
        print(" my world")
e=d()
e.action()
e.action1()
e.action2()
e.action3()

super()
-------
this super() function is used to access the parent class methods or constructor in the child class...

class a:
    def show(self):
        print("your")
class b(a):
    def show1(self):
        print("are")
class c(b):
    def show2(self):
        print("mine")
class d(c):
    def show3(self):
        super().show1()
        super().show2()
        super().show3()
        print("babe")
e=d()
e.show()
"""





class animal:
    def sound(self):
        print("animals")
class cat(animal):
    def sound1(self):
        print("meow")
class dog(cat,animal):
    def sound2(self):
        print("bow bow")
c=dog()
c.sound2()
c.sound()
c.sound1()

class father:
    def house(self):
        print("10 acres")
class son(father):
    def land(self):
        print("is mine")
class sis(son):
    def work(self):
        print("all")
s=sis()
s.house()
s.land()
s.work()

class father:
    def action(self):
        print("driving")
class mother:
    def action1(self):
        print("cooking")
class son:
    def action2(self):
        print("coding")
class sister(father,mother,son):
    def action3(self):
        print("fighting")
s=sister()
s.action()
s.action1()
s.action2()
s.action3()


class f:
    def action(self):
        print("10")
class m(f):
    def action1(self):
        print("acres")
class s(m):
    def action2(self):
        print("is")
class d(s):
    def action3(self):
        print("mine")
e=d()
e.action()
e.action1()
e.action2()
e.action3()

class f:
    def action(self):
        print("10")
class s(f):
    def action1(self):
        print("kg")
class m(f):
    def action2(self):
        print("gold")
class da(f):
    def action3(self):
        print("is mine")
a=da()
b=m()
c=s()
a.action3()
a.action()
b.action2()
b.action()
c.action1()
c.action()


class a:
    def action(self):
        print("hi")
class b(a):
    def action1(self):
        print("welcome")
class c(a):
    def action2(self):
        print("to")
class d(b,c):
    def action3(self):
        print(" my world")
e=d()
e.action()
e.action1()
e.action2()
e.action3()



class a:
    def __init__(self,name):
        self.name=name
class b(a):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
c=b("sanjay",32)
c.display()


class a:
    def show(self):
        print("your")
class b(a):
    def show1(self):
        print("are")
class c(b):
    def show2(self):
        print("mine")
class d(c):
    def show3(self):
        super().show()
        super().show1()
        super().show2()
        print("babe")
e=d()
e.show3()


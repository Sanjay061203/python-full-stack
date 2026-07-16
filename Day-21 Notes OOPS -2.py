





"""
constructor
----------
-->This constructor initializes the object automatically when it is created.....
"""
class Batch:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def names(self):
        print("Name:",self.name)
        print("Branch:",self.branch)
b4=Batch('Yogesh','EEE')
b4.names()


#
class fam:
    def __init__(self):
        self._name="Yogesh"
f=fam()
print(f._name)

#
class bank:
    def __init__(self):
        self.__pin = "4400"
Ac=bank()
print(Ac._bank__pin)

#
class Bank:
    def __init__(self):
        self.__pin = "7700"
    def display(self):
        print(self.__pin)
oc=Bank()
oc.display()

#Encaplation
#--> Means wrapping the data and methods into a single unit (class while controling to the data)
class atm:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        self._balance += amount
        print(self._balance)
tran=atm(balance=int(input("Enter Amount:")))
tran.deposit(amount=int(input("Enter Amount:")))

#private,public,protected
class school:
    def __init__(self,name,branch,age):
        self.name=name
        self._branch=branch
        self.__age=age
    def display(self):
        print(self.name)
        print(self._branch)
        print(self.__age)
s=school("yogesh","eee",22)
s.display()

class display():
    def __init__(self,a,b):
        self.__a=a#private
        self._b=b#protect
class demo(display):
    def output(self):
        #print(self._b)#protect we can acces in child class and parent class
        print(self.__a)#private we can acces in private only
d=demo(5,6)
d.output()     

        








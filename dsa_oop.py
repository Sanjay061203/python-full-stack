'''
function --> house
class --> power house

class classname:
    """docstring"""
    attributes (define the data)
    ......
    ......
    def fname(self):#behaviour
    def __init__(self):
        statements(s)...
        ................

obj = classname()


#students -->name,age
class students:
    """students details"""
    name = "akash"
    age = 20
    place = "vizag"

    def details(self):
        print(f'{self.name} is in {self.place} and age of {self.age} years')
#creation of objects
s1 = students()
print(s1)
#print(dir(s1))
print(s1.age)
print(s1.details(),s1.name,s1.age,s1.place)
s1.details()
s2 = students()
s2.details()


class students:
    """student details for multiple students"""
    def details(sanjay,name,age,place):
        sanjay.name=name
        sanjay.age=age
        sanjay.place=place
        #sanjay.age=age

    def display(self):
        print(f'hi {self.name} your currently at {self.place} and celebrating your {self.age} birthday')
        print(f'hi {self.name} welcome to {self.place} {self.age}')

s1=students()
s1.details(name="rocky",place="vizag",age=22)
print(s1.name,s1.place,s1.age)
s1.display()
print(s1.__class__)
print(s1.__doc__)
print(s1.__dict__)
s2=students()
s2.details("sanjay",22,"hyd")
s2.display()
print(s2.__dict__)

class students:
    """student details for multiple students"""
    def __init__(sanjay,name,age,place):
        sanjay.name=name
        sanjay.age=age
        sanjay.place=place
        
    def display(self):
        print(f'hi {self.name} your currently at {self.place} and celebrating your {self.age} birthday')
        print(f'hi {self.name} welcome to {self.place} {self.age}')


s1=students("rock",22,"vizag")
s1.display()
print(s1.__dict__)
s2=students("ganesh",23,"hyd")
s2.display()
print(s2.__dict__)


class cars:
    """you can get the best cars here"""
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price

    def display(self):
        print(f'we have {self.brand} with {self.name} at {self.price}')

c1=cars("audi","vxi2",9999999)
c1.display()
print(c1.__dict__)
c2=cars("ferrari","lvx4",785643)
c2.display()
print(c2.__dict__)


class users:
    def __init__(self,username):
        self.user=username
    def display(self):
        print(f'username is {self.username}')

u1=users("rocky")
print(u1.user)
#u1.display()
print(u1.user)
u1.user="sanjay"
print(u1.user)
'''

class users:
    def __init__(self,username,_otp):
        self.user = username
        self._otp = _otp

    def display(self):
        print(f'username is {self.user}')
        print(f'OTP is {self._otp}')

u1 = users("sanjay",4352)
u1.display()
u1._otp = 5435
u1.display()

        




    
        
    


    

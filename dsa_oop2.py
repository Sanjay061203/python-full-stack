'''
single inheritance

class baseclass: #parent class
    statements.....
class derivedclass(baseclass):#child class
    statements....

class user:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def fullname(self):
        return f'{self.fname + self.lname}'

#u1=user('sanjay','rocky')
#print(u1.fullname())

class update_user(user):
    def update(self):
        return f'{self.fname.title().strip()+" "+self.lname.title().strip()}'
#u1=update_users('sanjay','rocky')
#print(u1.fullname())
u1 = update_user('sanjay ',' rocky')
print(dir(u1))
print(u1.fullname())
print(u1.update())


class RBI:
    cash = 9999999999
    @classmethod
    def rbi_cash(sanjay):
        return f'availiable cash with RBI is {sanjay.cash}'
#b1=RBI()
#print(b1.cash)
#print(b1.rbi_cash())
#print(RBI.cash)
#print(RBI.rbi_cash())
class sbi(RBI):
    pass
#b1=sbi()
#print(b1.cash)
#print(b1.rbi_cash())

class HDFC(RBI):
    amount = 69000
    @classmethod
    def hdfc_cash(sanjay):
        print(f'hdfc cash is {sanjay.amount}')
        print(f'total accessible cash is {sanjay.amount + RBI.cash}')
b1 = HDFC()
print(b1.cash)
print(b1.amount)
print(b1.rbi_cash())
b1.hdfc_cash()


class father:
    def __init__(self,fproperty):
        self.fproperty = fproperty
    def father_property(self):
        print(f'father property is {self.property}')

#u1 = father()
#u1.father_property()
class kid(father):
    pass
#u1 = kid()
#print(u1.property)
#u1.father_property()

class kid(father):
    def __init__(self):
        super().__init__()
        self.property = 891011
        #super().__init__()
    def kid_property(self):
        print(f'kid property is {self.property}')
        print(f'kid and father property is {self.property+self.property}')

u1 = kid()
u1.father_property()
u1.kid_property()

class father:
    def __init__(self,fproperty):
        self.fproperty = fproperty
    def father_property(self):
        print(f'father property is {self.fproperty}')

class kid(father):
    def __init__(self,kproperty,fproperty):
        super()l.__init__(fproperty)
        self.kproperty = kproperty
        #super().__init__()
    def kid_property(self):
        print(f'kid property is {self.kproperty}')
        print(f'kid and father property is {self.fproperty+self.kproperty}')

u1 = kid(500000,250000)
u1.kid_property()
u1.father_property
print(u1.__dict__)

class square:
    """area of sqaure"""
    def __init__(self,x):
        self.x = x
    def area(self):
        return f'area of square is {self.x*self.x}'

class rectangle(square):
    """derived class"""
    def __init__(self,y,x):
        self.y = y
        super().__init__(x)
    def area(self):
        super().area()
        return f'area of rectangle is {self.x*self.y}'

r1 = rectangle(6,9)
print(r1.area())
x,y = map(int,input("enter values: ").split(','))
s1 = rectangle(x,y)
print(s1.area())

class users:
    """basic features"""
    def voice_call(self):
        print("user can make voice calls")
class notifications:
    """notifications"""
    def send_notification(self):
        print("user can get pop-up")
class premiumusers(users,notifications):
    """extra features added"""
    def verfication_badge(self):
        print("user is verififed and bluetick added")

u1 = premiumusers()
u1.verfication_badge()
u1.voice_call()
print(dir(u1))

class users:
    """users class"""
    def send_message(self):
        print("user send message")
    def voice_call(self):
        print("making voice calls")
class busers(users):
    """first class"""
    def create_catalog(self):
        print("details added")
class pusers(busers):
    """second class"""
    def verification_badge(self):
        print("account is verified")
u1 = pusers()
u1.verification_badge()
u1.create_catalog()
u1.send_message()
u1.voice_call()
'''
class amazon:
    def operation(self):
        print("operation is going on",end=" ")
class payment(amazon):
    def operation(self):
        print("payment is done")
class items(amazon):
    def operation(self):
        print("items added to cart")
        super().operation()
class wishlist(amazon):
    def operation(self):
        super().operation()
        print("items added to wishlist")

w=wishlist()
w.operation()
i=items()
i.operation()
p=payment()
p.operation()

        
        
        
    

        
    

    


    

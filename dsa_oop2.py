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
'''

class father:
    def __init__(self):
        self.property = 4567
    def father_property(self):
        print(f'father property is {self.property}')

#u1 = father()
#u1.father_property()
class kid(father):
    pass
u1 = kid()
print(u1.property)
u1.father_property()

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
        
    

    


    

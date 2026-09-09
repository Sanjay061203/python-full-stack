"""
def <funname>(parameters):
#'''doc dtring'''
statements(s)...
.................#body of func
return value(s)...
fname(args)#func call
"""
"""
def add(a,b):
    '''addition function'''
    c=a+b
    return c
print(add(4,78))
c,d='sanjay','rocky'
print(add(c,d))
e,f=map(str,input("enter values: ").split(','))
print(add(e,f))
print(add([1,3,4],[4,5,6]))
#print(add(1,2,3,4)) positional arguments fail
"""

#variable length arguments--*args we can pass any number of positional
#arguments-->data will be stored in tuple...
def sample(*a):
    print(a)
    print(type(a))
sample()
sample(1,2,3,4)
sample('sanjay',[1,2],'rocky',2+5j)

marks = [1,2,3,4,5,6,7,8,9]
sample(marks)
sample(*marks)

a,*b,c=1,2,'sanjay','rocky',34,56,432,4544,32,465,2345
print(a)
print(b)
print(c)

def add(*a):
    print(a)
    result = 0
    for i in a:
        #print(i)
        #if type(i) == int or type(i) == float
        if type(i) in [int,float]:
            result += i
    return result
print(add(2,3,4))
print(add(23,43,543,43,'sanjay',43,543,'rocky',34.54,435.43,4356.8765))

#keyword arguments-->we can pass the name for the arguments
def batch(name,age,place='hyd'):
    print(f'hi my name is {name} and my age is {age} and i am from {place}')
batch('sanjay',22,'viz')
batch(place='vjy',age=23,name='rocky')
batch(age=28,name='rocky')

print(4,5)
print(4,5,sep=':')

#keyword variable length arguments (**kwargs)-->any number of
#keyword arguments,data is stored in dictionary

def batch(**a):
    print(a)
    print(type(a))
batch()
batch(name='sanjay',age=22,place='hyd',branch='cse')

data = {'name':['rocky','prem'],
        'place':['hyd','viz']}

data.update({'batch':'PFS-VSP-004'})
batch(**data)

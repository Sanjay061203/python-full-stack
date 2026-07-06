"""
functions()
===========
it is a block of code that can be reusable
it avoids repeated line of code...

2 types of functions()
=====================
1.built-in-function()
---------------------print(),max(),type(),min(),sum()

2.user defined()
================
it starts with a keyword "def"

def fun_name(parameter):#definition line
----------------------
----------------------
----------------------
fun_name(arguments)#calling line
eg
--
def add(a,b):
    print(a+b)
add(3,5)
eg
--
def s():
    print("hello")
s()

types of argumrnts
==================
1.requared arguments
====================we have to pass same number of arguments with def of fun.
eg
--
def sub(z,x):
    print(z)
sub(8)

2.default arguments
===================
eg
--
def sub(z,x):
    print(z+x)
sub(z=67,x=89)

3.keyword arguments
===================we can pass as a pair like (variable = datatype)
eg
--

num = int(input(""))
num_ = int(input(""))
num_1 = int(input(""))
def add(x,y,z):
    print(x)
    print(y)
    print(z)
add(num,num_,num_1)

4.variable length
=================can pass n number of arguments and just use args in the parameters,will receive tuple of arguments
eg
--
num = int(input(""))#* for tuples
num_ = int(input(""))
num_1 = int(input(""))
num_2 = int(input(""))
def add(*x):
    print(x)
    print(y)
    print(z)
    print(a)
add(num,num_,num_1,num_2)

eg
--
def all_(**any):# ** for dict
    print(any['age'])
    print(any['name'])
all_(name = "rocky",age = 22)




num = int(input(""))
num_ = int(input(""))
num_1 = int(input(""))
num_2 = int(input(""))
def add(*x):
    print(x)
    print(y)
    print(z)
    print(a)
add(num,num_,num_1,num_2)


num = int(input(""))
num_ = int(input(""))
num_1 = int(input(""))
num_2 = int(input(""))
def add(*x):
    print(x)
    print(y)
    print(z)
    print(a)
add(num,num_,num_1,num_2)

num = 22#global variable
def fun_():
    print(num)
fun_()

print(num)


def fun_():#local variable
    num = 22
    print(num)
fun_()

print(num)

num = 22# to change the global variable by using keyword(global) that can change completely inside the fun
def fun_():
    global num
    num = 55
    print(num)
fun_()
"""

num = int(input(""))
num_ = int(input(""))
num_1 = int(input(""))
num_2 = int(input(""))
def add(*x):
    print(x)
add(num,num_,num_1,num_2)

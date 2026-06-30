"""
input formatting from user
--------------------------

input()
=======
the input() function is used to take input from the user

1.int()
=======
eg
--
num = int(input("enter number: "))
num_2 = int(input("enter number: "))
print(num+num_2)

2.str()
=======
eg
--
a = (input("enter char: "))
b = (input("enter char: "))
print(a+b)

3.float()
=========
eg
--
b = float(input("enter num: "))
print(a+b)
print(a,"is ur salary")

4.list()
========
eg
--
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(a)
print(b)

5.tuple()
=========
eg
--
a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
c = tuple(input().split())
print(a)
print(b)
print(c)

6.EVAL()
=======
eg
--
a = eval(input("enter: "))
print(type(a))

7.f.string{()}
==============
eg
--
a = eval(input("enter: "))
b = eval(input("enter: "))
print(a,"your age is ",b)
print(f"{a} your age is {b}")

8.modulas()
===========
eg
--
a = eval(input("enter: "))
b = eval(input("enter: "))
print(a,"your age is ",b)
print(f"{a} your age is {b}")
print("my name is %s i'm %s years old" %(a,b))








"""
a = eval(input("enter: "))
b = eval(input("enter: "))
print(a,"your age is ",b)
print(f"{a} your age is {b}")
print("my name is %s i'm %s years old" %(a,b))

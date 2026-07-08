"""
lambda function()
=================
this is also called as annonymous function..
a lambda function can take n number of arguments but having only one expression.
eg
--
s = lambda x,y,z,a,b,c : x+y+z+a+b+c*x*z
print(s(10,34,2,4,3,323))

filter()
========
it is a built-in-function used to filter elements from an itterables such as list,tuple and set based on conditions.

syntax
------filter(function,itterable)
--it returns filter object so we convert that
eg
--
n = eval(input("enter number: "))
s = filter(lambda a: a%2==0,n)
print(list(s))
print(tuple(s))
print(set(s))


list comprehension()
====================
this offers a shorter syntax when we want to create a new list from the old

syntax
------varaiable_name = [expression loop condition]
eg
--
o = [1,2,3,4,5,6,7] with comdition
n = [i for i in o if i%2==0]
print(n)


eg
--
o = [1,2,3,4,5,6,7] without comdition
n = [i for i in o ]
print(n)

dictionary comprehension()
==========================
this offers a shorter syntax when we want to create a new dict from the old dict

syntax
------variable_name = [expression loop]
"""

old_dict = {1:2,3:7,5:8}
new_dict = {i:j for (i,j) in old_dict.items() if i%2 != 0}
print(new_dict)

#passing by value()
def fun(a):
    for i in a:
        print(i+2)
fun([1,2,3])
fun((1,2,3))

#passing by reference()
a = (1,2,3)
def fun(a):
    for i in a:
        print(i)
fun(a)

#return keyword()it is a function if a return is excuted then it will exit from the function  with certain returned values
def fun(n):
    return 5+n
a = fun(10)
b = fun(89)
print(a)
print(b)

#built in functions()
import builtins

builtin_functions = [name for name in dir(builtins)
                     if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"total builtin functions are {len(builtin_functions)}") 

#recursive functions()
#======================that calls itself repeatedly until a specified condition in met...
#syntax
"""
def fun_name(parameters):
    if condition:-->base case
    return statement
    else:
        return statement
print(fun_name(arguments))
"""

def fun_name(n):
    if n == 1:
        return 1
    else:
        return n * fun_name(n-1)
n = 5
print(fun_name(n))

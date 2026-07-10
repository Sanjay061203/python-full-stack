"""
GENERATORS()
============
it is a special funciton that returns the iterator. instead of returning all the  values at once
here we are going to used yield keyword

def sun():
    yield 1
    yield 2 
    yield 3
moon = sun()
print(next(moon))
print(next(moon))
print(next(moon))

working of generators()
=======================
when a function is called
it won't execute function immediately
will return generate object
pauses at each yield
it executes only when next() is called.
eg
--
def sun():#with generators
    print("hi")
    yield 1
    print("hello")
    yiel 2
    print("fghgfd")
    yield 3
moon = sun()
print(next(moon))
print(next(moon))
print(next(moon))
print(next(sun()))
print(next(sun()))
print(next(sun()))
print(next(sun()))

eg
--
def fun(s):
    for i in range(s):
        yield i*i
r = fun(6)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

without generators()
--------------------
def fun(s):
    for i in range(s):
        print(i*i)
fun(6)

FUNCTION()
==========
return
returns complete result
function will end after the return the values
more memory usage
this function never resume
GENERATORS()
============
yield
return one value at once
pauses after every yield
less memory usage
resumes after next()

yield keyword()
---------------
this will produces the value
but the yield pauses the function
and yield will save the functions current state
yield will continues where it stoped...

next() keyword
==============
the next() function is used to retrieve the next value from a generator

stop itetration()
=================
calling next() function after all values retrive then it will raise stop iteration exception

genetrator expression()
======================
the generator expression is similar to a list comprehension nut uses parenthesis () imstead of []


 

"""

gen = (x*x for x in range(435))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))





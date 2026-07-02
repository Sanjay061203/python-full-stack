"""
loops
=====

1.for loop()
============it is used to itterate over a squence, list,tuple,dict
eg
--
n = [1,2,3,4,5,567,766]
for i in n:
    print(i)
eg
--
n = "dfgnthnd rghbdrt rthgw"
for i in n:
    print(i)
eg
--
n = (324,45,23452,34,435,34634,5643,56)
for i in n:
    print(i)
eg
--
n = {"name":"sanjay",
     "age":22,}
for key in n.values():#u can print keys(),values(),items()
    print(key)

else in for loop()
==================
else block will be executed after the for loop but in case the loop is breaked then it will never entered in the esle. 

eg
--
n = [1,2,3,4,5,567,766]
for i in n:
    print(i)
else:
    print("program ended")

while loop()
============while loop will execute untill the condition becomes true
eg
--
i = 1
while i < 5:
    print(i)
    i+=1


conditional statements()
========================

1.break()
=========
eg
--
n = [1,2,3,4,5,567,766]
for i in n:
        if i == 3:
            break
        print(i)
else:
        print("program ended")


2.continue()
============
eg
--
n = [1,2,3,4,5,567,766]
for i in n:
        if i == 3:
            continue
        print(i)
else:
        print("program ended")

3.pass()
========
eg
--
n = [1,2,3,4,5,567,766]
for i in n:
        if i == 3:
            pass
        print(i)
else:
        print("program ended")

4.range()
=========range() is a in-built function that is used to generate a sequence upto user given range
syntax-->range(start,end,step)
eg
--

for i in range(1,10):
    print(i)
for i in range(2,11):
    if i%2==0:
        print(i)


5.assert()
==========

--used to check the condition , but it wil raise an error incase it is false...
eg
--
n = eval(input("enter age: "))
assert n >= 18, "you must have 18 years"





"""

for i in range(0,100,2):#odd numbers
    print(i)



   
    
"""   
n = {"name":"sanjay",
     "age":22,}
for key in n.values():
    print(key)
    
n = eval(input("enter number: "))
for i in  n:
    if (i%2==0):
        print(f"{i} is even number")
    else:
        print(f"{n} is odd number")
    
"""

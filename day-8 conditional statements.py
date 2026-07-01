"""
 statements
 ==========

 1.conditions()
 --------------
 if()
 ====
 eg
 --
 n = int(input())
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

    
 if-else()
 =========
 eg.1
 ----
 n = int(input())
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
eg.2
----
n = eval(input("enter pin: "))
if n == 3530:
    print("welcome to rocky's bank")
else:
    print("you entered incorrect pin")

 
 nested if()
 ===========
 eg
 --
 n="6600"
pin=input("enter pin: ")
if len(pin)==4:
    if pin==n:
        print("welcome to rocky's bank")
    else:print("you entered incorrect pin")
else:
    print("you entered incorrect pin")
 
 elif()
 ======
 eg
 --
 marks = int(input("enter marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("FAIL")
 

 2.control()
 ===========

 1.break()
 2.continue()
 3.pass()

 3.loop()
 ========

 1.for()
 2.while()
 
"""
"""
n = eval(input("enter pin: "))
if n == 3530:
    print("welcome to rocky's bank")
else:
    print("you entered incorrect pin")
"""
"""
marks = int(input("enter marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("FAIL")
"""       
"""  
n = eval(input("enter numbers: "))
m = max(n)
print(m)
"""


n = (input("enter word: "))
v = "a,e,i,o,u,A,E,I,O,U"
if n in v:
    print("vowel")
else:
    print("consonant")
    
a = eval(input(""))
b = eval(input(""))
c = eval(input(""))
d = eval(input(""))
if (a>b and a>c and a>d):
    print(a)
if (b>a and b>c and b>d):
    print(b)
if (c>a and c>b and c>d):
    print(c)
else:
    print(d)

"""
modules()
=========
a module a python file(.py) that contains resuable code
1.varaiables
2.classes
3.objects
4.statements

why this
--------
instead of writing the same code repeatedly, we can store it in a module and use it whenever needed...

types of  modules()
===================
1.user-defined

import specific function
------------------------
from sanjay import add,sub
print(sanjay.add(34,657))
print(sanjay.sub(34,657))
print(sanjay.mul(34,657))
print(sanjay.divi(34,657))
print(sanjay.int_divi(34,657))
print(sanjay.pow(34,657))

import sanjay 
print(sanjay.add(34,657))
print(sanjay.sub(34,657))
print(sanjay.mul(34,657))
print(sanjay.divi(34,657))
print(sanjay.int_divi(34,657))
print(sanjay.pow(34,657))

from sanjay import *
print(add(34,657))
print(sub(34,657))
print(mul(34,657))
print(divi(34,657))
print(int_divi(34,657))
print(pow(34,657))

import sanjay as s
print(s.add(34,657))
print(s.sub(34,657))
print(s.mul(34,657))
print(s.divi(34,657))
print(s.int_divi(34,657))
print(s.pow(34,657))

2.built-in()
============
1.math
------

import math as m
print(m.sqrt(25))#square root
print(m.factorial(25))#factorial
print(m.pow(2,5))#power
print(m.pi)#pi
print(m.ceil(4.67654))#round up
print(m.ceil(4.23654))#round up
print(m.floor(4.23654))#floor


2.os
----
the os module is used to interact with operating system

import os
print(os.getcwd())current directory
os.mkdir("rocky")create folder
os.rmdir("rocky")remove folder


3.sys
-----
this will provide the information about python interpeter

import sys
print(sys.version)

4.random
---------
used to generate random values

import random
print(random.randint(1000,9999))


"""

import random
print(random.randint(1000,9999))
print(random.randint(1000,9999))
print(random.randint(1000,9999))
print(random.randint(1000,9999))
print(random.randint(1000,9999))

colors = ['brown','red','green','yellow']
print(random.choice(colors))


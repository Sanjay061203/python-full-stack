

"""
syntax error
-----------
-----------
for i in range(1,10)
    print(i)

o/p--Syntax Error
-----------------
for j in range(1,10):
    print(j)
Indentation Error
-----------------

    a=20
for j in range(a):
    print(j)
else:
print()

o/p-IndentationError

Value error
----------

num = int(input("Enter a num:"))

o/p-Value Error


try:The try block will test the code for error
syntax-- try:

except:This except let us handle the errors in the code
syntax: except:

try:
    num = int(input("enter a num: "))
except NameError:
    print('will get name error')

else:if the try block does not have any error than the else block will exc
finally:
"""

try:
    num = int(input("enter a num: "))
    num_2=int(input("Enter a num: "))
    print(num / num_2)
except ZeroDivisionError:
    print('will get zero devision error')
except ValueError:
    print('Will get value error ')

else:
    print('No error')
finally:
    print("end")
               
               

'''
s = [i for i in range(1,11) if i>4]
print(s)
print(type(s))

s = (i for i in range(1,11) if i>4)
print(s)
print(type(s))


#Generators --> Generators are also special functions in python which
#produces values one by one,which makes program memory efficient

def details():
    return f'sanjay'
    return 'rocky'
print(details())

def details():
    return 'sanjay','rocky'
print(details())



def dinesh():
    yield 'i'
    yield 'luv'
    yield 'u'
    yield 'wifeyboss'
w=dinesh()
print(*dinesh())
print(type(w))
#print(next(w))
#print(next(w))
#print(next(w))
#print(next(w))

for i in w:
    print(i)


s = (i for i in range(1,11) if i>4)
#print(*s)
print(type(s))
for i in s:
    print(f'number {i}')



a,*b,c=3,4,5,6,7,8,9,'sanjay','rocky','raaka',567
print(a)
print(b)
print(c)


try:
    #program to execute/conditions...
except:
    #it will handle the error
finally:
    #irrespective of try,except it executes




try:
    a,b = map(int,input("Enter the Values").split(','))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Make sure the denominator values is only +ve/-ve not zero")
except ValueError:
    print("Invalid value type error entry only intergers")
except NameError:
    print("Sargiaa Chuskoo")
    





try:
    a=[234,654,765,765,765]
    print(a[4])
    a.append('sanjay rocky')
    print(a)
except IndexError:
    print("sorry")
except AttributeError:
    print("ediot")
finally:
    print("well done")
'''
with open('rocky.txt','r+') as f:
    print(f.read())
    f.write(" welcome to guinness world records")
    f.write(" dinesh handsome boy")
    print(f.read())

    










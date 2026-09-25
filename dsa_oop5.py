'''
s = [i for i in range(1,21) if(i%2==0)]
print(s)
print(len(s))
r = [i**2 for i in range(1,21) if(i%2==0)]
print(r)
print(len(r))


s = int(input("enter value: "))
def r(s):
    result = []
    for i in range(1,s):
        if s>0:
            if i%2==0:
                result.append(i)
    return result
print(r(s))

h = list(filter(lambda i:i%2==0,range(1,21)))
print(h)

k=list(filter(lambda x:len(x)>=3,['code','gnan','sanjay','rocky']))
print(k)
print(len(k))


s=['code','gnan','sanjay','rocky']
a=list(map(lambda x:len(x),s))
print(a)
print(len(a))



s=list(map(int,input("enter values: ").split(',')))
print(s)


r,k,j=map(str,input("enter values: ").split())
print(f'r value is{r},k value is {k},j value is {j}')


names=list(map(str,input("enter names: ").split()))
print(names)


s=['sanjay','rocky','nsksnk','simha']
r=list(map(lambda x:x.upper(),s))


prices=[2500,3500,5000,7500]
n_prices=list(map(lambda x:x-(x*10/100),prices))
print(n_prices)


#list comprehension with if-else usage
#syntax -->[true_value if condition else false_value for expression in collection

#filter even odd values in given range
result = ["even" if i%2==0 else "odd" for i in range(1,21)]
print(result)


#even number will be squared odd will be printed as it is
result = [i**2 if i%2==0 else i for i in range(1,21)]
print(result)


#nested loops with list comprehension
#syntax --> [expression for item1 in iterable1 for item2 in iterable2]

c=['red','green','violet','blue','ornage']
s=['xxs','xs','s','m','l','xl','xxl','xxxl']
m=[(i,j)for i in c for j in s]
print(m)
'''

m=[25,25,24,20]
w=[35,30,45,48]
f=[(i+j)for i in m for j in w]
print(f)
f=list(map(lambda i,j:(i+j),m,w))
print(f)

#nested comprehension with if-else combination
#syntax --> [true_value if <condition> else false_value for item1 in
#iterable for item2 in iterable2

f=[i+5 if(i>=j) else i-5 for i in range(1,10) for j in range(1,10)]
print(f)
print(*f)
for i in f:
    print(i,end=' ')









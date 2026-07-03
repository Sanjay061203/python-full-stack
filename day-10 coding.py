"""

"""
"""
n = eval(input("enter number: "))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count += 1
if count == 0:
    print(f"{n} is prime number")
else:
    print(f"{n} is not a prime number")
"""
"""
n = 10
for i in range(1,n+1):
    count = 0
    for j in  range(1,i+1):
        if j % i == 0:
            count += 1
    if count == 2:
        print(f"{j} is prime")

"""
"""
n = int(input("enter number: "))
count = 0
for i in range(1,n-1):
    for j in range(1,i+1):
        count += 1
        print(count, end = " ")
    print()
"""
"""
n = int(input("enter number: "))
length_ = len(str(n))
sum = 0
for i in str(n):
    sum += int(i)
if sum == n:
    print(f"{n} is armstrong")
else:
    print(f"{n} is not an armstrong")
    """
n = eval(input("enter number: "))
for i in range(n):
    print(" "*(n - i -1),end = " ")
    print("*" *(2 * i + 1))

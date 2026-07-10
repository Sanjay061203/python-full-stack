"""
nums = [34,54,534,654]
def removes_(nums):
    for i in nums:
        if i == i:
            nums.remove()
    print(i)
removes_(nums)

prime = 7
count = 0
def prime_not(prime,count):
    for i in range(1,prime+1):
        if prime % j == 0:
            count += 1
    if count == 2:
        print(f"{prime}is a prime")
    else:
        print(f"{prime}is not a prime")
prime_not(prime,count)

s = "sanjay rocky is a monster"
count = 0
def counting(s,count):
    g = s.split(' ')
    for i in s:
        count+=1
    print(count)
counting(s,count)
        
"""
s = "SANJAY IS A ROCKING HUMANS"
cap_count = 0
small_count = 0
space_count = 0
def cap_small(s,cap_count,small_count,space_count):
    for i in s:
        if i.isupper():
            cap_count += 1
        elif i.islower():
            small_count += 1
        else:
            space_count += 1
    print(f"there are total {cap_count} capitals in string")
    print(f"there are total {small_count} capitals in string")
    print(f"there are total {space_count} capitals in string")
          
cap_small(s,cap_count,small_count,space_count)

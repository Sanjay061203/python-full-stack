email_ids=["saketh@codegnan.com","sanjay@gmail.com","rocky@gmail.com","theodore@gmail.com"]

print(email_ids[0])
print(email_ids[1])
print(email_ids[2])
print(email_ids[3])

print(email_ids[-2:])

email_ids.extend(["sun@gmail.com","moon@gmail.com","star@gmail.com"])
print(email_ids)
for i in email_ids:
    print(f"mailid of person is {i}")

s={}
print(type(s))
s=dict.fromkeys(email_ids)
print(s)

for i in range(len(email_ids)):
    s[i+1] = email_ids[i]
print(s)

print(dict(enumerate(email_ids,1)))


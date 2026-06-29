"""
type conversions
----------------
this is process of converting one data type to another
int-->string;float
eg
--
num = 89
num_2 = float(num)
print(num_2)
print(type(num))
so = str(num)
print(so)

float-->string;integer
eg
--
num = 8.9
how = str(num)
print(how)
print(type(how))
num_2 = int(num)
print(num_2)


string-->integer;float;list;tuple
eg
--
hai = "78"
num = int(hai)

hello = "67.89"
num_2 = float(hello)
print(num_2 + num)

eg2
---
any_ = "python4567432"
con_ = list(any_)
print(con_)
con_2 = tuple(any_)
print(con_2)

list-->string,list
eg
--
var_ = ['p','y','t','h','o','n']
text = "".join(var_)
print(text)

eg
--
var_ = ['p','y','t','h','o','n']
text = tuple(var_)
print(text)
eg_2
----
var_ = ['45','98','78','87','65','56']
text = tuple(var_)
print(text)

tuple-->string;lists
eg
--
fam = ('h','e','l','l','o')
text_2 = "".join(fam)
print(text_2)







built in functions
------------------

string()
float()
int()
list()
dict()
"""
fam = ('h','e','l','l','o')
text_2 = "".join(fam)
print(text_2)

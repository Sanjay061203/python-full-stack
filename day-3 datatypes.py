""" Data Types:What Kind type data can be store
#1:Integer"""
#int
#num=8
#float
num_2=7.89#Numeric Data Type
num = 6.89
print(num//2)#Floor Devision nearest value

#string:It is sequence of the character that Enclosed in ' '," " is called string
#string is immutable:which cannot be change
#string is Concatinatio:Here,the(+)operator act as to concatinate more than two strings...
#Example of Concatinatio
so="python"
any_=" is a Language"
print(so+any_)

#Indexing:This is used to access the particular to the string by passing index position value
#Index starts from o
#we have negative indexing count position from last to first..

so="Python is a Language"
print(so[-1]) 
print(so[3])

#Methods:1,Replace() 2,Join() 3,split() 4,count()
#Replace():Remove the old string and add new string,This method is used to change any substring in that particular string
#syntax:variable.replace("Old string","New string",count)
so="python is a Language"
print(so.replace("python","Java"))
print(so.replace("a","b",2))#It replace by two times
#2,Join():This method used to add new substring after each char  in the string...
#syntax:"String".join(variable_name)
so="python is a Language"
print("-".join(so))
#3,split():This Method can divide the string into different index into list,based on the string pass by us..
#syntax:variable_name.split('substring')
so="python is a Language"
print(so.split())
#4,count():It used to count the substring in the particular string and also specify the index position
#syntax:variable_name.("substring",start index,ending index)
so="python is a Language"
print(so.count("a",0,11))
#string bulit-in functions
#1,len 2,max() 3,min()
#len:This will find the length of the string,which is number char present in the string
#syntax:
so="python is a Language"
print(len(so))
#max():we will get the max char in the string
so="python is a Language"
print(max(so))
#min():we will get min char in the string
so="python is a Language"
print(min(so)) #output space is min character,space is also a character
so="pythonisalanguage"
print(min(so))
a="Yogesh","Yogesh"
print(a)



























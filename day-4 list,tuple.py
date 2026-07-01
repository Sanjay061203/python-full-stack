#List:It is collection of dufferent dataypes that are Enclosed in [],separated by ,
#list is muttable
all_type =[1,'Python',[1,2]]
for j in all_type:
    print(j)
#Method:1.Append() 2,Extend() 3,pop() 4,remove() 5,index()
#append():It used add new item into list, it will take one item
#ex:
any=[1,2,3,4]
print(any)
any.append(5)
print(any)
#Mutable                                Immtable
#The data type can be modified          #It can not be modified
any=[1,2,3,4]                           #a="python is Language"
print(any)                              #x= print(a.replace('J','p'))
                                        #print(x)
any.append(5)                           #print(a)"""
print(any)              
#apppend:Example
a=["Apple","Yogesh",2]
a.append(10)
print("Append:",a)
#Extend:This is also in the last index position but it will give each value in the each index position,It will take interables: staring,tuple
a=["Apple","Yogesh",2]
a.extend([10,20])
print("Extend:",a)
#Index()
any=[1,2,'python is a language',[45,78,"Java is a Language",[1,23],90],'Hello']
print(any[3][3][1])#This is called indexing different types of data

#pop():Used to Delete the item from th list, but it will del based on index position
#synatx:variable_name,pop(index position)
any=[1,2,3,4,5]
any.pop(2)
print("Pop:",any)

#Remove():It used to del the item from the list,but it will del the direct value from it
#synatx:variable_name,pop(value)
any=[1,2,3,4,4,5,'yogesh']
any.remove(4)
print("Remove:",any)

#Index:
any_=[56,[1,2],['python','java',['python is a language',153,90],[78,6],'I Know c']]
#find Knowand 153 #index,count,insert
print(any_)
print(any_[0])


#Tuple:It is collection of dufferent dataypes that are Enclosed in (),separated by ,
#it is immutable it can not be modifiy
how=(1,2,3,4,"Python",[4,5,'yogi'],(90,60))
print(type(how))
print(how)
#index():
print(how.index("Python"))

print("index:",how[2])
#count():It count occurences
print(how.count(3))
print(len(how))

result=[1,2]
result.append([3,4])
print(result)
a=[1,2,[3,4],5]
print(a)

a=[10,[20,30]]

print(a[1][0])

a=[1,2,3]
x=tuple(a)
print(x)





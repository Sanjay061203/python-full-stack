"""Operators
1,Arithmetic Operator = +,-,*,
2,Assignment Operator
3,Comparision Operator
4,Logical Operator
5,Identity Operator
6,Membership Operator
7,Bitiwise Operator

1,Arithmetic Operator"""
a=5
b=20
print(a+b) #Addition
print(a*b) #Multiplication
print(a**b)#Power Exponational
print(a-b) #Sub
print(a/b) #Division(Quotient)
print(a//b)#Flooring(only one value means Quotient Value will get)
print(a%b) #Division(Remainder)

#2,Assignment Operator:=,+=,-=,*=,%=
a=20
a +=4
print(a)
a -=4
print(a)
a *=4
print(a)
a %=b
print(a)
a //=b
print(a)


#3,Comparision Operator:==,!=,>,<,>=,<=)
a= 20
b=7
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)#It used in Grade Ex:The marks is Greater than equal to year is true In the Grades
Marks = 90
if Marks >= 90:
    print("a+")
    
print(a>=b)#It used in Grade Ex:The marks is Greater than equal to year is true In the Grades

#4,Logical Operator:And,Or ,Not
#1,And:It return true if both are true
a=20
b=7
c=89
print("And",a >=b and b<=c) #20>=7,7<=89:True Both are return true
#2,Or:It return true if any true
print(a >=b or b<=c)# If any one condition is true is called or operator
#3,Not:Reverse the output
print(not(a >=b or b<=c))# Expcte the output false will become the true

#5,Identity Operator:is,isnot
#Diffirence between is and ==

#is:Obeject is same or not
a=20
b=20
print(a==b)
print(a is b)
a=[20,30]
b=[20,30]
print(id(a))
print(id(b))
print(a is b)
print(a==b)


#isnot:Not the same object
a=20
b=20
print(a==b)
print(a is not b)
a=[20,30]
b=[20,30]
print(a is not b)
print(a==b)


#6,Membership Operator:In,notin
#in:It will tells the inside number is they or not
a=[1,2,3,4,5]
print(2 in a) # It will tells the inside number is they or not
#notin:It will tells the inside number is they or not
print(2 not in a)

#7,Bitiwise Operator:&,<<,>>,|,^
print(6 & 2) #Binary 5:0101,3:0011=0001 #It gives  the Binary values 
print(6 | 2) #Or:Returns 1 if at least one value is 1 result becomes 1 5:0101 3:0011,compare:0111=7
print(5 ^ 3) #Xor:Compares bits:1-if both bits are different,0-if both bits are same,Ex:5:0101,3:0011,compare:0110=6
print(~5) #Not:Reverse all bits:formuale:~n=-(n+1) -5=-(5+1),-5=-6
print(5<<1)#Left Shift(<<):Each left shift 1 position means Multiply by 2, 2 means Multiply by 4,5:Convert into Binary 5:0101,1010=10
print(9<<1)#<<1 Multiply by 2 so answer is 18:9*2:18
print(9<<3)#<<2 Multiply by 4 so answer is 36:9^4:36
print(9>>1)#Right Shift :>>1 Divide by 2,>>2 Divide by 4,3 Divide by 8:>>1:9/2=4
print(9>>2)#2:9/4=2






















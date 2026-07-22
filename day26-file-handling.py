""" --------------------File handling---------------------
File Handling is an object that gives more options like creating,updating
two ways  to open the file...
1.open()
----------

syntax----> do=open('file_name','mode')
            close()
2.with (keyword)
---------------
syntax --> with open ('file_name','mode')as do:

with open('yogesh.txt','r')as do:
    print(do.read())

3.modes
-------

r --> used to read the file,in case the file is not present it will raised error
w --> used to  write the text inside the file and it will override the text inside the file
a --> This is used to add the text at last postition inside the file
x-->This used to create a new by adding the inside the file,in case if the file present it will raise the error...

with open('H.txt','w')as do:
    print(do.write("we are using file handling and yogesh is good")) # it overides the file

with open('H.txt','w')as do:
    print(do.write("yogesh varma and lokesh "))

with open('H.txt','a')as do:
    print(do.write('sanjay and yogesh varma '))

with open('Hello.txt','x')as do:
    print(do.write('sanjay and yogesh varma '))

write():The write method functionality is used to add the text inside the file or update a file with a new text...
read():used to read a file and this read() will read file chunk by chunk..
with open('hello.txt','r')as do:
    print(do.read(4))

readline():This readline() function will read only
with open('hello.txt','r')as do:
    print(do.readline())
    
readlines():This function will read  whole file and give it in a list each line is
one index in that list



"""
with open('H.txt','r')as do:
    print(do.read())

with open('H.txt','w')as do:
    print(do.write("YOGESH LOVES "))


with open('H.txt','a')as do:
    print(do.write("loki"))

#with open('Hello.txt','x')as do:
    print(do.write("loki gymfreak"))


with open('hello.txt','r')as do:
    print(do.read(7))

with open('hello.txt','r')as do:
    print(do.readline())

with open('hello.txt','r')as do:
    print(do.readlines())



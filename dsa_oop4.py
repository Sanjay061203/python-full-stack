'''
oop-->encapsualtion,inheritance,polymorphism,abstraction

import abc
print(dir(abc))#returns the available methoods,classes...
from abc import ABC,abstractmethod
print(help(ABC))

#now we will create some base classes to have abstraction applied for all classes
class content(ABC):
    @abstractmethod
    def upload(self):
        pass

class photo(content):
    def upload(self):
        print('photo uploaded successfully')
        print('absolute pics have been captured')
        print('photo is posted')
class video(content):
    def upload(self):
        print('video is uploaded')
        print('video has best resolution')
        print('video is posted')
class reel(content):
    def upload(self):
        print('reel is uploaded')
        print('reel crossed 1M views')
        print('reel is successfully banned')

s1=[photo(),video(),reel()]
print(s1)
for content in s1:
    content.upload()
'''
l = [4,5,6,7,8]
for i in l:
    l.append(i**2)
print(l)
    


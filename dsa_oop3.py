'''
class hotstar:
    """default args usage"""
    def watch(self,*movie):
        self.movie=movie
        if movie==():
            print(f'welcome to my world')
        else:
            print(f'your watching {self.movie}')
s1=hotstar()
s1.watch()
s1.watch("KGF-2","vikram")

class jio:
    """args args usage"""
    def watch(self,movie=None):
        print(f'welcome to raaka')
    def add_to_wishlist(self,*movies):
        print(movies)
        for movie in movies:
            print(movie)
u1=jio()
u1.add_to_wishlist("kgf","kgf-2","raaka","leo")
u1.watch()


class jio:
    """usage of type of args"""
    def watch(self,movie=None):
        print(f'welcome to raaka')
    def list(self,content):
        self.content = content
        if isinstance(content,str):
            print(f'user watching {self.content}')
        elif isinstance(content,list):
            print(content)
            for movie in content:
                print(movie)

u1=jio()
u1.watch()
u1.list(["kgf","kgf-2"])

class jio:
    """usage of type of args"""
    def watch(self,movie=None):
        print(f'welcome to raaka')
    def list(self,content):
        self.content = content
        if isinstance(content,str):
            print(f'user watching {self.content}')
        elif isinstance(content,list):
            print(content)
            for movie in content:
                print(movie)

u1=jio()
u1.watch()
u1.list(["kgf","kgf-2"])


#free user --> can watch free content with advertisements
#premium user -->can watch premium content without advertisements
#vip user -->can watch premium content along with devices count,streaming

class User:
    def __init__(self, name):
        self.name = name

    def watch_content(self):
        print("User can watch content")


class FreeUser(User):
    def watch_content(self):
        print(self.name, "is a Free User")
        print("Can watch FREE content")
        print("Advertisements are shown")


class PremiumUser(User):
    def watch_content(self):
        print(self.name, "is a Premium User")
        print("Can watch FREE and PREMIUM content")
        print("No advertisements")


class VIPUser(User):
    def __init__(self, name, devices):
        super().__init__(name)
        self.devices = devices

    def watch_content(self):
        print(self.name, "is a VIP User")
        print("Can watch FREE and PREMIUM content")
        print("No advertisements")
        print("Number of devices:", self.devices)
        print("Streaming is available")


# Objects
free = FreeUser("Ravi")
premium = PremiumUser("Teja")
vip = VIPUser("Sanjay", 4)

# Calling methods
free.watch_content()
print()

premium.watch_content()
print()

vip.watch_content()

class User:
    def __init__(self, name):
        self.name = name
    def watch(self):
        print(self.name, "can watch free content with advertisements")


class Premium(User):
    def watch(self):
        print(self.name, "can watch premium content without advertisements")


class VIP(User):
    def __init__(self, name, devices):
        super().__init__(name)
        self.devices = devices
    def watch(self):
        print(self.name, "can watch premium content")
        print("Devices:", self.devices)
        print("Streaming available")



u1 = User("narasimha")
u1.watch()
u2 = Premium("shiva")
u2.watch()
u3 = VIP("Sanjay", 6)
u3.watch()



#u1.watch()
#u2.watch()
#u3.watch()
class jio:
    def watch(self):
        print('welcome to raaka')

class freeusers(jio):
    def watch(self):
        super().watch()
        print(f'free movies with break')

class premium(freeusers):
    def watch(self):
        super().watch()
'''
class watchhistory:
    def duration(self,hours):
        self.hours=hours
    def __add__(self,other):
        return self.hours+other.hours
u1=watchhistory()
u1.duration(25)
u2=watchhistory()
u2.duration(35)
print(u1.__add__(u2),u1+u2,u1.hours+u2.hours)


        

"""
Dictionary
----------
-->dict is a key : value pair seperates by : , and keys are unique in the place of keys we have use immutable data type...
methods()
---------

-->keys()
   ------ used to get all the keys from the dict
   syntax--> variable_name.keys()
   eg: details_ = {"name" : "rocky",
            "age" : 22,
            "gender" : "male"}
        print(details_.keys())
-->values()
   --------used to get all the values from the dict
   syntax--> varaiable_name.values()
   eg:details_ = {"name" : "rocky",
            "age" : 22,
            "gender" : "male"}
        print(details_.values())
-->items()
   -------used to get both keys n values
   syntax-->varaiable_name.items()
   eg:details_ = {"name" : "rocky",
            "age" : 22,
            "gender" : "male"}
        print(details_.items())
-->clear()
   ------it is used to clear the dict
   eg:details_ = {"name" : "rocky",
            "age" : 22,
            "gender" : "male",
            "aadhaar" : 77520456,
            "institute" : "codegnan"}
print(details_["name"])
print(details_["age"])
print(details_["gender"])
print(details_["aadhaar"])
print(details_["institute"])
details_.clear()
print(details_)

-->update()
   -------- used to update the values of keys
   eg:details_ = {"name" : "rocky",
            "age" : 22,
            "gender" : "male",
            "aadhaar" : 77520456,
            "institute" : "codegnan"}
print(details_["name"])
print(details_["age"])
print(details_["gender"])
print(details_["aadhaar"])
print(details_["institute"])
details_.update({"name" : "sanjay"})
details_.update({"mob" : 35473527})
print(details_)
"""

details_ = {"name" : "rocky",
            "age" : 22,
            "gender" : "male",
            "aadhaar" : 77520456,
            "institute" : "codegnan"}
print(details_["name"])
print(details_["age"])
print(details_["gender"])
print(details_["aadhaar"])
print(details_["institute"])
details_.update({"name" : "sanjay"})
details_.update({"mob" : 35473527})
print(details_)
"""
   sets()
   ------it is a collection of unordered elements thar are seperated by ,
   -------their mutable
   ------can remobve duplicate valuesby itself
   eg:s = {2,3,4,5,6}
      print(s)
   methods()
   ---------
   union()(|)
   ---------- it is usesd to combine the elements from both sets
   syntax-->set1 | set2 or set1.union(set2)
   eg:s = {2,3,4,5,6}
      a = {1,7,8,98,65,6,5}
      print(s | a)
      print(s.union(a))
   intersection()
   --------------common element from both sets
   syntax-->set1.intersect(set2)
   eg:s = {2,3,4,5,6}
      a = {1,7,8,98,65,6,5}
      print(s & a)
      print(s.intersection(a))
       symmetric difference()
       ----------------------all different elements from both sets
       syntax-->set1.symmetric_difference(set2)
       eg:s = {2,3,4,5,6}
          a = {1,7,8,98,65,6,5}
          print(s ^ a)
          print(s.symmetric_difference(a))
    add()
    ----used to add new elementsinto set
    eg:s = {2,3,4,5,6}
       a = {1,7,8,98,65,6,5}
       s.add(45)
       a.add(345)
       print(s)
       print(a)
    remove()
    --------to del the elements from set based on elements
    eg:s = {44,55,66,2,3,4,5,6}
       a = {1,7,8,98,65,6,5}
       s.remove(4)
       a.remove(345)
       print(s)
       print(a)
       s.pop()
       print(s)

       discord()
       --------it dosen't throws an error
       eg:s = {44,55,66,2,3,4,5,6}
          a = {1,7,8,98,65,6,5}
          s.discard(77)
          print(s)
       
"""
"""
s = {44,55,66,2,3,4,5,6}
a = {1,7,8,98,65,6,5}
s.discard(77)
print(s)
"""
details_ = {"name" : "rocky",
            "age" : 22,
            "gender" : "male",
            "aadhaar" : 77520456,
            "institute" : "codegnan"}
details_.clear()
print(details_)

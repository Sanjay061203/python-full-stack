from datetime import datetime
current_ = datetime.now()
print(current_)
print(current_.strftime('%y'))
print(current_.strftime('%m'))
print(current_.strftime('%d'))
print(current_.strftime('%H'))
#print(current_.strftime('%I'))
print(current_.strftime('%M'))
print(current_.strftime('%S'))
print(current_.strftime('%p'))

"""
%d--day
%m--month
%y--year
%H--hour
%M--minutes
%S--seconds
%I--12 hour clock
%p--am or pm
"""

import calendar
print(calendar.calendar(2003))

import calendar
print(calendar.month(2003,12))
print(calendar.weekday(2003,12,7))
print(calendar.isleap(2003))


import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
"""
Data Analysis:It is the process of inspecting,cleaning,transform and modeling data to discover useful insights,support decision
making and identify patterns, it is widely used in industries such as finanace,healthcare,marketing and technology.

Types of Data Analysis
1.Descriptive Analysis - Summarizing data
2.Diagonstic Analysis - Understanding casuses
3.Predictive Analysis - Forecasting future outcome
4.Prescriptive Analysis - suggesting actions based on data
------------
-->Clean the data
-->Transfer the data
-->Vi
"""
#numpy:Numpy is a library in python which is know as numerical python,This numpy have different diamentinal array such as
#1d,2d,3d how to used the we have to import libarary as import numpy as np
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)

#1Dimensional array
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1)
#Indexing in array:As we used indexing in the list or tuple,here the same way it works,By calling index position from array,we will
#get the value,And Neagative indexing also will work
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1[1]) # Normal index
print(arr_1[-1]) #Neagative Indexing
#Slicing:
print(arr_1[::-1])
print(arr_1[:2])
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1.sum())
print(arr_1.mean())
print(arr_1.max())
print(arr_1.min())

#2D:
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr_1)

#3D:
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)

#reshape()
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)

arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr_1.reshape(3,2))

arr_1 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(arr_1)
print(arr_1.reshape(4,3))

#pandas : It is an powerful python library and this is bulit on the top of numpy
"""-->By using pandas data manipulation will be done..
-->pandas have data structures like series and dataframes
-->to use this we have import the library"""
55
import pandas as pd
Data = pd.Series([2000,4000,7000],
                 index = ['Earphone','Charger','Mobile']
)
print(Data)

import pandas as pd
Data = pd.Series([2000,4000,7000],
                 index = ['Earphone','Charger','Mobile']
)
print(Data)

import pandas as pd
df = {
    "Product" :['Laptop','Mobile','Earphone'],
    "Brand" :['Mac','Realme','Iphone'],
    "Price" :[5700,1500,2500],
    "stocks" :[5,15,9],
    "Sales" :['Amazon','Offline','Flipcart']
}
data = pd.DataFrame(df)
print(data)



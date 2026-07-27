
import matplotlib.pyplot as sanjay
s=[2026,2025,2024,2023,2022,2021,2020,2019,2018,2017]
r=[100,250,150,240,320,310,120,300,240,330]
sanjay.figure()

sanjay.subplot(2,4,1)
sanjay.plot(s,r,color='black')
sanjay.title("aeroplane sales")
sanjay.xlabel("years")
sanjay.ylabel("sales")


sanjay.subplot(2,4,2)
sanjay.bar(s,r,color='black')
sanjay.title("aeroplane sales")
sanjay.xlabel("years")
sanjay.ylabel("sales")





subjects=['python','java','c','c++']
stu=[69,13,50,60]

sanjay.subplot(2,4,3)
sanjay.pie(stu,labels=subjects,autopct='%1.lf%%',colors=['red','yellow','blue','green'])
sanjay.legend(subjects)
sanjay.title('courses')


sanjay.subplot(2,4,4)
sanjay.scatter(s,r,color='black')
sanjay.title("aeroplane sales")
sanjay.xlabel("years")
sanjay.ylabel("sales")


sanjay.subplot(2,4,5)
sanjay.hist(s,bins=200)
sanjay.title("aeroplane sales")
sanjay.xlabel("years")
sanjay.ylabel("sales")


sanjay.subplot(2,4,6)
sanjay.plot(s,r,color='black')
sanjay.title("aeroplane sales")
sanjay.xlabel("years")
sanjay.ylabel("sales")


sanjay.subplot(2,4,7)
sanjay.bar(s,r,color='black')
sanjay.title("aeroplane sales")
sanjay.xlabel("years")
sanjay.ylabel("sales")

sanjay.subplot(2,4,8)
sanjay.scatter(s,r,color='black')
sanjay.title("aeroplane sales")
sanjay.xlabel("years")
sanjay.ylabel("sales")
sanjay.show()

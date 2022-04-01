import random
import time
#A
a = 1.0
b = 500.0
mylist = list()
mytuple = tuple()
for i in range(1,10000):
    mytuple = (i,random.uniform(a, b))
    mylist.append(mytuple)
#print(mylist)

#B
random.shuffle(mylist)
#print(mylist)

#C
after = 0
before = time.time()
for x in mylist:
    if x[0] == 5000:
        after = time.time()
        #print(x[1])
print("loop research time elapsed :", after-before)

#D
mydict = dict()
mydict.update({x[0] : x[1] for x in mylist})
#print(mydict)

#E
before = time.time()
val = mydict.get(5000)
after = time.time()
print("dict research time elapsed :", after-before)
#print(val)
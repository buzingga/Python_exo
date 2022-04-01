import matplotlib.pyplot as plt
import numpy as np

#A
import csv
file = open("FCHI.csv", 'r')
colreader = csv.DictReader(file,delimiter=',')

#B
lower_stock_list = list()
highest_stock_list = list()
for col in colreader:
    lower_stock_list.append(float(col["Low"])) 
    highest_stock_list.append(float(col["High"]))
lower_stock_index = min(lower_stock_list)
highest_stock_index = max(highest_stock_list)

#reset file iterator
file.seek(0)
next(file)

for col in colreader:
    if lower_stock_index == float(col["Low"]):
        print("lower_stock_index: ",lower_stock_index,"| min date: ",col["Date"])
    if highest_stock_index == float(col["High"]):
        print("highest_stock_index: ",highest_stock_index,"| max date: ",col["Date"])

#C
R = (10000,10033,55212,2372372,23823,288323,39293,329932,329392,3293,232323,382372742)
for i in range(1,12):
    Ry *= (1+R[i])-1

plt.plot(R, linestyle = 'dotted')
plt.show()
#D


file.close()

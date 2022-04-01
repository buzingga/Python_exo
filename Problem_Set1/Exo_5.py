r = 0.07
I = 100000
CF = (10000,25000,30000,50000)
N = len(CF)
sum = 0
for i in range(len(CF)):
    sum = sum + (CF[i]/pow(1+r,i))
NPV = -I + sum
print("NPV:",NPV)
# A
divisors = list()
sum = 0
for i in range(1,100):
    for n in range(1,i):
        if i%n == 0:
            divisors.append(n)
    for x in divisors:
        sum += x
    if i == sum:
        print(i," is a perfect number")
    divisors.clear()
    sum = 0
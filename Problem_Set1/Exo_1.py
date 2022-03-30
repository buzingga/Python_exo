def swap(a,b,c):
    temp = c
    c = b
    b = a
    a = temp
    return a,b,c

print("Hello Word !")
a,b,c = 1,2,3
print(a,b,c,"\n")
a,b,c = swap(a,b,c)
print(a,b,c,"\n")


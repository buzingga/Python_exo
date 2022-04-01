# A
username1 = input("please enter a name: ")
username2 = input("please enter a name: ")
# B
username1.lower()
username2.lower()
# C
username1 = set(username1)
username2 = set(username2)
# D
union = username1 & username2
inter = username1 | username2
print("union :",union)
print("inter :",inter)
# E
similarity = len(union)/len(inter)
print("similarity :",similarity)
# A
val = input("please enter the current stock price :")
current_stock_price = float(val)
tick_size = 0.01
val = 10
# for i in range(-10,10):
#     quotable_price = current_stock_price + i*tick_size
#     print(quotable_price)
#B
i = -10
while i < 10:
     quotable_price = current_stock_price + i*tick_size
     i+=1
     print(quotable_price)
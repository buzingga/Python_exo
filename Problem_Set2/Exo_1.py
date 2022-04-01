# A
stock_price = input("please enter a stock price: ")
stock_price = int(stock_price)
# if stock_price > 50:
#     intrinsic_value = stock_price - 50
# else:
#     intrinsic_value = stock_price
# B
if stock_price >= 100:
    intrinsic_value = 0
elif stock_price > 50:
    intrinsic_value = stock_price - 50
else:
    intrinsic_value = stock_price
print(intrinsic_value)
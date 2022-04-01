# A
stock_price = input("please enter a stock price: ")
stock_price = int(stock_price)
temp = stock_price - 50
#intrinsic_value = stock_price > 50 and stock_price - 50 or stock_price
# B
intrinsic_value = ((stock_price,temp)[stock_price > 50],0)[stock_price >= 100]
print(intrinsic_value)
# A
init_stock_price = input("please enter a stock price: ")
init_stock_price = int(init_stock_price)
#intrinsic_value = stock_price > 50 and stock_price - 50 or stock_price
# B
stock_price = init_stock_price
first_intrinsic_value = stock_price > 50 and init_stock_price - 50 or stock_price
print(first_intrinsic_value)
second_intrinsic_value = stock_price >=100 and 0 or first_intrinsic_value
print(second_intrinsic_value)
third_intrinsic_value = stock_price > 50 and first_intrinsic_value or second_intrinsic_value
print(third_intrinsic_value)
#Assignment-1 Questions

# swap two numbers without using a third variable
'''
x =20
y = 10
print("before swapping ","x=" ,x, " y=",y)

x +=y
y = x-y
x-=y

print("after swapping ","x=" ,x, " y=",y)
'''

#price of each apple is 7.5rs.total there are 100 apples.20 apples are sold at 10rs ,30 apples are sold at 20rs.find the profit or loss.
#Also find the no of apples that can be bought with the earned profit.
'''
total_num_apples =100
buy_amount = 7.5
print("Total no of apples", total_num_apples," price of each apple is ",buy_amount)

total_price = total_num_apples*buy_amount
print("Total price of 100 apple is ",total_price)

apples_sold1 = 20
price_apples_sold1 = 10
print("No of apples sold  in first set is ",apples_sold1, "price of sold apples is ", price_apples_sold1)
total_price_sold1 = apples_sold1*price_apples_sold1
print("Total price gained from first set of apples is ",total_price_sold1)

apples_sold2 = 30
price_apples_sold2 = 20
print("No of apples sold  in second set is ",apples_sold2, "price of sold apples is ", price_apples_sold2)
total_price_sold2 = apples_sold2*price_apples_sold2
print("Total price gained from first set of apples is ",total_price_sold2)

total_apple_sold = apples_sold1 + apples_sold2
print("total no of sold apples is ",total_apple_sold)

Total_amount_sold = total_price_sold1 + total_price_sold2
print("Total sold amount is " , Total_amount_sold)

profit = Total_amount_sold  - total_price
print("Profit earned is ",profit)

remain_apple = total_num_apples  - total_apple_sold
print("no of unsold apples is ", remain_apple)

apple_from_profit = int(profit/buy_amount)
print("Total no of apples that can be bought from earned profit is ",apple_from_profit)
'''



# 1
'''
num_days = int(input("Enter the number of days : "))
def myfunc(num_days):
    years = int(num_days/365)
    months = int(num_days/30)
    days = int((num_days%365) % 7)
    print(num_days," is equal to ",years,"year,",months,"month,",days,"day")

 '''   

# 2
'''
print("Fibonacci Series")
a =0
b =1
c = 1
while c<=20:
    print(c)
    a = b
    b =c
    c =a+b

'''

#3
'''
player1_name = input("enter player name 1: ")
player2_name = input("enter player name 2: ")
choices = print("select from rock/scissor/paper")
player1_choice = input("enter player 1 choice: ")
player2_choice = input("enter player 2 choice: ")

if(player1_choice=="rock" and player2_choice=="scissor"):
    print(player1_name,"with choice ",player1_choice," Wins and",player2_name,"with choice",player2_choice,"Lose")
elif(player1_choice=="rock" and player2_choice=="paper"):
    print(player2_name,"with choice",player2_choice,"Wins and ",player1_name,"with choice ",player1_choice,"Lose")
elif(player1_choice=="scissor" and player2_choice=="paper"):
    print(player1_name,"with choice ",player1_choice," Wins and",player2_name,"with choice",player2_choice,"Lose")
else:
    print("Tie")

'''

#4
'''
basic_salary = int(input("enter your basic salary: "))

def allowances_func(basic_salary):
    hra = (22/100)*basic_salary
    da = (18/100)*basic_salary
    ta = (10/100)*basic_salary
    allowances = hra + da + ta
    return allowances


def deductions_func(basic_salary):
    if(basic_salary > 8000):
        proftax = 200
    else:
        proftax = 150
        
    pf = (12/100)*basic_salary
    insurance = (8/100)*basic_salary
    deductions = proftax + pf + insurance
    return deductions
   
gross_salary = basic_salary + allowances_func(basic_salary)
print("Gross salary is ",gross_salary)
net_salary = gross_salary - deductions_func(basic_salary)
print("Net salary is ", net_salary)
'''
#5
'''
vowel_count_a = 0
vowel_count_e = 0
vowel_count_i = 0
vowel_count_o = 0
vowel_count_u = 0
consonant_count = 0

input_string ="""

Python is a widely used general-purpose, high level programming language. It was created
by Guido van Rossum in 1991 and further developed by the Python Software Foundation.
It was designed with an emphasis on code readability, and its syntax allows programmers
to express their concepts in fewer lines of code"""


input_string =input_string.lower()

for i in range(0,len(input_string)):
    
    if (input_string[i] == "a"):
        vowel_count_a += 1
    elif(input_string[i] == "e"):
        vowel_count_e += 1
    elif(input_string[i] == "i"):
        vowel_count_i += 1
    elif(input_string[i] == "o"):
        vowel_count_o += 1
    elif(input_string[i] == "u"):
        vowel_count_u += 1    
    elif (input_string[i] >="a" and input_string[i] <="z"):
        consonant_count+=1
    else:
        pass
        
print("Count of a : ",vowel_count_a)
print("Count of e : ",vowel_count_e)
print("Count of i : ",vowel_count_i)
print("Count of o : ",vowel_count_o)
print("Count of u : ",vowel_count_u)
print("total no of consonants : ",consonant_count)

'''
#6
'''
input_str = input("enter a string : ")
input_str = input_str.lower()
rev_input_str = input_str[::-1]

if(input_str == rev_input_str):
    print("palindrome")
else:
    pass
    
'''
#7
'''
email = input("Enter your email id : ")
count = 0
if(email[0]!="@" and email[0] !="."):
    for i in email:
        if(i == "@" or i=="."):
            count+=1
        elif(count == 2):
            print("valid mail ")
            break
        if(count > 2):
            print("invalid email")
            break
else:
    print("invalid email ")
'''

#9
'''
bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
    
while(True):
    print(""" Enter choice
            1. View the bakery items
            2. Add the item into the cart
            3. View the cart
            4. Update item in the cart
            5. Remove item from the cart
            6. Checkout and generate bill
            """)
    

    choice = int(input("enter a choice: "))

    if(choice == 1):
        print("Bakery Items: \n", bakery_items)

    elif(choice == 2):
        key_items = input("enter an item : ")
        value_items = int(input("enter item price :"))
        if key_items in bakery_items:
            print("Item already exists")
        else:
            bakery_items[key_items]= value_items
            print(bakery_items)

    elif(choice == 3):
        print("Items in cart \n ", bakery_items.keys())


    elif(choice == 4):
        print(bakery_items)
        key_items = input("enter the item name you want to update: ")
        value_items = input("enter the updated price : ")
        if key_items not in bakery_items:
            print("item not available")
        else:
            update_item = {key_items:value_items}
            bakery_items.update(update_item)
            print("After updation the price of",key_items,"is ",value_items)
            print( "Updated Cart \n ",bakery_items)
    
    elif(choice ==5):
        print(bakery_items)
        key_items = input("enter the item name you want to remove: ")
        del(bakery_items[key_items])
        #remove_item = bakery_items.pop(key_items)
        print("New Cart \n" , bakery_items)

    elif(choice ==6):
        bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
    
        print("******Available Bakery Items*******  \n ")
        for keys,values in bakery_items.items():
            print("Item - ",keys,"       Price - ",values)
        
        print(" \n ")    
        purchase_item = list(map(str,input("Please enter the items to Purchase:").split()))
    
        print(" \n ")
        for item in purchase_item:
            print("Purchased Items - ",item)

        print(" \n ")
     
        items_count = list((item,purchase_item.count(item)) for item in purchase_item)
        print("Total count of purchased items : ",items_count)
        print(" \n ")   
        cart_total = 0
        for item in purchase_item:
            item_price = bakery_items.get(item,0)
            cart_total += item_price
        print("Amount to be paid ", cart_total)
        print(" \n ")
        print(" ************Thank you for Shopping.Have a good day**************")

    else:
        print(" Invalid Choice " )

'''
#8

def computepay(hour,rate):

    pay=(hour*rate)+((hour%40)*(rate*1/2))

    return pay

hour=int(input("Enter hour:"))

rate=int(input("Enter rate:"))

print("Total pay: ",computepay(hour,rate))

def hotel_cost(night):

    return 140*night

def plane_ride_cost(city):

    price_list={"Charlotte": 183,"Tampa": 220,"Pittsburgh": 222,"Los Angeles": 475}

    return price_list[city]

def rental_car_cost(days):

    cost=40*days

    if (days>=7):

        cost-=50

    elif (days>=3):

        cost-=20

    return cost

def trip_cost(city,days):

    return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)

def trip_cost(city,days,spend_money=None):

    if(spend_money!=None):

        return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)+spend_money

    else:

        return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)

days = int ( input ( "Enter the trip days: "))


days=int(input("Enter the trip days: "))

print("enter the city name you going to visit:")

city=input("Charlotte , Tampa , Pittsburgh , Los Angeles:  ")

print("Total cost: ",trip_cost(city,days))

spend_money= int(input("Enter the spending cost:"))

print("Total cost: ",trip_cost(city,days,spend_money))



        
        
        
    

    

    

    
    

    
        


    
   
    


   
    
    



   
    









    
    

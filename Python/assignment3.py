# Assignment 3
 #1. Take an input from the user and check if the number is prime.
'''
num = int(input("Enter a number : "))

if num > 1:
    for i in range(2,int(num/2)+1):
        if(num%i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num,"is a prime number")
else:
    print(num, "is not a prime number")
'''
#2. Take  a starting range and ending range from the user and find out all the prime numbers
# in that range

starting_range = int(input("Enter the starting number: "))
ending_range = int(input("Enter the ending number: "))

for num in range(starting_range,ending_range + 1):
    if num > 1:
        for i in range(2,num):
            if(num%i) == 0:
                break
        else:
            print(num)
            
   

        
        
    
    

    

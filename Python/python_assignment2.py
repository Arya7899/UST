#ASSIGNMENT 2

#1.take an input from user and find whether the  number is odd or even
#2.take 2 inputs from user, number and conversion type. convert the given number into
#fahrenheit or celcius
#3.take length in inches as input from user and convert it into meters and centimeters

#1
number = int(input("enter a number :"))
if(number%2 ==0):
    print("number is even")

else:
    print("number is odd")

#2

number = int(input("enter a number "))
conversion_type = input("choose C or F ")
if(conversion_type == 'F'):
    C = number
    F = C*(9/5) + 32
    print(C, "celcius = ",F, " FARENHEIT ")

else:
    F = number
    C =F*(5/9) - 32
    print(F, "farenheit = ",C, " celcius")

#3

length_inch = int(input("enter length in inches : "))
length_meters = int(length_inch/(39.37))
length_cms = int(length_inch*(2.54))
print("length in meters is ",length_meters)
print("length in cms is ", length_cms)
print(length_inch, "inches= ",length_meters,"meters ",length_cms ,"centimeters ")

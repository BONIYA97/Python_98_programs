# 6. Python Program to Swap Two Variables
a=3
b=4
print("Before swapping a={0} and b={1}".format(a,b))
temp=a
a=b
b=temp
print("After swapping a={0} and b={1}".format(a,b))

# 7. Python Program to Generate a Random Number
import random
rand=random.randint(0,10)
print(rand)

# 8. Python Program to Convert Kilometers to Miles
km=float(input("Enter the Kilometers"))
mile=km*0.621371
print("{0} km = {1} miles".format(km,mile))

#9. Python Program to Convert Celsius To Fahrenheit
celsius=float(input("enter the celsius"))
fahrenheit = (celsius * 1.8) + 32
print("{0} degree celsius is {1} Fahrenheit".format(celsius,fahrenheit))

#10. Python Program to Check if a Number is Positive, Negative or 0
num=int(input("enter a number"))
if(num==0):
    print(" number is zero")
elif(num>0):
    print("number is positive")
else:
    print("number is negative")


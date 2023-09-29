# 11. Python Program to Check if a Number is Odd or Even
num=int(input("enter a number"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")

# 12. Python Program to Check Leap Year
year=int(input("Enter the year"))
if((year%100==0) and (year%400==0)):
    print("{0} is a leap year".format(year))
elif((year%100!=0) and (year%4==0)):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

# 13. Python Program to Find the Largest Among Three Numbers
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>b and a>c):
    print("{0} is largest".format(a))
elif(b>a and b>c):
    print("{0} is largest".format(b))
else:
    print("{0} is largest".format(c))

# 14. Python Program to Check Prime Number
num=int(input("enter a number"))
c=0
if(num==1):
    print("not a prime number")
else:
    for i in range(2,num):
        if(num%i==0):
            c=c+1
            break
if(c==1):
    print("Not Prime number")
else:
    print(" Prime number")

# 15. Python Program to Print all Prime Numbers in an Interval

Limit=int(input("enter the limit"))

for i in range(0,Limit+1):
    if(i>1):
        for j in range(2,i):
            if (i%j) == 0:
               break
        else:
            print(i)



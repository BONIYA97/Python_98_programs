# 16. Python Program to Find the Factorial of a Number
def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))
num=int(input("enter number"))
factorial = fact(num)
print("factorial of {0} is {1}".format(num,factorial))

# 17. Python Program to Display the multiplication Table
num=int(input("enter number"))
for i in range(1,11):
    mul=num*i
    print("{0} * {1} = {2}".format(i,num,mul))

# 18. Python Program to Print the Fibonacci sequence

limit=int(input("enter the limit"))
count=0
f=1
i=0
print(i)
print(f)
while(count<=limit):
    fa=i+f
    i=f
    f=fa
    count=count+1
    print(fa)

# 19. Python Program to Check Armstrong Number
num=int(input("enter number"))
sum=0
temp=num
while(num>0):
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10

    print("Number is amstrong")
else:
    print("Number is not amstrong")

#20. Python Program to Find Armstrong Number in an Interval

lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
for num in range(lower,upper+1):
    sum=0
    temp=num
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem*rem)
        num=num//10
    if(sum==temp):
        print(temp)

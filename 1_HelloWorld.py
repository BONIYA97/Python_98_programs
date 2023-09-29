# 1. Python Program to Print Hello world!
print("hello world")

# 2. Python Program to Add Two Numbers
a=int(input("enter first number"))
b=int(input("enter second number"))
sum=a+b
print("sum of {0} and {1} is {2}".format(a,b,sum))

# 3. Python Program to Find the Square Root
import math
num=int(input("enter the number"))
Squareroot=math.sqrt(num)
print("square root of {0} is{1}".format(num,Squareroot))

# 4. Python Program to Calculate the Area of a Triangle
import math
a=float(input("enter first side"))
b=float(input("enter second side"))
c=float(input("enter third side"))
s = (a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle is =", area)

# 5.Python Program to Solve Quadratic Equation
import math
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
d=math.sqrt((b**2)-(4*a*c))
Solution1= (-b+d)/(2*a)
Solution2= (-b-d)/(2*a)
print("Solutions of given equation are {0} and {1}".format(Solution1,Solution2))
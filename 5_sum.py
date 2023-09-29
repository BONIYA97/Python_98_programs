# 21. Python Program to Find the Sum of Natural Numbers
limit=int(input("enter the limit"))
sum=0
for i in range(0,limit+1):
    sum=sum+i
print(sum)

# 22. Python Program to Display Powers of 2 Using Anonymous Function
limit=int(input("enter the power limit"))
power=list(map(lambda x: 2**x, range(limit)))
print(power)

# 23. Python Program to Find Numbers Divisible by Another Number
lst=[33, 25, 47, 20, 100, 37]
div=list(filter(lambda x: (x%5==0), lst))
print(div)

# 24.Python Program to Convert Decimal to Binary, Octal and Hexadecimal
dec=int(input("enter the decimal value"))
binary=bin(dec)
octal=oct(dec)
hexa=hex(dec)
print("binary value of {0} is {1}".format(dec,binary))
print("octal value of {0} is {1}".format(dec,octal))
print("hexadecimal value of {0} is {1}".format(dec,hexa))

# 25. Python Program to Find ASCII Value of Character
c='a'
print(ord(c))

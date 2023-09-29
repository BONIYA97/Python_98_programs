
# 26. Python Program to Find HCF or GCD
def hcf(num1,num2):
    list=[]
    if num1>num2:
        small=num2
    else:
        small=num1
    for i in range(1,small+1):
        if(num1%i==0 )and (num2%i==0):
            list.append(i)
            list.sort(reverse=True)
    return list[0]

num1=int(input("enter first number"))  
num2=  int(input("enter second number"))  
HCF=hcf(num1,num2)
print("HCF of {0} and {1} is {2}".format(num1,num2,HCF))

# 27. Python Program to Find LCM
num1 = 12
num2 = 14
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print("LCM of", num1, "and", num2, "is", lcm)

# 28.Python Program to Find the Factors of a Number
num=int(input("enter number"))  
for i in range(1,num+1):
    if(num%i==0):
        print(i)

# 29. Python Program to Make a Simple Calculator

print("----Basic Calculator----")
choice=int(input("Enter your choice 1/2/3/4"))
num1=int(input("enter first number"))  
num2=  int(input("enter second number")) 
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
if(choice==1):
    add=num1+num2
    print(add)
elif(choice==2):
    sub=num1-num2
    print(sub)
elif(choice==3):
    mul=num1*num2
    print(mul)
else:
    div=num1/num2
    print(div)

# 30. Python Program to Shuffle Deck of Cards
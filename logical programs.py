# 1.FACTORIAL PROGRAM

"""count = int(input("Enter the number to find factorial of : "))
a = 0
b = 1
print(a)
print(b)

for i in range(1 , count):
    c = a+b
    a = b
    b = c
    print(c)"""


# 2.PRIME NUMBERS PROGRAM

"""num = int(input ("Enter number to find the prime number : "))

for i in range(2 , num):
    if num%i==0:
        print(num , "is not a prime numbee")
        break
    else:
        print(num , "is a prime number")
        break""" 

# 3.PALINDROME PROGRAM

"""pstr = input("enter string to find palindrome : ")

if pstr == pstr[::-1]:
    print(pstr , "is a palindrome")
else:
    print(pstr , "is not a palindrome")"""

# 4.PRINTING SEQUENCE IN NEXT LINE

"""seq = input("enter a word to print in sequence : ")
index = 0

for i in seq:
    print(seq[0:index+1])
    index+=1"""


# 5.FACTORIAL

"""num = int(input("Enter number to find factorial : "))
fact = 1

for i in range(1 , num+1):
    fact = fact*i
print("Factorial of" , num , "is" , fact)"""

"""upperbound = int(input("provide upper bound value="))
fact = 1
for i in range(1 , upperbound+1):
    for j in range(1 , i+1):
        fact = fact*j
    print(i , "is" , fact)"""

# 6.SUM OF DIGITSOF GIVEN NUMBER

"""digits = int(input("Enter digits to find the number : "))
backupvalue = digits
sum = 0

while digits>0:
    remainder = digits % 10
    sum = sum + remainder
    digits = digits//10
print("sum of" ,backupvalue ,"is" , sum)"""

# 7. TEMPRATURE CONVERSION
# 0C = 32F 
# CELCIIUS TO FARENHEIT = F = C*9/5 + 32
"""celcius = float(input("Enter celcius value : "))
farhenheit = celcius*(9/5) + 32
print(f"The value of {celcius}celcius is {farhenheit}fahrenheit")"""

# FARENHEIT TO CELCIIUS = C = (F-32)* 5/9
"""farhenheit = float(input("Enter farhenheit value : "))
celcius = (farhenheit-32)*5/9
print(f"The value of {farhenheit}farhenheit is {celcius}celcius")"""

# 8.FACTORS OF A GIVEN NUMBER

"""num = int(input("Enter a number to find the factors of the number : "))
sum = 0

for i in range(1 , num+1):
    if num%i==0:
        print(i , "is factor of" , num)
        sum = sum+i
print("the sum of factors is : " , sum)"""

"""pstr = input("enter string to find palindrome : ")
st = eval(pstr)

if st == st[::-1]:
    print(st , "is a palindrome")
else:
    print(st , "is not a palindrome")"""

# 9.REVERSE NUMBER

"""num = int(input("enter s number : "))
temp = num

sum = 0
reverse = 0

while num>0:
    remainder = num%10
    reverse = reverse*10 + remainder
    num = num //10
print("reverse number is : " , reverse)

if (temp == reverse):
    print("palindrome")
else:
    print("not a p,aindriome")"""

# 10.WEIGHT CONVERSION

print("WEIGHT CONVERSION \n")
weight = float(input("Enter your weight : "))
unit = input("Kilograms or Pounds? (K or L) : ")

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight , 1)}{unit}")

elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight , 1)}{unit}")

else:
    print(f"{unit} is not valid")

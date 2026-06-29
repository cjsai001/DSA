#arithmetic operators
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#comparison operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#Logical operators
age = 20
print(age > 18 and  age < 30)

print(5 > 10 or 10 > 5)

print(not True)
print(not False) 

#Type casting
x = "10"
print(int(x) + 5)
 
price = "99.99"
print(float(price))

a = "21"
print("Age: " + str(int(a)))

#pratice
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

n = int(input())
print(n ** 2)
print(n ** 3)

a = int(input())
b = int(input())
print(a == b)     

n = int(input())
print(n > 0)


#mini challenges
a = 10
b = 23
print(a + b)
print(a - b)
print(a * b)
print(a % b)

a = int(input("Enter a number: "))
if a % 2 == 0:
    print("even")
else:
    print("odd")


age = int(input("Enter your age: "))
if age >= 18:
    print("your are eligible to vote")
else:
    print("your are not eligible to vote")


#leetcode
num = int(input("Enter a number: "))
print(-num)
    
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("It is divisible by 5")
else:
    print("It is not divible by 5")
    

a = int(input("Enter a number: ")) 
b = int(input("Enter b number: "))
if a > b:
    print(f"{a} is larger than {b}")
elif b > a:
    print(f"{b} greater than {a}")
else:
    print(f"{a} is equal to {b}")


a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

total = a + b + c

print(total)
print(total / 3)

if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is less than {a}")

if a > 0 and b > 0 and c > 0:
    print("all are positive")
else:
    print("not all are positive")

#Find which is biggest number
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

if a > b and a > c:
    print(f"{a} is greatest")
elif b > c and b > a:
    print(f"{b} is greater")
elif c > a and c > b:
    print(f"{c} is greatest")
else:
    print("all are equal")

#Finding the year is leap year or not
year = int(input("Enter a year:"))
if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")

#Print Numbers from 1 to 20
for i in range(1, 21):
    print(i)

#Multiplication Table
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#Count Digits
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Digits = ", count)

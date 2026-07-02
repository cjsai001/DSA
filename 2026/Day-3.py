#elif
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >=80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("fail")

#nested if
age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")

if age >= 18:

    if citizen == "yes":
        print("You are eligible to vote. ")
    else:
        print("Not eligible.")
else:
    print("too young.")



#for loop 
for i in range(0, 6):
    print("hello")

#while loop
count = 1
while count <=5:
    print(count)
    count += 2


#pratice
for i in range(1, 51):
    print(i)

for i in range(1, 51):
    if i % 2 == 0:
        print(i) 

for i in range(1, 51):
    if i % 2 != 0:
        print(i)

for i in range(0,10):
    print("sai")

n = int(input("Enter a table: "))
count = 1
while count <= 10:
    multiply = n * count
    print(f"{n} x {count} = {multiply}")
    count += 1

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
if  a > b and a > c:
    print(a)
elif  b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("all are equal")

n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

total = 0
for i in range(1, 101):
    total = total + i
print("sum = ", total)

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, 11):
    factorial = factorial * i
    print("factorial of ", i, "is", factorial) 

num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num //10
    print("Reverse: ", reverse)


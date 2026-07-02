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




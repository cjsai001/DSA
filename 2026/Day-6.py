1.Array
numbers = [10, 20, 30, 40, 50]
print(numbers)


2. Access Elements
Indexing starts from 0.
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[2])
print(numbers[-1])


3. Update Elements
numbers = [10, 20, 30]
numbers[1] = 100
print(numbers)


4. Add Elements
append()
Adds an element at the end.
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)


insert()
numbers = [10, 20, 40]
numbers.insert(2, 30)
print(numbers)


extend()
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

5. Remove Elements
remove()
numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)
pop()
numbers = [10, 20, 30]
numbers.pop()
print(numbers)
del
numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)
clear()
numbers = [10, 20]
numbers.clear()
print(numbers)


6. Length
numbers = [1, 2, 3, 4]
print(len(numbers))


7. Traversing a List
Using for loop
numbers = [10, 20, 30]
for num in numbers:
    print(num)
Using range()
numbers = [10, 20, 30]
for i in range(len(numbers)):
    print(numbers[i])


8. Membership
numbers = [5, 10, 15]
print(10 in numbers)
print(50 in numbers)


9. Sorting
Ascending
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)
Descending
numbers.sort(reverse=True)
print(numbers)


10. Reverse List
numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)
11. Find Maximum and Minimum
numbers = [4, 8, 2, 10]

print(max(numbers))
print(min(numbers))
12. Sum of Elements
numbers = [10, 20, 30]

print(sum(numbers))

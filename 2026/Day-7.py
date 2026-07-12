numbers = [10, 20, 30, 40, 50]
target = 30
found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)
        found = True
        break
if not found:
    print("Not Found")


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
numbers = [5, 10, 15, 20]
print(linear_search(numbers, 15))


numbers = [10,20,30,40,50,60,70]
target = 50
left = 0
right = len(numbers)-1
while left <= right:
    mid = (left + right)//2
    if numbers[mid] == target:
        print("Found at index", mid)
        break
    elif target < numbers[mid]:
        right = mid-1
    else:
        left = mid+1


#time complexity
numbers = [10,20,30]
print(numbers[1])


for num in numbers:
    print(num)


for i in numbers:
    for j in numbers:
        print(i, j)


numbers = [12, 45, 2, 78, 25]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)


numbers = [1,2,2,3,2,4]
target = 2
count = 0
for num in numbers:
    if num == target:
        count += 1
print(count)


numbers = [1,2,2,3,4,4,5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)

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

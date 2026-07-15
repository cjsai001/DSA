numbers = [5, 2, 8, 1, 4]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)


numbers = [64, 25, 12, 22, 11]
n = len(numbers)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
print(numbers)


numbers = [12, 11, 13, 5, 6]
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key
print(numbers)


numbers = [8, 3, 1, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)


numbers.sort(reverse=True)
print(numbers)


numbers = [9, 4, 2, 7]
new_list = sorted(numbers)
print(new_list)


numbers = [10, 4, 8, 2]
print(sorted(numbers))
print(sorted(numbers, reverse=True))


numbers = list(map(int, input("Enter numbers: ").split()))
n = len(numbers)
for i in range(n):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Sorted List:", numbers)



class Solution:
    def sortColors(self, nums):
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)
        nums[:] = [0] * zero + [1] * one + [2] * two


class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

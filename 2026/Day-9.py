matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)



matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[0][0])  
print(matrix[1][2])  



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
print("Matrix:")
for row in matrix:
    print(row)


matrix = [
    [1, 2],
    [3, 4]
]
total = 0
for row in matrix:
    for num in row:
        total += num
print("Sum:", total)


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
for row in matrix:
    print("Row Sum:", sum(row))


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
rows = len(matrix)
cols = len(matrix[0])
for j in range(cols):
    total = 0
    for i in range(rows):
        total += matrix[i][j]
    print("Clumn Sum:", total)



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = 0
for i in range(len(matrix)):
    total += matrix[i][i]
print("Diagonal Sum:", total)


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
rows = len(matrix)
cols = len(matrix[0])
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = 0
for row in matrix:
    for element in row:
        total += element
print("Sum:", total)


matrix = [
    [10, 25, 5],
    [8, 40, 15],
    [12, 7, 30]
]
largest = matrix[0][0]
for row in matrix:
    for element in row:
        if element > largest:
            largest = element
print("Largest element:", largest)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    total = 0
    for element in row:
        total += element
    print("Row sum:", total)

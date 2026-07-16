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
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()



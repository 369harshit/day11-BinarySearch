mat = [[1, 4, 9],
       [2, 5, 6],
       [3, 8, 7]]

arr = []

for i in range(3):
    for j in range(3):
        arr.append(mat[i][j])

arr.sort()

print("Median of the given matrix is :", arr[4])
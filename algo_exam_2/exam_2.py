n = int(input())
matrix = [[0] * n for i in range(n)]

for i in range(n):
    matrix[i][0] = 1
    matrix[i][i] = 1

for i in range(2, n + 1):
    for j in range(2, i):
        matrix[i - 1][j - 1] = matrix[i - 2][j - 2] + matrix[i - j - 1][j - 1]

print(sum(matrix[-1]) % (10 ** 9 + 7))
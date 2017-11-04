n = int(input())
matrix = [[0] * n for i in range(n)]

for i in range(n):
    matrix[i][0] = 1

for i in range(3, n + 1):
    for j in range(2, i):
        matrix[i - 1][j - 1] = matrix[i - j - 1][j - 1] + matrix[i - j - 1][j - 2]

print(sum(matrix[-1]) % (10 ** 9 + 7))
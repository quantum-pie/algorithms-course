"""
Calculating minimal correction distance for two strings
"""

str1, str2 = input(), input()
n, m = len(str1), len(str2)

# prepare two dimensional array for distances of prefixes
D = [[0] * (m + 1) for i in range(n + 1)]

d_it = iter(D)

# fill first row
next(d_it)[:] = range(m + 1)

# fill first column
for i in range(1, n + 1):
    next(d_it)[0] = i

for i in range(1, n + 1):
    for j in range(1, m + 1):
        diff = int(str1[i - 1] != str2[j - 1])
        D[i][j] = min(D[i][j - 1] + 1, D[i - 1][j] + 1, D[i - 1][j - 1] + diff)

print(D[n][m])


"""
Simple calc task: n can be reached from 1 by sequence of operations,
possible operations: x + 1, 2x, 3x
Need to calculate minimal number of required operations for given n and write results of each operation
"""
n = int(input())

# array[i] is minimal number of required operations to reach i from 1
array = [0] * (n + 1)

# fill array iteratively
for i in range(1, n + 1):
    d_2 = n
    d_3 = n
    if i % 3 == 0:
        d_3 = array[i // 3]
    if i % 2 == 0:
        d_2 = array[i // 2]
    array[i] = min(d_2, d_3, array[i - 1]) + 1

# array for results of operations
values = [n]
start = array[n]

# backward results restoring
for i in range(n - 1, 0, -1):
    f1 = values[-1] / i == 3
    f2 = values[-1] / i == 2
    f3 = values[-1] - i == 1
    if (f1 or f2 or f3) and start - array[i] == 1:
        values.append(i)
        start = array[i]

print(array[n] - 1)
print(*values[::-1])

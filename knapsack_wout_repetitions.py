"""
Find maximum weight of elements than can pe placed into knapsack without repetitions
"""
# W is knapsack capacity, n is number of elements
W, n = map(int, input().split())

# c is weights of elements
c = list(map(int, input().split()))

# D[w][i] is maximum weight of elements than can be placed in knapsack with w capacity and if only 1...i elements
# are available
D = [[0] * (n + 1) for i in range(W + 1)]

for i in range(1, n + 1):
    for w in range(1, W + 1):
        D[w][i] = D[w][i - 1]
        if c[i - 1] <= w:
            D[w][i] = max(D[w][i], D[w - c[i - 1]][i - 1] + c[i - 1])

print(D[W][n])

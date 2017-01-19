n = int(input())
a = list(map(int, input().split()))

D = [0] * (n + 2)

for i in range(2, n + 2):
    D[i] = max(D[i - 1], D[i - 2]) + a[i - 2]

print(D[n + 1])

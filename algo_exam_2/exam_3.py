n, x = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse=True)

if n < 3:
    idx = n
else:
    idx = 2
    while (idx < n) and (array[idx] + array[idx - 1] + array[idx - 2]) > x:
        idx += 1

print(idx)

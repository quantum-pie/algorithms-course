from bisect import bisect_right
n, w, *array = map(int, input().split())
sorted_array = sorted(array)
k, val = 0, 0
out = list()
while val < w:
    idx = bisect_right(sorted_array, w - val)
    val += sorted_array[idx - 1]
    out.append(sorted_array[idx - 1])
    k += 1

print(k, *out)
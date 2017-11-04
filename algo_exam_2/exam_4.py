n = int(input())
array = list(map(int, input().split()))

occurencies = dict.fromkeys(set(array), 0)
res = 0
for val in array:
    occurencies[val] += 1
    if(occurencies[val]) > n / 3:
        res = 1
        break

print(res)

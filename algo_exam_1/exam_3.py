n = int(input())
array = map(int, input().split())
sorted_array = sorted(array, reverse=True)
print(sorted_array[0] * sorted_array[1])

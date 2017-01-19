"""
Algorithm for calculating longest non-increasing subsequence of input sequence
Asymptotic time complexity is O(n log n)
"""

from bisect import bisect_right
from random import randint

# size of input array
SIZE = 100

# bounds of input array
MIN_VAL, MAX_VAL = 0, 1000

# construct random input array
array = [randint(0, 1000) for i in range(SIZE)]

print(*array)

# indices of input array in sorted array
# sorting complexity is O(n log n)
sorted_idx = sorted(range(SIZE), key=lambda x: array[x], reverse=True)

# new positions of input array elements in sorted array
new_positions = sorted(range(SIZE), key=lambda x: sorted_idx[x])

# auxiliary array for maximum lengths of sequences that ends up in every input element (sorted by input elements)
aux_array = [0] * SIZE

# array of input elements indexed by maximum lengths of sequences that ends up in them
d_array = aux_array.copy()

# current length of d_array
d_len = 0

# total maximum length of sequence
d_max = 0

# index of d_max in aux_array (corresponding ending element)
d_max_idx = SIZE

# for all elements in input order
for i in range(SIZE):

    # get position of input element in sorted array
    pos = new_positions[i]

    # bisect d_array to find most suitable index for value placing
    # this operation searching maximum d in aux_array that corresponds to element lesser than on pos index
    # complexity is O(log n)
    d = bisect_right(d_array, pos, 0, d_len)

    # update current maximum length
    aux_array[pos] = 1 + d
    d_array[d] = pos
    d_len = max(d_len, aux_array[pos])

    if aux_array[pos] > d_max:
        d_max = aux_array[pos]
        d_max_idx = pos

print(d_max)

idx_arr = [sorted_idx[d_max_idx] + 1]
k = d_max - 1

# this procedure restores maximum length sequence indices using aux_array and d_max
for i in range(d_max_idx - 1, -1, -1):
    if aux_array[i] == k:
        idx_arr.append(sorted_idx[i] + 1)
        if k == 1:
            break
        else:
            k -= 1

print(*idx_arr[::-1])

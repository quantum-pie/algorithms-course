from bisect import bisect_right
from random import randint

SIZE = 100                                                                  # size of input array
MIN_VAL, MAX_VAL = 0, 1000                                                  # bounds of input array

array = [randint(0, 1000) for i in range(SIZE)]                             # construct random input array

print(*array)

sorted_idx = sorted(range(SIZE), key=lambda x: array[x], reverse=True)      # indices of input array in sorted array
new_positions = sorted(range(SIZE), key=lambda x: sorted_idx[x])            # new positions of input array elements in sorted array

aux_array = [0] * (SIZE + 1)                                                # auxiliary array for maximum lengths of sequences that ends up in every input element (sorted by input elements)
d_array = [0] * SIZE                                                        # array of input elements indexed by maximum lengths of sequences that ends up in them
d_len = 0                                                                   # current length of d_array

d_max = 0                                                                   # total maximum length of sequence
d_max_idx = SIZE                                                            # index of d_max in aux_array

for i in range(SIZE):                                                       # for all elements in input order
    pos = new_positions[i]                                                  # get position of input element in sorted array
    d = bisect_right(d_array, pos, 0, d_len)                                # bisect d_array to find most suitable index for value placing
                                                                            # this operation searching maximum d in aux_array that is by the left side of current value

    aux_array[pos] = 1 + d                                                  # update current maximum length
    d_array[d] = pos                                                        # update d_array
    d_len = max(d_len, aux_array[pos])                                      # update length of d_array

    if aux_array[pos] > d_max:                                              # update total maximum
        d_max = aux_array[pos]
        d_max_idx = pos

print(d_max)

idx_arr = [sorted_idx[d_max_idx] + 1]
k = d_max - 1

for i in range(d_max_idx - 1, -1, -1):                                      # this procedure restores maximum length sequence indices using aux_array and d_max
    if aux_array[i] == k:
        idx_arr.append(sorted_idx[i] + 1)
        if k == 1:
            break
        else:
            k -= 1

print(*idx_arr[::-1])

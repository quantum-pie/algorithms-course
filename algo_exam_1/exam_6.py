from array import array


def sift_up(child_idx):
    parent_idx = child_idx // 2
    while parent_idx != child_idx and heap[parent_idx - 1] > heap[child_idx - 1]:
        tmp = heap[parent_idx - 1]
        heap[parent_idx - 1] = heap[child_idx - 1]
        heap[child_idx - 1] = tmp
        child_idx = parent_idx
        parent_idx = child_idx // 2


n = int(input())
in_array = map(int, input().split())

heap = array('L', [0] * n)
heap_size = 0
for val in in_array:
    heap[heap_size] = val
    sift_up(heap_size + 1)
    heap_size += 1

print(*heap)

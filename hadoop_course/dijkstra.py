# Dijkstra's algorithm
import heapq
import math

V, G = map(int, input().split())
adj_matrix = [[0] * V for v in range(V)]

# Fill adjacency matrix
for g in range(G):
    i, j, w = map(int, input().split())
    adj_matrix[i - 1][j - 1] = w

start, end = map(int, input().split())
start -= 1
end -= 1

V_array = [math.inf for i in range(V)]
V_array[start] = 0

Q = []
heapq.heappush(Q, (0, start))

while len(Q) > 0:
    u = heapq.heappop(Q)
    cur_v = u[1]
    for j in range(V):
        w = adj_matrix[cur_v][j]
        if w != 0 and V_array[j] > u[0] + w:
            V_array[j] = u[0] + w
            heapq.heappush(Q, (V_array[j], j))

print(V_array[end] if V_array[end] != math.inf else -1)


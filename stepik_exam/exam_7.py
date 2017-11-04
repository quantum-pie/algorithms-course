# Having fun with ninja climbing up the walls

n, k = map(int, input().split())
left_str = input()
right_str = input()
danger = [['X', 'X']] + [list(i) for i in zip(left_str, right_str)] + k * [['-', '-']]

pos = [1, 0]
res = False
while True:
    step_num = pos[0]
    side = pos[1]
    if step_num > n:
        res = True
        break
    if danger[step_num + 1][side] == '-':
        pos[0] += 1
    elif danger[step_num + k][(side + 1) % 2] == '-':
        pos[0] += k
        pos[1] = (side + 1) % 2
    elif danger[step_num - 1][side] == '-':
        danger[step_num][side] = 'X'
        pos[0] -= 1
    else:
        break

print("YES") if res else print("NO")

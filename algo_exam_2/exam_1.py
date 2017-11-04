input_str = input()
str_len = len(input_str)
ones_ops = [0] * (str_len + 1)
zeros_ops = ones_ops.copy()

for i in range(1, str_len + 1):
    if input_str[i - 1] == "0":
        zeros_ops[i] = zeros_ops[i - 1]
        ones_ops[i] = zeros_ops[i - 1] + 1
    else:
        zeros_ops[i] = ones_ops[i - 1] + 1
        ones_ops[i] = ones_ops[i - 1]

print(zeros_ops[-1])

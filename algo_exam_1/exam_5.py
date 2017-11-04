input_string = input()
pattern = input()

k = 0
for i in range(len(input_string)):
    if input_string[i:].startswith(pattern):
        k += 1

print(k)
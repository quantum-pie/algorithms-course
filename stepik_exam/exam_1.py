# Read n lines and print first m most frequent words
# Code is pretty easy and self-documentary
n, m = map(int, input().split())

input_dict = dict()

for i in range(n):
    str_lst = input().split()
    for word in str_lst:
        if word in input_dict.keys():
            input_dict[word] += 1
        else:
            input_dict.update({word: 1})

sorted_items = sorted(input_dict.items(), reverse=True, key=lambda x: x[1])
[print(sorted_items[i][0], sorted_items[i][1]) for i in range(m)]

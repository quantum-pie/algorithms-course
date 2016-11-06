def find(prefix):
    pref_len = len(prefix)
    return (letter for letter in huffman_code.keys()
            if huffman_code[letter].startswith(prefix)
            and len(huffman_code[letter]) == pref_len)


def tree_build(parent, prefix=''):

    zero_child = {
        'value': None,
        '0': None,
        '1': None
    }

    one_child = zero_child.copy()

    zero_prefix = prefix + '0'
    one_prefix = prefix + '1'

    try:
        zero_child['value'] = next(find(zero_prefix))
    except StopIteration:
        pass

    try:
        one_child['value'] = next(find(one_prefix))
    except StopIteration:
        pass

    parent['0'] = zero_child
    parent['1'] = one_child

    if len(prefix) + 1 != max_len:
        tree_build(zero_child, zero_prefix)
        tree_build(one_child, one_prefix)


letters, length = map(int, input().split())
huffman_code = dict()
for i in range(letters):
    str_lst = input().split(':')
    huffman_code.update({str_lst[0]: str_lst[1].lstrip()})

max_len = max(map(len, huffman_code.values()))

huffman_tree = {
    'value': None,
    '0': None,
    '1': None
}

tree_build(huffman_tree, '')
to_decode = input().strip()

out_str = ''
node = huffman_tree
for char in to_decode:
    node = node[char]
    if node['value'] is not None:
        out_str += node['value']
        node = huffman_tree

print(out_str)



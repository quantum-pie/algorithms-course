def find(prefix):
    """
    Trying to find letter with minimal code length corresponding given code prefix
    :param prefix: Code prefix
    :return: Found letter
    """
    pref_len = len(prefix)
    return (letter for letter in huffman_code.keys()
            if huffman_code[letter].startswith(prefix)
            and len(huffman_code[letter]) == pref_len)


def tree_build(parent, prefix=''):
    """
    Function to build huffman coding binary heap
    Starting from root (very seldom character with shortest code) creates children and calls itself recursively on them
    :param parent: Parent node
    :param prefix: Prefix of parent node (just code string)
    :return: Nothing
    """

    # left child that appends '0' to prefix
    zero_child = {
        'value': None,
        '0': None,
        '1': None
    }

    # right child that appends '1' to prefix
    one_child = zero_child.copy()

    zero_prefix = prefix + '0'
    one_prefix = prefix + '1'

    # try to find letters corresponding to children prefixes
    try:
        zero_child['value'] = next(find(zero_prefix))
    except StopIteration:
        pass

    try:
        one_child['value'] = next(find(one_prefix))
    except StopIteration:
        pass

    # after all give children to the father
    parent['0'] = zero_child
    parent['1'] = one_child

    # build tree in depth if it have sense
    if len(prefix) + 1 != max_len:
        tree_build(zero_child, zero_prefix)
        tree_build(one_child, one_prefix)

# read number of alphabet letters and length of string to decode
letters, length = map(int, input().split())
huffman_code = dict()

# dictionary with letter-code pairs
for i in range(letters):
    str_lst = input().split(':')
    huffman_code.update({str_lst[0]: str_lst[1].lstrip()})

# maximum length of character code
max_len = max(map(len, huffman_code.values()))

# root of huffman binary heap
huffman_tree = {
    'value': None,
    '0': None,
    '1': None
}

tree_build(huffman_tree, '')
to_decode = input().strip()

out_str = ''
node = huffman_tree
for bit in to_decode:

    # move down the huffman heap until first value is in alphabet
    node = node[bit]
    if node['value'] is not None:
        out_str += node['value']

        # return to the root
        node = huffman_tree

print(out_str)

class TreeNode:
    """
    Binary tree node.
    Note that node value is tuple (a, d), where a is sequnece value,
    and d is maximum length of subsequence that ends up in a
    """
    def __init__(self, *value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, a, d=0):
        """
        Inserts new tuple (a, d) to the tree
        Note that tuples by default are compared item by item: by a first and then by d
        """
        new_node = TreeNode(a, d)                           # create new node
        if self.root:                                       # check if root exists
            current_node = self.root                        # assign initial current node
            while True:
                if new_node.value <= current_node.value:
                    if current_node.left:
                        current_node = current_node.left    # iterate over left subtree
                    else:
                        current_node.left = new_node        # stop iteration
                        break
                else:
                    if current_node.right:                  # iterate over right subtree
                        current_node = current_node.right
                    else:
                        current_node.right = new_node       # stop iteration
                        break
        else:
            self.root = new_node                            # create root

    def search_maximum(self, value):
        """
        Function to calculate maximum length of subsequence
        that ends up in node with a >= value
        :param value:
        :return:
        """
        current_node = self.root                            # assign initial current node
        maximum = 0                                         # assign initial maximum length d
        while True:
            if value <= current_node.value[0]:              # this node is 'good' i.e. a is >= value
                if current_node.value[1] > maximum:         # so check maximum length
                    maximum = current_node.value[0]
                if current_node.left:                       # and iterate further over the left subtree
                    current_node = current_node.left
                else:
                    break
            else:                                           # 'bad' node
                if current_node.right:
                    current_node = current_node.right       # just iterate further
                else:
                    break
        return maximum

    def update_root(self, d):
        """
        Update root d when available
        :param d:
        :return:
        """
        self.root[1] = d


n = int(input())
array = list(map(int, input().split()))

sorted_array = sorted(array)                # sort input - n*log(n)
median = sorted_array[n // 2]               # calculate median to build balanced tree

binary_tree = BinarySearchTree()
binary_tree.insert(median)                  # push median as root with default d (0)

lengths = [0] * n

for val in array:                                   # n
    new_len = binary_tree.search_maximum(val) + 1   # log(n)
    if val == median and binary_tree.root[1] == 0:
        binary_tree.update_root(new_len)
    else:
        binary_tree.insert(val, new_len)                # log(n)

ans = max(0, *lengths)
print(ans)



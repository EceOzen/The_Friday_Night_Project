class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, key, index):
    if root is None:
        return TreeNode((key, index))
    if key < root.value[0]:
        root.left = insert(root.left, key, index)
    elif key > root.value[0]:
        root.right = insert(root.right, key, index)
    return root

def search(root, key):
    if root is None:
        return None
    if root.value[0] == key:
        return root.value
    if key < root.value[0]:
        return search(root.left, key)
    return search(root.right, key)
    
def pairSum_n2(total, lst):
    pairs = []
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] + lst[j] == total:
                pairs.append((i, j))
    return pairs

def pairSum_n(total, lst):
    pairs = []
    complement_dict = {}
    for i, num in enumerate(lst):
        complement = total - num
        if complement in complement_dict:
            pairs.append((complement_dict[complement], i))
        complement_dict[num] = i
    return pairs
  
def pairSum_bst(total, lst):
    n = len(lst)
    if n < 2:
        return None

    # Sort the list and build BST
    sorted_list = sorted([(num, i) for i, num in enumerate(lst)])
    root = None
    for num, index in sorted_list:
        complement = total - num
        pair = search(root, complement)
        if pair is not None:
            return (index, pair[1])
        root = insert(root, num, index)
    return None

total_value = 10
numbers_list = [3, 4, 5, 6, 7]
result_n2 = pairSum_n2(total_value, numbers_list)
result_n = pairSum_n(total_value, numbers_list)
result_bst = pairSum_bst(total_value, numbers_list)


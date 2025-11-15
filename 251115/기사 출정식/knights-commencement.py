n, q = map(int, input().split())


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node_dict = {}
node_vals = list(map(int, input().split()))
for i in range(n):
    node_val = node_vals[i]
    node_dict[node_val] = Node(node_val)
    if i > 0:
        node_dict[node_vals[i - 1]].right = node_dict[node_val]
        node_dict[node_val].left = node_dict[node_vals[i - 1]]
node_dict[node_vals[-1]].right = node_dict[node_vals[0]]
node_dict[node_vals[0]].left = node_dict[node_vals[-1]]


ret = []
for _ in range(q):
    num = int(input())
    target_node = node_dict[num]
    if target_node.left is not None:
        target_node.left.right = target_node.right
    if target_node.right is not None:
        target_node.right.left = target_node.left
    ret.append(str(target_node.right.value) + " " + str(target_node.left.value))
print("\n".join(ret))

n, m, q = map(int, input().split())


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node_dicts = [dict() for _ in range(m)]

names = input().split()

x = int(n / m)

import math

for i in range(n):
    line_num = math.ceil((i + 1) / x) - 1
    line_idx = (i) % x
    new_node = Node(names[i])
    node_dicts[line_num][line_idx] = new_node

# link nodes
for i in range(m):
    curr_dict = node_dicts[i]
    sorted_nodes = sorted(curr_dict.items(), key=lambda item: item[0])
    for j in range(len(sorted_nodes) - 1):
        curr_node = sorted_nodes[j][1]
        next_node = sorted_nodes[j + 1][1]
        curr_node.right = next_node
        next_node.left = curr_node
    node_dicts[i] = {node.val: node for _, node in sorted_nodes}


def get_dict_idx(x):
    for i in range(m):
        if x in node_dicts[i]:
            return i
    return -1


def insert_before(node, new_node):
    if node.left:
        node.left.right = new_node
    if new_node.left:
        new_node.left.right = new_node.right
    if new_node.right:
        new_node.right.left = new_node.left
    new_node.left = node.left
    new_node.right = node
    node.left = new_node


def insert_after(node, new_node):
    if node.right:
        node.right.left = new_node
    if new_node.left:
        new_node.left.right = new_node.right
    if new_node.right:
        new_node.right.left = new_node.left
    new_node.right = node.right
    new_node.left = node
    node.right = new_node


for _ in range(q):
    cmd = list(input().split())
    if cmd[0] == "1":
        x, y = cmd[1], cmd[2]
        idx_x = get_dict_idx(x)
        idx_y = get_dict_idx(y)
        node_x = node_dicts[idx_x][x]
        node_y = node_dicts[idx_y][y]

        insert_before(node_y, node_x)
        if idx_x != idx_y:
            del node_dicts[idx_x][x]
            node_dicts[idx_y][x] = node_x

    elif cmd[0] == "2":
        x = cmd[1]
        idx_x = get_dict_idx(x)
        node_x = node_dicts[idx_x][x]

        if node_x.left:
            node_x.left.right = node_x.right
        if node_x.right:
            node_x.right.left = node_x.left
        del node_dicts[idx_x][x]
    else:
        x, y, z = cmd[1], cmd[2], cmd[3]
        idx_x = get_dict_idx(x)
        node_x = node_dicts[idx_x][x]
        idx_y = get_dict_idx(y)
        node_y = node_dicts[idx_y][y]
        idx_z = get_dict_idx(z)
        node_z = node_dicts[idx_z][z]

        while True:
            next_node = node_x.right
            insert_before(node_z, node_x)
            if idx_x != idx_z:
                del node_dicts[idx_x][node_x.val]
                node_dicts[idx_z][node_x.val] = node_x
            if node_x == node_y:
                break
            node_x = next_node
            idx_x = get_dict_idx(node_x.val)

ret = []
for i in range(m):
    curr_dict = node_dicts[i]
    if not curr_dict:
        ret.append("-1")
    else:
        curr_node = None
        for node in curr_dict.values():
            if not node.left:
                curr_node = node
                break
        vals = []
        while curr_node:
            vals.append(str(curr_node.val))
            curr_node = curr_node.right
        ret.append(" ".join(vals))
print("\n".join(ret))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node_dict = {}
start_node = Node(1)
node_dict[start_node.value] = start_node

q = int(input())


def insert_after(parent_value, child_value):
    parent_node = node_dict.get(parent_value)
    if not parent_node:
        return

    new_node = Node(child_value)
    node_dict[child_value] = new_node

    if parent_node.right is None:
        parent_node.right = new_node
        new_node.left = parent_node
    else:
        current_right = parent_node.right
        parent_node.right = new_node
        new_node.left = parent_node
        new_node.right = current_right
        current_right.left = new_node


def insert_before(parent_value, child_value):
    parent_node = node_dict.get(parent_value)
    if not parent_node:
        return

    new_node = Node(child_value)
    node_dict[child_value] = new_node

    if parent_node.left is None:
        parent_node.left = new_node
        new_node.right = parent_node
    else:
        current_left = parent_node.left
        parent_node.left = new_node
        new_node.right = parent_node
        new_node.left = current_left
        current_left.right = new_node


ret = []
cur_value = 2
for _ in range(q):
    command = input().strip().split()
    if command[0] == "1":
        parent_value = int(command[1])
        child_cnt = int(command[2])
        for i in range(child_cnt):
            if i == 0:
                insert_after(parent_value, cur_value)
            else:
                insert_after(cur_value - 1, cur_value)
            cur_value += 1
    elif command[0] == "2":
        parent_value = int(command[1])
        child_cnt = int(command[2])
        for i in range(child_cnt):
            if i == 0:
                insert_before(parent_value, cur_value)
            else:
                insert_after(cur_value - 1, cur_value)
            cur_value += 1
    else:
        target_value = int(command[1])
        target_node = node_dict.get(target_value)
        left_value = target_node.left.value if target_node.left else -1
        right_value = target_node.right.value if target_node.right else -1
        if left_value == -1 and right_value == -1:
            ret.append("-1")
        else:
            ret.append(f"{left_value} {right_value}")
print("\n".join(ret))

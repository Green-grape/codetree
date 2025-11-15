n, q = map(int, input().split())


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


head = None
node_list = []
node_vals = list(map(str, input().split()))
for i in range(n):
    node_val = node_vals[i]
    if head is None:
        head = Node(node_val)
        node_list.append(head)
    else:
        new_node = Node(node_val)
        node_list.append(new_node)
        node_list[i - 1].right = new_node
        new_node.left = node_list[i - 1]
node_list[-1].right = node_list[0]
node_list[0].left = node_list[-1]

ret = []
for _ in range(q):
    cmd = input().split()
    if cmd[0] == "1":
        if head.right is not None:
            head = head.right
    elif cmd[0] == "2":
        if head.left is not None:
            head = head.left
    elif cmd[0] == "3":
        if head.right is not None:
            head.right = head.right.right
            if head.right is not None:
                head.right.left = head
    elif cmd[0] == "4":
        new_node = Node(cmd[1])
        new_node.right = head.right
        new_node.left = head

        if head.right is not None:
            head.right.left = new_node
        head.right = new_node

    left_val = head.left.value if head.left is not None else -1
    right_val = head.right.value if head.right is not None else -1
    if (left_val == right_val) or (left_val == -1) or (right_val == -1):
        ret.append("-1")
    else:
        ret.append(f"{left_val} {right_val}")
print("\n".join(ret))

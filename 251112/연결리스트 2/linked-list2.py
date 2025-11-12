class DoubleLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def insert_after(node, new_node):
    new_node.prev = node
    new_node.next = node.next
    if node.next:
        node.next.prev = new_node
    node.next = new_node


def insert_before(node, new_node):
    new_node.next = node
    new_node.prev = node.prev
    if node.prev:
        node.prev.next = new_node
    node.prev = new_node


n = int(input())

nodes = [DoubleLinkedListNode(i) for i in range(1, n + 1)]

q = int(input())

ret = []
for _ in range(q):
    command = input().split()
    x = int(command[1]) - 1
    if command[0] == "1":
        if nodes[x].next:
            nodes[x].next.prev = nodes[x].prev
        if nodes[x].prev:
            nodes[x].prev.next = nodes[x].next

        nodes[x].prev = None
        nodes[x].next = None
    elif command[0] == "2":
        y = int(command[2]) - 1
        insert_before(nodes[x], nodes[y])
    elif command[0] == "3":
        y = int(command[2]) - 1
        insert_after(nodes[x], nodes[y])
    else:
        before_value = nodes[x].prev.value if nodes[x].prev else 0
        after_value = nodes[x].next.value if nodes[x].next else 0
        ret.append(f"{before_value} {after_value}")


ret.append(
    " ".join(str(node.next.value) if node.next is not None else "0" for node in nodes)
)

print("\n".join(ret))

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

for i in range(n):
    nodes[i].prev = nodes[i - 1] if i > 0 else None
    nodes[i].next = nodes[i + 1] if i < n - 1 else None

q = int(input())

for _ in range(q):
    a, b, c, d = map(int, input().split())
    node_a = nodes[a - 1]
    node_b = nodes[b - 1]
    node_c = nodes[c - 1]
    node_d = nodes[d - 1]

    temp_a_prev = node_a.prev
    node_a.prev = node_c.prev
    if node_c.prev:
        node_c.prev.next = node_a
    temp_b_next = node_b.next
    node_b.next = node_d.next
    if node_d.next:
        node_d.next.prev = node_b

    node_c.prev = temp_a_prev
    if temp_a_prev:
        temp_a_prev.next = node_c
    node_d.next = temp_b_next
    if temp_b_next:
        temp_b_next.prev = node_d

# find start
for node in nodes:
    if node.prev is None:
        start_node = node
        break

ret = []
while start_node:
    ret.append(str(start_node.value))
    start_node = start_node.next
print(" ".join(ret))

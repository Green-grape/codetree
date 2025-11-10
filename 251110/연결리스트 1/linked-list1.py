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


init = input()
cur_node = DoubleLinkedListNode(init)

n = int(input())

ret = []
for _ in range(n):
    inputs = input().split()
    com = int(inputs[0])
    if com == 1:
        new_node = DoubleLinkedListNode(inputs[1])
        insert_before(cur_node, new_node)
    elif com == 2:
        new_node = DoubleLinkedListNode(inputs[1])
        insert_after(cur_node, new_node)
    elif com == 3:
        if cur_node.prev:
            cur_node = cur_node.prev
    elif com == 4:
        if cur_node.next:
            cur_node = cur_node.next
    before = cur_node.prev.value if cur_node.prev else "(Null)"
    cur = cur_node.value
    after = cur_node.next.value if cur_node.next else "(Null)"
    ret.append(f"{before} {cur} {after}")

print("\n".join(ret))

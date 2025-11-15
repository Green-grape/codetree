# test_case_file = "./test_case.txt"
# answer_file = "./answer.txt"

# import sys

# f = open(test_case_file, "r")
# answer = open(answer_file, "r")


# input = f.readline

n, m, q = map(int, input().split())


class Node:
    __slots__ = ("val", "left", "right")  # 메모리/속도 미세최적화

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 값 -> 노드 객체
node_pos = {}

# 초기 M개의 원 만들기
for _ in range(m):
    nums = list(map(int, input().split()))
    k = nums[0]

    prev = None
    first = None
    for i in range(1, k + 1):
        v = nums[i]
        node = Node(v)
        node_pos[v] = node
        if prev is None:
            first = node
        else:
            prev.right = node
            node.left = prev
        prev = node
    # 원형으로 연결
    first.left = prev
    prev.right = first


def get_node(val: int) -> Node:
    return node_pos[val]


def merge_circles(x: int, y: int):
    node_x = get_node(x)
    node_y = get_node(y)

    cur = node_x.right
    while cur is not node_x:
        if cur is node_y:
            return  # 이미 같은 원
        cur = cur.right

    # Connect the two circles
    left_x = node_x.left
    right_x = node_x.right
    left_y = node_y.left
    right_y = node_y.right

    node_x.right = node_y
    node_y.left = node_x
    if right_x:
        right_x.left = left_y
    if left_y:
        left_y.right = right_x


def divide_circle(x: int, y: int):
    head = get_node(x)
    boundary = get_node(y)

    if head is boundary:
        return

    # head에서 시작해 boundary 직전까지가 잘라낼 구간
    curr = head
    while True:
        nxt = curr.right
        if nxt is boundary:
            tail = curr  # 잘라낼 구간의 마지막 노드
            break
        curr = nxt
        if curr is head:
            # 한 바퀴 돌았는데 boundary를 못 만나면 다른 원이므로 무시
            return

    # 현재 구조:
    # ... <-> left_head <-> head ... tail <-> boundary <-> ...
    left_head = head.left
    left_y = boundary.left  # 이게 tail

    # 1) 남는 원: left_head <-> boundary
    left_head.right = boundary
    boundary.left = left_head

    # 2) 새 원: tail(left_y) <-> head
    left_y.right = head
    head.left = left_y


ret = []

for _ in range(q):
    cmd = list(map(int, input().split()))
    t = cmd[0]

    if t == 1:
        _, x, y = cmd
        merge_circles(x, y)

    elif t == 2:
        _, x, y = cmd
        divide_circle(x, y)

    else:
        _, x = cmd
        node_x = get_node(x)

        # 같은 원에서 최소값 노드 찾기 (오른쪽으로 한 바퀴)
        curr = node_x
        min_node = node_x
        while True:
            curr = curr.right
            if curr.val < min_node.val:
                min_node = curr
            if curr is node_x:
                break

        # 최소값 노드에서 왼쪽으로 한 바퀴 돌며 출력
        curr = min_node
        res = []
        while True:
            res.append(str(curr.val))
            curr = curr.left
            if curr is min_node:
                break
        ret.append(" ".join(res))

print("\n".join(ret))

# answer_list = answer.readline()
# res = ret[0]
# for line in answer:
#     expected = line.strip()
#     actual = ret.pop(0)
#     assert expected == actual, f"Expected: {expected}, Actual: {actual}"
# print("All test cases passed!")

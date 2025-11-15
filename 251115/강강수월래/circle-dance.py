MAX_N = 100000

class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

# 두 사람을 연결합니다.
def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

# 두 원을 연결합니다.
def connect_circle(u, v):
    v_prev = v.prev
    u_next = u.next

    connect(u, v)
    connect(v_prev, u_next)

# 두 원을 쪼갭니다.
def split_circle(u, v):
    u_prev = u.prev
    v_prev = v.prev

    connect(u_prev, v)
    connect(v_prev, u)

# 원을 출력합니다.
def print_line(target):
    # 원에서 학생 번호가 가장 작은 학생을 찾습니다.
    mn = target.id
    cur = target
    while True:
        cur = cur.next  
        if cur is not None:
            mn = min(mn, cur.id)
        if cur == target:
            break

    # 가장 작은 학생부터 출력합니다.
    init = nodes[student_id[mn]]
    cur = nodes[student_id[mn]]
    while True:
        print(cur.id, end=' ')
        # 반시계 방향으로 돌면서 출력합니다.
        cur = cur.prev
        if cur.id == init.id:
            break
    print()

n, m, q = map(int, input().split())

# 학생들을 관리해줄 배열입니다.
nodes = [None] * (MAX_N + 2)

# 학생들의 번호의 범위가 1 ~ 10억이기 때문에, map으로 학생들의 번호들을 관리해줍니다.
student_id = {}

node_cnt = 1
for i in range(m):
    line = list(map(int, input().split()))
    circle_size = line[0]
    start = tail = None
    for j in range(1, circle_size + 1):
        student_num = line[j]
        student_id[student_num] = node_cnt
        nodes[node_cnt] = Node(student_num)

        if j == 1:
            start = tail = nodes[node_cnt]
        else:
            connect(tail, nodes[node_cnt])
            tail = nodes[node_cnt]
            if j == circle_size:
                # 원에서의 마지막 학생은 해당 원의 첫 학생과 연결합니다.
                connect(tail, start)
        node_cnt += 1

# q개의 행동을 진행합니다.
for _ in range(q):
    line = list(map(int, input().split()))
    option = line[0]

    if option == 1:
        a, b = line[1], line[2]
        connect_circle(nodes[student_id[a]], nodes[student_id[b]])

    elif option == 2:
        a, b = line[1], line[2]
        split_circle(nodes[student_id[a]], nodes[student_id[b]])

    elif option == 3:
        a = line[1]
        print_line(nodes[student_id[a]])

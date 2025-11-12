import sys

input = sys.stdin.readline


class Node:
    __slots__ = ("val", "prev", "next")

    def __init__(self, v):
        self.val = v
        self.prev = None
        self.next = None


def build_list(n: int):
    nodes = [Node(i) for i in range(1, n + 1)]
    for i in range(n):
        if i:
            nodes[i].prev = nodes[i - 1]
        if i < n - 1:
            nodes[i].next = nodes[i + 1]
    return nodes, nodes[0]  # (모든 노드 배열, head)


def swap_segments(head: Node, A: Node, B: Node, C: Node, D: Node):
    """
    [A..B] 와 [C..D] (서로 겹치지 않음, 각 구간 내부는 연속) 를 위치 교환.
    인접/비인접 모두 처리. 새 head 반환.
    """
    Ap, Bn = A.prev, B.next
    Cp, Dn = C.prev, D.next

    if Bn is C:
        # ... Ap <-> A ... B <-> C ... D <-> Dn ...
        # -> ... Ap <-> C ... D <-> A ... B <-> Dn ...
        if Ap:
            Ap.next = C
        else:
            head = C
        C.prev = Ap

        D.next = A
        A.prev = D

        B.next = Dn
        if Dn:
            Dn.prev = B

    elif Dn is A:
        # ... Cp <-> C ... D <-> A ... B <-> Bn ...
        # -> ... Cp <-> A ... B <-> C ... D <-> Bn ...
        if Cp:
            Cp.next = A
        else:
            head = A
        A.prev = Cp

        B.next = C
        C.prev = B

        D.next = Bn
        if Bn:
            Bn.prev = D

    else:
        # 비인접 일반 케이스
        # 바깥 연결: Ap–C , Cp–A , D–Bn , B–Dn
        if Ap:
            Ap.next = C
        else:
            head = C
        C.prev = Ap

        if Cp:
            Cp.next = A
        else:
            head = A
        A.prev = Cp

        if Dn:
            Dn.prev = B
        B.next = Dn

        if Bn:
            Bn.prev = D
        D.next = Bn

    return head


def main():
    n = int(input().strip())
    q = int(input().strip())

    nodes, head = build_list(n)

    for _ in range(q):
        a, b, c, d = map(int, input().split())
        # a<=b, c<=d, 서로 겹치지 않음이 문제에서 보장
        A, B, C, D = nodes[a - 1], nodes[b - 1], nodes[c - 1], nodes[d - 1]
        head = swap_segments(head, A, B, C, D)

    # 최종 출력
    out = []
    cur = head
    while cur:
        out.append(str(cur.val))
        cur = cur.next
    print(" ".join(out))


main()

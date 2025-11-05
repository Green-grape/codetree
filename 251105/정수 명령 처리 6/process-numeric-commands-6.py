import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority=None):
        if priority is None:
            priority = -item
        heapq.heappush(self.elements, (priority, item))

    def size(self):
        return len(self.elements)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        return heapq.heappop(self.elements)[1]

    def top(self):
        if self.is_empty():
            raise IndexError("top from an empty priority queue")
        return self.elements[0][1]


n = int(input())

pq = PriorityQueue()

ret = []
for _ in range(n):
    cmds = input().split()
    if cmds[0] == "push":
        item = int(cmds[1])
        pq.put(item)
    elif cmds[0] == "pop":
        ret.append(pq.pop())
    elif cmds[0] == "size":
        ret.append(pq.size())
    elif cmds[0] == "top":
        ret.append(pq.top())
    elif cmds[0] == "empty":
        ret.append(1 if pq.is_empty() else 0)

print("\n".join(map(str, ret)))


import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]

    def top(self):
        return self.elements[0][1] if self.elements else None


n = int(input())

pq = PriorityQueue()

ret = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if pq.is_empty():
            ret.append(0)
        else:
            ret.append(pq.pop())
    else:
        pq.put(num, -num)
    #print(pq.elements)

print("\n".join(map(str, ret)))

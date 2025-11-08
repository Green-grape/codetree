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


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

pq = PriorityQueue()

for cords in grid:
    x, y = cords
    dist = x + y
    pq.put((x, y), dist)

for _ in range(m):
    x, y = pq.pop()
    x += 2
    y += 2
    dist = x + y
    pq.put((x, y), dist)

print(f"{pq.top()[0]} {pq.top()[1]}")

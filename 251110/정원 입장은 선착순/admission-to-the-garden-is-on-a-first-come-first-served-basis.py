import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, *item):
        heapq.heappush(self.elements, item)

    def pop(self):
        return heapq.heappop(self.elements)

    def top(self):
        return self.elements[0][1] if self.elements else None


pq = PriorityQueue()

n = int(input())

inputs = []

for i in range(n):
    start, duration = map(int, input().split())
    inputs.append((start, i + 1, duration))

inputs.sort()

pq.put(inputs[0][1], inputs[0][0], inputs[0][2])
i = 1
cur_time = inputs[0][0]
max_wait = 0
while i < n or not pq.is_empty():
    if pq.is_empty():
        pq.put(inputs[i][1], inputs[i][0], inputs[i][2])
        cur_time = inputs[i][0]
        i += 1
    else:
        task_id, start_time, duration = pq.pop()
        max_wait = max(max_wait, cur_time - start_time)
        cur_time += duration
        while i < n and inputs[i][0] <= cur_time:
            pq.put(inputs[i][1], inputs[i][0], inputs[i][2])
            i += 1
print(max_wait)

n = int(input())

dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = float("inf")
answer = 0

for i in range(n - 1):
    min_cost = min(min_cost, cost[i])
    answer += min_cost * dist[i]
print(answer)

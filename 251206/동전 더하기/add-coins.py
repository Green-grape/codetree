n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

total = 0
for i in range(n - 1, -1, -1):
    if k >= coins[i]:
        count = k // coins[i]
        k -= count * coins[i]
        total += count
print(total)

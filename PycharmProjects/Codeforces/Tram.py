count = 0
curr = 0
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    curr += b - a
    count = max(count, curr)
print(count)
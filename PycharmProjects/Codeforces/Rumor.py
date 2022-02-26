n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
connect = {}
for _ in range(m):
    a, b = list(map(int, input().split()))
    if a in connect:
        connect[a].append(b)
    else:
        connect[a] = [b]
    if b in connect:
        connect[b].append(a)
    else:
        connect[b] = [a]
print(connect)

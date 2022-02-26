n, e = list(map(int, input().split()))
network = {}
arr = []
for i in range(e):
    a, b = map(int, input().split())
    if a in network:
        network[a].append(b)
    else:
        network[a] = [b]
    if b in network:
        network[b].append(a)
    else:
        network[b] = [a]
for k in network:
    arr.append(len(network[k]))
if arr.count(1) == 2 and arr.count(2) == n - 2:
    print("bus topology")
elif arr.count(2) == n:
    print("ring topology")
elif arr.count(n-1) == 1 and arr.count(1) == n - 1:
    print("star topology")
else:
    print("unknown topology")

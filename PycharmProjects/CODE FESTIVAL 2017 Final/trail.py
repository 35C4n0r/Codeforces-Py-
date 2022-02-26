arr = []
for _ in range(int(input())):
    t = list(map(int, input().split()))
    arr.append(t)
q = int(input())
for j in range(q):
    l, r, h = list(map(int, input().split()))
    count = 0
    for g in arr:
        print(g)
        if h == g[1] and l <= g[0] <= r:
            count += 1
            g[1] = g[0] = -1
            print(arr)
    print(count)


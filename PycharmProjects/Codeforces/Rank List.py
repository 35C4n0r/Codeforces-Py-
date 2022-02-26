n, k = map(int, input().split())
l = []
for i in range(n):
    p, t = map(int,input().split())
    l.append((p, t))
l = sorted(l, key=lambda x: (x[0], -x[1]), reverse=True)
print(l.count(l[k-1]))
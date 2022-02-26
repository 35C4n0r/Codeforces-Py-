n = int(input())
arr = list(map(int, input().split()))
m = 10**9 + 7
q = int(input())
a = list(map(int, input().split()))
z = sum(arr) / 2
for h in range(q):
    z *= 2
    if z < 0:
        z = -z
    print(int(z) % m)

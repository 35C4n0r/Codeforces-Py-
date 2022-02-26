t, m = list(map(int, input().split()))
arr = {}
for _ in range(t):
    z = input()
    abc = list(z)
    if 'alloc' in z:
        if int(abc[-1]) > m:

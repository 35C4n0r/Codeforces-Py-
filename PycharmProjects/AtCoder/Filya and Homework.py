n = int(input())
s = sorted(map(int, input().split()))
d = sorted(set(s))
if len(d) <= 2:
    print('Yes')
    exit()
if len(d) > 3:
    print('No')
    exit()
if d[2] - d[1] == d[1] - d[0]:
    print('Yes')
else:
    print('No')
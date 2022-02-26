n = int(input())
arr = list(map(int, input().split()))
nn = int(input())
result = []
count = 0
if nn == 0:
    print(-1)
    exit()
for _ in range(nn):
    ll, ul = list(map(int, input().split()))
    result.append([ll, ul])
result = sorted(result)
s = sum(arr)
if s <= result[-1][1]:
    count += 1
    print(s)
else:
    for k in result:
        if k[1] >= sum(arr):
            print(k[0])
            count += 1
            break
        elif k[0] >= sum(arr):
            print(k[0])
            count += 1
            break
if count == 0:
    print(-1)

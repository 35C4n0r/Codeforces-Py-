n = int(input())
arr = list(map(int, input().split()))
cur = 0
coun = 0
for k in range(n):
    if arr[k] == 0:
        cur += 1
        coun = max(coun, cur)
    else:
        cur = 0
print(arr.count(1) + coun)
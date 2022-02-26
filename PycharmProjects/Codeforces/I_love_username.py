n = int(input())
arr = list(map(int, input().split()))
mn = arr[0]
mx = arr[0]
count = 1
for k in arr[1:]:
    if k > mx:
        count += 1
        mx = k
    elif k < mn:
        count += 1
        mn = k
print(count - 1)
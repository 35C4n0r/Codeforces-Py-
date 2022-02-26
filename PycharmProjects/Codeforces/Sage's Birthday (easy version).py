n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr2 = []
count = 0
z = n//2
if n % 2 == 0:
    for k, kk in zip(arr[:z], arr[z:]):
        arr2.append(kk)
        arr2.append(k)
else:
    vv = sorted(arr[z:], reverse=True)
    for k, kk in zip(arr[:z], vv):
        arr2.append(kk)
        arr2.append(k)
    arr2.insert(len(arr), vv[-1])
for ka in range(1, n-1, 2):
    if arr2[ka] < arr2[ka+1] and arr2[ka-1] > arr2[ka]:
        count += 1
print(count)
for i in arr2:
    print(i, end=" ")
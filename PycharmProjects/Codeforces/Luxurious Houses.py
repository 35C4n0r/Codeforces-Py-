# 1100
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
count = 0
arr2 = []
for k in arr:
    arr2.append(max(count+1-k, 0))
    count = max(count, k)
arr2.reverse()
for kk in arr2:
    print(kk, end=" ")
n = int(input())
arr = list(map(int, input().split()))
arr2 = arr.copy()
arr2.sort()
m = int(input())
for _ in range(m):
    a, x, y = list(map(int, input().split()))
    if a == 1:
        print(sum(arr[x-1:y]))
    else:
        print(sum(arr2[x-1:y]))
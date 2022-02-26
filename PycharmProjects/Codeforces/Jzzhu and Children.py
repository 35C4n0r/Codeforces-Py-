n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = []

for k in range(n):
    if m < arr[k]:
        arr.insert(len(arr), arr[k] - m)
        arr.pop(k)
        if len(arr) == 1:
            print()
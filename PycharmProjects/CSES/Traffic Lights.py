x, n = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = [0]*(x+1)
for k in arr:
    arr2[k] = 1
    print(arr2)


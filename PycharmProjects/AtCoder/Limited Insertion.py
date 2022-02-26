n = int(input())
arr = list(map(int, input().split()))
arr2 = []
#print(arr)
for k in range(n):
    if arr[k] > k + 1:
        print(-1)
        exit()
    else:
        #print(k, arr[k], arr[k]-1)
        arr2.insert(arr[k] - 1, arr[k])
for d in arr2:
    print(d)
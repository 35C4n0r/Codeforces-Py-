h, w = list(map(int, input().split()))
count = 0
arr = []
for _ in range(w):
    arr.append([])
#print(arr)
for _ in range(h):
    s = input()
    #count += s.count('..')
    arr2 = list(s)
    #print(arr2)
    for k in range(w - 1):
        #print(arr2[k], arr2[k+1])
        if arr2[k] == '.' and arr2[k+1] == '.':
            count += 1
    z = 0
    for kk in range(w):
        arr[kk].append(arr2[kk])
#print(arr)
for kkk in arr:
    for k in range(h - 1):
        if kkk[k] == '.' and kkk[k+1] == '.':
            count += 1

print(count)
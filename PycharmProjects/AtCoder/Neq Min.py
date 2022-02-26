n = int(input())
arr = list(map(int, input().split()))
z = 0
xxx = 0
if 0 in arr:
    z = arr.index(0)
    for _ in range(z):
        print(0)
for k in range(z, n):
    doubt = False
    arr2 = arr[:k+1]
    arr3 = arr2.copy()
    arr2 = list(set(arr2))
    arr2.sort()
    #print(arr2)
    for kkk in range(xxx - 1, len(arr2) - 1):
        #print(111)
        #print(arr2[kkk], arr2[kkk+1])
        if arr2[kkk] + 1 != arr2[kkk+1]:
            xxx = kkk
            ans = arr2[kkk] + 1
            print(ans)
            doubt = True
            break
    if not doubt:
        print(arr2[-1] + 1)
        xxx = len(arr2)
        #print(len(arr2) - 1)




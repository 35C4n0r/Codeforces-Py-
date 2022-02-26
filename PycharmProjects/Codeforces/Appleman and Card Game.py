n, k = list(map(int, input().split()))
s = input()
arr = list(s)
#print(abcd)
arr100 = []
count = 0
arr2 = list(set(arr))
#print(arr2)
if len(arr2) == n:
    print(k)
else:
    for _ in arr2:
        arr100.append(arr.count(_))
    arr100.sort(reverse=True)
    #print(arr1000)
    for kk in arr100:
        smh = min(k, kk)
        k -= smh
        count += smh ** 2
        if k == 0:
            print(count)
            exit()

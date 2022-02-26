arr = list(input())
arr2 = list(input())
arr3 = list(input())
for k in arr:
    if k in arr3:
        arr3.remove(k)
    else:
        print("NO")
        exit()
for kk in arr2:
    if kk in arr3:
        arr3.remove(kk)
    else:
        print("NO")
        exit()
if len(arr3) == 0:
    print("YES")
else:
    print("NO")
    exit()
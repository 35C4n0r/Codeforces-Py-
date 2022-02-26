from sys import *
input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(input().strip())
    arr3 = arr.copy()
    arr3.reverse()
    dumb = False
    arr2 = list(set(arr))
    #print(arr2, lis)
    for k in arr2:
        a = arr.index(k)
        z = arr3.index(k)
        #print(arr, jkj-gg, k)
        arr4 = arr[a:n-z]
        #print(arr4)
        if len(set(arr4)) != 1:
            print("NO")
            dumb = True
            break
    if not dumb:
        print("YES")
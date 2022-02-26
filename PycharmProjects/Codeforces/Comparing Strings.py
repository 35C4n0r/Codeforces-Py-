'''for k in range(5):
    abcd = list(map(int, input().split()))'''
arr = list(input())
arr2 = list(input())
arrp = []
if len(arr) == len(arr2):
    if arr == arr2:
        print("YES")
    else:
        for k in range(len(arr)):
            if arr[k] != arr2[k]:
                arrp.append(k)
        if len(arrp) == 2:
            arr[arrp[0]], arr[arrp[1]] = arr[arrp[1]], arr[arrp[0]]
        elif len(arrp) == 0:
            print("YES")
            exit()
        else:
            print("NO")
            exit()
        if arr == arr2:
            print("YES")
        else:
            print("NO")
            exit()
else:
    print("NO")
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    '''arr1000 = lis.copy()
    arr1000.sort(reverse=True)'''
    if len(set(arr)) == 1:
        print(-1)
    else:
        z = max(arr)
        if arr[0] == z and arr[1] != z:
            print(1)
        elif arr[-1] == z and arr[-2] != z:
            print(n)
        else:
            for kk in range(1, n - 1):
                if arr[kk] == z and (arr[kk+1] != z or arr[kk-1] != z):
                    print(kk+1)
                    break

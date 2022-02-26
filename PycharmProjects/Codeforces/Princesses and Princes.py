for _ in range(int(input())):
    n = int(input())
    arr6 = [hh for hh in range(1, n+1)]
    arr2 = []
    arr5 = []
    count = 0
    pre = 123456789987654321
    for i in range(n):
        arr = list(map(int, input().split()))
        arr3 = arr.copy()
        for jn in arr2:
            while jn in arr3:
                arr3.remove(jn)
        if len(arr3) > 0 and 0 not in arr3:
            pre = min(arr3)
            arr5.append(pre)
            arr2.append(pre)
            count += 1
        else:
            arr5.append(0)
    if 0 not in arr5:
        '''print(arr5)
        print(arr1000)
        print(arr6)'''
        print("OPTIMAL")
    else:
        print("IMPROVE")
        '''print(arr5)
        print(arr1000)
        print(arr6)'''
        for hj in arr2:
            if hj in arr6:
                arr6.remove(hj)
        ans = arr6[0]
        print(arr5.index(0) + 1, ans)

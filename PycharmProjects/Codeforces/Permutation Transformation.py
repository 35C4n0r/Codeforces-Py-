for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    mep = {}
    for k, kk in enumerate(arr):
        mep[kk] = k+1
    z = max(arr)
    pre = z
    arr2 = [0]*(n+1)
    arr3 = []
    for i in range(z, 0, -1):
        arr3.append(mep[i])
        for ii in range(mep[z], n+1):
            if ii not in arr3:
                arr2[ii] += 1
        for j in range(0, mep[i]):
            if j not in arr3:
                arr2[j] += 1

        print(arr2, i)
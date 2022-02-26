for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    s = input()
    arr = list(s)
    for _ in range(q):
        once = False
        ans = 0
        l, r = list(map(int, input().split()))
        if l == r:
            print("NO")
        else:
            arr2 = arr[l - 1:r]
            dam = 0
            for kk in arr2:
                #print(dam)
                if dam <= n-1:
                    for jl in range(dam, n):
                        if kk == arr[jl]:
                            if once == True:
                                dam = jl+1
                            else:
                                dam = jl+2
                            ans += 1
                            once = True
                            break
                    if not once:
                        break
            if ans == len(arr2):
                print("YES")
            else:
                print("NO")
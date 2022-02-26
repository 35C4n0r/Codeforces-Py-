for _ in range(int(input())):
    n = int(input())
    #property of no_soul
    arr = list(map(int, input().split()))
    jjj, kkkkf = arr.index(min(arr)), arr.index(max(arr))
    #print(jjj, kkkkf)
    ans = min(max(jjj + 1, kkkkf + 1), jjj + 1 + n - kkkkf, kkkkf + 1 + n - jjj, max(n - jjj, n - kkkkf))
    print(ans)

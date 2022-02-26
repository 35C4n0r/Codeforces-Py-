import itertools
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr2 = list(set(arr))
    result = 0
    ans = 0
    for k in range(2, 2*n + 1):
        result2 = 0
        arr3 = []
        for kk in arr:
            if kk > k / 2:
                break
            else:
                arr3.append(kk)
        arr100 = []
        for s in itertools.combinations(arr3, 2):
            if s not in arr100:
                if sum(s) == k:
                    arr100.append(s)
                    if s[0] != s[1]:
                        result = min(arr3.count(s[0]), arr3.count(s[1]))
                    else:
                        result = arr3.count(s[0]) // 2
                    result2 += result
        ans = max(ans, result2)
    print(ans)
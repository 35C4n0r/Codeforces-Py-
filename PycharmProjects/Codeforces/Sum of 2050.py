for _ in range(int(input())):
    a = int(input())
    if a % 2050 == 0:
        aa = a // 2050
        aa = str(aa)
        arr = list(map(int, list(aa)))
        print(sum(arr))
    else:
        print(-1)
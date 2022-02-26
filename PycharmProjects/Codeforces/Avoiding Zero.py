for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    m = True
    if sum(arr) == 0:
        print("NO")
    else:
        print("Yes")
        arr.sort(reverse=True)
        for k in arr:
            count += k
            if count == 0:
                m = False
                arr.sort()
                print(*arr)
                break
        if m is True:
            print(*arr)
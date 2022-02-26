for _ in range(int(input())):
    n = int(input())
    arr = []
    count = 1
    for k in range(3, (4*n) + 1):
        if count < n:
            flag = False
            for kk in arr:
                if k%kk == 0:
                    flag = True
                    break
            if not flag:
                arr.append(k)
                count += 1
                print(arr)
        if len(arr) == n:
            print(*arr)


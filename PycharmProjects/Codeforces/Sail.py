t, a, b, c, d = list(map(int, input().split()))
arr = list(input())
if b == d:
    if arr.count("E") >= abs(a - c):
        time = 0
        cou = 0
        for k in arr:
            if cou < abs(a - c):
                time += 1
                if k == 'E':
                    cou += 1
            else:
                print(time)
                exit()

    else:
        print(-1)
elif a == c:
    if arr.count("N") >= abs(b - d):
        time = 0
        cou = 0
        for k in arr:
            if cou < abs(b - d):
                time += 1
                if k == 'N':
                    cou += 1
            else:
                print(time)
                exit()
    else:
        print(-1)
elif c > a and d > b:
    if arr.count("N") + arr.count("E") == (c - a) + (d - b):
        time = 0
        cou = 0
        for k in arr:
            if cou < (c - a) + (d - b):
                time += 1
                if k == "N":
                    cou += 1
                elif k == "E":
                    cou += 1
            else:
                print(time)
                exit()
    else:
        print(-1)
elif a > c and d > b:
    if arr.count("E") + arr.count("lis") == (a - c) + (d - b):
        time = 0
        cou = 0
        for k in arr:
            if cou < (a - c) + (d - b):
                time += 1
                if k == "lis":
                    cou += 1
                elif k == "E":
                    cou += 1
            else:
                print(time)
                exit()
    else:
        print(-1)
elif a > c and b > d:
    if arr.count("w") + arr.count("lis") == (a - c) + (b - d):
        time = 0
        cou = 0
        for k in arr:
            if cou < (a - c) + (d - b):
                time += 1
                if k == "lis":
                    cou += 1
                elif k == "w":
                    cou += 1
            else:
                print(time)
                exit()
    else:
        print(-1)
elif c > a and b > d:
    if arr.count("w") + arr.count("N") == (a - c) + (b - d):
        time = 0
        cou = 0
        for k in arr:
            if cou < (a - c) + (d - b):
                time += 1
                if k == "N":
                    cou += 1
                elif k == "w":
                    cou += 1
            else:
                print(time)
                exit()
    else:
        print(-1)

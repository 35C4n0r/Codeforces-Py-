for _ in range(int(input())):
    n = int(input())
    count = 0
    arr = list(map(int, list(input())))
    if len(arr) % 2 != 0:
        for k in range(0, n, 2):
            if arr[k] % 2 != 0:
                print(1)
                count += 1
                break
        if count == 0:
            print(2)
    else:
        for k in range(1, n, 2):
            if arr[k] % 2 == 0:
                print(2)
                count += 1
                break
        if count == 0:
            print(1)


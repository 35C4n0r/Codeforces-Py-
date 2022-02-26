for _ in range(int(input())):
    n = input()
    arr = list(n)
    t = arr.count('T')
    m = len(arr) - t
    if t % 2 != 0:
        print('NO')
        exit()
    if t / 2 != m:
        print("NO")
        exit()
    count = 0
    ar = [0]*m

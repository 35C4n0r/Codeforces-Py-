for _ in range(int(input())):
    arr = list(map(int, input().split()))
    a = arr[0]
    b = arr[1]
    c = arr[2]
    if len(set(arr)) == 1:
        print(arr[1])
    elif arr[2] == 0:
        print((a+b)//3)
    else:
        while sum(arr) >= 3:

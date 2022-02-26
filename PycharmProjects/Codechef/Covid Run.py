for _ in range(int(input())):
    arr = []
    z = True
    n, k, x, y = list(map(int, input().split()))
    while True:
        x = (x+k)%n
        if x not in arr:
            arr.append(x)
            if y == x:
                print("YES")
                z = False
                break
        else:
            break
    print(arr)
    if z:
        print(arr)
        print("NO")




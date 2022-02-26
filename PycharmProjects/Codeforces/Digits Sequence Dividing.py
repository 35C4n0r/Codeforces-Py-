for _ in range(int(input())):
    n = int(input())
    nn = int(input())
    ann = str(nn)
    if n == 1 or (n == 2 and len(set(ann)) == 1) or nn % 100 == 0:
        print("NO")
    elif n == 2:
        arr = list(map(int, list(ann)))
        if arr[0] >= arr[1]:
            print("NO")
        else:
            print("YES")
            print(2)
            print(arr[0], arr[1])
    else:
        print("YES")
        print(2)
        arr = list(ann)
        print(arr[0], ''.join(arr[1:]))
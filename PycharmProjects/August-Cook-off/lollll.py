for _ in range(int(input())):
    arr1 = list(input())
    arr = list(map(int, arr1))
    arr2 = arr.copy()
    x = int(input())
    for i in range(len(arr)):
        if i + 1 > x and arr2[i - x] == 1:
            arr[i] = 1

        elif i + 1 + x <= len(arr) and arr2[i + x] == 1:
            arr[i] = 1

        else:
            arr[i] = 0
    if len(set(arr)) == 1:
        print("-1")
    else:
        for b in arr:
            print(b, end="")
        print()



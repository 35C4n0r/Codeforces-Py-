for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    m = ((n*(n-1)) // 2) - 1
    count = 0
    if len(set(arr)) == 1 and len(arr) != 1:
        print("YES")
    else:
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    count += 1
                    if count > m:
                        print("NO")
                        break
            if not swapped:
                break
        if count <= m:
            print("YES")


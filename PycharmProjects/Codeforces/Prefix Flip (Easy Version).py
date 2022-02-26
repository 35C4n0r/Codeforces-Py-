for _ in range(int(input())):
    n = int(input())
    arr = list(input())
    arr2 = list(input())
    arr100 = []
    if arr == arr2:
        print(0)
    else:
        for k in range(n):
            if arr[k] != arr2[k]:
                if k > 0:
                    arr100.append(k+1)
                arr100.append(1)
                if k > 0:
                    arr100.append(k+1)
        print(len(arr100), end=' ')
        print(*arr100)
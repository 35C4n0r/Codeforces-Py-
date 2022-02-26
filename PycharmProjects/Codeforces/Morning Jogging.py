for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr = []
    arr3 = {}
    for i in range(n):
        arr2 = list(map(int, input().split()))
        arr.append(arr2)
        for j in arr2:
            arr3[j] = i
# Wasn't able to solve
# Date: 24/11/2021

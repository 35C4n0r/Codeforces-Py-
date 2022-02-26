import math
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    odd = []
    even = []
    result = []
    for k in range(a):
        if arr[k] % 2 != 0:
            odd.append(arr[k])
        else:
            even.append(arr[k])
    if b % 2 != 0:
        if b <= len(odd):
            print("Yes")
        else:
            if len(odd) % 2 != 0:
                if b - len(odd) <= len(even):
                    print("Yes")
                else:
                    print("No")
            else:
                if b - len(odd) + 1 <= len(even):
                    print("Yes")
                else:
                    print("No")
    else:
        if b <= len(odd) - 1 and len(even) >= 1:
            print("Yes")
        else:
            if len(odd) % 2 != 0:
                if b - len(odd) <= len(even):
                    print("Yes")
                else:
                    print("No")
            else:
                if b - len(odd) + 1 <= len(even):
                    print("Yes")
                else:
                    print("No")
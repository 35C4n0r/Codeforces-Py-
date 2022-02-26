for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr3 = []
    for k in range(n):
        l1 = list(map(int, input().split()))
        l2 = list(map(int, input().split()))
        if l1[1] == l2[0]:
            arr3.append(True)
    if m % 2 != 0:
        print("No")
    else:
        if True in arr3:
            print("Yes")
        else:
            print("No")
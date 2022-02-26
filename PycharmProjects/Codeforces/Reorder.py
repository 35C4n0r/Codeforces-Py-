for o in range(int(input())):
    j, k = list(map(int, input().split()))
    arr12 = list(map(int, input().split()))
    if sum(arr12) == k:
        print("YES")
    else:
        print("NO")

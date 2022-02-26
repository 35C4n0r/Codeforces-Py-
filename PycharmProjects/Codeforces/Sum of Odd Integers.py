for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if k ** 2 <= n and n % 2 == k % 2:
        print("YES")
    else:
        print("NO")
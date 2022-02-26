n = int(input())
if n % 2 == 1:
    print(-1)
else:
    arr = [i for i in range(n, 0, -1)]
    print(*arr)
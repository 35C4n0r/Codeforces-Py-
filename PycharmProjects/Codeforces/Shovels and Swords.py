for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    print(min(a, b, (a+b)//3))
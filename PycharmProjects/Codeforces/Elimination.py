zz = int(input())
for _ in range(zz):
    a, b, c, d = list(map(int, input().split()))
    print(max((a+b), (c+d)))
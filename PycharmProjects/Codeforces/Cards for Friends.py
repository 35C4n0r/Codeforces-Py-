import math
for _ in range(int(input())):
    w, h, n = list(map(int, input().split()))
    a = 1
    while w % 2 == 0:
        w //= 2
        a *= 2
    while h % 2 == 0:
        a *= 2
        h //= 2
    # print(arr *pre_n_post)
    if a >= n:
        print("YES")
    else:
        print("NO")

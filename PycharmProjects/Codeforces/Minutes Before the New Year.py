# 800
for _ in range(int(input())):
    count = 0
    h, m = list(map(int, input().split()))
    z = 24 - h
    count += (60*z) - m
    print(count)
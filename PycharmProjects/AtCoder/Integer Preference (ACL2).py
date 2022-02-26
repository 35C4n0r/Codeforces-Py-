a, b, c, d = list(map(int, input().split()))
if a <= c <= b or a <= d <= b:
    print("Yes")
elif a >= c and d >= b:
    print('Yes')
elif c <= a <= d or c <= b <= d:
    print("Yes")
elif c >= a and b >= d:
    print('Yes')
else:
    print("No")


a, b, c, d = list(map(int, input().split()))
if c > a:
    x = c - a
    r = b / d
    ans = ((r*x) / (1+r)) + a
else:
    a, c = c, a
    d, b = b, d
    x = c - a
    r = b / d
    ans = ((r * x) / (1 + r)) + a

print(ans)
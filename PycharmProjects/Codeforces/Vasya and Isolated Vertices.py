n, m = list(map(int, input().split()))
x = m*2
mn = 0
mx = 0
if x >= n:
    mn = 0
else:
    mn = n - x
if m < n:
    mx = (n - 1) - m
else:
    mx = 0
print(mn, mx)
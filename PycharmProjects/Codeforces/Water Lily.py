h, l = list(map(int, input().split()))
ans = ((l**2) + (h ** 2)) / (2*h)
print(ans - h)
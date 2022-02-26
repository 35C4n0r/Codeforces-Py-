a, b, n = list(map(int, input().split()))
z = n % 5
total = (z * a) + ((n // 5) * b)
print(min(total, n * a))
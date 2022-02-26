k = int(input())
arr = []
for n in range(1, k + 1):
    z = (((n**2) * ((n**2) - 1)) // 2) - (4 * (n-1) * (n-2))
    print(z)
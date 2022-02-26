'''n, m, k = list(map(int, input().split()))
if k < max(n, m):
    print("No")
elif k % n == 0 and k // n <= m or k%m == 0 and k // m <= n:
    print("Yes")
else:
'''
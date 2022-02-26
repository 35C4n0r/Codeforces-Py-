a, b, c = list(map(int, input().split()))
for k in range(a, 10**5, a):
    if k % b == c:
        print("Yes")
        exit()
print("No")
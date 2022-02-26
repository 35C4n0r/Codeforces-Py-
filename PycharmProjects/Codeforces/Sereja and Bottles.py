count = 0
arr = []
n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    if (a, b) not in arr:
        if a != b and 1 <= b <= n:
            count += 1
        arr.append((a, b))
#print(abcd)
print(n - count)
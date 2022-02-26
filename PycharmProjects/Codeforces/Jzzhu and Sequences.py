x, y = list(map(int, input().split()))
m = 10**9 + 7
n = int(input())
arr = [x, y]
n -= 1
for _ in range(4):
    x, y = y, y-x
    arr.append(y)
print(arr)
if n <= len(arr):
    print(arr[n] % m)
else:
    xxx = (n+1) % len(arr)
    #print(10 % 6)
    #print(xxx, jkj, len(abcd))
    print((arr[xxx - 1] % m)%m)
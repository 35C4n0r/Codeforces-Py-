n = int(input())
arr = list(map(int, input().split()))
sum = 0
if n % 3 == 0:
    z = n / 3
elif n <= 2:
    print(0)
    exit()
else:
    z = (n // 3) + 1
for time in arr:
    while z > 0:
        sum += min(arr)
        arr.remove(min(arr))
        z -= 1
print(sum)



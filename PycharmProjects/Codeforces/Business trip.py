n = int(input())
arr = list(map(int, input().split()))
count = 0
ccc = 0
while count < n:
    if len(arr) > 0:
        z = max(arr)
        count += z
        arr.remove(z)
        ccc += 1
    else:
        print(-1)
        exit()
print(ccc)

n = int(input())
b = 0
arr = sorted(list(map(int, input().split())))
z = len(arr)
med = int(arr[len(arr) // 2])
for i in arr:
    b += abs(i - med)
print(b)


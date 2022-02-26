n = int(input())
s = input()
arr = list(s)
count = 0
for k in range(n - 1):
    if arr[k] == arr[k + 1]:
        count += 1
print(count)

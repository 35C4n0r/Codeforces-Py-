n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
z = n
profit = arr[0] * n
for i in range(1, n):
    z -= 1
    profit = max(arr[i] * z, profit)
print(profit)


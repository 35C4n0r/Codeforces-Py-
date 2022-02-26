n = int(input())
arr = list(map(int, input().split()))
sum = 0
arr.sort()
for i in range(n - 1, -1, -1):
    sum += i * arr[i] - (n-1-i) * arr[i]
print(sum)
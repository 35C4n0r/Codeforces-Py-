sum = 0
n = int(input())
array = list(map(int, input().split()))
best = array[0]
for k in range(n):
    sum = max(array[k], sum+array[k])
    best = max(best, sum)
print(best)
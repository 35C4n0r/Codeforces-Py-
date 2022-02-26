n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.insert(0, 1)
#print(lis)
sum = 0
for k in range(k):
    diff = arr[k + 1] - arr[k]
    if diff < 0:
        diff += n
    #print(diff)
    sum += diff
print(sum)

arr2 = []
count = 0
count2 = 0
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr2.append(arr)
arr2.sort()
for k in arr2:
    count2 += k[0]
    count += k[1] - count2
print(count)

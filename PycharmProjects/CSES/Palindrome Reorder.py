arr = list(input())
arr.sort()
count1 = 0
lis = set(arr)
for i in lis:
    if arr.count(i) == 1:
        count1 += 1
if count1 > 1:
    print("NO SOLUTION")
else:


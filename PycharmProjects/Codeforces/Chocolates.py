# 1000
n = int(input())
arr = list(map(int, input().split()))
num = arr[-1]
arr2 = [num]
arr.reverse()
arr.pop(0)
for k in arr:
    num = min(num-1, k)
    if num < 0:
        arr2.append(0)
    else:
        arr2.append(num)
print(sum(arr2))
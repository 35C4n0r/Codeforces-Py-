n, k = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append((input()))
arr = sorted(arr, key=len)
ans = (input())
zz = len(ans)
arr2 = [0]*len(arr[-1])
'''if len(lis[0]) == len(lis[-1]):
    ans1 = 1
    ans2 = jkj
    if ans2 > k:
        ans2 += (ans2// k) * 5
    print(ans1, ans2)
    exit()'''
for j in range(n):
    l = len(arr[j])
    arr2[l-1] += 1
ans1 = sum(arr2[:zz - 1])
if ans1 > k:
    ans1 += (ans1//k)*5
    ans1 += 1
ans2 = sum(arr2[:zz])
if ans2 > k:
    ans2 += (ans2 - 1//k)*5
print(ans1, ans2)

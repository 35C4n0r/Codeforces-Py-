n, k = list(map(int, input().split()))
s = input()
arr = list(s)
alpha_arr = list('abcdefghijklmnopqrstuvwxyz')
d = {}
for i in range(26):
    d[alpha_arr[i]] = i
arr.sort()
ans = d[arr[0]] + 1
pre = d[arr[0]]
res = 1
if k == 1:
    print(ans)
    exit()
for j in range(1, n):
    word = arr[j]
    if pre+2 <= d[arr[j]]:
        res += 1
        pre = d[arr[j]]
        ans += d[arr[j]] + 1
        if res >= k:
            print(ans)
            exit()
print(-1)

n, x = list(map(int, input().split()))
s = input()
arr = list(s)
ans = x
for kk in arr:
    if kk == 'o':
        ans += 1
    else:
        if ans > 0:
            ans -= 1
print(ans)
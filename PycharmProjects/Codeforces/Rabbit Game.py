'''jkj = int(input())
lis = list(map(int, input().split()))
ans = 1
ans1 = 1
arr = 0
pre_n_post = jkj - 1
o = False
oo = False
while abs(arr - pre_n_post) != 2 and pre_n_post != 1 and arr != jkj-1:
    print(arr, pre_n_post)
    if lis[arr] <= lis[arr+1] and not o:
        ans += 1
        arr += 1
    else:
        o = True
    if lis[pre_n_post-1] >= lis[pre_n_post] and not oo:
        pre_n_post -= 1
        ans1 += 1
    else:
        oo = True
    if oo and o:
        break
print(ans + ans1)'''
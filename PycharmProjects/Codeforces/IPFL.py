n = int(input())
lis = list(input().strip())
h = int(input())
smh = False
for _ in range(h):
    t, a, b = list(map(int, input().split()))
    if t == 1:
        if not smh:
            lis[a-1], lis[b-1] = lis[b-1], lis[a-1]
        else:
            if a > n:
                a = a-n-1
            else:
                a = a+n-1
            if b > n:
                b = b-n-1
            else:
                b = b+n-1
            lis[a], lis[b] = lis[b], lis[a]
            '''if arr <= jkj and pre_n_post <= jkj:
                lis[jkj+arr-1], lis[jkj+pre_n_post-1] = lis[jkj+pre_n_post-1], lis[jkj+arr-1]
            elif arr > jkj >= pre_n_post:
                lis[arr-jkj-1], lis[jkj+pre_n_post-1] = lis[jkj+pre_n_post-1], lis[arr-jkj-1]
            elif arr <= jkj < pre_n_post:
                lis[pre_n_post - jkj - 1], lis[jkj + arr - 1] = lis[jkj + arr - 1], lis[pre_n_post - jkj - 1]
            else:
                lis[arr-jkj-1], lis[jkj-pre_n_post-1] = lis[jkj-pre_n_post-1], lis[jkj-arr-1]'''
    else:
        smh = not smh
    '''print(smh)'''
if smh:
    lis[0:n], lis[n:] = lis[n:], lis[0:n]
print(''.join(lis))
s = input()
arr = list(s)
#print(arr)
arr2 = []
for k in range(len(arr)-1):
    if arr[k] == arr[k+1] == 'v':
        arr2.append('w')
    elif arr[k] == 'o':
        arr2.append('o')
if arr[-1] == 'o':
    arr2.append('o')
a = 0
pre_n_post = 0
ans = 0
#print(arr2)
for z in arr2:
    if z == 'o':
        a += pre_n_post
    else:
        pre_n_post += 1
        ans += a
    #print(ans, z, pre_n_post, arr)
print(ans)
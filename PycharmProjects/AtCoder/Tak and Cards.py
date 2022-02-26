import itertools
n, a = list(map(int, input().split()))
arr = list(map(int, input().split()))
ans = []
for k in range(1, n+1):
    for kk in itertools.combinations(arr, k):
        #print(kk)
        if sum(kk)/k == a:
            ans.append(kk)
            #print(kk, ans)
print(len(set(ans)))
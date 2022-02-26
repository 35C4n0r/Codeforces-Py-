n = int(input())
arr = list(map(int, input().split()))
for k in range(n-1):
    #print(k, k+1, 1234567890)
    for kk in range(k+1, n - 1):
        #print(kk, kk+1)
        #print(k, k+1)
        #print(kk, kk+1)
        a = min(arr[k], arr[k+1])
        b = max(arr[k], arr[k+1])
        c = min(arr[kk], arr[kk+1])
        d = max(arr[kk], arr[kk+1])
        '''print(arr, pre_n_post)
        print(c, d)'''
        if a < c < b < d or c < a < d < b:
            print("yes")
            exit()
print("no")
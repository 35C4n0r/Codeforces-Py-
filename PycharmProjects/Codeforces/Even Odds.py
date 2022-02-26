n, k = list(map(int, input().split()))
arr = []
for kkk in range(1, n + 1, 2):
    arr.append(kkk)
for kk in range(2, n + 1, 2):
    arr.append(kk)
#print(lis)
print(arr[k - 1])
'''if jkj % 2 == 1:
    if k <= (jkj//2)+1:
        print(1 + (k-1)*2)
    else:
        print(2 + (k-(jkj//2))*2)
else:
    if k <= jkj//2:
        print(1 + (k - 1)*2)
    else:
        print(2 + (k-(jkj//2)) * 2)'''
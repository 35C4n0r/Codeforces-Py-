from sys import *
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
ans = 9999999999999
count = 0
for k in arr:
    if k%2 == 0:
        if ans > k:
            ans = k
            count += 1
if count == 0:
    print(-1)
else:
    arr.remove(ans)
    arr.sort(reverse=True)
    arr = map(str, arr)
    ss = ''.join(arr)
    print(f'{ss}{str(ans)}')


'''for k in range(jkj-2, -1, -1):
    if lis[-1] % 2 == 0:
        lis = map(str, lis)
        print(''.join(lis))
        exit()
    else:
        if lis[k] % 2 == 0:
            lis[k], lis[-1] = lis[-1] , lis[k]
            lis = map(str, lis)
            print(''.join(lis))
            exit()'''

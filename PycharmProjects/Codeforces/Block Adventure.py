from sys import *
input = stdin.readline
print = stdout.write
for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    bag = m
    for l in range(n-1):
        j = abs(arr[l] - arr[l+1])
        if arr[l] >= arr[l+1]:
            bag += min((j+k), arr[l])
        elif arr[l] < arr[l+1]:
            if k < j:
                bag -= (j-k)
            else:
                bag += min((k-j), arr[l])
        if bag < 0:
            break
        #print(bag, l, j)
    if bag >= 0:
        print("YES\n")
    else:
        print("NO\n")
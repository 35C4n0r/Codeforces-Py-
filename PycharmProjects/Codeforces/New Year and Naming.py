# 800
n, m = list(map(int, input().split()))
arr1 = list(map(str, input().split()))
arr2 = list(map(str, input().split()))
for _ in range(int(input())):
    k = int(input())
    zz = k % n
    zzz = k % m
    print(f"{arr1[zz - 1]}{arr2[zzz - 1]}")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
z = arr[-1]+arr[-2]
for  _ in range(2, z+1):

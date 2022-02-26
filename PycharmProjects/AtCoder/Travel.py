import itertools
n, k = list(map(int, input().split()))
lis = []
for _ in range(n):
    lis.append(list(map(int, input().split())))
arr = [itertools.permutations(range(1, n))]
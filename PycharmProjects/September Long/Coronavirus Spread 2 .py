import itertools
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if len(set(arr)) >= 2 and 0 in set(arr):
        print(0, 0)
    else:
        for k in itertools.combinations(arr, 2):
            if





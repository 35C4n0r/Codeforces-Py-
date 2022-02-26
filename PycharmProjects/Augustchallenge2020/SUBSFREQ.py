import itertools
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = len(arr) + 1
    count = [0]*x
    initcount = []
    for i in range(1, n+1):
        for k in itertools.combinations(arr, i):
            if len(k) == 1:
                count[k] += 1
            else:
                for h in k:
                    initcount.append(k.count[h])

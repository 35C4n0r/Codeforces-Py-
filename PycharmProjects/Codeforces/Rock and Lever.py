import itertools
for _ in range(int(input())):
    n = int(input())
    count = 0
    arr = list(map(int, input().split()))
    for k in itertools.combinations(arr, 2):
        if (k[0] & k[1]) >= (k[0] ^ k[1]):
            count += 1
    print(count)

import itertools
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
count = 0
for i in itertools.combinations(arr, 2):
    if abs(i[1] - i[0]) >= k:
            count += 1
print(count)
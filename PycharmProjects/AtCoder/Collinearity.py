import itertools
arr = []
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if (a, b) not in arr:
        arr.append((a, b))
for k in itertools.combinations(arr, 3):
    if ((k[0][0])*(k[1][1] - k[2][1])) + ((k[1][0])*(k[2][1] - k[0][1])) + ((k[2][0])*(k[0][1] - k[1][1])) == 0:
        #if (k[2][1] - k[0][1]) // (k[2][0] - k[0][0]) == (k[1][1] - k[0][1]) // (k[1][0] - k[0][0]):
        print("Yes")
        exit()
print("No")
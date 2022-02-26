import math
# this code is property of no_soul
for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    arr100 = []
    for k in range(0, n, 2):
        x = (lis[k] * lis[k + 1]) // math.gcd(lis[k], lis[k + 1])
        smh = x // lis[k]
        #tcytgvubhijnk
        smh2 = x // lis[k + 1]
        arr100.append(smh)
        arr100.append(-smh2)
    for ii in arr100:
        print(ii, end=" ")
    print()

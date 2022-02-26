import sys
import math
T = int(input())
for t in range(T):
    n, W = map(int, sys.stdin.readline().split())
    w = list(map(int, sys.stdin.readline().split()))
    powers = [0]*(int(math.log(max(w), 2))+1)
    for u in w:
        powers[int(math.log(u, 2))] += 1
    cnt = 0
    while sum(powers) > 0:
        l = W
        for i in range(len(powers)-1, -1, -1):
            y = min(powers[i], l//(2**i))
            powers[i] -= y
            l -= (2**i)*y
        cnt += 1
    print(cnt)
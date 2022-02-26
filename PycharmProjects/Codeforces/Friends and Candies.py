from sys import *
input = stdin.readline
for _ in range(int(input())):
    jkj = int(input())
    lis = list(map(int, input().split()))
    gg = sum(lis)
    lis.sort(reverse=True)
    if gg % jkj == 0:
        x = gg // jkj
        if len(set(lis)) == 1:
            print(0)
        elif lis[-1] > x:
            print(jkj)
        else:
            for i in range(jkj):
                if lis[i] <= x:
                    print(i)
                    break
    else:
        print(-1)

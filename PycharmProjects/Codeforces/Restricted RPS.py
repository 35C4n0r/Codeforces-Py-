from sys import *
input = stdin.readline
n, m = map(int, input().split())
rishabh = (m + 1) // 2
ans = []
smh = rishabh
for kk in range(n):
    ans.append(smh)
    if smh == rishabh and m%2 == 1:
        smh -= 1
    elif smh <= rishabh:
        smh = m - smh + 1
    else:
        smh = m - smh
    if smh == 0:
        smh = rishabh
for kkk in ans:
    print(kkk)
"""
ID: jay20ma1
LANG: PYTHON3
TASK: milk
"""
import math
fin = open('milk.in', 'r')
fout = open('milk.out', 'w')
arr = []
total = 0
price_total = 0
n, m = list(map(int, fin.readline().split()))
if n == 0 or m == 0:
    fout.write(str(0))
    fout.write('\n')
    for _ in range(m):
        p, a = list(map(int, fin.readline().split()))
        arr.append([p, a])
    #arr.sort()
else:
    for _ in range(m):
        p, a = list(map(int, fin.readline().split()))
        arr.append([p, a])
    arr.sort()
    for k in arr:
        if total < n:
            price_total += min(k[1], (n - total)) * k[0]
            total += min(k[1], (n-total))
            #price_total += min(k[1], (n-total)) * k[0]
            #print(total, price_total, k, n-total)
        else:
            break
            #print(price_total, arr, total, n)
            #fout.write('\n')

    fout.write(f'{price_total}')
    fout.write('\n')

fout.close()



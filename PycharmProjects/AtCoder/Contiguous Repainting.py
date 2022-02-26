import math
n, k = map(int, input().split())
arr = list(map(int, input().split()))

pos = 0
neg = 0

for a in arr[:k]:
    #print(a)
    if a > 0:
        pos += a
    else:
        neg += a
#print(pos, neg)
wp = pos
wn = neg
ans = math.inf
for i, a in enumerate(arr[k:]):
    if a > 0:
        pos += a
        wp += a
    else:
        neg += a
        wn += a
    b = arr[i]
    #print(b, a)
    if b > 0:
        wp -= b
    else:
        wn -= b
    ans = min(ans, wp, -wn)
    #print(i, a, ans, wp, wn)
print(max(pos - ans, pos + neg, 0))
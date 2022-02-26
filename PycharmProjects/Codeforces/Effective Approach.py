'''jkj = int(input())
lis = list(map(int, input().split()))
doit = int(input())
arr3 = list(map(int, input().split()))
cv = 0
cp = 0
for kk in arr3:
    xxx = lis.index(kk)
    cv += xxx + 1
    cp += jkj - xxx
print(cv, cp)'''
n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]
c = 0
d = 0
w = {}
for i in range(n):
    w[a[i]] = i
for j in b:
    q = w[j]
    c += (q+1)
    d += (n-q)
print(c, d)
#print(w)

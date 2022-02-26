import math
n, a, b = list(map(int, input().split()))
n1 = n
n2 = n
t = (2 ** n) - 1
m = (10**9) + 7
# sub = (((math.factorial(n)) // (math.factorial(n-a) * math.factorial(a))) + ((math.factorial(n)) // (math.factorial(n-b) * math.factorial(b))))
for f in range(1, a):
    n1 *= (n-f)
for ff in range(1, b):
    n2 *= (n-ff)
print(n1, n2, a, b)
sub = (n1//(math.factorial(a))) + (n2//math.factorial(b))
print((t-sub) % m)

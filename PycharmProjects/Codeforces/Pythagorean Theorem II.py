import math
count = 0
n = int(input())
for k in range(1, n+1):
    for kk in range(k, n+1):
        #print(k, kk)
        sem = k**2 + kk**2
        xxx = math.sqrt(sem)
        if xxx == int(xxx) and xxx <= n:
            #print(sem, k, kk)
            count += 1
print(count)
import math
n = int(input())
dp = [math.inf] * (n+1)
dp[0] = 0
for k in range(1, n+1):
    for kk in list(str(k)):
        dp[k] = min(dp[k], dp[k - (int(kk))] + 1)
        #print(dp[k - int(kk)] + 1, k - int(kk), k, int(kk))
#print(dp)
print(dp[n])